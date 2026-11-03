"""
PROGRAMMING ASSIGNMENT 06
Filename: 'exercise2.py'

The file 'exercise2.py' is a module that offers functions for managing a list of users and their
passwords.
The usernames and passwords are stored in a list of lists that we will name userList.
Each inner list represents a username/password pair in that order [username, password].
"""

# Place your imports here if any


def valid_username(user, L):
    """
    1. Displays a message (Valid , Invalid or User Name Exists) depending on username rules
    2. Returns if the username is valid → type bool
    """
    # WRITE YOUR CODE BELOW
    validity = True
    for Traverse in L:
        if user == Traverse[0]:
            validity = False
            break
    if not validity:
        print("User Name Exists")
    elif len(user)<4:
        print("Invalid")
        #print("User Name too short")
        validity = False
    elif not user.isalnum():
        print("Invalid")
        #print("User Name contains illegal characters")
        validity = False
    elif user[0].isdigit():
        print("Invalid")
        #print("the first character cannot be a digit")
        validity = False
    if validity:
        print('Valid')
    return validity
def valid_password(pwd):
    """
    1. Displays a message ( Valid or depending on password rules
    2. Returns if the password is valid → type bool
    """
    # WRITE YOUR CODE BELOW
    validity = True
    _1uc, _1lc, _1d = False, False, False
    for letter in pwd:
        if letter.isupper():
            _1uc = True
        if letter.islower():
            _1lc = True
        if letter.isdigit():
            _1d = True
    if len(pwd) <10:
        print("Invalid")
        #print("Password too short")
        validity = False
    elif not pwd.isalnum():
        #print("Password contains illegal characters")
        print("Invalid")
    elif not _1uc:
        print("Invalid")
        #print("Passwords need at least 1 uppper case letter")
    elif not _1lc:
        print("Invalid")
        #print("Passwords need at least 1 lower case letter")
    elif not _1d:
        print("Invalid")
        #print("Passwords need at least 1 digit")

    if validity and _1uc and _1lc and _1d:
        print('Valid')
        return True
    else:
        return False


def add_user(L):
    """
    1. Continuously ask the user to input a username, until it is a valid one
    2. Ask for a password with the following logic:
        (a) continuously ask the user to input a password, until it is a valid one
        (b) ask the user to input the password again:
            • if the 2 passwords match → move to 3.
            • otherwise → display `Passwords do not match` and go back to 2.(a)
    3. Add the username/password pair to the userList and display User created
    """
    # WRITE YOUR CODE BELOW

    while 1:
        username = input("Enter Username: ")
        if valid_username(username, L):
            break
    while 1:
        password = input("Enter Password: ")
        if valid_password(password):
            confirm_pwd = input("Confirm Password: ")
            if password == confirm_pwd:
                break
            else:
                print("Passwords do not match")
    new_user = [username, password]
    L.append(new_user)
    print("User created")

    
# DO NOT CHANGE THE CODE BELLOW
if __name__ == '__main__':
    userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'],
    ['likeA', 'pwd3AAAAAA'], ['qwerty', 'pwd4QWERTY']]

    add_user(userList)

    print(userList)
