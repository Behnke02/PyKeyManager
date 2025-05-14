import pandas
from string import printable
import secrets
import cryptography.fernet
PASSWORD_FILE = "passwords.csv"
COLUMN_NAMES = ['Website', 'Password', 'Current']
PASSWORD_CHARACTERS = printable
THIRTY_TWO_BYTES = 256

def main():
    #Read password file
    try:
        password_df = pandas.read_csv(PASSWORD_FILE, index_col=0)
    except pandas.errors.EmptyDataError:
        first_time_setup()
        #After the csv file is created, re-read it into working dataframe
        password_df = pandas.read_csv(PASSWORD_FILE, names=COLUMN_NAMES, index_col=0)
    
    #Print introductory list
    print("Welcome to PasswordManager!", end="\n\n")
    print("Please select an option from the list below:", end="\n\n")

    #Main Execution Loop
    while True:
        #Display options (Retrieve, Create, Generate, Update, Delete, Exit)
        print("Retrieve: Fetch a password you need (R)")
        print("Create: Store a new password (C)")
        print("    NEW: Generate a new password and store (G)")
        print("Update: Update an already-existing password (U)")
        print("Delete: Delete a password entry (D)")
        print("    NOTE: If you're just changing an expired password, you can UPDATE instead and it will store any previous passwords for a website.")
        print("Exit: Exit the program (E)")

        #Wait for user input
        option = input("Select your option (R, C, G, U, D, E): ").upper()
        print()
        if option == 'R':
            retrieve_password(password_df)
        elif option == 'C':
            create_entry(password_df)
        elif option == 'G':
            generate_entry(password_df)
        elif option == 'U':
            update_entry(password_df)
        elif option == 'D':
            delete_entry(password_df)
        elif option == 'E':
            print("Updating password file")
            #Password file does not update unless user ends program
            password_df.to_csv(PASSWORD_FILE, header=COLUMN_NAMES)
            break
        else:
            print("ERROR: Invalid Input! Please try again.")
    print("Exiting Program.  Enjoy your day!")

def first_time_setup():
    print("No password file detected.")
    if input("Are you a new user? (Y/N) ").upper() == "Y":
        print("Entering First-Time Configuring Mode")
        print("To get started, please enter your first password")
        website = input("What website is this password associated with? ")
        password = input("Enter your password here: ")
        temp_df = pandas.DataFrame([[website, password, True]], columns=COLUMN_NAMES)
        temp_df.to_csv(PASSWORD_FILE)
    else:
        print("Possible error encountered.  Shutting down program.")
        print("Please check that a password file exists and try again.")
        quit()

def retrieve_password(password_df : pandas.DataFrame) -> None:
    print("To retrieve a password for a website, please enter the website.")
    print("NOTE: Website entries are case-specific.")
    #NOTE: Could probably force upper-case on websites in the future.
    website = input("Please enter here: ")
    
    #master_key = input("Please enter your General-Purpose passcode to retrieve the right password")

    #Retrieve all active/expired passwords associated with website
    print(password_df.query('Website == @website'))
    
    input("Press \'Enter\' to return to menu")
    print('', end="\n\n")

def create_entry(password_df : pandas.DataFrame) -> None:
    print("Creating new password entry")
    website = input("What website is this password associated with? ")
    password = input("Enter your password here: ")
    #fernet = cryptography.fernet.Fernet(input("Please enter your General-Purpose passcode to encrypt the password: ").zfill(THIRTY_TWO_BYTES).encode(encoder='base64'))
    #password = fernet.encrypt(password.encode())

    #Append row to dataframe
    password_df.loc[-1] = [website, password, True]
    password_df.index += 1
    password_df.sort_index()
    print()

def generate_entry(password_df : pandas.DataFrame):
    print("Generating a new secure password")
    website = input("What website is this password associated with? ")
    #TODO: Enforce password requirements (Uppercase letter, number, special character, etc.)
    password = ''.join(secrets.choice(PASSWORD_CHARACTERS) for i in range(15))
    password_df.loc[-1] = [website, password, True]
    password_df.index += 1
    password_df.sort_index()
    print()

def update_entry(password_df : pandas.DataFrame) -> None:
    print("Updating existing password entry")
    website = input("What website is this password associated with? ")
    password = input("Enter your password here: ")

    try:
        password_df.loc[password_df.Website == website, 'Current'] = False
        password_df.loc[-1] = [website, password, True]
        password_df.index += 1
        password_df.sort_index()
    except KeyError:
        print("No website matches found.")
        if input("Would you like to create a new entry? ").upper == "Y":
            create_entry(password_df)
    print()

def delete_entry(password_df : pandas.DataFrame) -> None:
    print("WARNING: Deleting an entry is permanent and cannot be reversed.")
    print("All passwords associated with a specific website will be deleted upon completion")
    print("If a password is accidentally deleted, you will have to manually re-enter it")

    if input("Are you sure you wish to continue? (Y/N) ").upper() == "Y":
        website = input("What website entry do you wish to delete? ")
        try:
            password_df.drop(password_df[password_df.Website == website].index, inplace=True)
        except KeyError:
            print("No website matches found.")
    else:
        print("Deletion aborted.  Returning to main options list.")
    print()

if __name__ == "__main__":
    main()