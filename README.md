# Mini SaaS API Gateway

A robust, production-ready REST API backend for a SaaS application built with **FastAPI**. This backend handles secure user authentication, JWT session token management, database migrations, and isolated task management workflows.

## 🚀 Key Features

*   **Secure Authentication:** User registration and login utilizing cryptographically hashed passwords.
*   **JWT Bearer Security:** Completely custom HTTP Bearer token scheme for secure endpoint locking.
*   **Database Management:** Relational data persistence powered by **PostgreSQL** and orchestrated by **SQLAlchemy ORM**.
*   **Automated Migrations:** Database schema tracking and changes managed incrementally via **Alembic**.
*   **User Data Isolation:** Built-in multi-tenant logic ensuring users can only read/write their own data rows.
*   **Interactive Documentation:** Auto-generated interactive API playgrounds via Swagger UI.

---

## 🛠️ Technology Stack

*   **Framework:** [FastAPI](https://tiangolo.com)
*   **Database:** [PostgreSQL](https://postgresql.org)
*   **ORM:** [SQLAlchemy](https://sqlalchemy.org)
*   **Migrations:** [Alembic](https://sqlalchemy.org)
*   **Server Runtime:** [Uvicorn](https://uvicorn.org)

---

## 📦 Directory Structure

```text
├── app/
│   ├── core/
│   │   └── deps.py        # Global token authentication guards
│   ├── db/
│   │   ├── database.py    # SQLAlchemy connection engine & session
│   │   └── deps.py        # public get_db session generators
│   ├── models/
│   │   └── models.py      # PostgreSQL declarative table definitions
│   ├── routers/
│   │   ├── auth.py        # Registration and login JSON routes
│   │   └── tasks.py       # Authenticated user CRUD operations
│   ├── schemas/
│   │   └── schemas.py     # Pydantic data serialization schemas
│   └── main.py            # FastAPI initialization entrypoint
├── alembic/               # Database migration generation history files
├── .env                   # Local configuration keys & DATABASE_URL
└── requirements.txt       # Environment package installations
```

---

## 🔧 Local Development Installation

### 1. Clone the Project & Navigate
```bash
git clone https://github.com
cd mini-saas-api
```

### 2. Set Up the Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Local Environment Variables
Create a `.env` file in the root project directory:
```ini
DATABASE_URL=postgresql://your_user@localhost:5432/mini_saas
SECRET_KEY=your_generated_32_byte_cryptographic_secret
ALGORITHM=HS256
```

### 4. Initialize Database and Migrations
Ensure your local PostgreSQL server is running, then apply your database schema state:
```bash
alembic upgrade head
```

### 5. Launch the Server
```bash
uvicorn app.main:app --reload
```
The server will spin up on **`http://127.0.0.1:8000`**.

---

## 📖 API Documentation & Testing

Once your Uvicorn runtime server boots up, you can view the fully interactive, clean **HTTP Bearer layout documentation page** at:

👉 **`http://127.0.0`**

### Recommended Testing Flow:
1. Submit a JSON payload to `POST /auth/register` to create an account.
2. Submit your credentials to `POST /auth/login` to receive a `bearer` access token string.
3. Click the green **Authorize** padlock button at the top right of your Swagger page.
4. Paste the raw token code directly into the field box and hit authorize.
5. You can now test protected user endpoints like `GET /tasks` or `POST /tasks` safely!

