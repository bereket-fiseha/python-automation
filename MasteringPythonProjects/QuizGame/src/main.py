#this quiz app is  a console app that  fetches lot of  quizes from  a file using api call
#to improve
#load question from remote file 
#let user choose the tota; number of questions to be asked
#show fireworks or drawing at the end

class Quiz:
  totalScore=0
  #load quizes from a file using api call 
  def QuizGenerator(self)->list[object]:
         listOfQuiz=[
    {
"Question":"what is the capital city of kenya?",
"Choice":["A. Addis Ababa" ,"B. Nairobi" ,"C. Khartoum", "D. Legos"],
"Answer":"B",
 "Hint":" starts with N"
 

},
{
"Question":"what is the largest country in africa?",
"Choice":["A. Egypt" ,"B. Sudan" ,"C. Nigeria", "D. South africa"],
"Answer":"A",
 "Hint":" is arabic country"
 

}



                     ]
         return listOfQuiz



  def Play(self):
     listOfQuiz=self.QuizGenerator()
     n=input("how many quizes do you want? , default= 10")
     
     for quiz in listOfQuiz:
        print(f"{quiz['Question']}\n")
        for ch in quiz["Choice"]:
           print(f"{ch}\n")
        q=input("Enter your answer(A , B , C or D) else press H for Hint\n").upper()    
        if(str(q)=="H"):
            q=input(f"Hint: {quiz['Hint']} ,Choose your answer(A, B, C or D) \n")
        if(str(q)==quiz["Answer"]):
          self.totalScore+=1
          print("Correct! ,💪💪💪💪💪")
        else:
          print(f"wrong!,🙅‍♂️ the correct answer is {quiz['Answer']}\n")  
     print(f"You have scored, {self.totalScore}/{len(listOfQuiz)}")      
     print(f"👋 ,bye")
quiz=Quiz()

quiz.Play()