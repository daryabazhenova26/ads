w1 = input()
w2 = input()
for i in range(len(w1)):
    if len(w1) != len(w2):
        print("NO")
        break
    elif w1.count(w1[i]) != w2.count(w1[i]):
        print("NO")
        break
else:
    print("YES")