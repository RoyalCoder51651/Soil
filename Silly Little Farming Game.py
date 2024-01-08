# Silly Little Farming Game
# Coded By Royal
print("Welcome To Soil, A Silly Little Farming Game Made By @RoyalCoder51651")
import random
lane1 = []
lane2 = []
lane3 = []
lane4 = []
lane5 = []
level = 1
day = 0
nloop = 0
dayspassed = 0
iterator = 0
limit = 8
license = 21
season = "🍃"
xpearning = 0
dayearnings = 0
siter = 0
sloop = 0
money = 5
xp = 0
def pestsalive(pest):
    if (w2e(pest) not in lane1 and w2e(pest) not in lane2 and w2e(pest) not in lane3 and w2e(pest) not in lane4 and w2e(pest) not in lane5):
        return(True)
def printfarm():
    global list1
    global list2
    global list3
    global list4
    global list5
    print("------------------------------------------------")
    print(*lane1, sep=' | ')
    print("------------------------------------------------")
    print(*lane2, sep=' | ')
    print("------------------------------------------------")
    print(*lane3, sep=' | ')
    print("------------------------------------------------")
    print(*lane4, sep=' | ')
    print("------------------------------------------------")
    print(*lane5, sep=' | ')
    print("------------------------------------------------")
def dragonfruit(pest):
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    global dayearnings
    if (w2e(pest) in lane1 and w2e("Dragon") in lane1):
        lane1.remove(w2e(pest))
        return (True)
    if (w2e(pest) in lane2 and w2e("Dragon") in lane2):
        lane2.remove(w2e(pest))
        return (True)
    if (w2e(pest) in lane3 and w2e("Dragon") in lane3):
        lane3.remove(w2e(pest))
        return (True)
    if (w2e(pest) in lane4 and w2e("Dragon") in lane4):
        lane4.remove(w2e(pest))
        return (True)
    if (w2e(pest) in lane5 and w2e("Dragon") in lane5):
        lane5.remove(w2e(pest))
        return (True)
def w2e(word):
    match word:
        case "Evergreen":
            return ("🌲")
        case "Fly":
            return ("🪰")
        case "Winter":
            return ("❄️")
        case "Summer":
            return ("☀️")
        case "Spring":
            return ("🍃")
        case "Fall":
            return ("🍂")
        case "Starfruit":
            return ("⭐")
        case "Dragon":
            return ("🐉")
        case "Beetle":
            return ("🪲")
        case "Pumpkin":
            return ("🎃")
        case "Christmas Tree":
            return ("🎄")
def earnings(input):
    global money
    global day
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    global xpearning
    global season
    global dayearnings
    for item in input:
        if (item == w2e('Evergreen') and day %2 == 1):
            if (season == w2e("Winter")):
                dayearnings += 2
            elif (season == w2e("Summer")):
                dayearnings -= 1
            dayearnings += 3
        elif (item == w2e("Starfruit")):
            if (season == w2e("Spring")):
                xpearning += 2
            else:
                xpearning += 1
        elif (item == w2e("Pumpkin")):
            if (season == w2e("Fall")):
                dayearnings += 2
            else:
                dayearnings += 1
        elif (item == w2e("Dragon")):
            if (dragonfruit("Fly") == True):
                if (season == w2e("Winter")):
                    dayearnings += 0
                elif (season == w2e("Summer")):
                    dayearnings += 2
                else:
                    dayearnings += 1
            if (dragonfruit("Beetle") == True):
                if (season == w2e("Winter")):
                    dayearnings += 1
                elif (season == w2e("Summer")):
                    dayearnings += 3
                else:
                    dayearnings += 2
        elif (item == w2e("Beetle")):
            dayearnings -= 1
        elif (item == w2e("Christmas Tree") and season == w2e("Winter")):
            dayearnings += 10
            xpearnings += 3
def pestwipe(pest):
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    global xp
    while pest in lane1:
        lane1.remove(pest)
        xp += 2
    while pest in lane2:
        lane2.remove(pest)
        xp += 2
    while pest in lane3:
        lane3.remove(pest)
        xp += 2
    while pest in lane4:
        lane4.remove(pest)
        xp += 2
    while pest in lane5:
        lane5.remove(pest)
        xp += 2
def laser_shovel(lane, item,):
    global xp
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    while item in lane:
        lane.remove(item)
def shovel(lane, item):
    global xp
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    try:
        if (lane == '1'):
            lane1.remove(item)
        elif (lane == '2'):
            lane2.remove(item)
        elif (lane == '3'):
            lane3.remove(item)
        elif (lane == '4'):
            lane4.remove(item)
        elif (lane == '5'):
            lane5.remove(item)
    except:
        print("Choice Not Recognized, Sorry")
def swat(lane):
    global xp
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    try:
        for item in lane:
            if (item == w2e("Fly") or item == w2e("Beetle")):
                lane.remove(item)
                xp += 1
    except:
        print("Choice Not Recognized, Sorry")
def pests(pest):
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    if (len(lane1) != limit):
        lane1.append(pest)
    if (len(lane2) != limit):
        lane2.append(pest)
    if (len(lane3) != limit):
        lane3.append(pest)
    if (len(lane4) != limit):
        lane4.append(pest)
    if (len(lane5) != limit):
        lane5.append(pest)
def placement(item):
    global lane1
    global lane2
    global lane3
    global lane4
    global lane5
    global loop
    print("Where Would You Like To Place Your New Plant (Type 1-5)")
    while(loop == True):
        choice = input()
        if (choice == '1' and len(lane1) != limit):
            lane1.append(item)
            break
        elif (choice == '2' and len(lane2) != limit):
            lane2.append(item)
            break
        elif (choice == '3' and len(lane3) != limit):
            lane3.append(item)
            break
        elif (choice == '4' and len(lane4) != limit):
            lane4.append(item)
            break
        elif (choice == '5' and len(lane5) != limit):
            lane5.append(item)
            break
        elif(len(lane1) == limit or len(lane2) == limit or len(lane3) == limit or len(lane4) == limit or len(lane5) == limit):
            print("That Lane Is Too Full. Select Another Lane")
        else:
            print('Choice Not Recognized')

# MAIN GAMEPLAY
input("Press Enter To Start Game. Make Sure To Renew Your Farming License Every 21 Days")
loop = True
while (loop == True):
    event = random.randint(1,20)
    if (day != 0):
        if (event == 1 or day > 100):
            input("SOMETHING HAPPENED!!!!")
            print("Your Farm Suffers From A Fly Infestation. Each Lane Now Has A Bug, Which Will Take Up Space. Thankfully, This Wont Affect The Money You Make")
            pests('🪰')
            input("Press Enter To Continue")
        if (event == 2 and level > 5 or day > 200):
            input("SOMETHING HAPPENED!!!!")
            print("Your Farm Suffers From Beetles. This Will Decrease Your Overall Prodouction For Each Beetle")
            pests('🪲')
            input("Press Enter To Continue")
    day += 1
    xpearning += 2
    license -= 1
    print("Current Time On Farming License:", license)
    dayspassed += 1
    print("Day", day,"    Money:", money,"    Farming Level", level, "    XP:", xp,"    XP Till Level Up:",(8 + (level * level)) - xp,"    Season:", season)
    earnings (lane1)
    earnings (lane2)
    earnings (lane3)
    earnings (lane4)
    earnings (lane5)
    printfarm()
    if (dayearnings < 0 or license <= 0):
        dayearnings = 0
    if (xpearning < 0 or license <= 0):
        xpearning = 0
    print("You Made", dayearnings,"Dollars Today. This Puts Your Total To", money + dayearnings)
    print("You Made", xpearning,"Xp Today. This Puts Your Total To", xp + xpearning)
    money += dayearnings
    dayearnings = 0
    xp += xpearning
    xpearning = 0
    while (loop == True):
        choice = ''
        while (siter == sloop):
            print("Would You Like To Visit The Shop (Type Shop), Skip A Week (Type Skip), Or Move To The Next Day (Press Enter)")
            choice = input()
            break
        if (choice == "Shop"):
            print(" $$$$$    $     $    $$$$$    $$$$$$    ")
            print("$         $     $   $     $   $     $   ")
            print("$$$$$$    $$$$$$$   $     $   $$$$$$    ")
            print("      $   $     $   $     $   $         ")
            print("$$$$$$    $     $    $$$$$    $         ")
            while(loop == True):
                print("You Have", money,"Money. Type Exit To Exit")
                print("------------------------")
                print("PLANTS")
                print("------------------------")
                print("Evergreen (5 Money, Produces 3 Money On Odd Days. Winter Plant) (Type Evergreen)")
                print("------------------------")
                print("Punpkin (1 Money, Produces 1 Money Every Day. Fall Plant) (Type Pumpkin)")
                if (level > 5):
                    print("Starfruit (7 Money, Produces 1 Xp Per Day. Spring Plant) (Type Starfruit)")
                    print("------------------------")
                if (level > 12):
                    print("Dragon Fruit (30 Money, Eats One Small Pest Per Day, And Gives Money Based On The Pest. Summer Plant) (Type Dragon Fruit)")
                    print("------------------------")
                    print("Christmas Tree (15 Money, Earns 10 Dollars And 3 Xp During Winter, But Nothing The Rest Of The Year. Winter Plant) (Type Christmas Tree)")
                    print("------------------------")
                print("ITEMS")
                print("------------------------")
                print("Farming License (Free, Renews Your Farming License For Another 21 Days) (Type License)")
                print("------------------------")
                print("Swatter (10 Money, A Pest From A Lane. Can Be Used 5 Times. Used Right Away) (Type Swatter)")
                print("------------------------")
                print("Shovel (3 Money, Removes A Plant From A Specific Lane, Used Right Away) (Type Shovel)")
                if (level > 5):
                    print("------------------------")
                    print("Laser Guided Shovel (5 Money, Removes All Of A Specific Plant From A Lane) (Type Laser Shovel)")
                    print("------------------------")
                if (level > 17):
                    print("Pesticides (30 Money, Fully Clears The Screen Of Pests) (Type Pesticides)")
                    print("------------------------")
                choice = input()
                if (choice == "Evergreen" and money >= 5):
                    xp += 1
                    printfarm()
                    print('Which Lane Do You Want To Plant The Evergreen In?')
                    placement('🌲')
                    money -= 5
                    printfarm()
                    break
                elif (choice == "Evergreen" and money < 5):
                    input("You Don't Have Enough Money For That. Press Enter To Continue")
                elif (choice == "Pumpkin" and money > 0):
                    xp += 1
                    printfarm()
                    print('Which Lane Do You Want To Plant The Pumpkin In?')
                    placement('🎃')
                    money -= 1
                    printfarm()
                    break
                elif (choice == "Pumpkin" and money < 0):
                    input("You Don't Have Enough Money For That. Press Enter To Continue")
                elif (choice == "Starfruit" and money >= 7 and level > 5):
                    xp += 3
                    printfarm()
                    print('Which Lane Do You Want To Plant The Starfruit In?')
                    placement('⭐')
                    money -= 5
                    printfarm()
                    break
                elif (choice == "Starfruit" and money < 7 and level > 5):
                    input("You Don't Have Enough Money For That. Press Enter To Continue")
                elif (choice == "Dragon Fruit" and money >= 30 and level > 12):
                    xp += 5
                    printfarm()
                    print('Which Lane Do You Want To Plant The Dragon Fruit In?')
                    placement("🐉")
                    money -= 30
                    printfarm()
                    break
                elif (choice == "Dragon Fruit" and money < 30 and level > 12):
                    input("You Don't Have Enough Money For That. Press Enter To Continue")
                elif (choice == "Christmas Tree" and money >= 15 and level > 12):
                    xp += 5
                    printfarm()
                    print('Which Lane Do You Want To Plant The Christmas Tree Fruit In?')
                    placement("🎄")
                    money -= 15
                    printfarm()
                    break
                elif (choice == "Christmas Tree" and money < 15 and level > 12):
                    input("You Don't Have Enough Money For That. Press Enter To Continue")
                elif (choice == "License"):
                    license = 21
                    break
                elif (choice == "Shovel" and money >=3 ):
                    xp += 1
                    printfarm()
                    print("What Lane Do You Want To Remove From")
                    choice = input()
                    print("What Plant Do You Want To Remove? (Type The Plant's Name In English i.e Type Evergreen)")
                    choice2 = input()
                    shovel(choice, w2e(choice2))
                    money -= 3
                    printfarm()
                    break
                elif (choice == "Shovel" and money < 3):
                    input("You Don't Have Enough Money For That. Press Enter To Continue") 
                elif (choice == "Laser Shovel" and money >= 5 and level > 5):
                    printfarm()
                    print("What Lane Do You Want To Remove From")
                    choice = input()
                    print("What Plant Do You Want To Remove? (Type The Plant's Name In English i.e Type Evergreen)")
                    choice2 = input()
                    laser_shovel(choice, w2e(choice2))
                    money -= 5
                    printfarm()
                    break
                elif (choice == "Laser Shovel" and money < 5 and level > 5):
                    input("You Don't Have Enough Money For That. Press Enter To Continue") 
                elif(choice == "Swatter" and money >= 10):
                    printfarm()
                    print("Type The Lanes You Want To Swat")
                    nloop = 5
                    iterator = 0
                    while (iterator != nloop):
                        if (pestsalive("Fly") == True and pestsalive("Beetle") == True):
                            break
                        choice = input()
                        if (choice == '1'):
                            swat(lane1)
                            iterator += 1
                        elif (choice == '2'):
                            swat(lane2)
                            iterator += 1
                        elif (choice == '3'):
                            swat(lane3)
                            iterator += 1
                        elif (choice == '4'):
                            swat(lane4)
                            iterator += 1
                        elif (choice == '5'):
                            swat(lane5)
                            iterator += 1
                        else:
                            print("Choice Not Recognized")
                        printfarm()
                    break
                elif (choice == "Swatter" and money < 10):
                    input("You Don't Have Enough Money For That. Press Enter To Continue") 
                elif (choice == "Pesticides" and money >=30 and level > 17 ):
                    xp += 10
                    money -= 30
                    pestwipe(w2e("Fly"))
                    pestwipe(w2e("Beetle"))
                    printfarm()
                    break
                elif (choice == "Pesticides" and money < 30 and level < 17):
                    input("You Don't Have Enough Money For That. Press Enter To Continue") 
                elif (choice == "Exit"):
                    break
                else:
                    print("Choice Not Recognized, Or You Havent Unlocked That")
        elif(choice == ''):
            break
        elif (choice == "Skip"):
            sloop = 7
            siter = 0
            break
        else:
            print("Choice Not Recognized")
    if (siter != sloop):
        siter += 1
    if (xp > 8 + (level * level)):
        input("SOMETHING HAPPENED!!!")
        while(xp > 8 + (level * level)):
            level += 1
            xp -= (8 + (level * level))
            if (level == 6):
                print("Starfruit Unlocked!!!")
                print("Laser Guided Shovel Unlocked!!!")
            if (level == 9):
                print("Maximum Lane Length Increased To 12")
                limit = 12
            if (level == 13):
                print("Dragon Fruit Unlocked!!!")
                print("Christmas Tree Unlocked")
                print('Maximum Lane Length Increased To 16')
                limit = 16
            if (level == 18):
                print("Pesticides Unlocked!!!")
            if (level == 25):
                print("Maximum Lane Length Increased To 20")
                limit = 20
        print("LEVEL UP. You Are Now Level", level)
        input("Press Enter To Continue")
    if (dayspassed == 20):
        input("SOMETHING HAPPENED!!!")
        if (season == "🍃"):
            season = "☀️"
            print("Season Changed To Summer. Summer Plants Are Boosted, Winter Plants Are Hindered")
        elif (season == "☀️"):
            season = "🍂"
            print("Season Changed To Fall. Fall Plants Are Boosted")
        elif (season == "🍂"):
            season = "❄️"
            print("Season Changed To Winter. Winter Plants Are Boosted, Summer Plants Are Hindered")
        elif (season == "❄️"):
            season = "🍃"
            print("Season Changed To Spring. Spring Plants Are Boosted")
        dayspassed = 0
        input("Press Enter To Continue")
    
        
