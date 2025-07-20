# modules/feedback_engine.py
COMMON_PATTERNS = ['1234', 'password', 'qwerty', 'admin', 'abc']

def check_patterns(password):
    flags = []
    for pattern in COMMON_PATTERNS:
        if pattern in password.lower():
            flags.append(f"Contains common pattern: '{pattern}'")
    if password.lower() == password:
        flags.append("No uppercase letters used.")
    if password.isalnum():
        flags.append("No special symbols used.")
    if len(password) < 8:
        flags.append("Password is too short.")
    return flags
