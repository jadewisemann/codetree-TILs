import re
I =  lambda: int(re.sub('[a-zA-Z]', '', str(input())))

print(I() + I())