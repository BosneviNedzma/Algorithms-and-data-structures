 
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
    

    def zadatak8(g):
        
        if(g % 400 == 0)and(g % 100 == 0):
            print(str(g)+"Je prestupna")
        elif (g % 4==0)and(g%100 !=0):
            print(str(g)+" je prijestupna godina")
        else:
            print(str(g)+"nije prijestupna godina")


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
        