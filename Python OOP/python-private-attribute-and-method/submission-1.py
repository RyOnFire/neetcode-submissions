class PasswordManager:
    def __init__(self, my_password):
        self.__my_password = my_password
        
    
    # TODO: Implement the verify_password method
    def verify_password(self, ver_password):
        self.ver_password = ver_password
        if self.ver_password == self.__my_password:
            return True
        else:
            return False




# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
