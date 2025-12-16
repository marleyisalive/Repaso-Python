#Programa que calcula el area de diferentes figuras geometricas
option = 0
pi = 3.14
while option != 5:
    print("=================\n Area Calculator\n================= 📐")
    #Menu
    print(
        "1) Square\n"
        "2) Rectangle \n" 
        "3) Triangle \n" 
        "4) Circle \n" 
        "5) Quit")
    print()
    option = int(input("Enter your option: "))

    if option == 1:
        side = float(input("Enter the square side value: "))
        area = side ** 2
        print(f'\n The area of the square is {area}\n')

    elif option == 2:
        lenght = float(input("Enter the rectangle lenght: "))
        width = float(input("Enter the rectangle width: "))
        area = lenght * width
        print(f'\n The area of the rectangle is {area}\n')

    elif option == 3:
        area, height, base = 0.0, 0.0, 0.0
        height = float(input("Enter the triangle height: "))
        base = float(input("Enter the triangle base: "))
        area = (height * base)/2
        print(f'\n The area of the triangle is {area}\n')
    elif option == 4:
        radius = float(input("Enter the circle radius: "))
        area = pi * radius ** 2
        print(f'\n The area of the circle is {area}\n')
    elif option == 5:
        print("See you later")
    else:
        print("\n¡ Type a correct option in the menu! \n")
    

    


    