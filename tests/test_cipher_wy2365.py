from cipher_wy2365 import __version__
from cipher_wy2365 import cipher_wy2365
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_with_word():
    example = 'Columbia'
    expected = 'Dpmvncjb'
    actual = cipher_wy2365.cipher(example, 1)
    assert expected == actual, 'Should be True'