import sys



def solve(var):
    for pos,s in enumerate(var):
        n = s[0]
        p = s[1]
        ourpath = ""
        for letter in p:
            if letter == "S":
                ourpath += "E"
            elif letter == "E":
                ourpath += "S"
        print("Case #%s: %s" % (pos+1, ourpath))
        


def take_input(inputs):
    for i in range(len(inputs)):
        inputs[i] = inputs[i].rstrip("\n")
    t = int(inputs[0])
    var = []
    for x in range(t):
        inputs[2*x+1] = int(inputs[2*x+1])
        var.append([inputs[2*x+1], inputs[2*x+2]])
    solve(var)
        


inputs = sys.stdin.readlines()
take_input(inputs)
