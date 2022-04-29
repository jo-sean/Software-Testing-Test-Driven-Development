# Name: Sean Perez
# CS 362: A2
# Date: 4.29.22

from string import ascii_lowercase, ascii_uppercase


def check_pwd(pwd):
    if not pwd:
        return False

    if len(pwd) <= 7:
        return False

    if len(pwd) >= 21:
        return False

    if set(pwd).isdisjoint(ascii_lowercase):
        return False

    if set(pwd).isdisjoint(ascii_uppercase):
        return False

    return True
