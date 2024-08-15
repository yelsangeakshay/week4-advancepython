class SecurityException(Exception):
    def __init__(self,message):
        print(message)
    def logout(self):
        print("Logout from all device")

class Google:
    def __init__(self,email,password,device):
        self.email = email
        self.password = password
        self.device = device

        
    def login(self,email,password,device):
        if self.device != device:
            raise SecurityException("Lag gai")
        if self.email == email and self.password == password:
            print("Welcome")
        else:
            print("user id or password is wrong")

g = Google('akshay@gmail.com','1234','android')
try:
    g.login('','','windows')
except SecurityException as e:
    e.logout()
    pass

