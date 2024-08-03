# Interactive Document Q&A Chatbot

This project implements a web-based Q&A chatbot using Retrieval-Augmented Generation (RAG). Users can upload PDF documents, which are then processed to create vector embeddings. Once the embeddings are created, users can ask questions based on the content of the uploaded document.

## Features

- **PDF Upload:** Upload PDF documents for processing.
- **Vector Embeddings:** Create vector embeddings using Google Generative AI.
- **RAG Model:** Uses Retrieval-Augmented Generation (RAG) to answer questions based on document content.
- **Progress Indicator:** Visual feedback during document processing.
- **Responsive Design:** User-friendly interface with Bootstrap.

## Technologies Used

- **Flask:** Web framework for Python.
- **LangChain:** For document processing and vector embeddings.
- **Google Generative AI:** For generating embeddings.
- **FAISS:** For efficient similarity search.
- **Bootstrap:** For responsive web design.
- **HTML/CSS/JavaScript:** For front-end development.

## Setup and Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/sudeepjoelbayyee/Interactive-PDF-Assistant-Ask-Questions-Get-Answers.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd interactive-document-qa-chatbot
    ```

3. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables:**

    Create a `.env` file in the project root with the following content:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

6. **Run the Application:**

    ```bash
    python app.py
    ```

7. **Access the Application:**

    Open your browser and go to `http://localhost:5000`.
