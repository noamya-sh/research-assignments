import sys, math

w, h = [int(i) for i in input().split()]
jumps = input()  # number of turns before game over is useless
x0, y0 = [int(i) for i in input().split()]

# x0 y0 for store previous position
x, y = x0, y0

intervalX, intervalY = range(w), range(h)

while True:
    massage = input()
    # uses massage to abridge the interval where bomb could be
    if massage == "UNKNOWN":  # first turn
        pass
    elif len(intervalX) != 1:
        if massage == "SAME":  # you jumped to other side
            intervalX = [i for i in intervalX if abs(x0 - i) == abs(x - i)]
        elif massage == "WARMER":
            intervalX = [i for i in intervalX if abs(x0 - i) > abs(x - i)]
        else:
            intervalX = [i for i in intervalX if abs(x0 - i) < abs(x - i)]
    # if finish with x
    else:
        if massage == "SAME":  # you jumped to other side
            intervalY = [i for i in intervalY if abs(y0 - i) == abs(y - i)]
        elif massage == "WARMER":
            intervalY = [i for i in intervalY if abs(y0 - i) > abs(y - i)]
        else:
            intervalY = [i for i in intervalY if abs(y0 - i) < abs(y - i)]
    # chooses the new location so that it allows to split the area in half next turn
    x0, y0 = x, y
    # first get x of bomb
    if len(intervalX) != 1:
        # the bisection between x0 and x should cut the area in 2 so:
        # (x + x0)/2 = (xs[0] + xs[-1])/2
        if x0 == 0 and len(intervalX) != w:
            x = (intervalX[0] + intervalX[-1]) // 2
        elif x0 == w - 1 and len(intervalX) != w:
            # avoid stay in same place
            x = (intervalX[0] + 3 * intervalX[-1]) // 2 - x0
        else:  # not in edge
            x = intervalX[0] + intervalX[-1] - x0

        # to avoid fixed points
        if x == x0:
            x += 1
        x = min(max(x, 0), w - 1)

    else:
        # transition to second dichotomy
        if x != intervalX[0]:
            x = x0 = intervalX[0]
            print(x, y)
            info = input()
        # finishing
        if len(intervalY) == 1:
            y = intervalY[0]
        # dichotomy along y axis
        else:
            if y0 == 0 and len(intervalY) != h:
                y = (intervalY[0] + intervalY[-1]) // 2
            elif y0 == h - 1 and len(intervalY) != h:
                # avoid stay in same place
                y = (intervalY[0] + 3 * intervalY[-1]) // 2 - y0
            else:  # not in edge
                y = intervalY[0] + intervalY[-1] - y0
            y = min(max(y, 0), h - 1)

    print(x, y)
