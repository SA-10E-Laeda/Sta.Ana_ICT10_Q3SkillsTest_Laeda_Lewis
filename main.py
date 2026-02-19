from pyscript import display, document


def username_verification(e):
    document.getElementById('output').innerHTML = ''

    username = document.getElementById('username').value
    username_length = len(username)

    if username_length == 0:
        display('You have not filled the Username slot. Please type at least 7 characters.', target='output')
        return False
    elif username_length < 7:
        display(f'Your username is too short. Add at least {7 - username_length} more character/s to proceed.', target='output')
        return False
    else:
        return True


def password_verification(e):
    document.getElementById('output').innerHTML = ''

    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)

    if password_length == 0:
        display('You have not filled the Password slot. Please type at least 10 characters.', target='output')
        return False
    elif password_length < 10:
        display(f'Your password is too short. Add at least {10 - password_length} more character/s to proceed.', target='output')
        return False
    elif not password_has_letter:
        display('Password must contain at least one letter.', target='output')
        return False
    elif not password_has_number:
        display('Password must contain at least one number.', target='output')
        return False
    else:
        return True


def account_creation(e):
    document.getElementById('output').innerHTML = ''

    if username_verification(e) and password_verification(e):
        display('Account created. You may now log in using your credentials.', target='output')
    else:
        display('Try again.', target='output')