import random
user='abcdefghijklmnopqrstuvwxyzQWERTYUIOPLKJHGFDSAZXCVBNM!@#₹&$¢®©(){}'
length=int(input('Enter the length of password:'))
password=' '
for i in range(length):
	password+=random.choice(user)
print('your password:' ,password)