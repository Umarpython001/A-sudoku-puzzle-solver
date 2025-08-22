import time

def decorate_time(func):
    def wrapper(*args,**kwargs):
        time_1 = time.time()
        grnd = func(*args,**kwargs)
        time_2 = time.time()
        time_taken = time_2 - time_1
        print(f"Completed in {(time_taken):.2f} seconds")
        return grnd
    return wrapper    



@decorate_time
def quadrilateral(): 
    #This code creates a grid of "#" 

    #Takes the collected width and height and stores it in variables y and a respectively then itrates over the number of vertial lines and prints the width over each iteration.
    def main():
        y = width()
        a = vert()
        for i in range(a):
            print(y)
        

    #Collects the desired width of the grid from the user and returns it.
    def width():
        while True:
            try:
                x = int(input("How long should your grid be?"))
            except ValueError:
                print("input a valid number")    
            else:
                break    
        print(f"Your grid is {x} units long.")
        sign = input("Enter any symbol for your grid: ")
        return sign * x

    #Collects the desired height of the grid from the user.
    def vert():
        while True:
            try:
                n = int(input("What should the vertical height be?"))
            except ValueError:
                print("input a valid number")    
            else:
                print(f"Your grid is {n} units high.")
                return n
    main()             

@decorate_time
def right_triangle():
    def height():
        while True:
            try:
                H = int(input("Enter how tall your right triangle should be: "))
            except ValueError or TypeError:
                print("Enter only numbers")
            else:
                print(f"Your right triangle is {H} units high.")  
                return list(range(H))                
                break  

    def main():
        x = input("Enter any ascii symbol for the triangle: ")
        y = height()
        print("=======YOUR RIGHT TRIANGLE 🎺🎺🎺=======")
        for i in y:
            n = y.index(i)
            print(f"{x*n}")

    main()


@decorate_time
def tri():
    while True:
        try:
            # base =  int(input("Enter a number as the length of the base of the triangle: "))
            height = int(input("Enter a number as the height of the triangle: "))
        except ValueError:
            print("ENTER ONLY NUMBERS")    
        else:
            # print("Base:",base)
            print("Height:",height)
            symbol = input("Enter a symbol for the triangle: ")
            break
        
    for i in range(1,height+1):
        print(" "*(height-i)+(symbol+" ")*i)



@decorate_time
def diamond():
    while True:
        try:
            # base =  int(input("Enter a number as the length of the base of the triangle: "))
            height = int(input("Enter a number as the height of the diamond: "))
        except ValueError:
            print("ENTER ONLY NUMBERS")    
        else:
            # print("Base:",base)
            print("Height:",height)
            symbol = input("Enter a symbol for the triangle: ")
            break
    
    for i in range(1,height+1):
        print(" "*(height-i)+(symbol+" ")*i)
    for i in range(height-1,0,-1):
        print(" "*(height-i)+(symbol+" ")*i)    


if __name__=="__main__":
    quadrilateral()
    diamond()
    right_triangle()
    tri()