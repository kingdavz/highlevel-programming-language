#!/usr/bin/python
"""A module that checks password error"""

def check_password(password):
    try:
        if len(password) < 8:
            raise ValueError("error password is less than 8")
         
        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)

        if not all([has_upper, has_lower, has_digit]):
            raise ValueError("password must contain upper, lower, and digit characters")
        
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("password is strong")

if __name__ == "__main__":
    password = input("Enter password: ")
    check_password(password)
    
