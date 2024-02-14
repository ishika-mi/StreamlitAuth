import os
import streamlit as st
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()
# Database connection parameters
db_params = {
    "dbname": os.environ.get('DATABASE_NAME'),
    "user": os.environ.get('BATABASE_USER'),
    "password": os.environ.get('DATABASE_PASSWORD'),
    "host": os.environ.get('DATABASE_HOST'),
    "port": os.environ.get('DATABASE_PORT'),
}

# Function to create tables
def create_tables():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

# Function to insert user data
def insert_user(username, password):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    insert_query = sql.SQL("INSERT INTO users (username, password) VALUES ({}, {});").format(
        sql.Literal(username),
        sql.Literal(password),
    )

    cursor.execute(insert_query)
    conn.commit()
    conn.close()

# Function to retrieve user data
def get_user(username):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    select_query = sql.SQL("SELECT * FROM users WHERE username = {};").format(sql.Literal(username))
    cursor.execute(select_query)

    user = cursor.fetchone()

    conn.close()
    return user

# Main app
def main():
    st.title("Login and Signup App")

    # Create tables if not exist
    create_tables()

    # Sidebar
    page = st.sidebar.radio("Navigation", ["Login", "Signup"])

    if page == "Signup":
        st.header("Signup")
        new_username = st.text_input("Username:")
        new_password = st.text_input("Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")

        if st.button("Signup"):
            if new_password == confirm_password:
                if existing_user := get_user(new_username):
                    st.error("Username already exists. Please choose a different one.")
                else:
                    insert_user(new_username, new_password)
                    st.success("Signup successful. Please login.")
            else:
                st.error("Passwords do not match. Please try again.")

    elif page == "Login":
        st.header("Login")
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

        if st.button("Login"):
            user = get_user(username)

            if user and user[2] == password:
                st.success("Login successful.")
            else:
                st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
