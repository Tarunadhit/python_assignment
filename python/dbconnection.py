import pyodbc
import propertyUtil


class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                connection_string = propertyUtil.PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Connected Successfully")
            except pyodbc.Error as e:
                print(f"Connection failed: {e}")
        else:
            print("Connection already established")

        return DBConnection.connection


if __name__ == "__main__":
    conn = DBConnection.get_connection()
    if conn:
        conn.close()
