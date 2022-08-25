class Dot1:
     python = 32
     count = 0         # made for counting the the number of objects of a class.
     def __init__(self):
        Dot1.count= Dot1.count + 1
     ''' ^^^it doesn't work because second/next init constructor override it.'''
     # def __init__(self,name,standard,hobby):
     #      self.name = name
     #      self.standard = standard
     #      self.hobby = hobby
     def xyz(self):
          print('Hello',self.name)
# me = Dot1('ARV','00','Computer')
# me_too = Dot1('Anshul','10 G','Books')
x = Dot1()
c = Dot1()
D = Dot1()
# me_too.xyz()
# print(me.python)
# del python             #delete the class attribute
# print(me.python)       # Now it shows error because python attribute was deleted
# print(Dot1.__dict__)
# me.python = 23
# print(me.python)

# print(getattr(me,'standard'))
# setattr(me_too, 'hobby', 'coding')         #class buit-in functions
# print(me_too.hobby)
# delattr(me, 'standard')
print(Dot1.count)