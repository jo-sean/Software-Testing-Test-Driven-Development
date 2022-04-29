# Name: Sean Perez
# CS 362: A2
# Date: 4.29.22


def check_pwd(pwd):
    if not pwd:
        return False

    if len(pwd) == 7:
        return False

    return True
