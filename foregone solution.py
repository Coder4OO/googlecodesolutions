import sys

def solve(t, n):
    ans = []
    for c in n:
        s = 0
        for pos,d in enumerate(reversed(c)):
            if d == "4":
                s += 1*pow(10,pos)
        finalans = str(int(c)-s)+" "+str(s)
        ans.append(finalans)
    for i in range(len(ans)):
        print("Case #%s: %s" % (i+1, ans[i]))


def take_test_cases(inputs):
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
    t = int(lines[0])
    n = []
    for i in range(len(lines)-1):
        n.append(lines[i+1])
    solve(t, n)


lines = sys.stdin.readlines()
take_test_cases(lines)
