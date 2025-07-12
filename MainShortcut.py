import random
'''
1 : for snake
-1: for water
0 : for gun
'''
computer =random.choice([-1,0,1])
youstr = input("Enter your Choice: s/w/g  ") #among s,w,g 

youDictn ={"s":1,"w":-1,"g":0}
reverseDict ={1: "Snake", -1: "Water" , 0: "Gun"}

you= youDictn[youstr]

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")
if(computer==you):
    print("Match Draw ! ")
else:
   if((computer-you)==-1 or (computer-you)==2):
    print("you lose! ")
   else:
     print("You win! ")  