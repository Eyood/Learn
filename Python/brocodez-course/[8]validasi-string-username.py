#user menginput username lalu disimpan
username = input("username: ")

#memberikan kondisi penulisan username
#output username yang invalid
if not username.isalpha():
  print("username must be only countain alphabet character and just one word")
elif not 1 < len(username):
  print("username must be atleast 2 character")
elif not len(username) < 13:
  print("username must be equal or under 12 character")
  
#output username yang valid
else:
  print(f"your new username is {username}")