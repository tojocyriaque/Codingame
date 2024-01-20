r = int(input())
l = int(input())
con = [r]

for i in range(l-1):
    
    curr = con[0]
    count = 0
    new_con = []

    for val in con:
        if val==curr:
            count = count+1
        else:
            new_con.append(count)
            new_con.append(curr)
            curr = val
            count = 1

    new_con.append(count)
    new_con.append(curr)

    con = new_con

print(*con)
