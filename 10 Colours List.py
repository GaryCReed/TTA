#Gary Reed - 2022 - 10 Colours List Ext
#import random
colist=["Red","Orange","Yellow","Green","Blue","Indigo","Violet","Black","White","Gold"]
start=int(input("Enter a whole number from 0 to 4: "))
fin=int(input("\nEnter a whole number from 5 to 9: "))
counter=start
print("The colours you picked are",end=": ")
while counter>=start and counter<=fin:      
          print(colist[counter-1],end=",")
          counter=counter+1
