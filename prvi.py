 
    def zadatak1():
        print("Programming", "Essentials", "in", sep="***", end="...")
        print("Python")
    
    def zadatak2():
        print(" *"," * *"," * *"," * *","*** ***"," * *"," * *"," *****")
    
    def zadatak3():
        print("\"I'm\"\n\"\"Learning\"\"\n\"\"\"Python\"\"\"" )

    def zadatak4(a, b):
        c=((a**2)+(b**2))**(1/2)
        print("Rjesenje izraza c je:", c)
    
    def zadatak5(a):
        x = 3*(a**3)-2*(a**a)+3*a-1
        print("Rjesenje zadatka je: " x)

    def zadatak6():
        kilometers = 12.25
        miles = 7.38
        miles_to_kilometers = miles*1.61
        kilometers_to_miles = kilometers/1.61
        print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
        print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

    def zadatak7(a):
        income = float(input("Enter the annual income: "))
        
        if inclome>35500:
            tax = income*1.8-1390
        else:
            tax = 5000+35500*3.2

        tax = round(tax, 0)
        print("The tax is:", tax, "€")


    def zadatak8(g):
        
        if(g % 400 == 0)and(g % 100 == 0):
            print(str(g)+"Je prestupna")
        elif (g % 4==0)and(g%100 !=0):
            print(str(g)+" je prijestupna godina")
        else:
            print(str(g)+"nije prijestupna godina")


    def zadatak9():
        def is_year_leap(year):

        if(g % 400 == 0)and(g % 100 == 0):
            print(str(g)+"Je prestupna")
        elif (g % 4==0)and(g%100 !=0):
            print(str(g)+" je prijestupna godina")
        else:
            print(str(g)+"nije prijestupna godina")
    
        test_data = [1900, 2000, 2016, 1987]
        test_results = [False, True, True, False]
        for i in range(len(test_data)):
        yr = test_data[i]
        print(yr,"->",end="")
        result = is_year_leap(yr)
        if result == test_results[i]:
        print("OK")
        else:
        print("Failed")

    def zadatak11(g,m):

        def is_year_leap(year):
        
            if(g % 400 == 0)and(g % 100 == 0):
                print(str(g)+"Je prestupna")
                return True
            elif (g % 4==0)and(g%100 !=0):
                print(str(g)+" je prijestupna godina")
                return True
            else:
                print(str(g)+"nije prijestupna godina")
                return False
        
        def days_in_month(year, month):
        
            if(is_year_leap(year, month) and month == 2):
                print("29")
            elif(is_year_leap(year, month) == False and month == 2):
                print("28")
            elif(month == 1, 3, 5, 7, 8, 10, 12):
                print("31")
            else:
                print("30")

    def zadatak12():
        def liters_100km_to_miles_gallon(liters):
            lirers = 1609.344 * miles
        def miles_gallon_to_liters_100km(miles):
            miles = 3.785411784 * liters
        print(liters_100km_to_miles_gallon(3.9))
        print(liters_100km_to_miles_gallon(7.5))
        print(liters_100km_to_miles_gallon(10.))
        print(miles_gallon_to_liters_100km(60.3))
        print(miles_gallon_to_liters_100km(31.4))
        print(miles_gallon_to_liters_100km(23.5))
        