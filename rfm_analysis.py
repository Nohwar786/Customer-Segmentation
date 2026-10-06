import pandas as pd


# ==========================================
# Load Dataset
# ==========================================

file_path = "dataset/Online Retail.xlsx"

df = pd.read_excel(file_path)


# ==========================================
# Data Cleaning
# ==========================================

df = df.dropna(subset=["CustomerID"])

df = df[df["Quantity"] > 0]

df = df[df["UnitPrice"] > 0]


# ==========================================
# Calculate Total Amount
# ==========================================

df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]


# ==========================================
# Set Analysis Date
# ==========================================

analysis_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)


# ==========================================
# RFM Analysis
# ==========================================

rfm = df.groupby("CustomerID").agg({

    "InvoiceDate": lambda x: (
        analysis_date - x.max()
    ).days,

    "InvoiceNo": "nunique",

    "TotalAmount": "sum"

})


# ==========================================
# Rename Columns
# ==========================================

rfm.rename(
    columns={
        "InvoiceDate": "Recency",
        "InvoiceNo": "Frequency",
        "TotalAmount": "Monetary"
    },
    inplace=True
)


# ==========================================
# Create RFM Scores
# ==========================================

# Recency:
# Lower recency = better score

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
)


# Frequency:
# Higher frequency = better score

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)


# Monetary:
# Higher monetary value = better score

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1, 2, 3, 4, 5]
)


# ==========================================
# Convert Scores to Integers
# ==========================================

rfm["R_Score"] = rfm["R_Score"].astype(int)
rfm["F_Score"] = rfm["F_Score"].astype(int)
rfm["M_Score"] = rfm["M_Score"].astype(int)


# ==========================================
# Create Combined RFM Score
# ==========================================

rfm["RFM_Score"] = (
    rfm["R_Score"]
    + rfm["F_Score"]
    + rfm["M_Score"]
)


# ==========================================
# Create RFM Segment Code
# ==========================================

rfm["RFM_Segment"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)


# ==========================================
# Display Results
# ==========================================

print("\n========================================")
print("          RFM SCORES")
print("========================================")

print("\nFirst 10 Customers:")
print(
    rfm[
        [
            "Recency",
            "Frequency",
            "Monetary",
            "R_Score",
            "F_Score",
            "M_Score",
            "RFM_Score",
            "RFM_Segment"
        ]
    ].head(10)
)


print("\nRFM Score Statistics:")
print(
    rfm[
        [
            "R_Score",
            "F_Score",
            "M_Score",
            "RFM_Score"
        ]
    ].describe()
)


print("\nRFM Score Distribution:")
print(
    rfm["RFM_Score"].value_counts().sort_index()
)


print("\n========================================")
print("       RFM SCORING COMPLETED")
print("========================================")