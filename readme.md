# 💰 Expense Analytics Dashboard

<p align="center">

# 💸 Expense Analytics Dashboard

*A modern full-stack expense tracking application built with **Streamlit**, **FastAPI**, **MySQL**, **Pandas**, and **Plotly** for managing and visualizing personal expenses.*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=for-the-badge&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📌 Overview

Managing personal expenses shouldn't be complicated.

The **Expense Analytics Dashboard** helps users record daily expenses, organize them into categories, and gain insights through interactive charts and analytics.

The project follows a **Full Stack Architecture**:

- 🎨 **Frontend:** Streamlit
- ⚡ **Backend:** FastAPI
- 🗄 **Database:** MySQL
- 📊 **Visualization:** Plotly
- 🐍 **Language:** Python

---

# ✨ Features

### 📝 Expense Management
- Add daily expenses
- Update existing expenses
- Delete expenses
- Notes for every transaction
- Date-wise expense tracking

### 📊 Analytics Dashboard

#### 📈 Category Wise Analytics
- Percentage of spending
- Total expense by category
- Interactive Plotly charts

#### 📅 Monthly Analytics
- Month-wise expenditure
- Total spending comparison
- Year filtering

### ⚡ Backend API
- RESTful FastAPI APIs
- Pydantic Validation
- MySQL CRUD Operations

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | MySQL |
| Charts | Plotly |
| Data Processing | Pandas |
| Validation | Pydantic |
| Language | Python |

---

# 📂 Project Structure

```text
Expense-Analytics-Dashboard
│
├── backend
│   ├── db_helper.py
│   ├── server.py
│   ├── logging_setup.py
│   └── __init__.py
│
├── frontend
│   ├── app.py
│   ├── add_update_tab.py
│   ├── analytics_by_category.py
│   ├── analytics_by_months.py
│   └── __init__.py
│
├── tests
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/vaanshgarg/expense-management-system.git

cd expense-management-system
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

## Start FastAPI Backend

```bash
uvicorn backend.server:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

FastAPI Docs

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📸 Application Screenshots

## 🏠 Expense Management

> Save this image as:

```
images/dashboard1.png
```

```markdown
![Expense Management](images/dashboard1.png)
```

---

## 📊 Category Wise Analytics

Save image as

```
images/dashboard2.png
```

```markdown
![Category Analytics](images/dashboard2.png)
```

---

## 📈 Monthly Analytics

Save image as

```
images/dashboard3.png
```

```markdown
![Monthly Analytics](images/dashboard3.png)
```

---

# 📡 API Endpoints

## Expenses

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/expenses/{date}` | Fetch expenses by date |
| POST | `/expenses/{date}` | Add or Update Expenses |

---

## Analytics

| Method | Endpoint |
|---------|----------|
| POST | `/analytics/` |
| POST | `/analytics/months/` |

---

# 📊 Dashboard Modules

### 💰 Add / Update Expenses

✔ Date Selection

✔ Expense Amount

✔ Expense Category

✔ Notes

✔ Save Expenses

---

### 📊 Category Analytics

✔ Start Date

✔ End Date

✔ Category Breakdown

✔ Spending Percentage

✔ Interactive Bar Chart

---

### 📈 Monthly Analytics

✔ Select Year

✔ Monthly Expense Analysis

✔ Total Monthly Spending

✔ Interactive Plotly Visualization

---

# 🔮 Future Improvements

- Authentication
- User Accounts
- Export Reports (PDF/Excel)
- Dark Mode
- Budget Tracking
- AI Spending Suggestions
- Expense Prediction using Machine Learning
- Mobile Responsive UI

---

# 📦 Requirements

```
streamlit
fastapi
uvicorn
mysql-connector-python
pandas
plotly
requests
pytest
pydantic
```

---

# 👨‍💻 Developed By

## Vansh Garg

### Connect with me

- 💼 LinkedIn: https://www.linkedin.com/in/vaanshgarg/
- ⭐ GitHub: https://www.github.com/vaanshgarg

If you like this project,

⭐ **Star the Repository**

🍴 **Fork the Repository**

🤝 **Contribute**

---

# 📄 License

This project is licensed under the **MIT License**.

---

<p align="center">

### ⭐ If you found this project useful, don't forget to give it a Star ⭐

Made with ❤️ using Python, Streamlit & FastAPI

</p>
