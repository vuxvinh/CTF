with open(r'C:\Users\admin\Desktop\CTF\password.txt', "a") as file:
    file.truncate(0)
f=open(r'C:\Users\admin\Desktop\CTF\password.txt', "a")
for i1 in range(97,123):
    for i2 in range(97,123):
        for i3 in range(97,123):
            for i4 in range(97,123):
                for i5 in range(97,123):
                    for i6 in range(97,123):
                        if i1 & i3 == 96 and i2 | i5 == 97 and i4 ^ i6 == 6:
                            password=chr(int(i1))+chr(int(i2))+chr(int(i3))+chr(int(i4))+chr(int(i5))+chr(int(i6))
                            f.write(password+'\n')
f.close()