import sys


def solve(s):
    for pos, cs in enumerate(s):
        fs = ""
        cs += "0"
        depth = 0
        for cp, cd in enumerate(cs):
            cv = int(cd)
            if cp == 0:
                fs += "("*cv
                fs += cd
                depth = cv
            elif depth-cv > 0:
                fs += ")"*(depth-cv)
                fs += cd
                depth = cv
            elif cv-depth > 0:
                fs += "("*(cv-depth)
                fs += cd
                depth = cv
            elif depth-cv == 0:
                fs += cd
        fs = fs[0:len(fs)-1]

        print("Case #%s: %s" % (pos+1, fs))
                
            


ins = sys.stdin.readlines()

def take_input(ins):
    for i in range(len(ins)):
        ins[i] = ins[i].rstrip("\n")
    t = int(ins[0])
    del ins[0]
    s = ins
    solve(s)

take_input(ins)
