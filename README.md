# Customer Segmentation using RFM Analysis and K-Means Clustering

## Project Overview

This project performs customer segmentation using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering.

The goal is to identify groups of customers with similar purchasing behavior and provide meaningful customer segments for business analysis.

## Dataset

The project uses the Online Retail dataset from the UCI Machine Learning Repository.

The dataset contains transactional information including:

* Invoice Number
* Stock Code
* Product Description
* Quantity
* Invoice Date
* Unit Price
* Customer ID
* Country

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Excel

## Project Structure

```text
Customer-Segmentation/
│
├── screenshots/
│   ├── Screenshot 2026-10-11 172857.png
│   ├── Screenshot 2026-10-11 172932.png
│   ├── Screenshot 2026-10-11 172958.png
│   ├── Screenshot 2026-10-11 173023.png
│   └── Screenshot 2026-10-11 173042.png
│
├── app.py
├── clustering.py
├── data_analysis.py
├── rfm_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Methodology

### 1. Data Cleaning

The dataset was cleaned by:

* Removing records with missing Customer IDs
* Removing transactions with non-positive quantities
* Removing transactions with non-positive unit prices
* Calculating total transaction amount

### 2. RFM Analysis

Three customer-level metrics were calculated:

* **Recency:** Number of days since the customer's most recent purchase
* **Frequency:** Number of unique invoices associated with the customer
* **Monetary:** Total amount spent by the customer

### 3. RFM Scoring

Customers were assigned scores from 1 to 5 for Recency, Frequency, and Monetary value.

Higher Recency scores represent more recent purchases, while higher Frequency and Monetary scores represent more frequent purchases and greater spending.

### 4. K-Means Clustering

K-Means clustering was applied to the transformed and standardized RFM data.

The elbow method was used to examine different values of K, and 5 clusters were selected for the segmentation analysis.

### 5. Customer Segments

The resulting clusters were interpreted using their RFM characteristics:

* High-Value Customers
* Loyal Customers
* Regular Customers
* New/Low-Value Customers
* At-Risk Customers

## Results

The analysis identified 4,338 customers across five segments:

| Segment                 | Customers |
| ----------------------- | --------: |
| High-Value Customers    |       343 |
| Loyal Customers         |       944 |
| Regular Customers       |     1,015 |
| New/Low-Value Customers |       851 |
| At-Risk Customers       |     1,185 |
| **Total**               | **4,338** |

## Dashboard

The project includes an interactive Streamlit dashboard displaying:

* Total customer count
* Customer segment counts
* Customer segment distribution
* Recency vs Monetary analysis
* Customer segment filtering
* Customer-level RFM data
* Segment summary statistics

## How to Run

### 1. Clone the repository

```powershell
git clone https://github.com/Nohwar786/Customer-Segmentation.git
cd Customer-Segmentation
```

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the dashboard

```powershell
streamlit run app.py
```

The dashboard will open in your browser.

## Application Screenshots

![Screenshot 1](screenshots/Screenshot%202026-10-11%20172857.png)

![Screenshot 2](screenshots/Screenshot%202026-10-11%20172932.png)

![Screenshot 3](screenshots/Screenshot%202026-10-11%20172958.png)

![Screenshot 4](screenshots/Screenshot%202026-10-11%20173023.png)

![Screenshot 5](screenshots/Screenshot%202026-10-11%20173042.png)
