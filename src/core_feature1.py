"""
Core Feature 1 
This program allows the user to enter a product sub-category. 
It filters the dataset and displays the total sales and average salesfor the selected sub-category.
It also handles invalid or empty inputs.
"""

# importing Pandas library 
import pandas as pd

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Create function
def sales_by_subcategory(sub_category):

    if sub_category.strip() == "" :
        print("Please enter a Sub-Category.")
        return

    # Filter data
    filtered = df[df["Sub-Category"] == sub_category]

    if filtered.empty :
        print("Sub-Category not found.")
        return

    # Total sales
    total_sales = filtered["Sales"].sum()

    # Average sales
    average_sales = filtered["Sales"].mean()

    # Print results
    print("Sub-Category:", sub_category)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)

# Take input from user
subcategory = input("Enter Sub-Category: ")

# Call function
sales_by_subcategory(subcategory)

