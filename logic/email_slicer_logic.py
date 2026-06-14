"""
Pure email-address slicing logic.
"""


def slice_email(email):
    """
    Split an email address into (username, domain).

    Raises ValueError if the address does not contain exactly one '@'.
    """
    email = email.strip()
    if email.count("@") != 1:
        raise ValueError("Invalid email address: must contain exactly one '@'.")
    username, domain = email.split("@")
    if not username or not domain:
        raise ValueError("Invalid email address: username and domain must not be empty.")
    return username, domain
