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


## 🚀 Actionable Recommendations

- Keep the first gate at Level 30. The experiment showed that moving the gate to Level 40 did not improve overall retention and resulted in a lower Day 7 Retention.
- Prioritize improving the early-game experience. Since over 55% of players are in the 1–29 rounds segment and this group experienced lower retention under Gate 40, optimizing onboarding, early progression, and player motivation is likely to have a greater impact than delaying the first gate.
- Preserve progression pacing. Although players in the 30–39 rounds segment benefited from the delayed gate, the improvement was offset by lower retention among players in later stages, suggesting that the original gate placement provides a better gameplay pacing.
