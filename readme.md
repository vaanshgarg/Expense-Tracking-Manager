# Expense Management System

This project is an expense management system that consists of a  Streamlit frontend application and a FastAPI backend server.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend code.
- **tests/**: Contains the test cases for both frontend adn backend.
- **requirements.txt**: Lists the required Python Packages.
- **README.md** Provides an overview and instruction for the project.


## Setup Instruction

1. **Clone the respository**:
    ``` bash
   git clone https://github.com/vaanshgarg/expense-management-system
   cd expense-management-system
   ```
1. **Install dependencies:**:
    ```commandline
   pip install -r requirements.txt
   ```
2. **Run the FastAPI server:**:
    ```commandline
    uvicorn server.server:app --reload
   ```
3. **Run the Streamlit app:**:
    ```commandline
   streamlit run frontend/app.py
   ```


