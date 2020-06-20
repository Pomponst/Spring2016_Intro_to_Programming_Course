##Input
temp = float(input("Enter a temperature:"))
scale = str(input("Enter the scale (F or C):"))

##Logic
if scale=="F":
    conv_temp = round((temp-32) * (5/9),2)
    
else:
    conv_temp = round((temp * (9/5))+32,2)

if scale=="F":
    unit = "Fahrenheit"
    conv_unit = "Celsius"

else:
    unit = "Celsius"
    conv_unit = "Fahrenheit"

##Calculation
print("A temperature of",temp,unit,"equals",conv_temp,conv_unit+".")
