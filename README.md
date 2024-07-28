# AI_Document_Summarize


### Project Setup Instructions

#### Prerequisites

Before starting, make sure you have the following installed on your machine:
- **Git**: To clone the repository.
- **Docker**: To containerize and run your application.

#### Step 1: Clone the Repository

First, clone the repository to your local machine:
```
git clone https://github.com/Ashu-01/AI_Document_Summarize
cd AI_Document_Summarize
```

#### Step 2: Backend Setup

Navigate to the `backend` directory and ensure the `main.py` and `requirements.txt` files are present.
`backend/main.py` should contain your FastAPI application code.
```
docker-compose up --build
```
#### Step 3: Frontend Setup

Ensure your React installed.
Move to the `frontend` directory
and run following command in terminal
```
npm install axios
npm start
```
#### Step 4: Build and Run the Containers

Use Docker Compose to build and run the containers:
```
docker-compose up --build
```

#### Step 5: Access the Application

- **Frontend**: Open [http://localhost:3000](http://localhost:3000) in your web browser.
- **Backend**: The backend API will be available at [http://localhost:8000](http://localhost:8000).



## Approach and Challenges

### Approach
1. Set up a FastAPI backend with file upload and summarization capabilities.
2. Set up a React frontend to interact with the backend.
3. Use Docker and Docker Compose for local development and deployment.

### Challenges
- **File Handling:** Managing different file formats and ensuring they are correctly read and processed.
- **Model Integration:** Integrating and optimizing a pre-trained LLM for local deployment.
- **CORS Issues:** Ensuring smooth communication between frontend and backend services.
- **Performance:** Optimizing Docker setup for efficient development workflow.

### Solutions
- Used  `PyMuPDF` to handle different file formats.
- Used `transformers` library to integrate the LLM.
- Configured CORS settings in FastAPI to allow requests from the frontend.
- Structured Docker Compose file to streamline service dependencies and caching.

## Bibliography

1. [FastAPI Documentation](https://fastapi.tiangolo.com/)
2. [Docker Documentation](https://docs.docker.com/)
3. [Transformers Documentation](https://huggingface.co/transformers/)
4. [React Documentation](https://reactjs.org/)
5. [PyMuPDF Documentation](https://pymupdf.readthedocs.io/en/latest/)

