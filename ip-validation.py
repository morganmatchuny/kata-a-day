#Write an algorithm that will identify valid IPv4 addresses 
#in dot-decimal format. Input to the function is guaranteed 
#to be a single string.

#Examples of valid inputs: 1.2.3.4 123.45.67.89

#Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089


import re

IP_PATTERN = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')

def is_valid_IP(ipv4):
    match = re.match(IP_PATTERN, ipv4)
    if not match:
        return false
    parts = match.groups()

    for part in parts:
        if int(part) < 0 or int(part) > 255:
            return False
        if part.startswith('0') and len(part) > 1:
            return false
    return true
