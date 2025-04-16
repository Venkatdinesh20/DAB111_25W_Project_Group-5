import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style for better visualization
sns.set(style="whitegrid")

# Load the dataset
file_path = r"D:\python\flaskproject\data_preprocessing\amazon.csv"  # Update the file path if necessary
data = pd.read_csv(file_path)

# Show first 5 rows to check initial data
print("First 5 rows of the dataset:")
print(data.head())

# Check for missing data
print("\nMissing Data:")
print(data.isnull().sum())

# Step 1: Fill missing values for 'rating' and 'rating_count'
# Replace NaN with 0 for 'rating' column
data["rating"] = data["rating"].fillna(0)

# Replace NaN with 0 for 'rating_count' column
data["rating_count"] = data["rating_count"].fillna(0)

# Step 2: Clean 'rating' column (ensure it is numeric)
# Convert to numeric, invalid entries become NaN, then fill NaN with 0
data["rating"] = pd.to_numeric(data["rating"], errors="coerce")
data["rating"] = data["rating"].fillna(0)

# Step 3: Clean 'rating_count' column (convert to integer after removing non-numeric values)
# Remove commas from rating_count and convert to integer
data["rating_count"] = data["rating_count"].astype(str)
data["rating_count"] = data["rating_count"].apply(lambda x: x.replace(",", ""))
data["rating_count"] = pd.to_numeric(data["rating_count"], errors="coerce")
data["rating_count"] = data["rating_count"].fillna(0)
data["rating_count"] = data["rating_count"].astype(int)

# Step 4: Clean 'discounted_price' and 'actual_price' columns
# Remove '₹' and ',' from the prices and convert them to float
data["discounted_price"] = data["discounted_price"].astype(str)
data["discounted_price"] = data["discounted_price"].apply(
    lambda x: x.replace("₹", "").replace(",", "")
)
data["discounted_price"] = pd.to_numeric(data["discounted_price"], errors="coerce")

data["actual_price"] = data["actual_price"].astype(str)
data["actual_price"] = data["actual_price"].apply(
    lambda x: x.replace("₹", "").replace(",", "")
)
data["actual_price"] = pd.to_numeric(data["actual_price"], errors="coerce")

# Step 5: Clean 'discount_percentage' column
# Remove '%' and ',' from the discount percentage and convert to float
data["discount_percentage"] = data["discount_percentage"].astype(str)
data["discount_percentage"] = data["discount_percentage"].apply(
    lambda x: x.replace("%", "").replace(",", "")
)
data["discount_percentage"] = pd.to_numeric(
    data["discount_percentage"], errors="coerce"
)

# Display cleaned data sample
print("\nCleaned Data (First 5 rows):")
print(data.head())

# Step 6: Exploratory Data Analysis (EDA)

# Distribution of Discount Percentage
plt.figure(figsize=(10, 6))
sns.histplot(data["discount_percentage"], kde=True, color="blue")
plt.title("Distribution of Discount Percentage")
plt.xlabel("Discount Percentage")
plt.ylabel("Frequency")
plt.show()

# Distribution of Rating
plt.figure(figsize=(10, 6))
sns.histplot(data["rating"], kde=True, color="green")
plt.title("Distribution of Rating")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# Relationship between Discounted Price and Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data["discounted_price"], y=data["rating"], color="purple")
plt.title("Discounted Price vs Rating")
plt.xlabel("Discounted Price")
plt.ylabel("Rating")
plt.show()

# Step 7: Save the cleaned data to a new CSV file
cleaned_file_path = r"D:\python\flaskproject\data_preprocessing\cleaned_amazon.csv"
data.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned data has been saved to {cleaned_file_path}")
