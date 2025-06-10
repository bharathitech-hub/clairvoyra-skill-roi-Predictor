import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import random

# --- App Config ---
st.set_page_config(page_title="Clairvoyra – Skill ROI Predictor", layout="centered")
st.title("🔮 Clairvoyra")
st.subheader("✨ See your future. Learn smarter. Earn stronger.")

# --- Load Model ---
model = joblib.load("model.pkl")

# --- Skill Info ---
skills = {
    "Python": {"time": 3, "bundle": ["Pandas", "SQL", "Streamlit"], "avg_salary": 10},
    "SQL": {"time": 2, "bundle": ["Excel", "Power BI"], "avg_salary": 8},
    "JavaScript": {"time": 2, "bundle": ["React", "Node.js"], "avg_salary": 9},
    "Java": {"time": 3, "bundle": ["Spring", "Maven"], "avg_salary": 11},
    "Power BI": {"time": 1.5, "bundle": ["Excel", "DAX"], "avg_salary": 7},
    "React": {"time": 2.5, "bundle": ["JS", "Node.js"], "avg_salary": 10},
    "AWS": {"time": 3, "bundle": ["EC2", "Lambda"], "avg_salary": 13},
    "Prompt Engineering": {"time": 2, "bundle": ["LLMs", "LangChain"], "avg_salary": 14},
    "Cybersecurity": {"time": 3.5, "bundle": ["Networking", "Ethical Hacking"], "avg_salary": 12}
}

quotes = [
    "🎯 Learn smart. Earn smarter.",
    "📈 Your skills are your career currency.",
    "💡 Every great career starts with one great skill.",
    "🚀 Invest time in skills that pay off.",
    "🧠 Data beats opinion — choose skills with ROI."
]

# --- UI: Skill Selection ---
st.markdown(f"**💬 Tip of the Day:** _{random.choice(quotes)}_")
selected = st.selectbox("🛠️ Choose a skill to evaluate:", list(skills.keys()))

# --- Predict Salary Range ---
df = pd.DataFrame([[selected]], columns=["skill"])
df_encoded = pd.get_dummies(df)
salary_range = model.predict(df_encoded)[0]

# --- ROI Calculation ---
learn_time = skills[selected]["time"]
roi = round(int(salary_range.split("-")[-1]) / learn_time, 2)

# --- Output Results ---
st.success(f"💰 Predicted Salary Range: {salary_range} LPA")
st.info(f"⏱️ Time to Learn {selected}: {learn_time} months")
st.metric("📈 ROI Score", roi)
st.markdown("### 💼 Suggested Skill Bundle:")
st.write(", ".join(f"`{s}`" for s in skills[selected]["bundle"]))

# --- Visualize Salaries ---
st.markdown("---")
st.subheader("📊 Average Salary by Skill")
chart_df = pd.DataFrame([
    {"Skill": k, "Average Salary (LPA)": v["avg_salary"]}
    for k, v in skills.items()
])
fig = px.bar(chart_df.sort_values(by="Average Salary (LPA)", ascending=False),
             x="Skill", y="Average Salary (LPA)", color="Average Salary (LPA)",
             title="Skill vs Average Salary")
st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.caption("🔮 Clairvoyra — Smart learning decisions powered by data.")
❌ The environment doesn't support compiling that ver
