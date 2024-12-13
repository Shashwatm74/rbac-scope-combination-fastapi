from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from db.database import get_db_connection

api_key_header = APIKeyHeader(name="X-API-Key")

def get_current_user_role(api_key: str = Security(api_key_header)):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM roles WHERE name = %s", (api_key,))
            role = cursor.fetchone()
            if not role:
                raise HTTPException(status_code=403, detail="Invalid API Key")
            return {
                "name": role[1],
                "can_create_roles": role[2],
                "scopes": role[3].split(","),
            }
    finally:
        conn.close()
