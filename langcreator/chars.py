from string import ascii_lowercase, ascii_uppercase, ascii_letters, printable


lower = list(ascii_lowercase)
upper = list(ascii_uppercase)
letters = list(ascii_letters)
tletters = [lower, upper, letters]
sletters = ''.join([''.join(lower), ''.join(upper), ''.join(letters)])
asyms = printable[:-2]
