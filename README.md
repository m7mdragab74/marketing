# Marketing Data Analysis Project 📊

This project focuses on analyzing marketing campaign data using Python and preparing it for interactive visualization in Power BI. The goal is to extract actionable insights about campaign and channel performance.

---

## 1️⃣ Dataset

- Format: `xlsx` file containing 3000 rows and 11 columns.
- Key columns:
  - `Campaign_ID`: Campaign identifier
  - `Date`: Campaign date and time
  - `Campaign_Name`: Name of the campaign
  - `Channel`: Marketing channel (e.g., Facebook, Instagram, Google Ads)
  - `Region`: Target region
  - `Device`: Device type
  - `Impressions`, `Clicks`, `Spend`, `Conversions`, `Revenue`: Performance metrics

---

## 2️⃣ Data Cleaning

- Handling Missing Values:
  - `Region` → filled with `"Unknown"`
  - `Impressions` → filled with the mean value
- Ensured correct column formats:
  - `Date` → datetime
  - Numeric columns → int/float

---

## 3️⃣ Calculated Metrics

Key metrics were calculated for each campaign and channel:

| Metric | Description |
|--------|-------------|
| CTR (Click-Through Rate) | Clicks divided by Impressions |
| Conversion Rate | Conversions divided by Clicks |
| CPA (Cost per Acquisition) | Spend divided by Conversions |
| ROAS (Return on Ad Spend) | Revenue divided by Spend |
| Profit | Revenue minus Spend |
| Profit Margin | Profit divided by Revenue |

---

## 4️⃣ Exploratory Data Analysis (EDA)

- Trend analysis of CTR per channel over time
- Revenue comparison per channel
- Device and region insights for audience targeting

---
