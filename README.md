# Interactive Document Q&A Chatbot

## Overview

This project provides an interactive document Q&A chatbot that allows users to upload PDF documents, which are then processed to create vector embeddings. Once the embeddings are ready, users can ask questions related to the content of the uploaded document. The application is built with Flask and leverages several libraries for document processing and natural language understanding.

## Features

- **PDF Upload**: Upload a PDF document for processing.
- **Vector Embeddings Creation**: Convert the document into vector embeddings using Google Generative AI.
- **Question Answering**: Ask questions about the content of the processed document.
- **Loading Indicator**: Visual feedback during PDF processing.
- **Flash Messages**: Notifications for various actions and errors.

## Requirements

- Python 3.12
- Flask
- werkzeug
- langchain_groq
- langchain
- langchain_core
- langchain_community
- langchain_google_genai
- dotenv
- faiss-cpu
- PyPDF2

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your API keys:

    ```ini
    GROQ_API_KEY=your_groq_api_key
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Upload a PDF document, and once processed, you will be able to ask questions about the document content.

## API Endpoints

- `POST /upload`
  - **Description**: Upload a PDF document for processing.
  - **Request**: Form-data with a `file` field (PDF file).
  - **Response**: JSON message indicating success or failure.

- `POST /ask`
  - **Description**: Ask a question related to the uploaded document.
  - **Request**: Form-data with a `question` field (text).
  - **Response**: Rendered HTML with the answer to the question.

## Development

### Directory Structure

- `app.py`: Main application file with Flask routes and logic.
- `templates/`: HTML templates for rendering the frontend.
- `static/`: Static files such as CSS and JavaScript.

### Notes

- Make sure the `uploads` directory exists or is created automatically by the application.
- Ensure that your `.env` file contains the correct API keys for accessing the models.

## Contributing

Feel free to submit issues and pull requests to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or comments, please contact [your-email@example.com](mailto:your-email@example.com).
