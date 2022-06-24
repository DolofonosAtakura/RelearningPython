# to-do: 
# not do a users sub array so you can look up usernames afterwards

import time
# ^removed because i was curious on code speed:
# usersCSVtoDict: 0.0013560000000000013
# usersChanged:   0.00012119999999999839
# users3:         0.00011780000000000124
# unsure why users3 is so much slower than users2

# translates a user CSV to a dictionary, currently requires a blank line at the bottom to function, can add try/except to fix
def usersCSVtoDict(infile):
    # start = time.perf_counter()
    d = dict()

    with open(infile) as a:
        keys = a.readline().lower().strip().split(",")
        count = 0

        while True:
            r = a.readline().strip().split(",")
            if r == [""]:
                break
            else:
                d.update({f"User{count}":{}})
                count2 = 0
                for i in range(0,len(keys)):
                    d[f"User{count}"].update({f"{keys[i]}":r[count2]})
                    count2 += 1                    
            count += 1
    # print(time.perf_counter()-start)
    return d

def users2(infile):
    # start = time.perf_counter()
    d = dict()

    with open(infile) as a:
        fileInfo = a.read()

    slist = fileInfo.split("\n")
    del a, fileInfo
    keys = slist[0].lower().strip().split(",")

    for i in range(1,len(slist)):
        r = slist[i].split(",")
        ind = i - 1
        d.update({f"User{ind}":{}})

        for j in range(0,len(keys)):
            d[f"User{ind}"].update({f"{keys[j]}":r[j]})
        
    # print(time.perf_counter()-start)
    return d

def users3(infile):
    start = time.perf_counter()
    with open(infile) as a:
        slist = a.read().split("\n")
    
    del a
    d = dict()
    keys = slist[0].lower().strip().split(",")

    for i in range(1,len(slist)):
        r = slist[i].split(",")
        d.update({f"{r[0]}":{}})

        for j in range(0,len(keys)):
            d[r[0]].update({f"{keys[j]}":r[j]})


    print(time.perf_counter()-start)
    return d


def main():
    file = "userinfo.csv"
    
    # q1 = usersCSVtoDict(file)
    # q2 = users2(file)
    q3 = users3(file)
    
    #print(q3)

if __name__ == '__main__':
    main()
