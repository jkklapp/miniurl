import hashlib
import validators

def shortify(url):
    """
    Get short version of url.

    Essentially generate a hash for the string.

    :param url: A string with a valid url.
    :return: A string containing the generated hash.
    """
    return hashlib.sha224(url).hexdigest()

def is_valid(url):
    """
    Validate a url.

    :param url: A string with a valid url.
    :return: True if it is a valid URL, False otherwise
    """
    return validators.url(url)
