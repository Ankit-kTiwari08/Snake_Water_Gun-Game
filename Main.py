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
    if(computer==-1 and you==1):
       print("You win ! ")

    elif(computer ==-1 and you==0):
       print("You lose ! ") 

    elif(computer==1 and you==-1):
        print("You lose ! ")

    elif(computer ==-1 and you==0):
        print("You Win ! ")  

    elif(computer==0 and you==-1):
        print("You win ! ")

    elif(computer ==0 and you==1):
       print("You lose ! ")  

    else:
         print("something went wrong ")      


# if((computer-you)==-1 or (computer-you)==2):
#     print("you lose! ")
# else:
#     print("You win! ")    