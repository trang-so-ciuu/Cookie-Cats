# 🎮 Player Retention & Engagement Analysis
## 🛠️ Tools Used
- Python 
- SQL Server
- Power BI
- DAX
## 📌 Project Overview

This project analyzes an A/B testing experiment conducted in the mobile game Cookie Cats. The goal is to evaluate whether moving the first progression gate from Level 30 to Level 40 improves player engagement and retention.

The analysis combines Python, SQL Server, and Power BI to perform data cleaning, exploratory analysis, statistical testing, and interactive dashboard visualization.

## ❓ Business Problem

- The Product Team wants to answer the following question: Does moving the first gate from Level 30 to Level 40 improve player engagement and retention?

- Changing game progression can influence player behavior. While delaying the first gate may allow players to enjoy uninterrupted gameplay for longer, it may also reduce the psychological motivation to return.

- This experiment aims to determine whether the new gate placement produces measurable improvements before releasing the update to all players.

## 📁 Dataset

- userid :	Unique player ID
- version : 	gate_30 / gate_40
- sum_gamerounds :	Total game rounds played
- retention_1 : 	Returned after 1 day
- retention_7	: Returned after 7 days

## 🧹 Data Cleaning

The following preprocessing steps were performed:
- Checked missing values.
- Checked duplicate players.
- Converted Boolean values (True/False) into Binary (1/0).
- Investigated missing values in sum_gamerounds.
- Excluded missing game rounds only for engagement analysis to avoid creating synthetic player behavior.

## 📊 Dashboard Architecture & Key Visuals

![Dashboard 1](gamingdashboard.png)

**Key Insights**
1. Overall Retention Declined
- Day 1 Retention decreased from 45.84% to 45.24% (-0.59%).
- Day 7 Retention decreased from 25.06% to 24.47% (-0.60%).
- Moving the first gate from Level 30 to Level 40 did not improve player retention. The decline in Day 7 Retention suggests a negative impact on long-term player retention.
  
2. The Impact Differs by Player Progress: 
- Players in the 30–39 rounds group showed slightly higher retention after the gate was moved, while players in the 40–89 and 90+ rounds groups experienced lower retention.
- Delaying the gate only benefited a small segment of players but reduced long-term retention for more engaged players.

3. Early Game Is the Biggest Retention Challenge
- Over 55% of players stopped within the first 1–29 rounds, and only 24.8% returned by Day 7.
- The largest retention loss occurs during the early-game experience, indicating that onboarding and early progression have a greater impact than gate placement.

4. Engagement Requires Further Validation
- The current dashboard does not compare Game Rounds Distribution between versions.
- Additional engagement analysis (e.g., Box Plot) is needed before concluding whether Gate 40 improves player engagement.
---
### 👥 Dashboard 2 – Customer Conversion Insights

![Dashboard 2](dashboard2.png)

**Key Insights**
- Website engagement is the most important factor influencing conversion; customers who view 5–6 pages and spend 6–10 minutes on the website achieve Conversion Rates above 91%.
- Converted customers demonstrate significantly higher Website Visits, Email Engagement, and Previous Purchases than non-converted customers, indicating that customer engagement is a strong predictor of purchase behavior.
- Customers aged 35–44 with medium income represent the highest-converting customer segment, making them the priority target for future marketing campaigns.
- Returning customers with 3–5 previous purchases achieve higher conversion rates than first-time customers, highlighting the importance of effective Customer Retention strategies.

---
### 💰 Dashboard 3 – Budget Optimization & Recommendations

![Dashboard 3](dashboard3.png)

**Key Insights**
- Referral, PPC, and SEO provide the best investment performance by combining high Conversion Rates with low Cost per Conversion, making them the highest-priority channels for budget expansion.
- The PPC – Conversion campaign combination delivers the highest cost efficiency, generating a large number of converted customers while maintaining a Customer Acquisition Cost (CAC) below the overall average.
- Email and Social Media either produce lower conversion performance or incur higher acquisition costs than the other channels, indicating that these channels should be optimized or receive reduced investment.
- The Marketing Action Matrix suggests that reallocating budget from lower-performing channels to Referral, PPC, and SEO would improve budget efficiency and maximize overall marketing performance.



## 🎯 Actionable Recommendations

Based on the analysis across the three dashboards, the following strategic recommendations are proposed to improve marketing performance and maximize budget efficiency.

### 💰 1. Optimize Marketing Budget Allocation

- Reallocate **10–15%** of the marketing budget from underperforming channels (**Social Media** and **Email**) to higher-performing channels.
- Increase investment in **Referral** and **PPC**, particularly for **Conversion** campaigns, which consistently achieved the highest conversion rates and lower customer acquisition costs (CAC).
- Continuously monitor Cost per Conversion (CAC) to ensure budget is allocated to the most efficient campaign-channel combinations.

---

### 🌐 2. Improve Website Engagement & Conversion Rate Optimization (CRO)

- Enhance website UI/UX to encourage visitors to:
  - Stay on the website for **more than 6 minutes**.
  - View **at least 5 pages per session**.
- Optimize landing pages, navigation, and call-to-action (CTA) placement to increase customer engagement and improve conversion rates.

---

### 👥 3. Strengthen Customer Targeting & Retention

- Prioritize marketing campaigns targeting customers aged **35–44 years** with **medium income**, the highest-converting customer segment identified in the analysis.
- Expand customer loyalty and retention programs for customers with **3–5 previous purchases**, as they demonstrate significantly higher conversion probabilities than first-time customers.
- Increase personalized email campaigns and remarketing efforts to maintain long-term customer relationships and encourage repeat purchases.

---

### 📈 Expected Business Impact

Implementing these recommendations is expected to:

- Improve overall marketing ROI.
- Reduce customer acquisition costs (CAC).
- Increase conversion rates through better customer targeting.
- Enhance long-term customer retention and lifetime value.
- Support data-driven marketing budget allocation decisions.
