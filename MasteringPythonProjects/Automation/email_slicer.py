def email_slice(email:str)->object:
  splited=email.split("@")
   
  return  {"userName":splited[0],"domain":splited[1]}


if __name__=="__main__":
    email=input("enter your email\n")
    sliced=email_slice(email)
    print(f"your user name is {sliced['userName']}, and your domain is {sliced['domain']}")

