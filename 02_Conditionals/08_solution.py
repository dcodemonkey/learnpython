password = "Secure4P@455667"
password_length = len(password)

if len(password) < 6:
    strngth = "Weak"
elif len(password) <= 10:
    strngth = "Medium"
else:
    strngth = "Strong"

print("Password strength is", strngth)