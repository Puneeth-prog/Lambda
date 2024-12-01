import re

def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

# Example usage
print(validate_email("example@example.com"))  # True
print(validate_email("invalid-email.com"))    # False

def validate_bangladesh_mobile(number):
    mobile_pattern = r'^01[3-9]\d{8}$'  # Starts with 01, followed by a digit between 3-9 and 8 other digits
    return bool(re.match(mobile_pattern, number))

# Example usage
print(validate_bangladesh_mobile("01712345678"))  # True
print(validate_bangladesh_mobile("0131234567"))   # False (because 13 is not valid)
def validate_usa_telephone(number):
    usa_telephone_pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(usa_telephone_pattern, number))

# Example usage
print(validate_usa_telephone("(123) 456-7890"))  # True
print(validate_usa_telephone("123-456-7890"))    # True
print(validate_usa_telephone("123 456 7890"))    # True
print(validate_usa_telephone("1234567890"))      # False
def validate_password(password):
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{16}$'
    return bool(re.match(password_pattern, password))

# Example usage
print(validate_password("Password123!@#$"))  # True
print(validate_password("short123"))         # False (too short)
print(validate_password("password123!@#$"))  # False (no uppercase letter)
