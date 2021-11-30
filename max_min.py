def maxAndMinFunc(a,b,c,d):
    import math as m
    
    #Find the first derivative of the function
    a_der= a*3 
    b_der =b*2
    
    #Find the discriminant
    forDis = b_der**2 - 4*a_der*c
    #print(forDis)
    if forDis >= 0:
        x1 = (-b_der - m.sqrt(forDis))/ (2*a_der)
        x2 = (-b_der + m.sqrt(forDis))/ (2*a_der)
    # Calculate the values of the function at the ends of the interval
    f_4 = a*m.pow(-4,3) + b*m.pow(-4,2) + c*(-4) + d
    f_1 = a*m.pow(1,3) + b*m.pow(1,2) + c*1 + d
    f_x1 = a*m.pow(x1,3) + b*m.pow(x1,2) + c*x1 + d
    f_x2 = a*m.pow(x2,3) + b*m.pow(x2,2) + c*x2 + d
    # Calculate the max value
    fmax = (max(f_1, f_4, f_x1, f_x2))
    # Calculate the min value
    fmin = (min(f_1, f_4, f_x1, f_x2))
    print("Max", fmax)
    print("Min", fmin)

print("Max and min fucnt 3.1x^3 + 10.3x^2 - 2.8x + 10.3")
maxAndMinFunc(3.1,10.3,-2.8,10.3)
print("Max and min fucnt 2.1^3 + 8.8x^2 - 11.3x - 5.6")
maxAndMinFunc(2.1,8.8,-11.3,-5.6)
print("Max and min fucnt 1.6x^3 + 0.2x^2 - 20.8x + 38.5")
maxAndMinFunc(1.6,0.2,-20.8,38.5)