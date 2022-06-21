file = ""

#translates a user CSV to a dictionary, currently requires a blank line at the bottom to function, can add try/except to fix
def usersCSVtoDict(infile):
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

    return d

def main():
    q = usersCSVtoDict(file)
    print(q)

if __name__ == '__main__':
    main()