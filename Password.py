def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    if len(password) < 8:
        return False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False


password = input("Enter your password: ")

if check_password_strength(password):
    print("✅ Strong password! It meets all security requirements.")
else:
    print("❌ Weak password. Try using uppercase, lowercase, numbers, and special characters.")
