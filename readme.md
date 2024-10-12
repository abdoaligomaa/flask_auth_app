# User Authentication and Management API

This project is a Flask-based RESTful API that provides user authentication and management functionality. It includes features such as user registration, login, and role-based access control.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [API Documentation](#api-documentation)

## Features
- User registration with password hashing
- User login with JWT token generation
- Role-based access control (admin and regular users)
- Protected routes for authenticated users
- Admin-only routes

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7+
- pip (Python package manager)

## Setup
Follow these steps to get your development environment set up:

1. Clone the repository:
   ```
   git clone project url from this repo
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up your environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   DATABASE_URL=your_database_url_here
   SECRET_KEY=your_secret_key_here
   ```

6. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Running the Application
To run the application, use the following command:
```
flask run
```
The API will be available at `http://localhost:5000`.

## API Endpoints

### Public Endpoints
- `POST /register`: Register a new user
- `POST /login`: Authenticate a user and receive a JWT token
- `GET /visitor`: Public endpoint accessible to all

### Protected Endpoints
- `GET /all_users`: Accessible to all authenticated users
- `GET /admin_only_page`: Accessible only to admin users

For detailed information about request/response formats, please refer to the API Documentation.

## Authentication
This API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints:

1. Obtain a token by logging in via the `/login` endpoint.
2. Include the token in the `Authorization` header of your requests:
   ```
   Authorization: Bearer <your_token_here>
   ```

## API Documentation
[postman docs](https://documenter.getpostman.com/view/27578637/2sAXxS7Wrg)
