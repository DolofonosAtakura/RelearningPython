# to-do: 
# not do a users sub array so you can look up usernames afterwards

# import time
# ^removed because i was curious on code speed:
# usersCSVtoDict: 0.0013560000000000013
# usersChanged:   0.00012119999999999839
# roughly 10x faster

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

def usersChanged(infile):
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


def main():
    file = "userinfo.csv"
    q1 = usersCSVtoDict(file)
    q2 = usersChanged(file)
    if q1 == q2:
        print(q1)
    else:
        print("not the same")

if __name__ == '__main__':
    main()
