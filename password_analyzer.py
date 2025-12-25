import re

def password_analyzer(password):
    score = 0
    feedback = []

    # 1️⃣ Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # 2️⃣ Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 3️⃣ Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 4️⃣ Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # 5️⃣ Special character
    if re.search(r"[!@#$%^&*()_+=<>?/{}~]", password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$ etc.).")

    # 6️⃣ Common password check
    common = ["123", "password", "admin", "qwerty"]
    if any(word in password.lower() for word in common):
        feedback.append("Avoid common or easy passwords.")
    else:
        score += 1

    # 🔐 Final strength decision
    if score <= 2:
        strength = "WEAK ❌"
    elif score <= 4:
        strength = "MODERATE ⚠️"
    else:
        strength = "STRONG ✅"

    return strength, score, feedback

# -------- MAIN PROGRAM --------
print("\n🔐 PASSWORD ANALYZER 🔐")
password = input("Enter your password: ")

strength, score, suggestions = password_analyzer(password)

print("\nPassword Strength :", strength)
print("Security Score    :", score, "/ 6")

if suggestions:
    print("\nSuggestions:")
    for tip in suggestions:
        print("•", tip)
else:
    print("\n✔ Great! Your password is strong.")
