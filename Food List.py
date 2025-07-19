import pandas as pa
import lxml
from openpyxl import load_workbook

Dishes = {
    "food_name": ["Biryani", "Zinger", "Nihari", "Pizza", "Pulao", "Shawarma" ],
    "prices": [260, 280, 400, 500, 150, 600],
    "category": ["Desi", "Fast Food", "Desi", "Italian", "Desi", "Fast Food"],
    "main_ingredient": ["Rice", "Chicken Fillet", "Mutton", "Flour Dough", "Rice", "Marinated Meat"],
    "quantity": [1, 2, 5, 6, 7, 9],
    "status": ["available", "available", "not available", "available", "available", "not available"],
}

df_food = pa.DataFrame(Dishes)
df_food["country"] = ["Pakistan", "United States", "Pakistan", "Italy", "Pakistan", "United States"]
df_food["sale_price"] = [200, 150, 300, 400, 100, 500]
print(df_food[df_food["prices"] > 500])
print(df_food[df_food["status"] == "available"])
print(df_food[(df_food["status"] == "available") & (df_food["category"] == "Fast Food")])
print(df_food[(df_food["status"] == "available") & (df_food["prices"] > 1500)])
print(df_food[df_food["food_name"] == "Biryani"])
choice = input("Enter  c - CSV\nx - XML\nj - JSON\ne - EXCEL")
if choice.lower() == "c":
    df_food.to_csv("food_list.csv", index=False)
elif choice.lower() == "x":
    df_food.to_xml("food_list.xml")
elif choice.lower() == "j":
    df_food.to_json("food_list.js")
elif choice.lower() == "e":
    df_food.to_excel("food_list.xlsx")
else:
    print("Invalid input")






