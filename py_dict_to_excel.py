
from math import prod
import pandas as pd

student = [
    {"Name": "Vishvajit Rao", "age": 23,
        "Occupation": "Developer", "Language": "Python"},
    {"Name": "Niaj", "age": 29, "Occupation": "Engineer", "Language": "Python"},
    {"Name": "John", "age": 33, "Occupation": "Front End Developer", "Skills": "Angular"},
    {"Name": "Harshita", "age": 21, "Occupation": "Tester", "Skills": "Selenium"},
    {"Name": "Mohak", "age": 30, "Occupation": "Full Stack", "Skills": "Python, React and MySQL"}]

product_data = {
    "category": "",
    "shop_sku": "",
    "title": "",
    "description": "",
    "brand": "",
    "image_1": "",
    "image_2": "",
    "colour_group": "",
    "colour": "",
    "material": "",
    "gender": "",
    "age": "",
    "size": "",
    "bed_size": "",
    "shape": "",
    "mattress_material": "",
    "sku": "",
    "product-id": "",
    "product-id-type": "",
    "offer-description": "",
    "internal-description": "",
    "price": "",
    "price-additional-info": "",
    "quantity": "",
    "min-quantity-alert": "",
    "state": "",
    "available-start-date": "",
    "available-end-date": "",
    "logistic-class": "",
    "discount-price": "",
    "discount-start-date": "",
    "discount-end-date": "",
    "leadtime-to-ship": "",
    "update-delete": "",
    "pi": "",
    "presale-date": "",

}

# convert into dataframe
df = pd.DataFrame(data=student)

# convert into excel
df.to_excel("students.xlsx", index=False)
print("Dictionary converted into excel...")
