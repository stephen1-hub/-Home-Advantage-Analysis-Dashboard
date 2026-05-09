# Home Advantage Analysis Dashboard
# Overview

This project is a football analytics dashboard built with Python and Streamlit that analyzes home advantage patterns across the Premier League and Bundesliga.

Using match results and bookmaker probabilities, the dashboard evaluates:

Home win rates
Home vs away scoring differences
Bookmaker home expectations
Team-level home overperformance
Market pricing efficiency

The project combines sports analytics, probability modeling, and interactive dashboard development into a professional portfolio project.

# Live Demo

(Add your Streamlit Cloud link here once deployed)

# Objectives

The main objective of this project is to evaluate whether home advantage is:

Structurally significant across leagues
Accurately reflected in bookmaker odds
Consistent at team level
Overestimated or underestimated by the market

The dashboard answers questions such as:

How strong is home advantage in each league?
Do bookmakers overprice home teams?
Which clubs outperform expectations at home?
Are there systematic home bias inefficiencies?
# Dataset

Leagues analyzed:

English Premier League
German Bundesliga

Key features include:

Match outcomes (H/D/A)
Goals scored (home and away)
Betting odds (Bet365)
Implied probabilities
Team-level performance metrics
# Tech Stack
Python
Pandas
Streamlit
Plotly
OpenPyXL
NumPy
# Methodology
1. Convert Odds to Probabilities

Bet365 odds are converted into implied probabilities:

Home Win Probability
Draw Probability
Away Win Probability
2. Normalize Probabilities

Probabilities are normalized to remove bookmaker margin (overround), ensuring fair comparison between expected and actual outcomes.

3. Encode Match Outcomes

Match results are encoded as:

H → Home Win
D → Draw
A → Away Win
4. Home Advantage Metrics

The model evaluates:

Home win rate
Average home goals
Average away goals
Bookmaker average home probability
Team-level home overperformance
5. Calculate Home Overperformance

The model compares:

Actual Home Win − Bookmaker Home Probability

Positive values:
→ Team exceeds home expectations

Negative values:
→ Team underperforms at home relative to market pricing

# Dashboard Features
📊 League-Level Home Analysis

Compares home win rates and bookmaker home expectations across leagues.

⚽ Home vs Away Scoring Comparison

Visualizes structural scoring differences between home and away teams.

📈 Market Home Probability Comparison

Evaluates whether bookmakers overestimate home advantage.

🏆 Team-Level Home Overperformance

Ranks teams by home efficiency relative to market expectations.

🔍 Interactive Filtering

Allows league-based exploration and detailed team analysis.

# Sample Insights
Home teams score significantly more goals than away teams across both leagues.
Bundesliga shows slightly higher overall scoring than the Premier League.
Bookmakers slightly overestimate home win probability.
Certain clubs significantly outperform expectations at home.
Market inefficiencies vary substantially at team level.
# Business Recommendations

Based on the analysis, the project highlights several opportunities for improving market efficiency.

1. Refine Home Advantage Weighting

If bookmakers consistently overestimate home advantage, probability models should incorporate dynamic home-edge adjustments.

Recommendation:

Use rolling home performance metrics
Adjust home weighting by league season trends

Business Impact:

Improved pricing accuracy
Reduced structural bias
2. Integrate Team-Specific Home Strength

Not all teams have equal home advantage.

Recommendation:

Model home performance at club level
Distinguish strong home teams from weak ones

Business Impact:

More granular probability modeling
Enhanced predictive accuracy
3. Monitor Persistent Home Inefficiencies

Some teams consistently outperform home expectations.

Recommendation:

Track rolling home overperformance metrics
Flag persistent deviations

Business Impact:

Faster market recalibration
Improved forecasting systems
4. Combine Statistical and Behavioral Insights

Home advantage may also reflect:

Crowd influence
Travel fatigue
Tactical setup differences
Public betting psychology

Recommendation:

Combine statistical modeling with behavioral analysis
Segment high-profile teams separately

Business Impact:

Stronger risk management
Better market balancing
# Strategic Insight

This project demonstrates how data analytics can measure structural home advantage, evaluate bookmaker pricing accuracy, and identify team-level inefficiencies in football markets.

It bridges sports performance analysis with probability modeling and interactive dashboard development.

# Installation
Clone Repository
git clone https://github.com/yourusername/home-advantage-analysis.git
Navigate Into Project
cd home-advantage-analysis
Install Dependencies
pip install -r requirements.txt
Run Streamlit App
streamlit run app.py
# Project Structure
├── app17.py
├── data/
│   ├── E0.xlsx
│   └── D1.xlsx
├── requirements.txt
├── README.md
└── assets/
# Future Improvements
Home advantage statistical significance testing
Confidence intervals
Expected points model
Logistic regression prediction model
Time-trend home advantage analysis
Team logo integration
Live Streamlit cloud deployment
# Author

Stephen Yaw Ayamah

Aspiring Football Data Analyst | Sports Analytics | Python & Streamlit Projects
