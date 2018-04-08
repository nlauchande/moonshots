def calculate_damage(p):
    damage = 0
    charge = 1
    for c in p :
        if c == "C":
            charge = charge*2
        elif c =="S":
            damage = damage+charge
    return damage


def solve_it(damage, p):
    nshoots = p.count('S')
    
    if nshoots > damage:
        return "IMPOSSIBLE"

    if calculate_damage(p)<=damage:
        return 0

    nswaps = 0

    i = len(p)-1
    while i>0:
        if p[i] == 'S':
            # Try to push the next C in this direction
             j = i-1
             while p[j]!='C':
                 j = j-1

             for k in range(j,i):
                p[k+1], p[k] = p[k], p[k+1]
                nswaps += 1
                if calculate_damage(p) <= damage:
                    return nswaps
        i = i-1

    return nswaps


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  damage, p = input().split(" ") # Read a string

  print("Case #{}: {}".format(i, solve_it(int(damage), list(p))))
