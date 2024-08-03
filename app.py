import os
from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask application setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
app.secret_key = 'supersecretkey'

# Ensure uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load APIs
groq_api = os.getenv("GROQ_API_KEY")
google_api = os.getenv("GOOGLE_API_KEY")

# Initialize models and prompt
llm = ChatGroq(groq_api_key=groq_api, model="gemma2-9b-it")
prompt = ChatPromptTemplate.from_template("""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question.
<context>
{context}
<context>
Questions:{input}
""")

# Global in-memory store for vectors
global_vector_store = {}

# Helper functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def clean_text(text):
    # Remove surrogate pairs and other unsupported characters
    return ''.join(c for c in text if c.isprintable() and ord(c) < 65536)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the PDF
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            final_documents = text_splitter.split_documents(docs)
            cleaned_final_documents = [clean_text(doc.page_content) for doc in final_documents]
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api)
            vectors = FAISS.from_texts(cleaned_final_documents, embeddings)

            # Store vectors in the global store and mark as ready
            global_vector_store['vectors'] = vectors
            session['vectors_ready'] = True  # Mark vectors as ready
            flash('Analyzed. You can now ask questions.', 'success')
            return redirect(url_for('index'))

    return render_template('index.html')

import re

def format_answer(answer):
    # Replace markdown-like **bold** with HTML <strong>
    answer = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', answer)

    # Replace markdown-like *italic* with HTML <em>
    answer = re.sub(r'\*(.*?)\*', r'<em>\1</em>', answer)

    # Replace markdown-like ## Heading 2 with HTML <h2>
    answer = re.sub(r'## (.*)', r'<h2>\1</h2>', answer)

    # Replace markdown-like # Heading 1 with HTML <h1>
    answer = re.sub(r'# (.*)', r'<h1>\1</h1>', answer)

    # Replace markdown-like - List item with HTML <li>
    answer = re.sub(r'^\- (.*)', r'<li>\1</li>', answer, flags=re.MULTILINE)

    # Replace multiple list items with <ul> and </ul>
    answer = re.sub(r'(<li>.*?</li>)+', r'<ul>\g<0></ul>', answer, flags=re.DOTALL)

    # Replace markdown-like ```code``` with HTML <pre><code>
    answer = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', answer, flags=re.DOTALL)

    # Replace newlines with <br> for better paragraph separation
    answer = re.sub(r'\n+', r'<br><br>', answer)

    # Wrap in a paragraph tag
    return f"<p>{answer}</p>"

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    if not question:
        flash('Please enter a question.', 'danger')
        return redirect(url_for('index'))

    if not session.get('vectors_ready'):
        flash('Please upload a PDF and create vector embeddings first.', 'danger')
        return redirect(url_for('index'))

    # Retrieve and respond
    vectors = global_vector_store['vectors']
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'input': question})
    answer = response['answer']

    # Format the answer
    formatted_answer = format_answer(answer)

    return render_template('index.html', answer=formatted_answer)

if __name__ == '__main__':
    app.run(debug=True)