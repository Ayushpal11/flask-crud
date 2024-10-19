# CRUD Application

This is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API.

## Features

- RESTful API for User management
- MongoDB integration
- Docker support for easy deployment
- Password hashing for security

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- MongoDB (if not using Docker)

## Setup and Installation

### Using Docker

1. Clone the repository:
   ```
   git clone https://github.com/your-username/flask-mongodb-crud.git
   cd flask-mongodb-crud
   ```

2. Create a `.env` file in the root directory with the following content:
   ```
   MONGO_URI=mongodb://mongo:27017/user_db
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

3. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

The application will be available at `http://localhost:5000`.

### Without Docker

1. Clone the repository:
   ```
   git clone https://github.com/your-username/flask-mongodb-crud.git
   cd flask-mongodb-crud
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```
   MONGO_URI=mongodb://localhost:27017/user_db
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

5. Ensure MongoDB is running on your local machine.

6. Run the application:
   ```
   python run.py
   ```

The application will be available at `http://localhost:5000`.

## API Endpoints

- GET /users - Retrieve all users
- GET /users/<id> - Retrieve a specific user
- POST /users - Create a new user
- PUT /users/<id> - Update a user
- DELETE /users/<id> - Delete a user

## Testing

Used Postman to test the API endpoints. Ensured that all the appropriate HTTP endpoints and included any required data in the request body for POST and PUT requests.

## License

[MIT](https://choosealicense.com/licenses/mit/)
# flask-crud
