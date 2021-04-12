import time 
from datetime import datetime as dt

now = dt.now()
dateTime = now.strftime('%B %d, %Y %H:%M:%S')

print('       Welcome to Zuri Dev Bank')
print("**humanity's last stand against inflation**\n")
print(dateTime)

time.sleep(5)

print('\nInput your Details')

zuriNames = ['Micheal', 'Jakande', 'Lizzy', 'Roku', 'Zane']
zuriPasswords = ['Michealp', 'Jakandep', 'Lizzyp', 'Rokup', 'Zanep']
credit = [120987, 12000, 15000, 23098, 54000]

name = input('Zuri Name\n')
name = name.title()
print('\n******Verifying******')
time.sleep(3)

if name in zuriNames:
    password = input('\nZuri Password \n')
    password = password.title()
    userId = zuriNames.index(name)
    balance = credit[userId]
    balance = int(balance) 

    print('\n******Verifying******')
    if password == zuriPasswords[userId]:
        time.sleep(3)
        print(f'\nWelcome Back, Zurite {name.title()}\n')
        print(dateTime)

        time.sleep(2)
        print('\nThese are the Available Banking Operations.')
        print('1. Withdrawal 2. Deposit 3. Check Balance 4. Complaint\n')
        time.sleep(2)
        option = input('Please Select an Option\n')
        option = int(option)
        print('\n******Processing******')

        time.sleep(2)
        if option == 1:
            print('\nNote that Zuri will deduct a token of $1000 for every withdrawal.'
            ' Fighting inflation is a costly business.')
            withdrawal = input('\nHow much would you like to withdraw?\n$ ')
            withdrawal = int(withdrawal)
            if withdrawal > (balance + 1000):
                print(f"\nHushPuppy {name.title()}, the money wey you give us plus our"
                " charges no reach how much you wan withdraw nah.")
                time.sleep(3)
                print(f"\nZurite, hustle more. Apply for more 2k jobs.")
            else:
                print('\n******Processing******')
                time.sleep(2)
                print(f"\nEsteemed Zurite, would you like to donate a token of 40% of your"
                " cash to aid FGN's fight against corruption")
                time.sleep(2)
                print("\n1. Definitely!! That's what loyal citizens do 2. NO!! I'm not a loyal"
                " citizen. Infact I'm from Niger.")
                option = input('\nPlease Select an Option\n')
                print('\n******Processing******')
                time.sleep(2)
                option = int(option)
                if option == 1:
                    print(f"\nEsteemed Zurite, take your cash of ${60/100 * withdrawal}"
                    " Please do well by dropping a robust tip for our security outfit."
                    " The economy's a bit hard, their salary is (30%) of all Zurite's tip.")
                    time.sleep(8)
                    print(f"\nYour balanace stands at ${balance - 1000 - withdrawal}")
                    time.sleep(5)
                    print('\nThanks for banking with us. We remain your surest bet against'
                    ' inflation. Please remind your unbanked friends that FGN demands every'
                    ' citizen should embrace the "Digital Audacity" policy by registering with a'
                    ' FGN approved bank.')
            
                elif option == 2:
                    print(f"\nTssk. Here's your ${withdrawal}. Please be notified that"
                    " FGN's nation building policy compels us to report every unpatriotic"
                    f" citizen. Drop (20%) of this cash which amounts to ${20/100 * withdrawal}"
                    " with our security outfit if you want this transaction erased from our"
                    " main server. And please do well by dropping a robust tip for our security"
                    " outfit. The economy's a bit hard, their salary is (30%) of all Zurite's tip.")
                    time.sleep(8)
                    print(f"\nYour balanace stands at ${balance - 1000 - withdrawal}")
                    time.sleep(5)
                    print('\nThanks for banking with us. We remain your surest bet against'
                    ' inflation. Please remind your unbanked friends that FGN demands every'
                    ' citizen should embrace the "Digital Audacity" policy by registering with a' 
                    ' FGN approved bank.')
    
        elif option == 2:
            print('\nNote that Zuri will deduct a service charge of (20%) from your deposit.'
            ' Fighting inflation is a costly business.')
            deposit = input('\nHow much will you like to deposit?\n')
            deposit = int(deposit)
            print('\n******Processing******')
            time.sleep(2)
            print(f"\n${80/100 * deposit} has been successfully logged in. Your balanace"
            f" stands at ${deposit + balance}")
            time.sleep(5)
            print('\nThanks for banking with us. We remain your surest bet against'
            ' inflation. Please remind your unbanked friends that FGN demands every'
            ' citizen should embrace the "Digital Audacity" policy by registering with a' 
            ' FGN approved bank.')

        elif option == 3:
            print('\nChecking your balance will cost you $250.')
            time.sleep(3)
            print(f'\nYour account balance is ${balance - 250}')
            time.sleep(5)
            print('\nThanks for banking with us. We remain your surest bet against'
            ' inflation. Please remind your unbanked friends that FGN demands every'
            ' citizen should embrace the "Digital Audacity" policy by registering with a' 
            ' FGN approved bank.')

        elif option == 4:
            print('\nThank you for contacting us.')
            time.sleep(2)
            print('\nLodging a complaint will cost you $1999.99')
            time.sleep(2)
            complaint = input('\nEsteemed Zurite, what issue will you like to report. please type in your complaint that we are'
            ' sure will be an absolute waste of our time\n')
            print('\n******Processing******')
            time.sleep(4)
            print(f'\nZurite {name.title()}, we received "{complaint}" from your account.' 
            ' Resolving this kind of issue takes an average period of 6 months. Would you like'
            ' to pay an additional $15000 to give your complaint VIP priority? A VIP'
            ' categorized case takes an average of 24 hours to resolve.\n')
            time.sleep(8)
            print('\n1. Yes 2. No')
            option = input('\nPlease Select an Option\n')
            option = int(option)
            print('\n******Processing******')
            time.sleep(3)
            if option == 1:
                if balance < (15000 + 1999.99):
                    print("\nTssk. You are too broke to be VIP'd. Please do more 2k jobs.")
                    time.sleep(2)
                    print('\nCheck back in 6 months')
                    print('\nThanks for banking with us. We remain your surest bet against inflation. Please remind your unbanked friends'
                    ' that FGN demands every citizen should embrace the "Digital Audacity" policy by registering with a' 
                    ' FGN approved bank.')
                else:
                    print('\nPlease check back in 24hrs')
                    time.sleep(3)
                    print(f'\nYour account balance is ${balance - 1999.99 - 15000}')
                    time.sleep(5)
                    print('\nThanks for banking with us. We remain your surest bet against'
                    ' inflation. Please remind your unbanked friends that FGN demands every'
                    ' citizen should embrace the "Digital Audacity" policy by registering with a' 
                    ' FGN approved bank.')

            elif option == 2:
                print('\nPlease check back in 6months')
                time.sleep(3)
                print(f'\nYour account balance is ${balance - 1999.99}')
                time.sleep(5)
                print('\nThanks for banking with us. We remain your surest bet against'
                ' inflation. Please remind your unbanked friends that FGN demands every'
                ' citizen should embrace the "Digital Audacity" policy by registering with a' 
                ' FGN approved bank.')


    else:
        print('Password Error!! Please Try Again.')

else:
    print(f'\nError!! Zuri Name, {name.title()} Not Found. Please Try Again.')