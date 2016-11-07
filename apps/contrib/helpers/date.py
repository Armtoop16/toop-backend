# -*- coding: utf-8 -*-

# Stdlib imports
from datetime import date


def birthday_to_age(birthday):
    """ Converts a given birthday in `datetime` to age """
    if birthday is not None:
        today = date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    return None
