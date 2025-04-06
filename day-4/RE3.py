import re

pwd_pattern = r"[A-Za-z\d@$%*?&]{8,}"

passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]

for p in passwords:
    if re.match(pwd_pattern, p):
        print(p,"-> Valid")
    else:
        print(p,"-> Invalid")