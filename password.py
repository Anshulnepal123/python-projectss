import os

masterpw = input("Enter master password: ")

def add():
  user = input("Palatform: ")
  pw = input("Password: ")
  with open("password.txt", "a") as f1:
    f1.write( " Platform:" + user + " \n " +"Password:"+ pw + "\n"  )   

def view():
  with open("password.txt" , "r") as f:
    for lines in f.readlines():
     print(lines.rstrip())

def remove_text():
  os.remove("password.txt")
  with open("password.txt", "x"):
    pass    
       
while masterpw == "majorwalker123":
  user = input("Type q to quit\n Type clear to clear all the passwords\n What do you want (view or add) ")
  if user == "q": 
    break
  elif user == "view":
    view()
  elif user == "add":
    add()
  elif user == "clear":
    remove_text()
    
  else:
    print("invalid syntax")
