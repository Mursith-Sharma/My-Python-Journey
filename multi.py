class multifunction():
    def oddeven():
        num = int(input("enter the number")) 
        if(num%2 == 0):
           print("even number")
        else:
           print("odd number")

    def BMI():
        BMI = int(input("enter  the BMI index"))
        if(BMI<18.4):
            print("underweight")
        elif(18.5<= BMI <= 24.9):
            print("normal")
        elif(25.0<= BMI <= 39.9):
            print("over weight")
        else:
            print("obese")
            
multifunction.oddeven()
multifunction.BMI()