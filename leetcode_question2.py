
def sumlist(l1,l2):
    l = max(len(l1), len(l2))
    anw  = []
    flag = 0
    for i in range(l):
        if (len(l1) - i >= 0 and len(l2) - i >= 0):
            if flag == 1:
                sum = l1[i] + l2[i] + 1
                flag = 0
            else:
                sum = l1[i] + l2[i]
            if sum >= 10:
                anw.append(sum - 10)
                flag = 1
            else:
                anw.append(sum)
        elif (len(l1) - i < 0 and len(l2) - i >= 0):
            if flag == 1:
                anw.append(l2[i]+ 1)
            else:
                anw.append(l2[i])
        else:
            if flag == 1:
                anw.append(l2[i] + 1)
            else:
                anw.append(l2[i])
    return anw

if __name__ == '__main__':
    l1 = list(map(lambda x: int(x), input()[1:-1].split(",")))
    l2 = list(map(lambda x: int(x), input().split(",")))
    print(sumlist(l1,l2))