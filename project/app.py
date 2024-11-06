import pymysql
import hashlib

# Connect to the MySQL database
def create_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='tejaswini',  # Replace with your MySQL username
            password='Teju@1811',  # Replace with your MySQL password
            database='user_management'
        )
        # print("Database connection successful.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: '{e}'")
        return None

# Register a new user
def register_user(username, phone_number, email, password):
    connection = create_connection()
    if connection is None:
        print("Connection failed. Could not register user.")
        return

    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
    print("Password hashed successfully.")

    try:
        # Insert the user data into the database
        cursor.execute(
            "INSERT INTO users (username, phone_number, email, password) VALUES (%s, %s, %s, %s)",
            (username, phone_number, email, hashed_password)
        )
        connection.commit()
        print("Registration is successful!")
    except pymysql.MySQLError as e:
        print(f"Error inserting user data: '{e}'")
    finally:
        cursor.close()
        connection.close()
        print("Database connection closed.")

# Login a user
def login_user(username, password):
    connection = create_connection()
    if connection is None:
        print("Connection failed. Could not log in.")
        return

    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password

    try:
        # Check if the user exists and the password matches
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, hashed_password)
        )
        result = cursor.fetchone()
        if result:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    except pymysql.MySQLError as e:
        print(f"Error during login: '{e}'")
    finally:
        cursor.close()
        connection.close()
        print("Database connection closed.")

# Main program with registration and login menu
def main():
    while True:
        print("\nWelcome to our page")
        print("1. Login")
        print("2. Register")
        choice = input("Enter an Option: ")

        if choice == '2':
            print("\nRegistration")

            username = input("Username: ")
            phone_number = input("Phone number: ")
            email = input("Mail Id: ")

            # Password confirmation
            while True:
                password = input("Password: ")
                confirm_password = input("Re-enter password: ")
                if password == confirm_password:
                    break
                else:
                    print("Passwords do not match. Try again.")

            # Register user with collected details
            register_user(username, phone_number, email, password)

        elif choice == '1':
            print("\nLogin")
            username = input("Username: ")
            password = input("Password: ")

            # Attempt to log in the user
            login_user(username, password)
        else:
            print("Invalid option. Please select either 1 or 2.")

        # Ask if the user wants to continue or exit
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break

# Run the program
if __name__ == "__main__":
    main()
