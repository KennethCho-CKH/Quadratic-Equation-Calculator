# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math

print("Substitude the numbers according to this formula:")
print("ax^2 + bx + c")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

#Equation: (-b±√(b^2-4ac))/2a

try:
    delta = math.sqrt((b**2)-(4*a*c))

    solution_1 = (-b+delta)/(2*a)
    solution_2 = (-b-delta)/(2*a)

    if solution_1 == solution_2:
        print(f'x = {solution_1}')
    else:
        print(f'x = {solution_1} or')
        print(f'x = {solution_2}')
except:
    print("Error occured, please try again.")
