# Name: Sean Perez
# CS 362: A2
# Date: 4.29.22

from string import ascii_lowercase, ascii_uppercase, digits


def check_pwd(pwd):

    symbols_allowed = "~`!@#$%^&*()_+-="

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

    if set(pwd).isdisjoint(digits):
        return False

    if set(pwd).isdisjoint(symbols_allowed):
        return False

    if set(pwd).difference(ascii_lowercase + ascii_uppercase
                           + digits + symbols_allowed):
        return False

    return True
