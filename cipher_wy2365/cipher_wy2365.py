def cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts a text using Caesar cipher.

    Parameters
    ----------
    text: str
        A string that is to be encrypted or decrypted
    shift: int
        The number of positions that the text is shifted by
    encrypt: bool
        A boolean that states whether to encrypt (True) or decrypt (False)

    Returns
    -------
    str
        The encrypted or decrypted string

    Examples
    --------
    >>> from cipher_wy2365 import cipher_wy2365
    >>> cipher_wy2365.cipher('Columbia', 1)
    'Dpmvncjb'
    >>> cipher_wy2365.cipher('Dpmvncjb', 1, encrypt=False)
    'Columbia'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text