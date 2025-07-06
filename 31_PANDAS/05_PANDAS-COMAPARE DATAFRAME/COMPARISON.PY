import pandas as pd
dict={"Fruits":["Apple","Banana","Mango","Orange"],
       "Price":[100,50,80,60],
        "Quantity":[10,20,15,25],
        "Discount":[5,2,3,4]}
df=pd.DataFrame(dict)
df.set_index("Fruits", inplace=True)
def compare_prices(df, fruit1, fruit2):
    price1 = df.loc[fruit1, 'Price']
    price2 = df.loc[fruit2, 'Price']
    
    if price1 > price2:
        return f"{fruit1} is more expensive than {fruit2}."
    elif price1 < price2:
        return f"{fruit1} is cheaper than {fruit2}."
    else:
        return f"{fruit1} and {fruit2} have the same price."