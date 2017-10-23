f = open("World's Largest Countries.txt","r")
dic = {}
for i in range(125):
    tup = ""
    for b in range(5):
        a = f.readline()
        #a = str(a)
        a.strip()
        print(a)
        tup += a
    temp = i + 1
    tup = (tup[1],tup[2],tup[3],tup[4])
    dic[temp] = tup
f.close

STnum = [1,21,31,41,51,61,71,81,91,101,121]
NDnum = [2,22,32,42,52,62,72,82,92,102,122]
RDnum = [3,23,33,43,53,63,73,83,93,103,123]

def info(x):
    ending = ""
    if x in STnum:
        ending = "st"
    elif x in NDnum:
        ending = "nd"
    elif x in RDnum:
        ending = "rd"
    else:
        ending = "th"

    if x > 125:
        print("The highest city i have on record is 125th largest")
    else:
        print(dic[x][0],"is the",x,ending,"largest city in the world")
        print("The population is", dic[x][1])
