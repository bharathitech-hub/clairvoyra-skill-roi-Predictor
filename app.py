import streamlit as st
import pandas as pd
import plotly.express as px
import random
from io import BytesIO
from fpdf import FPDF

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

# --- Skill Data ---

# --- Updated Skill Roles for 2025 ---
skill_info = {
    "Python": {"learn_time": 3, "base_salary": 12, "bundle": ["Pandas", "SQL", "Streamlit"], "roles": ["Data Analyst", "Backend Developer", "ML Engineer"]},
    "Java": {"learn_time": 3, "base_salary": 13, "bundle": ["Spring Boot", "OOP"], "roles": ["Backend Developer", "Software Engineer"]},
    "C++": {"learn_time": 3, "base_salary": 12, "bundle": ["DSA", "OOP"], "roles": ["Software Engineer", "Game Developer"]},
    "C": {"learn_time": 3, "base_salary": 11, "bundle": ["Pointers", "Embedded C"], "roles": ["Embedded Systems Developer", "Firmware Engineer"]},
    "JavaScript": {"learn_time": 2, "base_salary": 11, "bundle": ["React", "Node.js"], "roles": ["Frontend Developer", "Full Stack Developer"]},
    "TypeScript": {"learn_time": 2.5, "base_salary": 12, "bundle": ["React", "Next.js"], "roles": ["Frontend Developer", "React Developer"]},
    "HTML & CSS": {"learn_time": 1.5, "base_salary": 8, "bundle": ["JavaScript", "Responsive Design"], "roles": ["Frontend Developer", "UI Developer"]},
    "React": {"learn_time": 2.5, "base_salary": 12, "bundle": ["JavaScript", "Redux"], "roles": ["Frontend Developer", "React Developer"]},
    "Angular": {"learn_time": 2.5, "base_salary": 12, "bundle": ["TypeScript", "RxJS"], "roles": ["Frontend Developer", "Web Developer"]},
    "Node.js": {"learn_time": 2, "base_salary": 12, "bundle": ["Express.js", "MongoDB"], "roles": ["Backend Developer", "Full Stack Developer"]},
    "Django": {"learn_time": 2.5, "base_salary": 12, "bundle": ["Python", "HTML", "SQLite"], "roles": ["Backend Developer", "Python Developer"]},
    "Spring Boot": {"learn_time": 2.5, "base_salary": 13, "bundle": ["Java", "Maven"], "roles": ["Java Backend Developer"]},
    "Express.js": {"learn_time": 2, "base_salary": 11, "bundle": ["Node.js", "MongoDB"], "roles": ["Node.js Developer", "Backend Developer"]},
    "PHP": {"learn_time": 2, "base_salary": 10, "bundle": ["MySQL", "Laravel"], "roles": ["Web Developer", "Backend Developer"]},
    "Flutter": {"learn_time": 2, "base_salary": 11, "bundle": ["Dart", "Firebase"], "roles": ["Mobile App Developer"]},
    "SQL": {"learn_time": 2, "base_salary": 10, "bundle": ["Joins", "Subqueries"], "roles": ["Data Analyst", "Data Engineer"]},
    "Pandas": {"learn_time": 1.5, "base_salary": 10, "bundle": ["NumPy", "Matplotlib"], "roles": ["Data Analyst", "ML Engineer"]},
    "Power BI": {"learn_time": 1.5, "base_salary": 9, "bundle": ["DAX", "Excel"], "roles": ["BI Analyst", "Data Analyst"]},
    "Tableau": {"learn_time": 1.5, "base_salary": 9, "bundle": ["Dashboards", "Data Sources"], "roles": ["Data Visualization Specialist", "BI Analyst"]},
    "Excel": {"learn_time": 1, "base_salary": 8, "bundle": ["Formulas", "Pivot Tables"], "roles": ["Data Entry Specialist", "Finance Analyst"]},
    "AWS": {"learn_time": 3, "base_salary": 15, "bundle": ["EC2", "Lambda"], "roles": ["Cloud Engineer", "DevOps Engineer"]},
    "Docker": {"learn_time": 2, "base_salary": 13, "bundle": ["Containers", "Images"], "roles": ["DevOps Engineer", "Infrastructure Engineer"]},
    "Kubernetes": {"learn_time": 2.5, "base_salary": 14, "bundle": ["Pods", "Helm"], "roles": ["Cloud Infra Engineer", "DevOps Engineer"]},
    "Git": {"learn_time": 1, "base_salary": 9, "bundle": ["GitHub", "Branching"], "roles": ["Software Developer", "DevOps Engineer"]},
    "CI/CD": {"learn_time": 1.5, "base_salary": 10, "bundle": ["Jenkins", "Pipelines"], "roles": ["DevOps Engineer", "Automation Engineer"]},
    "Linux": {"learn_time": 2, "base_salary": 10, "bundle": ["Bash", "Permissions"], "roles": ["System Administrator", "DevOps Engineer"]},
    "Networking": {"learn_time": 2, "base_salary": 9, "bundle": ["TCP/IP", "DNS"], "roles": ["Network Engineer", "Security Analyst"]},
    "Cybersecurity": {"learn_time": 3, "base_salary": 14, "bundle": ["Pen Testing", "Firewalls"], "roles": ["Security Analyst", "Penetration Tester"]},
    "Firebase": {"learn_time": 2, "base_salary": 10, "bundle": ["Firestore", "Auth"], "roles": ["Mobile App Developer", "Backend Developer"]},
    "MongoDB": {"learn_time": 2, "base_salary": 11, "bundle": ["NoSQL", "Mongoose"], "roles": ["Backend Developer", "Full Stack Developer"]},
    "Terraform": {"learn_time": 2.5, "base_salary": 13, "bundle": ["IaC", "AWS"], "roles": ["Cloud Engineer", "DevOps Engineer"]},
    "Ansible": {"learn_time": 2, "base_salary": 12, "bundle": ["Playbooks", "SSH"], "roles": ["DevOps Engineer", "Infrastructure Developer"]},
    "Chef": {"learn_time": 2, "base_salary": 12, "bundle": ["Cookbooks", "Ruby"], "roles": ["DevOps Engineer", "Infrastructure Engineer"]},
    "Jenkins": {"learn_time": 2, "base_salary": 12, "bundle": ["CI/CD", "Automation"], "roles": ["CI/CD Engineer", "DevOps Engineer"]},
    "RPA (UiPath / Blue Prism)": {"learn_time": 2.5, "base_salary": 11, "bundle": ["Automation", "Bots"], "roles": ["Automation Engineer", "RPA Developer"]},
    "Blockchain": {"learn_time": 3.5, "base_salary": 14, "bundle": ["Solidity", "Smart Contracts"], "roles": ["Blockchain Developer", "Smart Contract Engineer"]},
    "IoT": {"learn_time": 3, "base_salary": 12, "bundle": ["MQTT", "Sensors"], "roles": ["IoT Engineer", "Embedded Systems Developer"]},
    "Unity / Unreal Engine": {"learn_time": 3, "base_salary": 13, "bundle": ["C#", "Physics Engine"], "roles": ["AR/VR Developer", "XR Engineer"]},
    "3D Modeling (e.g., Blender)": {"learn_time": 2.5, "base_salary": 11, "bundle": ["Meshes", "Rigging"], "roles": ["AR/VR Developer", "Game Designer"]},
    "Snowflake": {"learn_time": 2.5, "base_salary": 13, "bundle": ["Cloud SQL", "Data Warehousing"], "roles": ["Data Engineer", "Cloud Data Architect"]},
    "Spark / Hadoop": {"learn_time": 3, "base_salary": 14, "bundle": ["Big Data", "ETL"], "roles": ["Big Data Engineer", "Data Engineer"]},
    "Platform Engineering": {"learn_time": 2.5, "base_salary": 13, "bundle": ["Tooling", "DevOps"], "roles": ["Platform Engineer", "DevOps Engineer"]},
    "Site Reliability Engineering (SRE)": {"learn_time": 3, "base_salary": 14, "bundle": ["Monitoring", "Incident Response"], "roles": ["SRE", "DevOps Engineer"]},
    "Storage Engineering": {"learn_time": 2.5, "base_salary": 12, "bundle": ["SAN", "NAS"], "roles": ["Storage Engineer", "System Administrator"]},
    "Mainframes (COBOL)": {"learn_time": 3.5, "base_salary": 13, "bundle": ["JCL", "IMS"], "roles": ["Mainframe Developer", "Legacy Systems Engineer"]},
    "Figma (UI/UX)": {"learn_time": 1.5, "base_salary": 10, "bundle": ["Prototyping", "Design Systems"], "roles": ["UI/UX Designer", "Product Designer"]},
    "Agile / Scrum / Kanban": {"learn_time": 1.5, "base_salary": 10, "bundle": ["Scrum Mastery", "Kanban Boards"], "roles": ["Scrum Master", "Agile Coach"]},
    "Prompt Engineering": {"learn_time": 2, "base_salary": 15, "bundle": ["LLMs", "Instruction Design"], "roles": ["Prompt Engineer", "AI Integration Specialist"]},
    "AI-assisted Coding (Vibe Coding)": {"learn_time": 1.5, "base_salary": 14, "bundle": ["Copilot", "Tabnine"], "roles": ["Software Engineer", "AI-Augmented Developer"]},
    "Green Tech / Sustainable IT": {"learn_time": 2, "base_salary": 12, "bundle": ["Cloud Optimization", "Energy Efficiency"], "roles": ["Sustainable Tech Engineer", "Green IT Specialist"]}
}
}

# --- Learning Resources ---
learning_resources = {
    "Python": [
        "Python for Everybody – Coursera",
        "Automate the Boring Stuff – Al Sweigart",
        "Learn Python – FreeCodeCamp"
    ],
    "SQL": [
        "W3Schools SQL Tutorial",
        "Mode SQL Lessons",
        "Khan Academy – Intro to SQL"
    ],
    "Power BI": [
        "Microsoft Learn – Power BI",
        "YouTube: Power BI Full Course",
        "Coursera: Data Visualization with Power BI"
    ],
    "JavaScript": [
        "JavaScript.info",
        "FreeCodeCamp JavaScript",
        "Eloquent JavaScript (Book)"
    ],
    "React": [
        "React Official Docs",
        "FreeCodeCamp React",
        "Codecademy – Learn React"
    ],
    "Java": [
        "Java Programming – Coursera",
        "Codecademy Java",
        "Java Brains – YouTube"
    ],
    "HTML & CSS": [
        "HTML & CSS – W3Schools",
        "FreeCodeCamp Web Dev",
        "MDN Web Docs – HTML/CSS"
    ],
    "Django": [
        "Django Girls Tutorial",
        "Real Python Django Guide",
        "MDN – Django Web Framework"
    ],
    "AWS": [
        "AWS Skill Builder",
        "Free AWS Bootcamp – YouTube",
        "AWS Certification Prep Guide"
    ],
    "Docker": [
        "Docker Getting Started",
        "FreeCodeCamp Docker Tutorial",
        "Play With Docker (Hands-on)"
    ],
    "Kubernetes": [
        "Kubernetes Official Docs",
        "Kelsey Hightower’s Kubernetes the Hard Way",
        "FreeCodeCamp Kubernetes"
    ],
    "Linux": [
        "Linux Journey",
        "OverTheWire Bandit",
        "Linux Command Line – Udemy"
    ],
    "Git": [
        "Git Handbook – GitHub",
        "Git Immersion",
        "FreeCodeCamp Git & GitHub"
    ],
    "Cybersecurity": [
        "TryHackMe – Cybersecurity Labs",
        "Cybrary Security Essentials",
        "YouTube: Cybersecurity Full Course"
    ],
    "Prompt Engineering": [
        "OpenAI Prompt Guide",
        "Learn Prompting – GitHub",
        "LangChain Docs"
    ],
    "Node.js": [
        "Node.js Crash Course – Traversy Media",
        "Node.js Docs",
        "Codecademy – Learn Node.js"
    ],
    "Flutter": [
        "Flutter.dev Official Docs",
        "Google Codelabs – Flutter",
        "Academind Flutter Tutorial"
    ],
    "Firebase": [
        "Firebase Fundamentals – YouTube (Google)",
        "Build Apps with Firebase – Firebase.dev",
        "FreeCodeCamp: Firebase Full Tutorial"
    ],
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

# --- Output ---
st.metric("💰 Salary Potential (LPA)", f"{salary} LPA")
st.metric("⏱️ Learning Time", f"{info['learn_time']} months")
st.metric("📈 ROI Score", roi)

# --- Clairvoyra Verdict ---
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

# --- Learning Resources Section ---
st.markdown("### 📚 Recommended Learning Resources:")
if skill in learning_resources:
    for res in learning_resources[skill]:
        st.write(f"- {res}")
else:
    st.info("Resources will be updated for this skill soon.")



# -------------------------------
# 🔁 Feature 1: Alternate Career Routes Generator
# -------------------------------
st.markdown("## 🔁 Alternate Career Routes Generator")

career_routes = {
    "Python": {
        "Safe": ["Learn Python", "Get Data Analyst Internship", "Become Mid-level Analyst"],
        "Growth": ["Learn Python", "Master ML + MLOps", "Become AI Infrastructure Engineer"],
        "Creative": ["Learn Python", "Explore Game Development (Pygame)", "Launch Indie Game or Freelance"]
    },
    "SQL": {
        "Safe": ["Learn SQL", "Become BI Analyst", "Promote to Data Analyst"],
        "Growth": ["SQL + Data Warehousing", "ETL + Big Data", "Data Engineer"],
        "Creative": ["SQL + Web Dev", "Build Custom Dashboards", "Freelance Analytics Developer"]
    },
    "JavaScript": {
        "Safe": ["Learn JavaScript", "Frontend Intern", "Frontend Developer"],
        "Growth": ["JS + React + Node", "Full Stack Developer", "Tech Lead"],
        "Creative": ["JS + Creative Coding", "Generative Art / Visual Tools", "Creative Technologist"]
    }
}

selected_skill = st.selectbox("🔧 Choose a skill to explore career routes:", list(career_routes.keys()))
if selected_skill:
    st.markdown("### 🧭 Your Alternate Career Paths:")
    for route in ["Safe", "Growth", "Creative"]:
        st.markdown(f"**{route} Route**: {' → '.join(career_routes[selected_skill][route])}")

# -------------------------------
# 📅 Feature 2: Career Calendar – 12 Weeks of Growth
# -------------------------------
st.markdown("## 📅 Career Calendar – 12 Weeks of Growth")

from datetime import datetime, timedelta
import random

resources = {
    "Python": ["FreeCodeCamp Python", "Automate Boring Stuff", "Python for Everybody"],
    "SQL": ["Mode SQL Tutorial", "Khan Academy SQL", "LeetCode SQL"],
    "JavaScript": ["JS.info", "FreeCodeCamp JS", "Eloquent JavaScript"],
}

challenges = [
    "Build a mini project",
    "Write a blog post about your learning",
    "Teach the concept to a friend",
    "Join a coding community",
    "Review past material",
    "Take a mock interview"
]

bonus_tips = [
    "Follow 5 industry leaders on LinkedIn",
    "Start building your personal portfolio website",
    "Contribute to an open-source project",
    "Write a case study on your favorite tech role"
]

start_date = datetime.today()
st.markdown("### 📆 Weekly Learning Plan")
for week in range(12):
    skill = random.choice(list(resources.keys()))
    res = random.choice(resources[skill])
    role = random.choice(["Frontend Developer", "Data Analyst", "DevOps Engineer", "Mobile App Developer"])
    challenge = random.choice(challenges)
    bonus = bonus_tips[week // 4] if week % 4 == 0 else None

    st.markdown(f"**Week {week+1} ({(start_date + timedelta(days=week*7)).strftime('%Y-%m-%d')})**")
    st.write(f"- 🔧 Skill: {skill}")
    st.write(f"- 📚 Resource: {res}")
    st.write(f"- 🎯 Role Goal: {role}")
    st.write(f"- 💪 Challenge: {challenge}")
    if bonus:
        st.success(f"🎁 Bonus Tip: {bonus}")
    st.markdown("---")



# -------------------------------
# 🔍 Filter Skills by Role & Learning Time
# -------------------------------
st.markdown("## 🔍 Filter Skills by Role & Learning Time")

# Input filters from user
selected_role = st.selectbox("🎯 Select a career role to filter by:", sorted({r for v in skill_info.values() for r in v['roles']}))
max_learn_time = st.slider("⏳ Maximum learning time (in months):", min_value=1, max_value=6, value=3)

# Filter logic
filtered_skills = []
for skill_name, details in skill_info.items():
    if selected_role in details['roles'] and details['learn_time'] <= max_learn_time:
        filtered_skills.append((skill_name, details['learn_time'], details['base_salary']))

# Display results
if filtered_skills:
    st.success(f"🔎 Found {len(filtered_skills)} skills for '{selected_role}' under {max_learn_time} months:")
    for skill_name, time, salary in sorted(filtered_skills, key=lambda x: x[1]):
        st.markdown(f"- **{skill_name}** — Learn Time: `{time} months`, Base Salary: `{salary} LPA`")
else:
    st.warning("No skills match this filter. Try increasing the max learning time or choosing a different role.")
