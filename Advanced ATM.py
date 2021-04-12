import time
from datetime import datetime as dt
import random

now = dt.now()
dateTime = now.strftime('%B %d, %Y %H:%M:%S')
number = random.randrange(1111111111, 9999999999)

database = {7237647892: ['David', 'Zane', 'Krane', 25000],
            2349542783: ['Daniel', 'Abraham', 'Dentor', 34000],
            7893123574: ['Islamiyat', 'Dede', 'Pringles', 12000],
            2345931234: ['Boris', 'Johnson', 'Ilena', 20000]}


def coloredText(text):
    print('\033[95m{}\033[00m'.format(text))


def initialization():
    print('\n       Welcome to Zuri Dev Bank')
    print("**humanity's last stand against inflation**\n")
    print(dateTime)
    time.sleep(5)
    option = int(input('Do you have an account with Zuri? \n'
                       " 1. Yes   2. No. I'll like to register  3. Exit\n"))
    if option == 1:
        login()
    if option == 2:
        register()
    if option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


def register():
    firstName = input('\nInput your first name\n')
    firstName = firstName.title()
    lastName = input('\nInput your last name\n')
    lastName = lastName.title()
    password = input('\nInput your password\n')
    password = password.title()
    money = 5000
    accountNumber = int(number)
    database[accountNumber] = [firstName, lastName, password, money]
    print('******Processing******')
    time.sleep(3)
    print(f'\nYour Zuri number is {accountNumber}\n'
          f' Your Zuri Password is {database[accountNumber][2]}')
    time.sleep(2)
    coloredText('\nYou are now officially a Zurite. Cheers'
                " You have been credited with $5000, a compliment of FGN's 'Digital Audacity' policy.")
    time.sleep(3)
    option = int(input('\nWould you like to login'
                       ' 1. Yes   2. No\n'))
    if option == 1:
        login()
    elif option == 2:
        exitt()
    else:
        print('Invalid option selected')
        exitt()


def exitt():
    coloredText('\nZuzuzuzuzuRiiiiiiii. No bank does it better.')
    time.sleep(3)


def logout():
    print('You are now logged out')


def login():
    global zuriNumber
    zuriNumber = int(input('\nInput your Zuri Number\n'))
    if zuriNumber in database:
        zuriPassword = input('Input your Zuri Password\n')
        zuriPassword = zuriPassword.title()
        if database[zuriNumber][2] == zuriPassword:
            bankingOperations()
        else:
            print('\nZuri Password Incorrect! Do you want to try again?')
            time.sleep(2)
            trial = input('1. Yes   2.No\n')
            trial = int(trial)
            if trial == 1:
                login()
            elif trial == 2:
                exitt()
            else:
                print('\nInvalid Option Selected')
                time.sleep(2)
                exitt()
    if zuriNumber not in database:
        print('Zuri Number incorrect! Do you want to try again?')
        time.sleep(2)
        trial = input('1. Yes   2.No\n')
        trial = int(trial)
        if trial == 1:
            print('Y')
        elif trial == 2:
            print('N')
        else:
            print('\nInvalid Option Selected')
            time.sleep(2)
            exitt()


def bankingOperations():
    print('\nThese are the Available Banking Operations.')
    print('1. Withdrawal 2. Deposit 3. Check Balance 4. Complaint\n')
    time.sleep(2)
    option = int(input('Please Select an Option\n'))
    print('\n******Processing******')
    time.sleep(2)
    if option == 1:
        withdrawal()
    elif option == 2:
        deposit()
    elif option == 3:
        balance()
    elif option == 4:
        complaint()
    else:
        print('\nInvalid Option Selected')
        bankingOperations()


def withdrawal():
    global withdrawal
    print('\nNote that Zuri will deduct a token of $1000 for every withdrawal.'
          ' Fighting inflation is a costly business.')
    withdrawal = input('\nHow much would you like to withdraw?\n$ ')
    withdrawal = int(withdrawal)
    if withdrawal > (database[zuriNumber][3] + 1000):
        hushpuppy()
    else:
        izzPlentyMaybe()


def hushpuppy():
    print(f"\nHushPuppy {database[zuriNumber][0]}!!!, the money wey you give us plus our"
          " charges no reach how much you wan withdraw nah.")
    time.sleep(3)
    print(
        f"\nZurite {database[zuriNumber][0]}, hustle more. Apply for more 2k jobs.")
    time.sleep(2)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


def izzPlentyMaybe():
    print('\n******Processing******')
    time.sleep(2)
    print(f"\nEsteemed Zurite, would you like to donate a token of 40% of your"
          " cash to aid FGN's fight against corruption")
    time.sleep(2)
    print("\n1. Definitely!! That's what loyal citizens do   2. NO!! I'm not a loyal"
          " citizen. Infact I'm from Niger.")
    option = input('\nPlease Select an Option\n')
    print('\n******Processing******')
    time.sleep(2)
    option = int(option)
    if option == 1:
        izzPlentyConfirmed()
    elif option == 2:
        izzPlentyScam()
    else:
        print('\nInvalid Option Selected')
        izzPlentyMaybe()


def izzPlentyConfirmed():
    print(f"\nEsteemed Zurite, take your cash of ${60/100 * withdrawal}"
          " Please do well by dropping a robust tip for our security outfit."
          " The economy's a bit hard, their salary is (30%) of all Zurite's tip.")
    time.sleep(8)
    balance = (database[zuriNumber][3] - withdrawal - 1000)
    print(f"\nYour balance stands at ${balance}")
    time.sleep(5)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        time.sleep(2)
        exitt()


def izzPlentyScam():
    print(f"\nTssk. Here's your ${withdrawal}. Please be notified that"
          " FGN's nation building policy compels us to report every unpatriotic"
          f" citizen. Drop (20%) of this cash which amounts to ${20/100 * withdrawal}"
          " with our security outfit if you want this transaction erased from our"
          " main server. And please do well by dropping a robust tip for our security"
          " outfit. The economy's a bit hard, their salary is (30%) of all Zurite's tip.")
    time.sleep(8)
    balance = database[zuriNumber][3] - withdrawal - 1000
    print(f"\nYour balanace stands at ${balance}")
    time.sleep(5)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        time.sleep(2)
        exitt()


def deposit():
    global deposit
    print('\nNote that Zuri will deduct a service charge of (20%) from your deposit.'
          ' Fighting inflation is a costly business.')
    deposit = input('\nHow much will you like to deposit?\n')
    deposit = int(deposit)
    print('\n******Processing******')
    time.sleep(2)
    balance = deposit + database[zuriNumber][3]
    print(f"\n${80/100 * deposit} has been successfully logged in. Your balanace"
          f" stands at ${balance}")
    time.sleep(5)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


def balance():
    print('\nChecking your balance will cost you $250.')
    time.sleep(3)
    balance = database[zuriNumber][3] - 250
    print(f'\nYour account balance is ${balance}')
    time.sleep(5)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


def complaint():
    print('\nThank you for contacting us.')
    time.sleep(2)
    print('\nLodging a complaint will cost you $1999.99')
    time.sleep(2)
    complaint = input('\nEsteemed Zurite, what issue will you like to report. please type in your complaint'
                      ' that we are sure will be an absolute waste of our time\n')
    print('\n******Processing******')
    time.sleep(4)
    print(f'\nZurite {database[zuriNumber][0].title()}, we received "{complaint}" from your account.'
          ' Resolving this kind of issue takes an average period of 6 months. Would you like'
          ' to pay an additional $15000 to give your complaint VIP priority? A VIP'
          ' categorized case takes an average of 24 hours to resolve.\n')
    time.sleep(8)
    print('\n1. Yes    2. No')
    option = input('\nPlease Select an Option\n')
    option = int(option)
    balance = database[zuriNumber][3]
    print('\n******Processing******')
    time.sleep(3)
    if option == 1:
        if balance < (15000 + 1999.99):
            izzScamVIP()
        else:
            izzVIP()
    elif option == 2:
        notVIP()


def izzScamVIP():
    print("\nTssk. You are too broke to be VIP'd. Please do more 2k jobs.")
    time.sleep(2)
    print('\nCheck back in 6 months')
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


def izzVIP():
    print('\nPlease check back in 24hrs')
    time.sleep(3)
    print(f'\nYour account balance is ${balance - 1999.99 - 15000}')
    time.sleep(5)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


def notVIP():
    print('\nPlease check back in 6months')
    time.sleep(3)
    print(f'\nYour account balance is ${balance - 1999.99}')
    time.sleep(5)
    print('\nWould you like to carry out another transaction?')
    option = int(input('1. Yes   2. Logout   3. Exit\n'))
    if option == 1:
        bankingOperations()
    elif option == 2:
        print('\nThanks for banking with us. We remain your surest bet against'
              ' inflation. Please remind your unbanked friends that FGN demands every'
              ' citizen should embrace the "Digital Audacity" policy by registering with a'
              ' FGN approved bank.')
        time.sleep(3)
        logout()
    elif option == 3:
        exitt()
    else:
        print('\nInvalid Option Selected')
        exitt()


initialization()
