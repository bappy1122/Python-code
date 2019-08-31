class User:
	name = " "
	email = " "
	password = " "
	login = False

	def __init__(self,name,email,password):

		self.name = name
		self.email = email
		self.password = password


	def login(self):
		email = input("Enter Email: ")
		password = input("Enter password: ")

		if email == self.email and password == self.password:
			login = True
			print("Login Successful")

		else:
			print("Login Failed!")

	def logout(self):
		login = False
		print("Logged Out!")

	def isloggedIn(self):
		if self.login:
			return True
		else:
			return False

	def profile(self):
		if self.isloggedIn():
			print(self.name,"\n",self.email)
		else:
			print("User is not logged in!")


user1 = User("Bappy", "bappyjafar@yahoo.com", "12345")


user1.login()

test = input()






