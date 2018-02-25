#!/usr/bin/python3

from z3 import *

def check_serial(key):
    if (key[4] != '-' or key[9] != '-' or key[14] != '-'):
        return False
    if (ord(key[5]) != (ord(key[6]) + 1)):
        return False
    if key[5] != key[18]:
        return False
    if (ord(key[1]) != (ord(key[18]) % 4) * 22):
        return False
    if ((ord(key[3])*ord(key[15]))/ord(key[17]))-1 != ord(key[10]):
        return False
    if key[10] != key[1]:
        return False
    if ord(key[13]) != ord(key[10]) + 5:
        return False
    if ord(key[10]) != ord(key[5]) - 9:
        return False
    if (ord(key[0]) % ord(key[7])) * ord(key[11]) != 1440:
        return False
    if (ord(key[2]) - ord(key[8]) + ord(key[12])) != (ord(key[10]) - 9):
        return False
    if ((ord(key[3]) + ord(key[12])) / 2) != ord(key[16]):
        return False
    if (ord(key[0]) - ord(key[2]) + ord(key[3])) != (ord(key[12]) + 15):
        return False
    if key[3] != key[13]:
        return False
    if key[16] != key[0]:
        return False
    if ord(key[7]) + 1 != ord(key[2]):
        return False
    if ord(key[15]) + 1 != ord(key[11]):
        return False
    if ord(key[11]) + 3 != ord(key[17]):
        return False
    if ord(key[7]) + 20 != ord(key[6]):
        return False
    return True

def solve():
    solver = Solver()
    var = []
    for i in range(19):
        var.append(Int(str(i)))
        if i == 4 or i == 9 or i == 14:
            solver.add(var[i] == ord('-'))
    solver.add(var[5] == (var[6] + 1))
    solver.add(var[5] == var[18])
    solver.add(var[1] == (var[18] % 4) * 22)
    solver.add(((var[3]*var[15])/var[17])-1 == var[10])
    solver.add(var[10] == var[1])
    solver.add(var[13] == var[10] + 5)
    solver.add(var[10] == var[5] - 9)
    solver.add((var[0] % var[7]) * var[11] == 1440)
    solver.add((var[2] - var[8] + var[12]) == (var[10] - 9))
    solver.add(((var[3] + var[12]) / 2) == var[16])
    solver.add((var[0] - var[2] + var[3]) == (var[12] + 15))
    solver.add(var[3] == var[13])
    solver.add(var[16] == var[0])
    solver.add(var[7] + 1 == var[2])
    solver.add(var[15] + 1 == var[11])
    solver.add(var[11] + 3 == var[17])
    solver.add(var[7] + 20 == var[6])

    if str(solver.check()) != "sat":
        return("Cannot solve :/")
    else:
        model = solver.model()
        ret = ""
        for x in var:
            try:
                c = chr(int(str(model[x])))
            except:
                c = '~'
            ret += c
        return ret

key = solve()
print(check_serial(key))
print(key)
