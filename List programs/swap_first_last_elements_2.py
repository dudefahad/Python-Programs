def swaplist(newlist):
    size=len(newlist)

    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist

newlist=[1,2,3,4,5]
print(swaplist(newlist))