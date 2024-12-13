from db.database import get_db_connection

def fetch_all_roles():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name, can_create_roles, scopes FROM roles")
            roles = cursor.fetchall()
            return [{"name": row[0], "can_create_roles": row[1], "scopes": row[2].split(",")} for row in roles]
    finally:
        conn.close()

def create_role(role_data: dict):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO roles (name, can_create_roles, scopes)
                VALUES (%s, %s, %s)
                """,
                (role_data["name"], role_data["can_create_roles"], ",".join(role_data["scopes"])),
            )
            conn.commit()
            return {"message": "Role created successfully"}
    finally:
        conn.close()
