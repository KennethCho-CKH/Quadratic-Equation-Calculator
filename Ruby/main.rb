module Math

    puts("Substitude the numbers according to this formula:")
    puts("ax^2 + bx + c")

    print("a = ")
    a = gets.to_f
    print("b = ")
    b = gets.to_f
    print("c = ")
    c = gets.to_f

    #Equation: (-b±√(b^2-4ac))/2a

    begin
        delta = Math.sqrt((b**2)-(4*a*c))

        solution_1 = (-b+delta)/(2*a)
        solution_2 = (-b-delta)/(2*a)

        if solution_1 == solution_2
            puts("x = %d" %solution_1)
        else
            puts("x = %d or" %solution_1)
            puts("x = %d" %solution_2)
        end
    rescue
        puts("Error occured, please try again.")
    end
end