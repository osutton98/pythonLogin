'''The Purpose of this Program is to implement the simple concepts learned in by Python Basics bootcamp course.
        This Program will consist of asking a user to create a username, password. then prompt them  and ask
        if they would like to login to the program if so it will ask for credentials, they are allowed to try 3 times before
         the program will end.

         1. Stretch goals will include email capture and sending email if correct security questions are answered

         2. GUI

         3. Two factor authentication with Twillio, and text message login notifications

         4. Password Constraints

         5. Set of all user information then store to database.

         6. Email Authentication before account Creation

         7. Password Timeouts

         '''
import time
def gainAccess():
    global firstName
    global lastName
    global email
    global userName
    global password


    answer = str.casefold(input("Would you like to create an account? (Type yes or no)"))
    if answer == "yes":
        firstName= input("What is your First Name?")
        lastName= input("What is you Last Name")
        email= input("Please enter your Email Address ")
    elif answer == "no":
        print("Maybe next time :)");
        breakpoint()
    else:
        print("Error please explicitly type yes or no for answer");
        gainAccess()

    userInfo = {'Name':firstName+" "+lastName, 'Email':email}

    print("Welcome, next you will create a username /n")
    time.sleep(5)
    userName=str.casefold(input("Please enter your username"))

    time.sleep(5)
    print("Nice Username!!!, Next you will need to enter a secure password")
    time.sleep(5)

    password = input("Please enter your password")
    userInfo.update({'userName': userName, 'password': password})
    print("Congratulations you have successfully created an Account!")
    answer = str.casefold(input("Would you like to log in now?"))
    if answer == "yes":
        Login()
    elif answer == "no":
        print("See you next time!")
        breakpoint()
    else:
        print("Invalid input, yes or no must be explicitly typed")
        Login()
def Login():
    global userInfo
    i = 0
    username = str.casefold(input("Please enter username"))
    if username == userName:
        time.sleep(5)
        Password = input("Please enter password ")
        if Password == password:
            time.sleep(5)
            print("Access Granted")
        else:
            print("Incorrect Password Entered")
            if i<3:
                i+=1
                if i==2:
                    print("Last Try")
                    Login()
                else:
                    print("Access Denied")

