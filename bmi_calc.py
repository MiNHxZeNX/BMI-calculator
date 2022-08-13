height = float(input("Welcome to BMI Calculator\n Please enter your height in meter : "))
weight = float(input("Please enter your weight in KiloGram : "))
bmi = weight /(height**2)
bmi2 = round(bmi,2)
print("Your Body Mass Index is : " + str(bmi2))
if (bmi2<18.5):
    print("you are underweight")
elif(bmi2>=18.5 and bmi2 <25):
    print("You have a normal weight")
elif(bmi2>=25 and bmi2 <30):
    print("You are overweight")
elif(bmi2>=30 and bmi2 <35):
    print("You are obese")
else:
    print("you are clinically obese")
