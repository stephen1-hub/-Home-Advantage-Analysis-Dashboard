import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Home Advantage Analysis",
    layout="wide"
)

st.title("🏠 Home Advantage Analysis Dashboard")

st.markdown("""
This dashboard analyzes:

• Home win rates  
• Home vs away scoring  
• Bookmaker home probability  
• Team-level home overperformance  

Across:
Premier League and Bundesliga.
""")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_data():

    epl = pd.read_excel("E0.xlsx", engine="openpyxl")
    epl["League"] = "Premier League"

    bundesliga = pd.read_excel("D1.xlsx", engine="openpyxl")
    bundesliga["League"] = "Bundesliga"

    return pd.concat([epl, bundesliga], ignore_index=True)

df = load_data()

# -------------------------------------------------
# CLEANING
# -------------------------------------------------
df = df.dropna(subset=["B365H", "B365D", "B365A", "FTR"])

# -------------------------------------------------
# IMPLIE​D PROBABILITIES
# -------------------------------------------------
df["home_prob"] = 1 / df["B365H"]
df["draw_prob"] = 1 / df["B365D"]
df["away_prob"] = 1 / df["B365A"]

total = df["home_prob"] + df["draw_prob"] + df["away_prob"]

df["home_prob"] /= total
df["draw_prob"] /= total
df["away_prob"] /= total

# -------------------------------------------------
# ACTUAL RESULTS
# -------------------------------------------------
df["actual_home"] = (df["FTR"] == "H").astype(int)

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------
st.sidebar.header("Filters")

league_filter = st.sidebar.multiselect(
    "Select League",
    df["League"].unique(),
    default=df["League"].unique()
)

filtered = df[df["League"].isin(league_filter)]

# -------------------------------------------------
# SECTION 1 — HOME WIN RATE
# -------------------------------------------------
st.header("📊 Home Win Rate by League")

home_win_rate = filtered.groupby("League")["actual_home"].mean().reset_index()

fig1 = px.bar(
    home_win_rate,
    x="League",
    y="actual_home",
    text="actual_home",
    title="Actual Home Win Rate"
)

fig1.update_traces(texttemplate='%{text:.3f}', textposition='outside')

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------------------------
# SECTION 2 — HOME vs AWAY GOALS
# -------------------------------------------------
st.header("⚽ Home vs Away Goals")

goal_stats = filtered.groupby("League").agg(
    avg_home_goals=("FTHG", "mean"),
    avg_away_goals=("FTAG", "mean")
).reset_index()

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=goal_stats["League"],
    y=goal_stats["avg_home_goals"],
    name="Home Goals"
))

fig2.add_trace(go.Bar(
    x=goal_stats["League"],
    y=goal_stats["avg_away_goals"],
    name="Away Goals"
))

fig2.update_layout(
    barmode="group",
    title="Average Goals: Home vs Away"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------
# SECTION 3 — BOOKMAKER HOME EXPECTATION
# -------------------------------------------------
st.header("📈 Bookmaker Home Probability")

home_prob = filtered.groupby("League")["home_prob"].mean().reset_index()

fig3 = px.bar(
    home_prob,
    x="League",
    y="home_prob",
    text="home_prob",
    title="Average Bookmaker Home Probability"
)

fig3.update_traces(texttemplate='%{text:.3f}', textposition='outside')

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------
# SECTION 4 — TEAM HOME OVERPERFORMANCE
# -------------------------------------------------
st.header("🏆 Team Home Overperformance")

filtered["home_overperf"] = (
    filtered["actual_home"] - filtered["home_prob"]
)

team_home = filtered.groupby("HomeTeam")["home_overperf"].mean()
team_home = team_home.sort_values(ascending=False).reset_index()
team_home.columns = ["Team", "Home Advantage Score"]

fig4 = px.bar(
    team_home.head(15),
    x="Home Advantage Score",
    y="Team",
    orientation="h",
    title="Top 15 Home Overperforming Teams"
)

st.plotly_chart(fig4, use_container_width=True)

# -------------------------------------------------
# INSIGHT SECTION
# -------------------------------------------------
st.header("🧠 Key Insights")

st.info("""
This analysis shows:

• Home advantage exists consistently across leagues.
• Bookmakers slightly overestimate home win probability.
• Significant variation exists at team level.
• Some clubs outperform expectations dramatically at home.
""")

st.markdown("---")
st.markdown("Built with Streamlit + Plotly + Football Betting Data")