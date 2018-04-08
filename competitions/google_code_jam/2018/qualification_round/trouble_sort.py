def trouble_sort(l):
    done = False
    while not done:
        done = True
        for i in range(0,len(l)-2):
            if l[i] > l[i + 2]:
                done = False
                l[i],l[i+2] = l[i+2],l[i]
    return l

result = trouble_sort([5,6,6,4,3])


def solve_it(l):
    sorted = trouble_sort(l)
    for i in range(0,len(sorted)-1):
        if sorted[i]>sorted[i+1]:
            return i
    return "OK"

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):

    n = int(input())

    list_numbers = [int(s) for s in input().split(" ")]

    print("Case #{}: {}".format(i, solve_it(list_numbers)))