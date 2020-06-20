purPrice = float(input("Enter the purchase price:"))
selPrice = float(input("Enter the selling price:"))
markup = selPrice - purPrice
markupPer = (markup/purPrice) * 100
profitMargin = (markup/selPrice) * 100
print("Markup: $",round(markup,2))
print("Percentage Markup:",round(markupPer,2),"%")
print("Profit Margin:",round(profitMargin,2),"%")
