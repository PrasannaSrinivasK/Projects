# modules/strength_checker.py
import math
from zxcvbn import zxcvbn

CHARSETS = {
    'lower': 'abcdefghijklmnopqrstuvwxyz',
    'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'digits': '0123456789',
    'symbols': '!@#$%^&*()-_+=~`[]{}|:;\"\'<>,.?/'
}

def entropy_score(password):
    charset_size = 0
    if any(c.islower() for c in password): charset_size += len(CHARSETS['lower'])
    if any(c.isupper() for c in password): charset_size += len(CHARSETS['upper'])
    if any(c.isdigit() for c in password): charset_size += len(CHARSETS['digits'])
    if any(c in CHARSETS['symbols'] for c in password): charset_size += len(CHARSETS['symbols'])

    entropy = math.log2(charset_size ** len(password)) if charset_size else 0
    return round(entropy, 2)

def analyze_password(password):
    zx = zxcvbn(password)
    ent = entropy_score(password)
    return {
        'password': password,
        'zxcvbn_score': zx['score'],
        'entropy_bits': ent,
        'crack_time': zx['crack_times_display']['offline_fast_hashing_1e10_per_second'],
        'feedback': zx['feedback']
    }
