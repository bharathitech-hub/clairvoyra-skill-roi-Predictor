import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- UI Setup ---
st.set_page_config(page_title="Clairvoyra: Skill ROI Predictor", layout="centered")
st.title("🔮 Clairvoyra")
st.markdown("Make smarter skill investments by predicting ROI and career growth potential.")

# --- Tip of the Day ---
quotes = [
    "🎯 Learn smart. Earn smarter.",
    "📈 Your skills are your career currency.",
    "💡 Every great career starts with one great skill.",
    "🚀 Invest time in skills that pay off.",
    "🧠 Data beats opinion — choose skills with ROI."
]
st.markdown(f"**💬 Tip of the Day:** _{random.choice(quotes)}_")

# --- Skill Input ---
skill = st.selectbox("🎓 Choose a tech skill to evaluate", [
    "Python", "SQL", "JavaScript", "Java", "Power BI", "React",
    "AWS", "Prompt Engineering", "Cybersecurity"
])

# --- Output Simulated Features ---
skill_info = {
    "Python": {"learn_time": 3, "salary_range": "10-15", "bundle": ["Pandas", "SQL", "Streamlit"], "roi": 4.5},
    "SQL": {"learn_time": 2, "salary_range": "8-12", "bundle": ["Excel", "Power BI"], "roi": 4.0},
    "JavaScript": {"learn_time": 2, "salary_range": "9-14", "bundle": ["React", "Node.js"], "roi": 4.7},
    "Java": {"learn_time": 3, "salary_range": "10-16", "bundle": ["Spring", "Maven"], "roi": 4.3},
    "Power BI": {"learn_time": 1.5, "salary_range": "7-10", "bundle": ["Excel", "DAX"], "roi": 4.2},
    "React": {"learn_time": 2.5, "salary_range": "10-15", "bundle": ["JS", "Node.js"], "roi": 4.8},
    "AWS": {"learn_time": 3, "salary_range": "12-18", "bundle": ["EC2", "Lambda"], "roi": 5.0},
    "Prompt Engineering": {"learn_time": 2, "salary_range": "14-20", "bundle": ["LLMs", "LangChain"], "roi": 5.5},
    "Cybersecurity": {"learn_time": 3.5, "salary_range": "12-17", "bundle": ["Networking", "Ethical Hacking"], "roi": 4.6}
}

info = skill_info[skill]

st.metric("💰 Salary Potential", f"{info['salary_range']} LPA")
st.metric("⏱️ Learning Time", f"{info['learn_time']} months")
st.metric("📈 ROI Score", info['roi'])
st.markdown("### 📦 Suggested Skill Bundle:")
st.write(", ".join([f"`{s}`" for s in info['bundle']]))

# --- Visualization ---
st.markdown("---")
st.subheader("📊 Skill ROI Comparison")
df = pd.DataFrame([
    {"Skill": k, "ROI": v["roi"]} for k, v in skill_info.items()
])
fig = px.bar(df.sort_values(by="ROI", ascending=False), x="Skill", y="ROI", color="ROI",
             title="Skill vs ROI Score", height=400)
st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.caption("🔮 Clairvoyra — Helping you choose high-value skills before you commit.")
