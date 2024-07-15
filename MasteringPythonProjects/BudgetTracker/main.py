import json
import os
class Expense:
     total_price=0
     def __init__(self,description,amount,unit_price) -> None:
          self.description=description
          self.amount=amount
          self.unit_price=unit_price
          self.total_price=amount*unit_price
     def __str__(self):
       return f"{
           'desc':self.description,
           'amount':self.amount,
           'unit_price':self.unit_price
       }"
class BudgetTracker:

     expenses=[]
     filepath="budget.json"
     def  __init__(self) -> None:
          self.total_buget=self.check_budget_from_file(self.filepath)
     def addExpense(self, exp:Expense)-> None:
           self.expenses.append(str(exp))

           print(self.expenses)
           self.total_buget-=exp.total_price
           self.add_expense_to_file(self.filepath,self.expenses)
     
     def add_expense_to_file(self,filepath,allexpenses:Expense):
      try:
        initial_budget= self.total_buget
        expenses=self.expenses
        
        print(allexpenses)
        data={
            "budget":initial_budget,
            "expenses":expenses

        }        
       
        with open(filepath,"w") as file:
           json.dump(fp=file,obj=data,indent=4)
      except(FileNotFoundError):
            print("file not found")


     def check_budget_from_file(self,filepath):
        try:
           with open(filepath,'r') as file :
             data= json.load(file)
             return data["budget"]
        except(FileNotFoundError ,json.JsonDecoderError):
           return -1         
       
  
     def play(self):

        while  True:
             print("Choose one of the following...\n")
             print("1. check your remaining budget\n")
             print("2. add new  expense\n")
             print("3. check all expense\n")
             print("4. exit\n")
             choice=input("\n")
             if choice == "1":
                  print(f"your remaining budget is {self.total_buget}\n")
             elif choice == "2":
                  desc=input("Enter description of the expense\n")
                  
                  unit_price=input("Enter the unit price of the expense\n")
                  amt=input("Enter the amount of the expense\n")
                  expense=Expense(description=desc,amount=float(amt),unit_price=float(unit_price))
                  if(expense.total_price>self.total_buget):
                        print("Error, The remaining budget is not sufficient for this expense!\n")
                  else : 
                    self.addExpense(expense)
             elif choice=="3":
                  print(self.expenses)
             elif  choice=="4":
                     print("Bye ,🙋‍♂️🙋‍♂️🙋‍♂️🙋‍♂️🙋‍♂️🙋‍♂️")
                     break
             else:
               raise("Unknown input")
 
 
if __name__== "__main__":
       tracker=BudgetTracker()
       tracker.play()
    