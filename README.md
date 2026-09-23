# FastAPI Full-Stack Blog Application

The project begins as a small REST API and gradually develops into a complete web application with server-rendered pages, CRUD operations, authentication, authorization, file uploads, pagination, password recovery, database migrations, automated tests, and cloud storage.

## Project Goals

I built this project to learn how the individual pieces of a real FastAPI application work together. Instead of creating isolated demo endpoints, I followed one application from its first route through database integration, security, cloud storage, and testing.

The main goals were to:

- Understand how FastAPI handles HTTP requests and responses
- Build and consume REST API endpoints
- Connect a frontend to a Python backend
- Store and query application data using SQLAlchemy
- Implement secure authentication and authorization
- Organize a growing application into maintainable modules
- Test API behavior and isolate external dependencies
- Understand the main concepts involved in preparing a FastAPI application for production

## Features

- Server-rendered frontend using Jinja2 templates
- REST API for managing users and blog posts
- Create, read, update, and delete operations
- Request and response validation with Pydantic
- Asynchronous routes and database operations
- User registration and login
- Password hashing and JWT-based authentication
- Route protection and resource ownership checks
- User profile and account management
- Image upload, validation, processing, and storage
- Paginated post listings
- Password reset using email and expiring tokens
- Background email tasks
- PostgreSQL database support
- Schema migrations with Alembic
- AWS S3 file storage through Boto3
- Automated API tests with pytest
- Mocked external services during testing

## Tech Stack

### Backend

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT authentication

### Frontend

- Jinja2
- HTML
- Bootstrap
- JavaScript
- Fetch API

### Files and external services

- Pillow for image processing
- AWS S3 for object storage
- Boto3 for communicating with AWS
- SMTP email for password recovery

### Testing

- pytest
- HTTPX

### Deployment topics studied but not implemented

- Docker
- Google Cloud Run
- Nginx
- Linux VPS
- HTTPS and custom-domain configuration



## What I Learned

1. FastAPI fundamentals

I learned how to create a FastAPI application, define routes with path-operation decorators, return JSON and HTML responses, and run the application with automatic reload during development. I also learned how FastAPI automatically generates interactive OpenAPI documentation.

1. Server-rendered pages with Jinja2

I learned how to serve an HTML frontend from the same FastAPI application using Jinja2 templates. This included passing backend data into templates, rendering dynamic pages, serving static assets, and understanding the difference between an API response and an HTML response.

1. Path parameters, validation, and error handling

I learned how path and query parameters are extracted from a request, validated through Python type hints, and exposed in the generated API documentation. I also learned to return suitable HTTP status codes and raise HTTPException when a requested resource does not exist or an operation is invalid.

1. Pydantic schemas

I learned to use Pydantic models as contracts at the API boundary. Separate request and response schemas prevent clients from submitting fields they should not control and prevent the API from accidentally exposing private data.

This clarified the difference between:

A request schema that validates incoming data

A response schema that controls serialized output

A SQLAlchemy model that represents persisted database data

1. SQLAlchemy models and relationships

I learned how to replace temporary in-memory data with persistent database storage. I created SQLAlchemy models, defined relationships between users and posts, managed database sessions, and queried related records.

I also learned why database models and Pydantic schemas solve different problems and should not be treated as interchangeable objects.

1. Complete CRUD operations

I implemented create, read, update, and delete operations and learned how HTTP methods communicate intent:

POST creates a resource

GET retrieves a resource

PUT replaces a resource

PATCH partially updates a resource

DELETE removes a resource

I also learned to handle missing records, validate updates, commit transactions, refresh ORM objects, and return appropriate response codes.

1. Synchronous and asynchronous code

I converted application and database operations to asynchronous code using async, await, AsyncSession, and an asynchronous database driver.

More importantly, I learned that asynchronous code is most useful for I/O-bound work such as database and network operations. It does not automatically make CPU-bound work faster, and a codebase should not use async merely because FastAPI supports it.

1. Organizing routes with APIRouter

I learned how to split routes into separate modules and register them with the main application using APIRouter. Prefixes, tags, and shared dependencies make route groups easier to maintain and keep main.py from becoming a landfill with decorators.

1. Connecting JavaScript to the API

I learned how a browser frontend communicates with FastAPI using JavaScript and the Fetch API. I used frontend forms to create, edit, and delete resources without requiring a full page reload, and handled success and error responses in the interface.

1. Authentication with JWT

I implemented registration and login using hashed passwords and JSON Web Tokens. I learned how credentials are verified, how tokens are created and signed, how clients send bearer tokens, and how the backend resolves the currently authenticated user.

I also learned that a JWT should contain only the minimum required claims and that passwords must never be stored in plain text.

1. Authorization and resource ownership

Authentication answers, "Who is making this request?" Authorization answers, "Is this user allowed to perform this action?"

I learned to protect routes with dependencies and verify ownership before allowing users to update or delete resources. Being logged in is not enough. Every protected operation must enforce the correct permission rule.

1. File uploads and image processing

I learned how to receive multipart file uploads with UploadFile, validate file type and size, process images with Pillow, and store a generated filename instead of blindly trusting the original client filename.

This also showed me why uploaded files must be treated as untrusted input.

1. Pagination

I implemented pagination using query parameters such as skip and limit. This prevents the server from loading every database row at once and gives clients a predictable way to request data in smaller pages.

1. Password reset flows and background tasks

I learned how password recovery works as a complete security flow rather than a single endpoint. The implementation includes secure random tokens, hashed token storage, expiration, single use, email delivery, and protection against email enumeration.

I also used FastAPI background tasks for work that should happen after the HTTP response, such as sending an email, without making the user wait for that operation to finish.

1. PostgreSQL and Alembic migrations

I moved the application from a local SQLite database to PostgreSQL and learned to manage schema changes with Alembic.

Instead of recreating tables or silently changing them at application startup, migrations provide a versioned and reviewable history of database changes. I learned the workflow of generating a revision, inspecting it, applying it, and committing it with the code that depends on it.

1. AWS S3 and Boto3

I moved uploaded files from local disk to AWS S3 using Boto3. This taught me why container and server filesystems should not be treated as permanent storage and how object storage separates uploaded data from the application process.

I also learned to keep AWS credentials and bucket configuration outside the source code.

1. API testing

I learned to test routes with pytest and HTTPX, use fixtures for reusable setup, override FastAPI dependencies, and isolate database state between tests.

I wrote tests for successful requests as well as validation failures, authentication failures, forbidden operations, pagination, file uploads, and other edge cases. External services such as S3 were mocked so that tests remained repeatable and did not depend on real cloud resources.

1. VPS deployment concepts, not implemented

I studied the major pieces involved in deploying a web application to a Linux server:

Connecting securely with SSH keys

Configuring environment variables and production dependencies

Running the application as a managed service

Using Nginx as a reverse proxy

Restricting network access with a firewall

Enabling HTTPS with an SSL certificate

Connecting a custom domain

This helped me understand what platforms such as Render and Vercel normally hide behind their deployment interface. I did not perform this deployment because I did not have hosting credits available.

1. Docker and Google Cloud Run deployment concepts, not implemented

I did not implement this part because I did not have cloud credits available. It remains a planned extension rather than a completed feature.

## Application Structure

The exact filenames may evolve as the project grows, but the application is organized around these responsibilities:

```text
.
├── app/
│   ├── main.py              # FastAPI application and router registration
│   ├── config.py            # Environment-based configuration
│   ├── database.py          # Engine, session factory, and DB dependency
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic request and response models
│   ├── routers/             # Route modules grouped by feature
│   ├── services/            # Email, storage, and other application services
│   ├── templates/           # Jinja2 templates
│   └── static/              # CSS, JavaScript, and images
├── alembic/                 # Database migration history
├── tests/                   # Unit and API tests
├── alembic.ini
└── README.md
```



## Running the Project Locally

Update the module path or dependency command below if your local project uses different names.

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-directory>
```



### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```



### 3. Install dependencies

```bash
uv sync
```



### 4. Configure environment variables

Create a .env file and provide the values used by the application:

```dotenv
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/database_name
SECRET_KEY=replace-with-a-long-random-value
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_SERVER=
MAIL_PORT=587

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_BUCKET_NAME=
```

Never commit the real .env file or production credentials.

### 5. Apply database migrations

```bash
alembic upgrade head
```



### 6. Start the development server

```bash
uv run fastapi dev main.py
```

After startup, open:

- Web application: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)



## Running Tests

```bash
uv run pytest
```

Run with more detail:

```bash
uv run pytest -v
```



## Security Notes

- Passwords are hashed before storage.
- Protected routes require a valid authenticated user.
- Update and delete operations verify resource ownership.
- Password-reset tokens are time-limited, stored as hashes, and usable only once.
- Uploaded files are validated before processing or storage.
- Secrets and cloud credentials are loaded from environment variables.
- Tests use isolated configuration and mocked external services.



## Possible Improvements

- Add role-based access control
- Add refresh-token rotation and token revocation
- Add rate limiting to login and password-reset endpoints
- Add structured logging and request IDs
- Add health and readiness endpoints
- Add continuous integration for linting and tests
- Add monitoring and error tracking
- Replace background tasks with a durable task queue for critical jobs
- Improve frontend accessibility and error feedback
- Dockerize the application
- Deploy the container to Google Cloud Run or deploy the application to a VPS

