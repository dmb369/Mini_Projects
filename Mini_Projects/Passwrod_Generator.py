import random
import string

# Input length of the password
password_len = int(input("Enter length of password: "))

# Character sets
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = '@#$*!%^&*()'

# Ensure at least one character from each category is included
password = [
    random.choice(UPPERCASE),
    random.choice(LOWERCASE),
    random.choice(DIGITS),
    random.choice(SPECIAL)
]

# If the password length is more than 4, add random characters to fill the remaining length
if password_len > 4:
    COMBINED_LIST = UPPERCASE + LOWERCASE + DIGITS + SPECIAL
    password += random.sample(COMBINED_LIST, password_len - 4)

# Shuffle the password list to mix the ensured characters with the random characters
random.shuffle(password)

# Join the list to form the final password string
password = "".join(password)

print(password)
