import json
from random import shuffle
class LangApp:
      list_of_words=[]

      def load_words(self):
            try:
              with open("list_of_words.json","r") as f:
                    self.list_of_words=json.load(f)
            except FileNotFoundError as notFound:
                   print(notFound.strerror())

      def Play(self):
            score=0
            self.load_words()
            shuffle(self.list_of_words)
            for word in self.list_of_words:
             
              inp=input(f"what is the english translation for the word {word['sp']}\n")    
              ans=word["en"]
              if(type(ans) == list):
                    if inp.strip().lower() in ans:
                             print("Correct! 💪💪💪💪💪")
                             score+=1
              elif(type(ans) == str and inp.strip().lower()==ans.lower()):
                     print("Exactly! 💪💪💪💪💪")
                     score+=1
              else:
                   print(f"🙅🙅 , the correct answer is {ans}")       
            print(f"your total score is {score}/{len(self.list_of_words)} , {'grate job!!!! 'if (score>len(self.list_of_words)/2) else 'next time you will do better.'}")

if __name__=="__main__":
     app=LangApp()
     app.Play()
     

