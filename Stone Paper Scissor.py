# print("Enter Two Numbers: ", end="")
# no = int(input())
# nt = int(input())

# a = no
# b = nt
# while b!=0:
#     x = b
#     b = a%b
#     a = x

# hcf = a
# lcm = int((no*nt)/hcf)

# print("\nLCM ("+str(no)+", "+ str(nt)+") = ",lcm)
# print("HCF ("+str(no)+", "+str(nt) +") = ", hcf)

##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::##

# import random
# print("\n########  Game Starts  #########\n")
# count = 0
# comp = 0
# mvp = 0

# # lst = ['Stone','Paper','Scissors']
# print("Choose any number:\n""1-Stone, 2-Paper, 3-Scissors\n")

# while count<10:
#     mac = random.randint(1,3)
#     print("************* TURN",(count+1),"****************")
#     you = int(input("Enter your number : "))

#     while you>3 or you<0:
#         print("\n<=--- Not Valid ---=>\n")
#         print("1-Stone, 2-Paper, 3-Scissors")
#         you = int(input("\nAgain enter your number : "))

#     print("\nYou choose -",you,"\nCPU choose -",mac)
#     if you==mac:
#         comp+=1
#         mvp+=1
#         print("-----Draw-----\n")
#     elif you==1 and mac==2:
#         comp+=1
#         print("-----You Lose-----\n")
#     elif you==2 and mac==3:
#         comp+=1
#         print("-----You Lose-----\n")
#     elif you==3 and mac==1:
#         comp+=1
#         print("-----You Lose-----\n")
#     elif you==1 and mac==3:
#         mvp+=1
#         print("-----You Win-----\n")
#     elif you==2 and mac==1:
#         mvp+=1
#         print("-----You Win-----\n")
#     elif you==3 and mac==2:
#         mvp+=1
#         print("-----You Win-----\n")
#     count+=1

# print("~~~~~~~~~~~~~~~~~~~~~Game Finish~~~~~~~~~~~~~~~~~~~~~\n")
# if comp==mvp: print("----------->>>>>>Draw<<<<<<----------\n")
# elif comp>mvp: print("----------->>>>>>You Lose<<<<<<----------\n")
# else: print("----------->>>>>>You Win<<<<<<----------\n")

##:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::##

import random
print("\n########  Game Starts  #########\n")
count = 0
comp = 0
mvp = 0

lst = ['-', 'Stone', 'Paper', 'Scissors']
print("Choose any number:\n""1-Stone, 2-Paper, 3-Scissors\n")

try:
    while count < 6:
        mac = random.randint(1, 3)
        print("************* TURN", (count+1), "****************")
        you = int(input("Enter your number : "))

        while you > 3 or you <= 0:
            print("\n<=--- Not Valid ---=>\n")
            print("1-Stone, 2-Paper, 3-Scissors")
            you = int(input("\nAgain enter your number : "))

        print("\nYou choose -", lst[you], "\nCPU choose -", lst[mac])
        if you == mac:
            comp += 1
            mvp += 1
            print("-----Draw-----\n")
        elif you == 1 and mac == 2:
            comp += 1
            print("-----You Lose-----\n")
        elif you == 2 and mac == 3:
            comp += 1
            print("-----You Lose-----\n")
        elif you == 3 and mac == 1:
            comp += 1
            print("-----You Lose-----\n")
        elif you == 1 and mac == 3:
            mvp += 1
            print("-----You Win-----\n")
        elif you == 2 and mac == 1:
            mvp += 1
            print("-----You Win-----\n")
        elif you == 3 and mac == 2:
            mvp += 1
            print("-----You Win-----\n")
        count += 1

    print("~~~~~~~~~~~~~~~~~~~~~Game Finish~~~~~~~~~~~~~~~~~~~~~\n")
    if comp == mvp:
        print("----------->>>>>>Draw<<<<<<----------\n")
    elif comp > mvp:
        print("----------->>>>>>You Lose<<<<<<----------\n")
    else:
        print("----------->>>>>>You Win<<<<<<----------\n")

except:
    print('\n+++++++++++ Oops... +++++++++++',
          '\n\n           Try Again...\n')
