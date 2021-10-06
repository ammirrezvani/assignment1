height=float(input("please enter your height in meter:"))
age=int(input("please enter your age:"))
weight=float(input("please enter your weight in kilogeram:"))
bmi=weight/(height*height)
print("ypur bmi index is :",bmi)
if bmi<18.5:
    print("you are underweight ; eat more:)")
elif bmi>18.5 and bmi<24.9:
    print("you have normal weight")
elif bmi>25 and bmi<29.9:
    print("you are overweight")    
elif bmi>30 and bmi<34.9:
    print("you are obese")
elif bmi>35:
    print("you are extremely obese")    
