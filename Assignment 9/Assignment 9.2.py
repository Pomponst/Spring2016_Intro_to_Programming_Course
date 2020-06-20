##Input
price = 28000
rate = 4000
year = 1
eoy = price - rate
acc = rate

##Heading
print("Year","\t","Depreciation","\t","EOY Value","\t","Acc.Dep.")

##Logic
while eoy >=0:
    print(year,"\t",rate,"\t\t",eoy,"\t\t",acc)
    year = year + 1
    eoy = eoy - rate
    acc = acc + rate
