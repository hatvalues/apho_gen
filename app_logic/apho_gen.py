"""Generates the aphorism (currently a stub)"""

import random

partial_texts = (
    "you can tell how smart people are by what they laugh at.",
    "do more of what makes you happy.",
    "free yourself of negative people and surround yourself with those who love you.",
)


def get_apho_for_name(name, partials=partial_texts):
    """
    Return a personalised affirming aphorism.

    Parameter
    ---------
    name : str
        Person to be named in aphorism.

    Returns
    -------
    apho
        Affirming message (must include name).
    """

    return f"Always remember, {name}, {random.choice(partials)}"
