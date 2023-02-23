#DAYDAYUP Q1
a = 1
for i in range(20):
    dayup = pow(1.07, i)
    print(dayup)
    a += 1
    print("a{}".format(a))
    if dayup > 2:
        print(i)

#print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
