# Interactive PDF Assistant: Ask Questions, Get Answers

## Overview

The Interactive PDF Assistant allows users to upload PDF documents and ask questions based on the content of these documents. The application uses advanced AI models to generate accurate and context-aware responses, making it a powerful tool for extracting information from large documents quickly and efficiently.

## Features

- **PDF Upload**: Users can upload their own PDF files to the platform.
- **Question and Answer**: Ask questions related to the content of the uploaded PDF and get precise answers.
- **AI-Powered**: Utilizes state-of-the-art AI models to understand and extract relevant information.
- **Fast and Accurate**: Quick response times with high accuracy, suitable for various use cases.

## How It Works

1. **Upload a PDF**: Start by uploading a PDF document using the file uploader.
2. **Create Vector Store**: The document is processed to create vector embeddings, enabling efficient information retrieval.
3. **Ask Questions**: Enter your question in the text input field. The AI model will retrieve relevant information from the document and provide an answer.

## Installation

To run the project locally, follow these steps:

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/your-username/interactive-pdf-assistant.git
    cd interactive-pdf-assistant
    ```

2. **Create a Virtual Environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

    Create a `.env` file in the root directory of the project and add your API keys:

    ```
    GROQ_API_KEY=your_groq_api_key
    GOOGLE_API_KEY=your_google_api_key
    ```

5. **Run the Application**:

    ```sh
    streamlit run app.py
    ```

    The app will be accessible at `http://localhost:8501`.

## Usage

1. **Upload a PDF**: Click on the file uploader to select a PDF document from your local system.
2. **Create Vector Store**: Click the "Create Vector Store from Uploaded PDF" button to process the document.
3. **Ask a Question**: Once the vector store is ready, enter your question in the text input field and get the answer.

## Technologies Used

- **Python**: The main programming language used.
- **Streamlit**: For creating the interactive web application.
- **Langchain**: For text splitting, document retrieval, and chain management.
- **Groq API**: For language model generation.
- **Google Generative AI**: For generating embeddings.
- **FAISS**: For efficient similarity search and clustering of the vector embeddings.
