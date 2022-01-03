import hashlib
import os
data = "a7312e17ba07ab09dacfebc4cdc2fe516043c1c2fd71078abcebb1e2a017f6c8"
path_of_the_directory = 'Q2'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory, filename)
    if os.path.isfile(f):
        with open(os.path.join('Q2', filename), 'r') as f:
            while True:
                flag = False
                text = f.readline()
                password = f"{text.strip()}{filename}"
                num, clean = password.split('_', 1)
                if num.isnumeric():
                    for i in range(int(num)):
                        hashed = hashlib.sha256(clean.encode('utf-8')).hexdigest()
                        clean = hashed
                        if hashed == data:
                            flag = True
                            print(f"the password is: {password}")
                            break
                        if not text:
                            break
                elif not num.isnumeric():
                    break
