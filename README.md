
# Blogging Platform API

## Project Overview

Blogging Platform API is a RESTful API built using Python, Flask, and PostgreSQL.

It allows users to create, retrieve, update, and delete blog posts using HTTP requests. SQLAlchemy is used to interact with the PostgreSQL database.


## Features

- Create new blog posts
- Retrieve all blog posts
- Retrieve a single blog post by ID
- Update existing blog posts
- Delete blog posts
- Input validation for title and content
- PostgreSQL database integration
- Persistent data storage using SQLAlchemy
- JSON-based API responses


## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- SQLAlchemy
- python-dotenv
- Postman (API Testing)
- Git and GitHub


## Project Structure

Blogging_Platform_API/
│
├── app.py
├── db.py
├── models.py
├── .gitignore
├── requirements.txt
└── README.md


## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RAHUL1332002/Blogging-Platform-API
```

### 2. Navigate to the project folder

```bash
cd Blogging_Platform_API
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment (Windows)

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```


## Database Configuration

This project uses PostgreSQL as its database.

1. Create a PostgreSQL database named `blog_db`.
2. Create a `.env` file in the project root directory.
3. Add the following database configuration to the `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=blog_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Replace `your_password` with your PostgreSQL password.

Make sure the `.env` file is not uploaded to GitHub because it contains sensitive database credentials.


## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | `/posts` | Create a new blog post |
| GET | `/posts` | Retrieve all blog posts |
| GET | `/posts/<post_id>` | Retrieve a single blog post |
| PUT | `/posts/<post_id>` | Update an existing blog post |
| DELETE | `/posts/<post_id>` | Delete a blog post |

All API responses are returned in JSON format.


## API Testing

The API was tested using Postman.

The following operations were tested:

- Creating a blog post using POST.
- Retrieving all blog posts using GET.
- Retrieving a single blog post by ID.
- Updating an existing blog post using PUT.
- Deleting a blog post using DELETE.
- Testing invalid input and missing post IDs.
    

## Author

Rahul Singh

This project was developed as part of my learning journey in Python backend development.

GitHub: [Rahul Singh](https://github.com/RAHUL1332002)
