import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- App Setup ---
st.set_page_config(page_title="Clairvoyra – Career ROI Engine", layout="centered")
st.title("🔮 Clairvoyra")
st.caption("Smarter Skill Decisions. Higher Career Returns.")

# --- Tip of the Day ---
quotes = [
    "🎯 Learn smart. Earn smarter.",
    "📈 Your skills are your career currency.",
    "💡 Every great career starts with one great skill.",
    "🚀 Invest time in skills that pay off.",
    "🧠 Data beats opinion — choose skills with ROI."
]
st.markdown(f"**💬 Tip of the Day:** _{random.choice(quotes)}_")

# --- Inputs ---
career_stage = st.selectbox("👤 Select your current career stage:", ["Fresher", "Junior", "Mid-level", "Career Switcher"])
location = st.selectbox("🌍 Preferred job location:", ["India", "USA", "Europe", "Remote"])
skill = st.selectbox("🛠️ Choose a tech skill to evaluate:", [
    "Python", "SQL", "JavaScript", "Java", "Power BI", "React",
    "AWS", "Prompt Engineering", "Cybersecurity"
])

# --- Skill Data ---
skill_info = {
    "Python": {"learn_time": 3, "base_salary": 12, "bundle": ["Pandas", "SQL", "Streamlit"], "roles": ["Data Analyst", "ML Engineer"]},
    "SQL": {"learn_time": 2, "base_salary": 10, "bundle": ["Excel", "Power BI"], "roles": ["BI Analyst", "Data Engineer"]},
    "JavaScript": {"learn_time": 2, "base_salary": 11, "bundle": ["React", "Node.js"], "roles": ["Frontend Dev"]},
    "Java": {"learn_time": 3, "base_salary": 13, "bundle": ["Spring", "Maven"], "roles": ["Backend Dev"]},
    "Power BI": {"learn_time": 1.5, "base_salary": 9, "bundle": ["Excel", "DAX"], "roles": ["BI Developer"]},
    "React": {"learn_time": 2.5, "base_salary": 12, "bundle": ["JS", "Node.js"], "roles": ["Frontend Dev"]},
    "AWS": {"learn_time": 3, "base_salary": 15, "bundle": ["EC2", "Lambda"], "roles": ["Cloud Engineer"]},
    "Prompt Engineering": {"learn_time": 2, "base_salary": 18, "bundle": ["LLMs", "LangChain"], "roles": ["AI Specialist"]},
    "Cybersecurity": {"learn_time": 3.5, "base_salary": 14, "bundle": ["Networking", "Ethical Hacking"], "roles": ["Security Analyst"]}
}

# --- Salary Adjustment by Region ---
location_multiplier = {"India": 1, "USA": 2.2, "Europe": 1.8, "Remote": 1.5}
multiplier = location_multiplier[location]

# --- ROI Calculation ---
info = skill_info[skill]
salary = int(info["base_salary"] * multiplier)
roi = round(salary / info["learn_time"], 2)

# --- Display Outputs ---
st.metric("💰 Salary Potential (LPA)", f"{salary} LPA")
st.metric("⏱️ Learning Time", f"{info['learn_time']} months")
st.metric("📈 ROI Score", roi)

st.markdown("---")
st.markdown("### 💼 Career Role Suggestions:")
st.write(", ".join(f"`{r}`" for r in info["roles"]))

st.markdown("### 📦 Recommended Skill Bundle:")
st.write(", ".join(f"`{b}`" for b in info["bundle"]))

# --- Visualization ---
st.markdown("---")
st.subheader("📊 Skill vs ROI")
df = pd.DataFrame([
    {"Skill": k, "ROI": round(v["base_salary"] / v["learn_time"], 2)} for k, v in skill_info.items()
])
fig = px.bar(df.sort_values(by="ROI", ascending=False), x="Skill", y="ROI", color="ROI", title="Skill ROI Comparison")
st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.caption("🔮 Clairvoyra – Your smart assistant for career-defining skill decisions.")
