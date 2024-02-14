# StreamlitAuth
This Streamlit project implements a simple Login and Signup application with a PostgreSQL database backend. Users can create new accounts (signup) and login using their credentials.
## Features
### Signup: Users can create new accounts by providing a unique username and password.
### Login: Existing users can log in using their username and password.
## Dependencies
### Streamlit: UI development library for creating web applications with Python.
### Psycopg2: PostgreSQL adapter for Python, used for database interactions.
### dotenv: Loads environment variables from a .env file.
PostgreSQL Database: Requires a PostgreSQL database to store user data.

## Project Setup
1. Clone the repository:
    ```bash
    git clone <REPOSITORY URL>
    cd StreamlitAuth
2. Install the required libraries by running the following command:

   ```bash
   pip install -r requirements.txt
3. Run streamlit
    ```bash  
    streamlit run main.py