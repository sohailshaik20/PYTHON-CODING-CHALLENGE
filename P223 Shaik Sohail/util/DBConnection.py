import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        # Connect to the new database InsuranceManagement
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=SOHAIL\SQLEXPRESS02;"
            "DATABASE=LoanManagementSystem;"
            "Trusted_Connection=yes;"
        )
        return pyodbc.connect(connection_string)