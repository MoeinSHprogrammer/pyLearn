
weight = int(input('Enter Weight in kg: '))
height = float(input('Enter Height in cm: '))

BMI = weight / (height/100)**2

if BMI < 18.5:
    print('Under Wight')

elif BMI > 18.5 and BMI < 24.9 :
    print('Normal')

elif BMI > 25 and BMI < 29.9 :
    print('Over Wight')

elif BMI > 30 and BMI < 34.9 :
    print('OBESE')

elif BMI > 35 :
    print('Extremely OBESE')



