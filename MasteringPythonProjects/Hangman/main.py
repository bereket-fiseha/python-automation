import random
#to improve
#load question from remote file  using api call
#show fireworks or drawing at the end


class Hangman:
  def __init__(self):
     self.listOfWords=["messi","poogba","debbruyne"]
     self.listOfHints=["He has 7 balandor!", "He is a french player who is ex midfielder of utd","He is currently midfielder of belgium who has most assists in priemer"]
  def Play(self):
      num=int(random.choice("012"))
      word=self.listOfWords[num]
      hint=self.listOfHints[num]
      #self.indexOfWord=self.listOfWords.indexOf(word)
        #use hashMapinary with linked list instead
       # store every letter of word as  key and value: the list of  index of every char within the word 
      hashMap=dict()
      for i,l in enumerate(word):
          if l in hashMap.keys():
            hashMap[l].append(i)
          else:
           hashMap[l]=[i]
      
      maxTrial=0
      arrayOfSpaces=[]
      for l in word:
          arrayOfSpaces.append("_")
      numOfSpaces=len(arrayOfSpaces)
      maxTrial=numOfSpaces
      print(f"hint:{hint} \n")
      while(numOfSpaces!=0 and maxTrial>0):    
       print(" ".join(arrayOfSpaces))   
       maxTrial-=1 
       guess=input(f"geuss a letter? \n").lower()
      #if using hashMapa
      
       if guess in hashMap.keys() and len(hashMap[guess])!=0:
    
           arrayOfSpaces[(hashMap[guess])[0]]=guess
           numOfSpaces-=1
           hashMap[guess].remove(hashMap[guess][0])
       else:
            print("wrong! 🙅‍♂️🙅‍♂️")    
       print(f"{maxTrial} trial only left!")

      
      if(numOfSpaces==0):
            print("💪💪💪💪💪 , You Got It.")
      else:
          print(" 🙅🙅🙅🙅🙅🙅 ,sorry")      
      q=input("wanna play again, enter Y for yes and N for no \n").upper()
      if q=="Y":
         self.Play()
      else :
            print("👋👋👋👋 ,Bye!!!")      
     

hangman=Hangman()
hangman.Play()