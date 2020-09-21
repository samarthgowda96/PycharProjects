str = str(input("enter the input:"))

def findLongSubarray(string):
    length = len(string)

    curStart = 0

    start = 0
    maxlen = 0

    pos = {}

    pos[string[0]]= 0

    for i in range(1,length):
        if string[i] not in pos:
            pos[string[i]] = i

        else:
            if pos[string[i]]>= curStart:
                curLength = i - curStart
                if maxlen < curLength:
                    maxlen = curLength
                    start = curStart

                curStart = pos[string[i]] +1

            pos[string[i]]= i
    if maxlen < i - curStart:
        maxlen = i - curStart
        start = curStart

    return string[start:start+maxlen]

x= findLongSubarray(str)
print(x)

