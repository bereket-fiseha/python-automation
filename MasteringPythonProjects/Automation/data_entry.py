# data entry from a user to existing file
import pandas as pd

try:
 try: 
   existing_data=pd.read_csv("data.csv")
   print(type(existing_data))
 except FileNotFoundError :
   existing_data=pd.DataFrame()
 name=input("Enter Name:\n")
 age=input("Enter Age:\n")
 gender=input("Enter Gender:\n")
 data=[{'name':name,'age':age,'gender':gender}]
 combinedData= pd.concat([existing_data,pd.DataFrame(data)],ignore_index=True)
 combinedData.to_csv("./data.csv",index=False)
 print("data entry successful!")
     



except Exception as e:
  print("data entry error!",{e})