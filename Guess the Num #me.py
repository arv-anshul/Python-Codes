#guess the number in 10 chance.

n=18
guess_number = 1
print("\n-=> You have only 10 chances to guess my number.\nSo, enter your number with concentration.")
while guess_number<=10:
     input_number = int(input("\nEnter your number : "))
     if input_number < n:
          print("Your number is smaller than my number.") 
     elif input_number > n:
          print("Your number is greater than my number.")
     else :
          print("\n-=> WOW! You guess my number.")
          print("-=> You finish in",guess_number,"chances.")
          print("\n!!.---YOU WON---.!!"*3+"\n")
          break
     
     print ("You have ",10-guess_number,"chances left to guess the number.")
     guess_number = guess_number + 1

if guess_number > 10:
     print("\nYou have no chance left.")
     print("\n----Game Over----"*3+"\n")