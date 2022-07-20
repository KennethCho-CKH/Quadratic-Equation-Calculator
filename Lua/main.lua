print("Substitude the numbers according to this formula:")
print("ax^2 + bx + c")

io.write("a = ")
a = io.read()
io.write("b = ")
b = io.read()
io.write("c = ")
c = io.read()

--Equation: (-b±√(b^2-4ac))/2a

delta = math.sqrt((b^2)-(4*a*c))

solution_1 = (-b+delta)/(2*a)
solution_2 = (-b-delta)/(2*a)
  
if(solution_1 == solution_2)
then
  print("x = " .. solution_1)
  print()
else
  print("x = " .. solution_1 .. " or ")
  print("x = " .. solution_2)
end