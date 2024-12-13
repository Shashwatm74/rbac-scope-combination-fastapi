# RBAC Scope Combination with FastAPI

A FastAPI application that implements Role-Based Access Control (RBAC) with customizable scope combinations. This project aims to provide a modular and scalable approach to managing roles and permissions in modern web applications.

---

## Features

- **Role Management**: Define and manage roles with specific scopes and permissions.
- **Scope Validation**: Validate user scopes to ensure proper access control.
- **Database Integration**: Store roles and scopes in a relational database.
- **Error Handling**: Robust error handling for database operations and permission checks.
- **API Endpoints**: Easy-to-use API for managing roles and validating permissions.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.9 or later
- PostgreSQL or compatible database

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Shashwatm74/rbac-scope-combination-fastapi.git
   cd rbac-scope-combination-fastapi
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:

   Create a `.env` file in the root directory with the following:

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
   ```

5. **Apply Database Migrations**:

   ```bash
   alembic upgrade head
   ```

6. **Run the Application**:

   ```bash
   uvicorn main:app --reload
   ```

---

## API Endpoints

### Roles Endpoints

- **GET /roles/**: Fetch all roles
- **POST /roles/**: Create a new role

### Example Request Body for Creating a Role

- **Authorization**: Give the authorization header as the name of the role you want to work with.

```json
{
  "name": "judge",
  "can_create_roles": false,
  "scopes": ["view_submissions", "manage_submissions"]
}
```

### Example Response

```json
{
  "message": "Role created successfully"
}
```

### Permissions Validation

- **GET /validate-permissions/**: Validate a user's permissions for specific scopes.

---

## Project Structure

```
directory_name/
├── main.py               # FastAPI app entry point
├── auth/
│   ├── dependencies.py   # Role and scope checking logic
│   ├── models.py         # Role and user models
│   └── utils.py          # Utility functions for role and scope validation
├── roles/
│   ├── endpoints.py      # Role management endpoints
│   ├── models.py         # Role models
│   └── services.py       # Business logic for role operations
├── db/
│   └── database.py       # Database connection and helpers
├── submissions/
│   ├── endpoints.py      # Submission management endpoints
│   ├── models.py         # Submission models
│   └── services.py       # Business logic for submission operations
├── .env                  # Environment file for sensitive information
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore file to prevent sensitive files from being committed
└── README.md


```

---

## Error Handling

This application includes robust error handling for various scenarios:

- **Database Errors**: Logs errors and returns user-friendly messages.
- **Permission Errors**: Returns HTTP 403 for unauthorized actions.
- **Validation Errors**: Ensures correct input structure for all endpoints.

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Psycopg2 Documentation](https://www.psycopg.org/)

---

## Contact

For issues, questions, or suggestions, please open an issue on this repository or contact the project owner at [Shashwat's GitHub Profile](https://github.com/Shashwatm74).
