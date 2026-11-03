# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    1) asks the user to input 5 usernames (only alphanumeric characters will be input,
       no space, no underscore, ...) and stores them into a list
    2) prints out the list of usernames
    3) calls clean_users function to clean the list
    4) prints out the cleaned list"""
    # WRITE YOUR CODE BELOW
    _list = []
    for i in range(5):
        _list.append(input("Username: "))
    print(_list)
    print(clean_users(_list))



def clean_users(L):
    """• input: 1 parameter L -> type list (of strings) - each element in the list is a username
• return: a new cleaned list (see the rules below) -> type list (of strings)

The logic for cleaning the list of usernames is:
    • if the username contains c, g or z, it should be removed (the same with C, G or Z)
    • otherwise, keep it in the list

Note: your function should not modify the original list!"""
    # WRITE YOUR CODE BELOW
    Stack_list = [Funnel for Funnel in L if "c" not in Funnel and "g" not in Funnel and "z" not in Funnel and "C" not in Funnel and "G" not in Funnel and "Z" not in Funnel]
    return Stack_list


#Call the main() function, DO NOT CHANGE THE CODE BELLOW
if __name__ == '__main__':
    main()
