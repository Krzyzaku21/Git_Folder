lst = []
passwd = ["PE7UZF8UDRBi"]
code = [["Z", "2"], ["8", "B"], ["D", "0", "O"]]
x = code[0]
y = code[1]
z = code[2]
num = 0
num2 = 0
while len(x) > num:
    for word in passwd:
        if "Z" in word:
            rep = "1--" + word.replace("Z", x[num])
            lst.append(rep)
        if "Z" in word:
            rep = "2--" + word.replace("2", x[num])
            lst.append(rep)
        if "8" in word:
            rep = "3--" + word.replace("8", y[num])
            lst.append(rep)
        if "B" in word:
            rep = "4--" + word.replace("B", y[num])
            lst.append(rep)
        if "D" in word:
            rep = "5--" + word.replace("D", z[num])
            lst.append(rep)
        if "0" in word:
            rep = "6--" + word.replace("0", z[num])
            lst.append(rep)
        if "O" in word:
            rep = "7--" + word.replace("O", z[num])
            lst.append(rep)
        else:
            pass
print(lst)
