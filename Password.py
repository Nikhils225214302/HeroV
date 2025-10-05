import re

def check_password_strength(password):
    
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


# --- Main program ---
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    if check_password_strength(pwd):
        print("✅ Strong password! It meets all security requirements.")
    else:
        print("❌ Weak password. Try using a mix of uppercase, lowercase, digits, and special characters.")
