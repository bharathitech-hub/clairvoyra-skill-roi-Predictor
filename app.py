import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- App Setup ---
st.set_page_config(page_title="Clairvoyra – Career ROI Engine", layout="centered", page_icon="🔮")
st.markdown("""
    <style>
        .stApp {
            background-color: #f7f9fc;
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

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
location = st.selectbox("🌍 Preferred job location:", ["India", "USA", "Europe", "Canada", "UK", "Germany", "Australia", "Remote"])
skill = st.selectbox("🛠️ Choose a tech skill to evaluate:", [
    "Python", "SQL", "JavaScript", "Java", "Power BI", "React",
    "AWS", "Prompt Engineering", "Cybersecurity", "C++", "Django",
    "Flutter", "Tableau", "Node.js", "Angular", "DevOps", "Docker",
    "Kubernetes", "Git", "Linux", "HTML & CSS", "Figma"
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
    "Cybersecurity": {"learn_time": 3.5, "base_salary": 14, "bundle": ["Networking", "Ethical Hacking"], "roles": ["Security Analyst"]},
    "C++": {"learn_time": 3, "base_salary": 11, "bundle": ["DSA", "STL"], "roles": ["System Engineer"]},
    "Django": {"learn_time": 2.5, "base_salary": 12, "bundle": ["Python", "HTML", "SQLite"], "roles": ["Backend Developer"]},
    "Flutter": {"learn_time": 2, "base_salary": 11, "bundle": ["Dart", "Firebase"], "roles": ["Mobile App Developer"]},
    "Tableau": {"learn_time": 2, "base_salary": 10, "bundle": ["SQL", "Excel"], "roles": ["Data Viz Analyst"]},
    "Node.js": {"learn_time": 2, "base_salary": 12, "bundle": ["Express", "MongoDB"], "roles": ["Full Stack Dev"]},
    "Angular": {"learn_time": 2.5, "base_salary": 11, "bundle": ["TypeScript", "RxJS"], "roles": ["Frontend Dev"]},
    "DevOps": {"learn_time": 3, "base_salary": 16, "bundle": ["CI/CD", "Jenkins"], "roles": ["DevOps Engineer"]},
    "Docker": {"learn_time": 2, "base_salary": 13, "bundle": ["Kubernetes", "Linux"], "roles": ["Infra Engineer"]},
    "Kubernetes": {"learn_time": 2.5, "base_salary": 14, "bundle": ["Docker", "Helm"], "roles": ["Cloud Infra Engineer"]},
    "Git": {"learn_time": 1, "base_salary": 9, "bundle": ["GitHub", "CI/CD"], "roles": ["Version Control Specialist"]},
    "Linux": {"learn_time": 2, "base_salary": 10, "bundle": ["Bash", "Networking"], "roles": ["SysAdmin"]},
    "HTML & CSS": {"learn_time": 1.5, "base_salary": 8, "bundle": ["JS", "Responsive Design"], "roles": ["UI Designer"]},
    "Figma": {"learn_time": 1.5, "base_salary": 9, "bundle": ["UI/UX", "Prototyping"], "roles": ["Product Designer"]}
}

location_multiplier = {
    "India": 1, "USA": 2.2, "Europe": 1.8, "Canada": 1.9,
    "UK": 2.0, "Germany": 1.85, "Australia": 2.1, "Remote": 1.6
}
stage_adjustment = {"Fresher": 0.8, "Junior": 1.0, "Mid-level": 1.2, "Career Switcher": 0.9}
multiplier = location_multiplier[location] * stage_adjustment[career_stage]

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

st.markdown("---")
st.markdown("### 🗺️ Suggested Learning Timeline:")
week_per_month = 4
weeks = int(info["learn_time"] * week_per_month)
st.success(f"Start learning **{skill}** this week and become job-ready in just **{weeks} weeks**!")

# --- Chart ---
st.markdown("---")
st.subheader("📊 Skill vs ROI")
df = pd.DataFrame([
    {"Skill": k, "ROI": round(v["base_salary"] / v["learn_time"], 2)} for k, v in skill_info.items()
])
fig = px.bar(df.sort_values(by="ROI", ascending=False), x="Skill", y="ROI", color="ROI", title="Skill ROI Comparison")
st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.caption("🔮 Clairvoyra – Your smart assistant for career-defining skill decisions.")
Let me know if you'd like this saved as a .py file or bundled into a .zip with your requirements.txt.







