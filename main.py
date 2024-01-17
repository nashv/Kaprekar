def differenceofsorted(x):
    a = int("".join(sorted(str(x))).strip())
    d = int("".join(sorted(str(x), reverse=True)).strip())
    q = d - a
    print(x, " : ", d, " - ", a, "= ", q)
    if (q == 6174):  # 4-digit Kaprekar constant
        print("Goal Reached for: ", x)
    elif (q == 495):  # 3-digit Kaprekar constant
        print("Goal Reached for: ", x)
    elif (q == 0):
        print("Zero difference encountered for :", x)
    else:
        x = differenceofsorted(q)


# Loop through all 4-digit numbers
for n in range(1, 999):
    differenceofsorted(n)
