import pandas as pd


# ==========================================
# Load Dataset
# ==========================================

file_path = "dataset/Online Retail.xlsx"

df = pd.read_excel(file_path)


print("\n========================================")
print("       BEFORE DATA CLEANING")
print("========================================")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")


# ==========================================
# Remove missing Customer IDs
# ==========================================

df = df.dropna(subset=["CustomerID"])


# ==========================================
# Remove invalid transactions
# ==========================================

# Keep only positive quantities
df = df[df["Quantity"] > 0]

# Keep only positive prices
df = df[df["UnitPrice"] > 0]


# ==========================================
# Create Total Amount
# ==========================================

df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]


# ==========================================
# Display cleaned data
# ==========================================

print("\n========================================")
print("       AFTER DATA CLEANING")
print("========================================")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")


print("\nMissing Values:")
print(df.isnull().sum())


print("\nFirst 5 Cleaned Rows:")
print(df.head())


print("\nCleaned Dataset Information:")
print(df.info())


print("\nTotal Sales:")
print(f"£{df['TotalAmount'].sum():,.2f}")


print("\nUnique Customers:")
print(df["CustomerID"].nunique())


print("\n========================================")
print("       DATA CLEANING COMPLETED")
print("========================================")