# Telecom Market Entry Analysis

This project presents a data-driven market entry strategy for launching eSIM services across three emerging markets: **Thailand**, **Mexico**, and **South Africa**. It combines infrastructure and affordability metrics with sentiment analysis to produce a ranked market recommendation, supported by a Power BI dashboard and a report.

## 🧠 Objective
Identify the most promising country for an eSIM market launch based on:
- Network infrastructure quality
- Mobile data affordability
- Customer sentiment toward telecom operators

## 🛠 Tools & Technologies
- **Power BI**: Dashboard development, KPI design, data visualization
- **Python**: Sentiment analysis using VADER
- **Power Query & DAX**: Data cleaning, transformation, and calculated columns
- **Web Scraping**: Manual Python script-based scraping and extraction of reviews from Trustpilot, HelloPeter, and Reddit

## 📊 Dashboard Features
The interactive Power BI dashboard presents:
- Market comparison by download/upload speed, latency, and tower density
- Affordability scores (% of monthly income spent on 1GB of mobile data)
- Sentiment breakdowns by country, including key complaint categories
- Composite market attractiveness scoring for decision support

![Image](https://github.com/user-attachments/assets/51a3d18a-57f3-40ed-a415-3c9e9608af23)

👉 **See the dashboard** in the ```Telecom-Market-Sentiment.pbix``` file.

## 💬 Sentiment Analysis
Over **280 user reviews** were scraped and analyzed using VADER (Valence Aware Dictionary for Sentiment Reasoning).  
Key insights include:
- **Mexico** had the lowest satisfaction (81.4% negative reviews)
- **Thailand** showed strong infrastructure but poor sentiment
- **South Africa** had the most balanced sentiment but lower affordability

## 🧾 Summary of Findings
- **Recommended Launch Market**: **Thailand**  
  Best balance of affordability and infrastructure, despite sentiment challenges.
- **Second Phase**: **Mexico**  
  Adequate technical foundation, but requires service differentiation due to poor sentiment.
- **Monitor**: **South Africa**  
  Strong download speeds, but affordability barriers limit mass adoption.

## 📄Report
The report outlines the methods used along with justifications ([Telecom Market Entry Analysis Report.pdf](https://github.com/user-attachments/files/20980443/Telecom.Market.Entry.Analysis.Report.pdf)). 
