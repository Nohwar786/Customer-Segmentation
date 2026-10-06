import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


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

df["TotalAmount"] = (
    df["Quantity"] * df["UnitPrice"]
)


# ==========================================
# Set Analysis Date
# ==========================================

analysis_date = (
    df["InvoiceDate"].max()
    + pd.Timedelta(days=1)
)


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
# Rename RFM Columns
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
# Log Transformation
# ==========================================

rfm_log = np.log1p(rfm)


# ==========================================
# Standardize Data
# ==========================================

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(
    rfm_log
)


# ==========================================
# K-Means Clustering
# ==========================================

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(
    rfm_scaled
)
# ==========================================
# Assign Customer Segment Names
# ==========================================

segment_names = {
    3: "High-Value Customers",
    1: "Loyal Customers",
    4: "Regular Customers",
    0: "New/Low-Value Customers",
    2: "At-Risk Customers"
}

rfm["Segment"] = rfm["Cluster"].map(
    segment_names
)

print("\nCustomer Segment Distribution:")

print(
    rfm["Segment"].value_counts()
)

# ==========================================
# Cluster Summary
# ==========================================

cluster_summary = rfm.groupby("Cluster").agg({

    "Recency": "mean",

    "Frequency": "mean",

    "Monetary": "mean",

    "Cluster": "count"

})


# ==========================================
# Rename Customer Count
# ==========================================

cluster_summary.rename(
    columns={
        "Cluster": "CustomerCount"
    },
    inplace=True
)


# ==========================================
# Sort by Monetary Value
# ==========================================

cluster_summary = cluster_summary.sort_values(
    "Monetary",
    ascending=False
)


# ==========================================
# Display Results
# ==========================================

print("\n========================================")
print("       CUSTOMER CLUSTERING")
print("========================================")

print("\nCluster Summary:")

print(
    cluster_summary.round(2)
)


print("\nCustomer Count by Cluster:")

print(
    rfm["Cluster"].value_counts().sort_index()
)


print("\nFirst 10 Customer Records:")

print(
    rfm.head(10)
)


# ==========================================
# Save Results
# ==========================================

rfm.to_csv(
    "customer_segments.csv"
)


print("\n========================================")
print("       CLUSTERING COMPLETED")
print("========================================")

print("\nCreated file:")
print("customer_segments.csv")
# ==========================================
# Customer Segment Visualization
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns


# Segment Distribution
plt.figure(figsize=(10, 6))

sns.countplot(
    data=rfm,
    x="Segment",
    order=rfm["Segment"].value_counts().index
)

plt.title("Customer Segment Distribution")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30)
plt.tight_layout()

plt.show()


# Recency vs Monetary
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=rfm,
    x="Recency",
    y="Monetary",
    hue="Segment",
    alpha=0.6
)

plt.title("Recency vs Monetary Value")
plt.xlabel("Recency (Days)")
plt.ylabel("Monetary Value")
plt.tight_layout()

plt.show()


# Frequency vs Monetary
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=rfm,
    x="Frequency",
    y="Monetary",
    hue="Segment",
    alpha=0.6
)

plt.title("Frequency vs Monetary Value")
plt.xlabel("Purchase Frequency")
plt.ylabel("Monetary Value")
plt.tight_layout()

plt.show()