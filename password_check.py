
keyPassword = 'Ok123'
attempts = 1

print('Welcome dear User, enter password to continue')


while (True):
    password = str(input('Password: '))
    attempts += 1

    if (attempts <= 3):
        if(password == keyPassword):
            print("You've logged in successfully")
            break
        else:
            print('Wrong Password! Try again')
    else:
        print('Gerarahiyaaa')
        break


