from db.database import get_db_connection

def get_all_submissions():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT title, description, submitted_by FROM submissions")
            submissions = cursor.fetchall()
            return [{"title": row[0], "description": row[1], "submitted_by": row[2]} for row in submissions]
    finally:
        conn.close()

def create_submission(submission: dict, submitted_by: str):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO submissions (title, description, submitted_by)
                VALUES (%s, %s, %s)
                """,
                (submission["title"], submission["description"], submitted_by),
            )
            conn.commit()
            return {"message": "Submission created successfully"}
    finally:
        conn.close()
