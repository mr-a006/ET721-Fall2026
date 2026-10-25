"""
Aqeel Hussain
Oct 23, 2026
homework 1: employee salary increase application
"""

import os
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# MySQL connection settings
# set MYSQL_PASSWORD in your local PowerShell session
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": os.environ.get("MYSQL_PASSWORD", ""),
    "database": "employee_data"
}

@app.route("/", methods=["GET", "POST"])
def index():
    employee_name = ""
    employee_id = ""
    salary = ""
    increase_salary = None
    message = None

    if request.method == "POST":
        employee_name = request.form.get("employee_name", "").strip()
        employee_id = request.form.get("employee_id", "").strip()
        salary = request.form.get("salary", "").strip()

        try:
            if not employee_name or len(employee_name) > 50:
                raise ValueError("Enter a name of 1 to 50 characters.")

            if not employee_id.isdigit() or len(employee_id) > 2:
                raise ValueError("Employee ID must contain no more than 2 digits.")

            if not salary.isdigit() or len(salary) > 6:
                raise ValueError("Salary must contain no more than 6 digits.")

            employee_id_num = int(employee_id)
            salary_num = int(salary)

            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()

            try:
                sql = """
                    INSERT INTO employee_salary
                    (employee_name, employee_id, salary)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(
                    sql,
                    (employee_name, employee_id_num, salary_num)
                )
                connection.commit()
            finally:
                cursor.close()
                connection.close()

            increase_salary = salary_num * 1.05

        except ValueError as error:
            message = str(error)
        except mysql.connector.Error as error:
            message = (
                "Database connection or insertion failed. "
                "Check your MySQL settings and database."
            )
            app.logger.error("MySQL error: %s", error)

    return render_template(
        "index_aqeel_hussain.html",
        employee_name=employee_name,
        employee_id=employee_id,
        salary=salary,
        increase_salary=increase_salary,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)