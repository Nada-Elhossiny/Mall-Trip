from random import randint
import time
def inputagain():
    print("You did not input an appropriate entry. Please try again!")

def mainmenu():
    goodReply1=0
    print('Choose where you want to go!')
    print('The options are...')
    time.sleep(1)
    print('A= Clothing store')
    time.sleep(1)
    print('B= Math fun room')
    time.sleep(1)
    print("C= Nurse's office")
    time.sleep(1)
    print("D= Escape room")
    time.sleep(1)
    print("X= Exit")
    
    while goodReply1==0:
        try:
            Option1 = input()
            Option1 = Option1.upper() 
            if Option1== "A" or Option1=="B" or Option1== "C" or Option1== "D" or Option1 == "X":
                goodReply1=1
                return(Option1)
            else:
                print('Please select one of the options')
        except ValueError:
            inputagain()

def trial():
    print("Make a guess")
    global guess 
    guess = int(input())

name = "Nada"
print("Hello, nice to meet you. My name is", name)
time.sleep(2)
print("What is your name?")
Theirname = input()
print("Hello", Theirname, "welcome to the mall! Today, you will get the chance to have fun doing various activities.")
print("Are you excited?! (Y/N)")
excited = input()
excited = excited.upper()  
if excited == "Y":
    print("GREAT! Let's get started")
else:
    print("We don't need that negativity here, you're no fun")
    print("You are being redirected to the exit door :)")
    exit()
print('To start, you must choose the amount of money you wish to spend today.')
goodreply=0
while goodreply==0:
    try:
        money = input()
        money= int(money)
        if money>0 and money<99999:
            goodreply=1
        else:
            print("Select an amount between 0 and 99999")
    except ValueError:
        print("Select an amount between 0 and 99999")
print("You're all set! You have $",money,"to spend :)")
time.sleep(1)
Option1=mainmenu().upper()
while Option1!='X':
    if Option1 == "A":
        print("Fun choice! Who doesn't love shopping!")
        options=["Earrings","Black dress pants","Blazer","Jeans","Sunglasses","Purse","Heels","Magic carpet"]
        prices=[10,60,70,40,12,100,25,1000]
        option_price={}
        for x in range(0,len(options)):
            option_price[options[x]]= prices[x]
        print("Welcome to our ~designer~ store. Haha just kidding, it's a regular store.")
        print("The amount of money you have avaliable to spend is $",money)
        print("Here is a list of clothing options & their prices:")
        order=1
        for x in options:
            print("Item Number:"+str(order)+"    Item Name:"+str(x) .ljust(17) +"    Price:"+str(option_price[x]))
            order+=1
        print("Please enter the number of the item you would like to select. Select 9 to complete your shopping experiece and check out:")
        money= int(money)
        selected_items=[]
        remaining_amount=money
        while money > 0:
            selection=input(int())
            selection=int(selection)
            if (selection <1 or selection >9):
                print("Please enter a number between 1-9")
            elif int(selection)== 9:
                print("Thank you for shopping with us. Here is your reciept")
                for item in selected_items:
                    print("-" + str(item))
                print("The amount of money you spent is: "+ str(money - remaining_amount)+ ". The amount of money you have remaining is: "+str(remaining_amount))
                break
            else:
                price=prices[selection-1]
                if remaining_amount-price>0:
                    selected_items.append(options[selection-1])
                    remaining_amount=remaining_amount-price
                    print("You have selected the item: "+options[selection-1])
                    print("The amount of money you have left is: "+ str(remaining_amount))
                elif remaining_amount-price==0:
                    print("You have run out of money. Enter '9' to view your reciept.")
                else:
                    print("You don't have enough money to purchase this item!")
        Option1=mainmenu().upper()
    elif Option1 == "B":
        print("I see you enjoy math:)")
        print("This activity is very simple. I am thinking of a number between 1 and 100. Guess that number in the fewest number of tries possible!")
        print("You only get 10 guesses though!")
        answer = randint(1, 100)
        answer = int(answer)
        for i in range(10):
            trial()
            if guess == answer:
                print('You guessed it!')
                break
            elif guess < answer:
                print('Too low')
            else:
                print('Too high')
                
        Option1=mainmenu().upper()
    elif Option1 == "C":
        print("Welcome to the nurse's office!")
        time.sleep(1)
        print("Enter some basic information about your health and I will analyze it:)")
        goodReply1=0
        print('Please enter your heart rate:')
        goodReply5=0
        while goodReply5==0:
            try:
                heartrate = int(input())
                if 0<=heartrate <= 200:
                    goodReply5=1
                else:
                    print('Please enter an Integer between 0 and 200. Try again!')
            except ValueError:
                inputagain()
        print('Enter your systolic (upper number) blood pressure')
        goodReply6=0
        while goodReply6==0:
            try:
                systolicpressure= int(input())
                if 0<=systolicpressure<=200:
                    goodReply6=1
                else:
                    print('Please enter an Integer between 0 and 200. Try again!')
            except ValueError:
                inputagain()
        print('Enter your diastolic (lower number) blood pressure')
        goodReply7=0
        while goodReply7==0:
            try:
                diastolicpressure= int(input())
                if 0<=diastolicpressure<=200:
                    goodReply7=1
                else:
                    print('Please enter an Integer between 0 and 200. Try again!')
            except ValueError:
                inputagain()
        if 60 <= heartrate <= 100:
            print('You are within the normal range! Generally, a lower heart rate correlates to more efficient heart function')
        elif heartrate >= 100:
            print('You are tachycardic. Your heart rate is way too fast')
            print('This is generally normal during exercise or when under a lot of stress')
            print('Try to relax/remain calm/practice deep breathing to lower your heart rate')
        elif heartrate >= 0: 
            print('You are bradycardic. Your heart rate is too slow')
            print('This is common during deep sleep')
            print('Try a quick exercise to raise your heart rate')
        else:
            inputagain()
        if systolicpressure <= 120:
            print('Your systolic blood pressure is within the normal category') 
        elif 120 <= systolicpressure <= 129:
            print('Your systolic blood pressure is within the elevated category')
        elif 130 <= systolicpressure <= 139:
            print('Your systolic blood pressure is within the first stage of hypertension')
        elif 140 <= systolicpressure <= 180:
            print('Your systolic blood pressure is within the second stage of hypertension')
        elif systolicpressure >= 180:
            print('Your systolic pressure indicates that you are experiencing a hypertensive crisis, contact a doctor immediately')
        else:
            inputagain()
        if diastolicpressure <=80:
            print('If your systolic pressure is normal, your current diastolic pressure indicates that you are within the normal range')
            print('If your systolic pressure is elevated, your current diastolic pressure indicates that you are within the elevated blood pressure range')
        elif 80<diastolicpressure<=89:
            print('Your diastolic pressure is within the first stage of hypertension')
        elif 90<=diastolicpressure<=120:
            print('Your diastolic pressure is within the second stage of hypertension')
        elif 120>= diastolicpressure:
            print('Your diastolic pressure indicates that you are experiencing a hypertensive crisis, contact your doctor immediately')
        else:
            inputagain()
            
        Option1=mainmenu().upper()
    elif Option1 == "D":
        print('Welcome to the escape room!')
        time.sleep(1)
        print('You will be asked a bunch of scenario questions, if you answer all the questions correctly you will proceed :)')
        time.sleep(2)
        print('if not... you will die')
        print('Are you ready to start?! (Y/N)')
        goodReply2=0
        while goodReply2 == 0:
            Option2 = input()
            Option2 = Option2.upper()
            if Option2 == "Y" or Option2== 'N':
                goodReply4=1
            else:
                inputagain()
            if Option2=="Y":
                print('Nice job! You have entered the escape room. Get ready for the first scenario')
                time.sleep(2)
                print('If a child was playing with a book and tore out pages 7,8,27,98,99. How many pages were torn out?')
                print('Options: 2,3,4,5')
                goodreply3=0
                while goodreply3==0:
                    answer1= input()
                    if answer1== "2" or "3" or "4" or "5":
                        goodreply3= 1
                    else:
                        print('Invalid entry, please try again')
                    if answer1 == "4":
                        print("You're a smart cookie! Congrats, you have progressed to the next round")
                        time.sleep(1)
                        print("Billy’s mother had five children. The first was named Lala, the second was named Lele, the third was named Lili, the fourth was named Lolo. What was the fifth child named?")
                        answer2= input()
                        if answer2 == "Billy":
                            print("Legendary! You're on a roll.")
                            time.sleep(1)
                            print('Next question :)')
                            time.sleep(1)
                            print('Which is heavier? A pound of feathers or a pound of rocks?')
                            print('Options: feathers, rocks, both')
                            goodreply4=0
                            while goodreply4== 0:
                                answer3 = input()
                                if answer3 == "feathers" or "rocks" or "both":
                                    goodreply4 = 1
                                else:
                                    inputagain()
                                if answer3== "both":
                                    print('Correct again!')
                                    time.sleep(1)
                                    print('When you divide 30 by 1/2 then add 10, what do you get?')
                                    answer4 = input()
                                    if answer4 == "70" or "seventy":
                                        print("And you're a math genius too? Wow!")
                                        print("1 question to go! Don't mess up!")
                                        time.sleep(1)
                                        print("What's full of holes but can still hold water?")
                                        answer5= input()
                                        if answer5 == "A sponge" or "sponge":
                                            print('YAY YOU ESCAPED')
                                        
                                        else:
                                            print('Unfortunately, that is not the correct answer. It was sponge!')
                                            print('Game over')
                                            exit()
                                    elif answer4 == "25" or "twenty-five" or "twenty five":
                                        print("You were so close, but remember DIVIDE by 1/2 not multiply")
                                        print("Game over")
                                        exit()
                                    else:
                                        print("The answer was 70")
                                        print("Game over")
                                        exit()
                                elif answer3== "feathers" or "rocks":
                                    print('Incorrect. They both weigh the same!')
                                    print('Game over')
                                    exit()
                                else:
                                    print('Invalid entry')
                            else:
                                print("Unfortunately, that is incorrect. The correct answer was Billy.")
                                print("Game over :(")
                                exit()
                    elif answer1=="2" or "3" or "5":
                        print('Unfortunately, that is not the right answer. 7 & 8 are on the same page, all the other ones are seperate answers.')
                        print('Therefore, the correct answer was 4. Game over :(')
                        exit()
                    else:
                        print('Invalid entry')
            elif Option2=="N":
                print('Booooooooooooring. Get out of here')
                exit()
            else:
                print('Please select either Y or N')
        Option1=mainmenu().upper()
    print('Good Bye! We hope you enjoyed your time here with us :)')
    exit()