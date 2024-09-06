   # Async Book Management System (Flask)

This is an asynchronous book management system built using Flask, SQLAlchemy with asyncio support, and PostgreSQL. It includes book CRUD operations, user management, authentication, a simple ML-based book recommendation system, and book summary generation using a Llama model.

## Features
-	Book Management: Add, retrieve, update, and delete books in the PostgreSQL database.
-	Asynchronous Operations: Fully asynchronous interactions with the PostgreSQL database using SQLAlchemy [asyncio] and asyncpg.
-	Book Summaries: Use the Llama3 model to generate AI-based summaries for books based on their content.
-	User Reviews and Ratings: Users can leave reviews and ratings for books.
-	Book Recommendations: Recommend books based on genre and average rating.
-	Basic Authentication: Secure access to routes using token-based authentication (JWT).
-	CI/CD: Integrated with GitHub Actions for automated testing and deployment.

## Tech Stack
-	Backend Framework: Flask (Python)
-	Database: PostgreSQL (async via asyncpg and SQLAlchemy)
-	Machine Learning Model: Llama3 for AI-based book summaries
-	Authentication: JSON Web Token (JWT)
-	API: RESTful API
-	Cloud Deployment: AWS (with Docker, optional)
-	Version Control: Git, GitHub

## Setup

### Requirements
- Docker
- Docker Compose

### Running the Application

1. ## Clone the repository:
   ```bash
   git clone https://github.com/Narsi2Pydev/book-management.git
   cd async-book-management-system-flask
   
## 2. API Documentation
Authentication
POST /auth/login: Log in and retrieve a JWT token.
POST /auth/register: Register a new user.
Book Management
GET /books: Retrieve all books.
POST /books: Add a new book.
GET /books/<book_id>: Get details of a specific book.
PUT /books/<book_id>: Update a book.
DELETE /books/<book_id>: Delete a book.

## 3. Book Summaries (AI-Generated)
POST /summaries: Generate a summary for a book using the Llama3 AI model.

## 4.User Reviews and Ratings
POST /books/<book_id>/review: Add a review to a book.
GET /books/<book_id>/reviews: Get all reviews for a book.

## 5.Book Recommendations
GET /recommendations: Get book recommendations based on user preferences (genre and rating).


## Docker Deployment
  ```bash
   docker build -t book-management.
  ```

## Run Docker Container
  ```bash
   docker-compose up
  ```

## Continuous Integration and Deployment
This project uses GitHub Actions for CI/CD. The deploy.yml file under .github/workflows/ automates testing and ensures that all changes are tested before being merged.


