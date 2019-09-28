from deli0061Library import calculateMpg

m = float(input("How many miles have you driven? "))
g = float(input("How many gallons of gas have you used? "))
mpg = calculateMpg(m, g)
print("Your car does", mpg, "miles per gallon.")