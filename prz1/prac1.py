import re

def check_password(password):
    recommendations = []
    if len(password) < 10:
        recommendations.append(f'add {10-len(password)} more symbols')
    if not (re.findall(r'[A-Z]', password)):
        recommendations.append(f'add 1 uppercase')
    if not (re.findall(r'[0-9]', password)):
        recommendations.append(f'add 1 digit')
    if not (re.findall(r'\W', password)):
        recommendations.append(f'add 1 symbol')
    if recommendations:
        print("Weak password. What should u do:", ", ".join(recommendations))
    else:
        print('Strong password')

loc = input("Path to file:")
file = open(loc, "r")
while True:
    password = file.readline()
    if not password:
        break
    print(password.strip())
    check_password(password.strip())
file.close()
    
