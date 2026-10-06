import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("📊 Customer Segmentation Dashboard")

st.write(
    "RFM Analysis and K-Means Clustering "
    "for Customer Segmentation"
)


# ==========================================
# Load Data
# ==========================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "customer_segments.csv"
    )

    return df


rfm = load_data()


# ==========================================
# Key Metrics
# ==========================================

st.subheader("Customer Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    len(rfm)
)

col2.metric(
    "High-Value Customers",
    len(
        rfm[
            rfm["Segment"] == "High-Value Customers"
        ]
    )
)

col3.metric(
    "Loyal Customers",
    len(
        rfm[
            rfm["Segment"] == "Loyal Customers"
        ]
    )
)

col4.metric(
    "At-Risk Customers",
    len(
        rfm[
            rfm["Segment"] == "At-Risk Customers"
        ]
    )
)


# ==========================================
# Segment Distribution
# ==========================================

st.subheader("Customer Segment Distribution")

segment_counts = (
    rfm["Segment"]
    .value_counts()
)


fig, ax = plt.subplots(
    figsize=(10, 5)
)

sns.barplot(
    x=segment_counts.index,
    y=segment_counts.values,
    ax=ax
)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

st.pyplot(fig)


# ==========================================
# RFM Scatter Plot
# ==========================================

st.subheader("Customer Segmentation Analysis")

fig2, ax2 = plt.subplots(
    figsize=(10, 6)
)

sns.scatterplot(
    data=rfm,
    x="Recency",
    y="Monetary",
    hue="Segment",
    alpha=0.6,
    ax=ax2
)

ax2.set_title(
    "Recency vs Monetary Value"
)

ax2.set_xlabel(
    "Recency (Days)"
)

ax2.set_ylabel(
    "Monetary Value"
)

st.pyplot(fig2)


# ==========================================
# Segment Filter
# ==========================================

st.subheader("Explore Customer Segments")

segments = sorted(
    rfm["Segment"].unique()
)

selected_segment = st.selectbox(
    "Select a customer segment:",
    segments
)


filtered_data = rfm[
    rfm["Segment"] == selected_segment
]


st.write(
    f"Customers in **{selected_segment}**: "
    f"{len(filtered_data)}"
)


st.dataframe(
    filtered_data[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "Cluster",
            "Segment"
        ]
    ].reset_index(drop=True),
    width="stretch"
)
# ==========================================
# Segment Summary
# ==========================================

st.subheader("Segment Summary")

segment_summary = (
    rfm.groupby("Segment")
    .agg(
        CustomerCount=("CustomerID", "count"),
        AvgRecency=("Recency", "mean"),
        AvgFrequency=("Frequency", "mean"),
        AvgMonetary=("Monetary", "mean")
    )
    .sort_values(
        "AvgMonetary",
        ascending=False
    )
)

segment_summary = segment_summary.round(2)

st.dataframe(
    segment_summary,
    use_container_width=True
)