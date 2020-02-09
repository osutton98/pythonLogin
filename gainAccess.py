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
from tkinter import *

def gui():
    window = Tk()
    window.title("Login ")
    window.geometry('350x200')

    #Welcome Label
    label = Label(window,text="Welcome")
    label.grid(column=0, row=0)


    # Username Entry Field
    uName = Entry(window, width=10)
    uName.grid(column=1, row=1)

    # Username Label
    uLabel = Label(window,text="Username: ")
    uLabel.grid(column=0, row=1)


    #Password Entry Field
    pWord = Entry(window, show ="*", width = 10)
    pWord.grid(column=1, row= 2)

    #Password Label
    pLabel = Label(window,text="Password: ")
    pLabel.grid(column=0, row=2)


    #Login Button
    btn=Button(window,text="Login", command=clicked)
    btn.grid(column=1, row = 3)

    # Create Account Button
    cAccount = Button(window,text="Create Account", command =cagui)
    cAccount.grid(column=1, row=4)

    window.mainloop()


def clicked():
    Login()

def cagui():
    global userinfo
    global cusername
    global cpassword
    global ufname
    global ulname
    global email
    create = Tk()
    create.title("Create Account")
    create.geometry("350x200")

    # Create username Label

    cuser = Label(create, text="Create Username: ")
    cuser.grid(column=0, row=0)


    # Created Username entry field
    cusername = Entry(create, width=10)
    cusername.grid(column=1, row=0)

    # Created Password Label
    cpass = Label(create,text="Create Password: ")
    cpass.grid(column=0, row=1)

    # Created Password Entry Field
    cpassword = Entry(create, show='*',width=10)
    cpassword.grid(column=1, row=1)

    # First Name Label
    ufname = Label(create, text = "First Name: ")
    ufname.grid(column=0, row=2)

    # Last Name Label
    ulname = Label(create, text= "Last Name: ")
    ulname.grid(column=0, row=3)

    # First Name Entry Field

    firstName= Entry(create,width=10)
    firstName.grid(column=1, row=2)

    # Last Name Entry Field
    lastName = Entry(create, width=10)
    lastName.grid(column=1, row=3)

    # Email Address Label

    uemail = Label(create,text="Email Address: ")
    uemail.grid(column=0, row=4)

    # Email Address Entry Field
    email = Entry(create, width=10)
    email.grid(column=1, row =4)

    userinfo={'Username':cusername,'Password':cpassword,'FirstName':firstName,'LastName':lastName,'Email':email}

    # Create Button
    created=Button(create,text="Create", command=gainAccess)
    created.grid(column=1,row=5)
    create.mainloop()


    return userinfo


def gainAccess():

    global firstName
    global lastName
    global email
    global userName
    global password
    global securityquestions
    global securityanswers
    global userInfo
    global userinfo
    global sq1
    global sqa1
    global sq2
    global sqa2
    global sq3
    global sqa3
    global cusername
    global cpassword
    global ufname
    global ulname
    print(ulname,ufname,cusername,cpassword,email)
    usersInfo = userinfo


    '''
    print("*Prompts in this program must be explicitly answered with yes or no*")
    answer = str.casefold(input("Would you like to create an account? "))
    if answer == "yes":
        firstName = input("What is your First Name? ")
        lastName = input("What is you Last Name?  ")
        email = input("Please enter your Email Address? ")
    elif answer == "no":
        print("Maybe next time :) ");
        breakpoint()
    else:
        print("Error please explicitly type yes or no for answer ");
        gainAccess()

    userInfo = {'Name': firstName+" "+lastName, 'Email':email}

    print("Welcome, next you will create a username ")
    time.sleep(1)
    userName=str.casefold(input("Please enter your username "))

    time.sleep(1)
    print("Nice Username!!!, Next you will need to enter a secure password ")
    time.sleep(1)

    password = input("Please enter your password ")
    userInfo.update({'userName': userName, 'password': password})
    print("Congratulations you have successfully created an Account!")
    print("In case you are locked out of your account you should create security questions!")'''
    answer = str.casefold(input("Would you like to add security questions?"))

    if answer=="yes":
        sq1=input("Please Enter Your First Security Question ")
        sqa1=input("Please Enter the Answer to your Security Question")
        securityquestions={'secuQuest1':sq1};
        securityanswers={'secuAns1':sqa1}
        answer = str.casefold(input("Would you like to add another Security Question? "))
        if answer =="yes":
            sq2 = input("Please Enter your Second Security Question ")
            sqa2= input("Please Enter the answer to your Second Security question ")
            securityquestions.update({'secuQuest2':sq2})
            securityanswers.update({'secuAns2':sqa2})
            answer = str.casefold(input("Would you like to add another Security Question? "))
            if answer == "yes":
                sq3 = input("Please Enter your Third Security Question ")
                sqa3 = input("Please Enter the answer to your Third Security question ")
                securityquestions.update({'secuQuest3': sq3})
                securityanswers.update({'secuAns3': sqa3})
                print("Thank you,  Your Security Questions have been added to your account! ")
    elif answer=="no":
        print("Ok , no security questions will be added to this account")
    else:
        print("Invalid input, yes or no must be explicitly typed ")

    answer = str.casefold(input("Would you like to log in now? "))
    if answer == "yes":
        Login()
    elif answer == "no":
        print("See you next time! ")
        breakpoint()
    else:
        print("Invalid input, yes or no must be explicitly typed ")
        Login()

def Login():
    global userInfo
    global sq1
    global sqa1
    global sq2
    global sqa2
    global sq3
    global sqa3
    i = 0
    username = str.casefold(input("Please enter username "))
    if username == userName:
        time.sleep(5)
        Password = input("Please enter password ")
        if Password == password:
            time.sleep(5)
            print("Access Granted")
        else:
            print("Incorrect Password Entered ")
            if i<3:
                i+=1
                if i==2:
                    print("Last Try ")
                Login()
            else:
                print("Access Denied ")
                print("Have You Forgotten your Password?, if you have added security questions added to "
                          "your account you may view and/or change your password")
                answer = str.casefold(input("Would you like to answer security question to gain access to your account?"))
                if answer =="yes":
                     SecurityQuestions()
                else:
                    breakpoint()

def SecurityQuestions():
    global securityquestions
    global securityanswers
    global userInfo
    global sq1
    global sqa1
    global sq2
    global sqa2
    global sq3
    global sqa3
    i=0;
    print(sq1)
    answer = str.casefold(input("Enter answer for Security Question 1 "))
    if answer == sqa1:
        if sq2 == True:
            print(sq2)
            answer = str.casefold(input("Enter answer for Security Question 2 "))
            if answer == sqa2:
                if sq3 == True:
                    answer = str.casefold(input("Enter answer for Security Question 3 "))
                    if answer == sqa3:
                        print(userInfo)
                else:
                    while i < 6:
                        i += 1
                        SecurityQuestions()
                        print('Incorrect answer')
                        if i == 5:
                            print('Last Try')
                breakpoint()

            else:
                while i < 6:
                    i += 1
                    SecurityQuestions()
                    print('Incorrect answer')
                    if i == 5:
                        print('Last Try')
            breakpoint()

        else:
            while i < 6:
                i += 1
                SecurityQuestions()
                print('Incorrect answer')
                if i == 5:
                    print('Last Try')
        breakpoint()

    else:
        while i<6:
            i+=1
            SecurityQuestions()
            print('Incorrect answer')
            if i == 5:
                print('Last Try')
    breakpoint()





gui()


