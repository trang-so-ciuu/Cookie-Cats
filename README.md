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
- Moving the first gate from Level 30 to Level 40 did not improve overall player retention, particularly for long-term retention (Day 7).

2. The Impact Varied Across Player Segments
- Players in the 30–39 rounds segment showed slightly higher retention under Gate 40, while the 40–89 and 90+ rounds segments experienced lower retention.
- The delayed gate benefited only a small portion of players, but this improvement was outweighed by lower retention among players who progressed further.

3. The Largest Player Segment Was Negatively Affected
- More than 55% of players were in the 1–29 rounds segment, which also showed lower retention under Gate 40.
- Because this is the largest player group, its lower retention contributed significantly to the overall decline in retention.

## 🚀 Actionable Recommendations

- Keep the first gate at Level 30, as moving it to Level 40 did not improve overall retention.
- Investigate why players in the 1–29 rounds segment experienced lower retention, since this group represents the majority of the player base.
- Further analyze player behavior after the first gate, as the retention improvements in the 30–39 rounds segment were not sustained in later stages.
- Validate future game design changes through A/B testing and statistical significance before deploying them to all players.
