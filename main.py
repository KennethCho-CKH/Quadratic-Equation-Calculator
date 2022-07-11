# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

#import module
import math

print("Substitude the numbers according to this formula:")
print("ax^2 + bx + c")

a = input("a = ")
b = input("b = ")
c = input("c = ")

#Equation: (-b±√(b^2-4ac))/2a
try:
    d = math.sqrt((float(b)**2)-(4*float(a)*float(c)))

    ans_1 = (-float(b)+d)/(2*float(a))
    ans_2 = (-float(b)-d)/(2*float(a))

    if ans_1 == ans_2:
        print(f'x = {ans_1}')
    else:
        print(f'x = {ans_1} or')
        print(f'x = {ans_2}')
except:
    print("Error occured, please try again.")