#WRITE A PROGRAM TO MULTIPLY ALL THE ITEMS IN A DICTIONARY

a={ "a":12,"b":30,"c":21,"d":56,"e":31,"f":79 }
print(a["c"])
product=1
for i in a:
    product *=a[i]
print(product)