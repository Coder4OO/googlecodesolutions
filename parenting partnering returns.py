import sys
import string

def sort_activities(activities):
    for i in range(len(activities)):
        for j in range(len(activities[i])-1):
            activities[i][j] = int(activities[i][j])
    orig = activities
    starttimes = []
    for i in range(len(orig)):
        starttimes.append(orig[i][0])
    starttimes.sort()
    returnlist = []
    for i in range(len(starttimes)):
        for j in range(len(orig)):
            if orig[j][0] == starttimes[i]:
                returnlist.append(orig[j])
    return returnlist

def assemble_finalstr(s):
    sortlist = s.split(' ')
    del sortlist[len(sortlist)-1]
    finalstr = ""
    digitlist = list(range(0, len(sortlist)))
    for i in range(len(sortlist)):
        s = sortlist[i]
        digit = int(sortlist[i][1])
        digitlist[digit] = s[0]
    for i in range(len(digitlist)):
        finalstr += digitlist[i]
    return finalstr

def solve(activities):
    cameron = 0
    jamie = 0
    rs = ""
    sortstr = ""
    orig = activities
    activities = sort_activities(activities)
    assemble = True
    for i in range(len(activities)):
        activity = [activities[i][0], activities[i][1]]
        tag = activities[i][2]
        starttime = int(activity[0])
        endtime = int(activity[1])
        if starttime >= cameron:
            sortstr += "C"+str(tag)+" "
            cameron = endtime
        elif starttime >= jamie:
            sortstr += "J"+str(tag)+" "
            jamie = endtime
        else:
            rs = "IMPOSSIBLE"
            assemble = False
            break
    if assemble:
        rs = assemble_finalstr(sortstr)
    return rs



def take_inputs(inp):
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip("\n")
    t = int(inp[0])
    del inp[0]
    for i in range(t):
        a = int(inp[0])
        del inp[0]
        activities = []
        for j in range(a):
            activity = inp[0]
            del inp[0]
            activity = activity.split(' ')
            activity.append(j)
            activities.append(activity)
        ans = solve(activities)
        print("Case #%s: %s" % (i+1, ans))
            
    

inp = sys.stdin.readlines()
take_inputs(inp)
