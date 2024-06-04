import re
import random
import string

handle = open("user.txt", "r")

text = handle.read()
users = re.findall("(\w.+)@", text)

emailst = []
para = text.split()
for word in para:
    if "@" in word:
        emailst.append(word)

passwords = []
for user in emailst:
    psw = "".join(random.choice(string.ascii_letters + string.digits) for i in range(8))
    passwords.append(psw)

for i in range(len(users)):
    print(f"{emailst[i]} username: {users[i]}, password: {passwords[i]}")

handle.close()