import pyodbc


def record_payment(conn, student_id, amount, payment_date):
    try:
        cursor = conn.cursor()

        # Retrieve Jane Johnson's student record from the database based on her student ID
        cursor.execute("SELECT * FROM students WHERE Student_ID = ?", (student_id,))
        student_record = cursor.fetchone()

        if student_record:
            # Record the payment information in the database
            cursor.execute("INSERT INTO payments (Student_ID, Amount, Payment_Date) VALUES (?, ?, ?)",
                           (student_id, amount, payment_date))
            print("Payment recorded successfully.")

            # Update Jane's outstanding balance in the database based on the payment amount
            cursor.execute("UPDATE students SET Outstanding_Balance = Outstanding_Balance - ? WHERE Student_ID = ?",
                           (amount, student_id))
            print("Outstanding balance updated successfully.")

            conn.commit()
        else:
            print("Student not found.")

    except pyodbc.Error as e:
        print(f"Error recording payment: {e}")
        conn.rollback()
    finally:
        cursor.close()


try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=server_name;DATABASE=SISDB; ')

    # Jane Johnson's details
    student_id = 101
    payment_amount = 500.00
    payment_date = '2023-04-10'

    record_payment(conn, student_id, payment_amount, payment_date)

except pyodbc.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()
