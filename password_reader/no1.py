with open("password.txt", "r") as password_file:
    password = password_file.read().strip()

i = 0
while i <= 9999:
    if str(i).zfill(4) == password:
        print(f"Password found: {password}")
        break
    i += 1
else:
    print("Password not found")
