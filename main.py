start = 1
end = 10000


def differenceofsorted(x):
    global steps
    a = int("".join(sorted(str(x))).strip())
    d = int("".join(sorted(str(x), reverse=True)).strip())
    q = d - a
    print(x, " : ", d, " - ", a, "= ", q)
    if q == 6174:  # 4-digit Kaprekar constant
        print("Goal Reached for: ", x, "in ", steps, " steps")
    elif q == 495:  # 3-digit Kaprekar constant
        print("Goal Reached for: ", x, "in ", steps, " steps")
    elif q == 0:
        print("Zero difference encountered for :", x, "in ", steps, " steps")
    else:
        differenceofsorted(q)

        steps += 1
    return ()


# Loop through all 4-digit numbers
for n in range(start, end):
    steps = 1
    differenceofsorted(n)
