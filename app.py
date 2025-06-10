import streamlit as st
import pandas as pd
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

# --- Career Goal Selection ---
goal = st.selectbox("🎯 What's your career goal?", [
    "Data Analyst", "Frontend Developer", "Backend Developer", "AI Engineer",
    "Mobile App Developer", "Cloud Engineer", "Cybersecurity Specialist", "DevOps Engineer"
])

# --- Skill Suggestion by Goal ---
goal_skills = {
    "Data Analyst": ["Python", "SQL", "Power BI"],
    "Frontend Developer": ["HTML & CSS", "JavaScript", "React"],
    "Backend Developer": ["Java", "Node.js", "Django"],
    "AI Engineer": ["Python", "Prompt Engineering", "Django"],
    "Mobile App Developer": ["Flutter", "Dart", "Firebase"],
    "Cloud Engineer": ["AWS", "Docker", "Kubernetes"],
    "Cybersecurity Specialist": ["Linux", "Cybersecurity", "Networking"],
    "DevOps Engineer": ["Git", "CI/CD", "Docker"]
}
st.markdown("### 🧭 Suggested Skills for Your Goal:")
st.write(", ".join(f"`{s}`" for s in goal_skills[goal]))

# --- User Inputs ---
career_stage = st.selectbox("👤 Select your current career stage:", ["Fresher", "Junior", "Mid-level", "Career Switcher"])
location = st.selectbox("🌍 Preferred job location:", ["India", "USA", "Europe", "Canada", "UK", "Germany", "Australia", "Remote"])
skill = st.selectbox("🛠️ Choose a tech skill to evaluate:", sorted(set([s for skills in goal_skills.values() for s in skills])))

# --- Skill Info Dictionary ---
skill_info = {
    "Python": {"learn_time": 3, "base_salary": 12, "bundle": ["Pandas", "SQL", "Streamlit"], "roles": ["Data Analyst", "ML Engineer"]},
    "SQL": {"learn_time": 2, "base_salary": 10, "bundle": ["Excel", "Power BI"], "roles": ["BI Analyst", "Data Engineer"]},
    "Power BI": {"learn_time": 1.5, "base_salary": 9, "bundle": ["Excel", "DAX"], "roles": ["BI Developer"]},
    "HTML & CSS": {"learn_time": 1.5, "base_salary": 8, "bundle": ["JS", "Responsive Design"], "roles": ["UI Designer"]},
    "JavaScript": {"learn_time": 2, "base_salary": 11, "bundle": ["React", "Node.js"], "roles": ["Frontend Dev"]},
    "React": {"learn_time": 2.5, "base_salary": 12, "bundle": ["JS", "Node.js"], "roles": ["Frontend Dev"]},
    "Java": {"learn_time": 3, "base_salary": 13, "bundle": ["Spring", "Maven"], "roles": ["Backend Dev"]},
    "Node.js": {"learn_time": 2, "base_salary": 12, "bundle": ["Express", "MongoDB"], "roles": ["Full Stack Dev"]},
    "Django": {"learn_time": 2.5, "base_salary": 12, "bundle": ["Python", "HTML", "SQLite"], "roles": ["Backend Developer"]},
    "Prompt Engineering": {"learn_time": 2, "base_salary": 18, "bundle": ["LLMs", "LangChain"], "roles": ["AI Specialist"]},
    "Flutter": {"learn_time": 2, "base_salary": 11, "bundle": ["Dart", "Firebase"], "roles": ["Mobile App Developer"]},
    "AWS": {"learn_time": 3, "base_salary": 15, "bundle": ["EC2", "Lambda"], "roles": ["Cloud Engineer"]},
    "Docker": {"learn_time": 2, "base_salary": 13, "bundle": ["Kubernetes", "Linux"], "roles": ["Infra Engineer"]},
    "Kubernetes": {"learn_time": 2.5, "base_salary": 14, "bundle": ["Docker", "Helm"], "roles": ["Cloud Infra Engineer"]},
    "Linux": {"learn_time": 2, "base_salary": 10, "bundle": ["Bash", "Networking"], "roles": ["SysAdmin"]},
    "Cybersecurity": {"learn_time": 3.5, "base_salary": 14, "bundle": ["Networking", "Ethical Hacking"], "roles": ["Security Analyst"]},
    "Git": {"learn_time": 1, "base_salary": 9, "bundle": ["GitHub", "CI/CD"], "roles": ["Version Control Specialist"]}
}

# --- ROI Calculation ---
location_multiplier = {
    "India": 1, "USA": 2.2, "Europe": 1.8, "Canada": 1.9, "UK": 2.0, "Germany": 1.85, "Australia": 2.1, "Remote": 1.6
}
stage_adjustment = {"Fresher": 0.8, "Junior": 1.0, "Mid-level": 1.2, "Career Switcher": 0.9}
multiplier = location_multiplier[location] * stage_adjustment[career_stage]

info = skill_info[skill]
salary = int(info["base_salary"] * multiplier)
roi = round(salary / info["learn_time"], 2)
weeks = int(info["learn_time"] * 4)

# --- Display Metrics ---
st.metric("💰 Salary Potential (LPA)", f"{salary} LPA")
st.metric("⏱️ Learning Time", f"{info['learn_time']} months")
st.metric("📈 ROI Score", roi)

# --- Verdict ---
if roi >= 6:
    verdict = "🔥 High ROI Skill – Top Career Investment"
elif roi >= 4:
    verdict = "💼 Solid Choice – Great Potential"
elif roi >= 2.5:
    verdict = "⚠️ Moderate ROI – Upskill Recommended"
else:
    verdict = "🔍 Niche Skill – Consider Bundling"
st.markdown(f"### 🔮 Clairvoyra Verdict:\n**{verdict}**")

# --- Roles & Bundle ---
st.markdown("### 💼 Career Role Suggestions:")
st.write(", ".join(f"`{r}`" for r in info["roles"]))

st.markdown("### 📦 Recommended Skill Bundle:")
st.write(", ".join(f"`{b}`" for b in info["bundle"]))

# --- Timeline ---
st.markdown("### 🗺️ Learning Timeline:")
st.success(f"Start learning **{skill}** now and be job-ready in **{weeks} weeks**.")






 

