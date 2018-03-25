#!/usr/bin/env python
# coding: utf-8

from z3 import *

# On declare notre solver z3
solver = Solver()

var = []
# java: serial.length()  ==  19
# On declare donc 19 variables à trouver puisque notre serial fait 19 caractères
for i in range(19):
   var.append(Int(str(i)))
   #java: serial.charAt(4)  ==  '-'  &&
   #      serial.charAt(9)  ==  '-'  &&
   #      serial.charAt(14)  ==  '-'
   # On indiques alors à notre solver que ces 3 valeurs vont être un '-'
   if i == 4 or i == 9 or i == 14:
      solver.add(var[i] == ord('-'))

# On recopie ensuite presque betement toutes les conditions

# java: serial.charAt(5)  == serial.charAt(6)  +  1
solver.add(var[5] == (var[6] + 1))
# java: serial.charAt(5)  == serial.charAt(18)
solver.add(var[5] == var[18])
# java: serial.charAt(1)  ==  (serial.charAt(18)  %  4)  *  22
solver.add(var[1] == (var[18] % 4) * 22)
# java: ((serial.charAt(3)  * serial.charAt(15))  / serial.charAt(17))  -  1  == serial.charAt(10)
solver.add(((var[3] * var[15]) / var[17]) - 1 == var[10])
# java: serial.charAt(10)  == serial.charAt(1)
solver.add(var[10] == var[1])
# java: serial.charAt(13)  == serial.charAt(10)  +  5
solver.add(var[13] == var[10] + 5)
# java: serial.charAt(10)  == serial.charAt(5)  -  9
solver.add(var[10] == var[5] - 9)
# java: (serial.charAt(0)  % serial.charAt(7))  * serial.charAt(11)  ==  1440
solver.add((var[0] % var[7]) * var[11] == 1440)
# java: (serial.charAt(2)  - serial.charAt(8))  + serial.charAt(12)  == serial.charAt(10)  -  9
solver.add((var[2] - var[8] + var[12]) == (var[10] - 9))
# java: (serial.charAt(3)  + serial.charAt(12))  /  2  == serial.charAt(16)
solver.add(((var[3] + var[12]) / 2) == var[16])
# java: (serial.charAt(0)  - serial.charAt(2))  + serial.charAt(3)  == serial.charAt(12)  +  15
solver.add((var[0] - var[2] + var[3]) == (var[12] + 15))
# java: serial.charAt(3)  == serial.charAt(13)
solver.add(var[3] == var[13])
# java: serial.charAt(16)  == serial.charAt(0)
solver.add(var[16] == var[0])
# java: serial.charAt(7)  +  1  == serial.charAt(2)
solver.add(var[7] + 1 == var[2])
# java: serial.charAt(15)  +  1  == serial.charAt(11)
solver.add(var[15] + 1 == var[11])
# java: serial.charAt(11)  +  3  == serial.charAt(17)
solver.add(var[11] + 3 == var[17])
# java: serial.charAt(7)  +  20  == serial.charAt(6)
solver.add(var[7] + 20 == var[6])

# On demande a z3 de résoudre nos conditions
if str(solver.check()) != "sat":
   print("Cannot solve :/")
else:
   model = solver.model()
   serial = ""
   # On itere sur les variables déclaré à z3
   for x in var:
      # z3 nous donnes la valeur dans la table ascii du caractere
      # on le retransforme en char et on concatene nos variables
      serial += chr(int(str(model[x])))

# Et voila, on a notre serial ;)
print(serial)

