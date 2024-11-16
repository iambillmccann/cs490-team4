# AI-Powered Resume Analyzer and Job Matcher

Project uses ChatGPT AI to take inputs (Resumes) and return feedback.

## Project Members:

- Arya Mazandarani
- Kyrylo Honcharov
- Daniel Olson
- Omoze Oyarebu
- Alen Kylyshbek
- Nifesimi Akintola

<a href="https://trello.com/b/KFmJz5Q3/cs490-ai-powered-resume-analyzer-and-job-matcher">Trello Board</a>

# How To Initialize And Run The FastAPI Endpoints

1. First you will need to initialize a local python environment in the root directory of the project. Run `python3 -m venv venv` while
   in <b>cs490-team4</b> folder.
2. After initializing the virtual environment, it should create a folder in your directory called <b>venv</b>.
3. Next, if the virtual environment did not activate for you, run `source venv/bin/activate`.
4. In your cli, you should see <b>(venv)</b> at the beginning of the prompt.
5. Then, run `pip install -r requiremenets.txt`. This will install all the packages necessary to run the project.
6. To run the API, in your console type in `fastapi dev backend/app.py`. This should enable the FastAPI endpoints on port 8000. To see the
   swagger with all the explanation head to <b>localhost:8000/docs</b>.

# How To Test The Backend Endpoints

1. After initializing, in your console, run the command `pytest tests/backend` to run all of the backend python tests.


<i>Good Luck Coding!</i>