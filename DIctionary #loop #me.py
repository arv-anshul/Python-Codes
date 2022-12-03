# dictonary with wrong loop.

print("Hi... IT'S ARV")
dic = {'fact': 'something that you know has happened or is true',
       'special': 'not usual or ordinary; important for some particular reason',
       'word': 'a group of letters',
       'program': 'a plan of things to do; a scheme'
       }
dic.update({"key": "something which unlocks a lock",
            "book": "a compiled set of pages which describes a certain topic",
            "comb": "a plastic item to set hairs",
            "mouse": "an animal which is afraid of cats",
            "joey": "kid of a kangroo"
            }
           )
print("Your keys are : ", dic.keys())
x = dic.get(input("Type your key : "))

while x == None:
    if x == None:
        print("Try Again!")
        y = dic.get(input("Type your key : "))
        x = y
        continue
    print("Answer:", y.capitalize())
print(x.capitalize())

# This is right Code.
# if x==None:
#      print("Oops! Rerun your program.""\n"*3)
# else:
#      print(x.capitalize())
# -----------------------------------
# Wrong*5

# Oooo Bhai bhai..! kya shi mai code likha hu dimag ka dahi ho gya yaar, mat puch kitna dimag lagya hu.


# while x==None :
#      print("Try Again!")
#      y = dic.get(input("Type your key : "))
#      x=y
#      print("Answer:",y.capitalize())

## '''Ohh Shit..! It take about 45 min. only for while loop. But this is also wrong.'''

# while x==None :
#      print("Try Again!")
#      y = dic.get(input("Type your key : "))
#      x=y
# print("Answer:",y.capitalize())
