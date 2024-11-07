import re

def check_password_strength(password):
    #check the length of a password
    if len(password) <12:
        return "weak: Password must be at least 8 characters long."
    
    
        #check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least 1 uppercase letter"
        
        #check for uppercase letters        
    if not re.search(r'[a-z]', password):
        return "weak: Password must contain at least 1 lowercase letter"
        
        
    if not re.search (r'[0-9]', password):
        return "Weak: Password must contain at least 1 number"
        
        
    if not re.search(r' [!@#$%^&*()_,.?":{}|<>]', password):
        return "Weak: Password must contain at least 1 speical character"
       
    return "Strong: Password is strong!"
    
while True:
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
    if result == "Strong: Your password is strong!":
        break