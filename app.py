import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- App Setup ---
st.set_page_config(page_title="Clairvoyra – Career ROI Engine", layout="centered", page_icon="🔮")
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

career_stage = st.selectbox("👤 Select your career stage:", ["Fresher", "Junior", "Mid-level", "Career Switcher"])
location = st.selectbox("🌍 Preferred job location:", ["India", "USA", "Europe", "Canada", "UK", "Germany", "Australia", "Remote"])
skill = st.selectbox("🛠️ Choose a tech skill to evaluate:", sorted(set([s for skills in goal_skills.values() for s in skills])))
skill_info = {
    "Python": {"learn_time": 3, "base_salary": 9, "bundle": ["Pandas", "SQL", "Streamlit"], "roles": ["Data Analyst", "ML Engineer"]},
    "SQL": {"learn_time": 2, "base_salary": 6, "bundle": ["Excel", "Power BI"], "roles": ["BI Analyst", "Data Engineer"]},
    "Power BI": {"learn_time": 1.5, "base_salary": 5, "bundle": ["Excel", "DAX"], "roles": ["BI Developer"]},
    "HTML & CSS": {"learn_time": 1.5, "base_salary": 4, "bundle": ["JS", "Responsive Design"], "roles": ["UI Designer"]},
    "JavaScript": {"learn_time": 2, "base_salary": 7, "bundle": ["React", "Node.js"], "roles": ["Frontend Dev"]},
    "React": {"learn_time": 2.5, "base_salary": 8, "bundle": ["JS", "Node.js"], "roles": ["Frontend Dev"]},
    "Java": {"learn_time": 3, "base_salary": 9, "bundle": ["Spring", "Maven"], "roles": ["Backend Dev"]},
    "Node.js": {"learn_time": 2, "base_salary": 8, "bundle": ["Express", "MongoDB"], "roles": ["Full Stack Dev"]},
    "Django": {"learn_time": 2.5, "base_salary": 8, "bundle": ["Python", "HTML", "SQLite"], "roles": ["Backend Developer"]},
    "Prompt Engineering": {"learn_time": 2, "base_salary": 12, "bundle": ["LLMs", "LangChain"], "roles": ["AI Specialist"]},
    "Flutter": {"learn_time": 2, "base_salary": 7, "bundle": ["Dart", "Firebase"], "roles": ["Mobile App Developer"]},
    "AWS": {"learn_time": 3, "base_salary": 10, "bundle": ["EC2", "Lambda"], "roles": ["Cloud Engineer"]},
    "Docker": {"learn_time": 2, "base_salary": 9, "bundle": ["Kubernetes", "Linux"], "roles": ["Infra Engineer"]},
    "Kubernetes": {"learn_time": 2.5, "base_salary": 10, "bundle": ["Docker", "Helm"], "roles": ["Cloud Infra Engineer"]},
    "Linux": {"learn_time": 2, "base_salary": 6, "bundle": ["Bash", "Networking"], "roles": ["SysAdmin"]},
    "Cybersecurity": {"learn_time": 3.5, "base_salary": 11, "bundle": ["Networking", "Ethical Hacking"], "roles": ["Security Analyst"]},
    "Git": {"learn_time": 1, "base_salary": 5, "bundle": ["GitHub", "CI/CD"], "roles": ["Version Control Specialist"]}
}

location_multiplier = {
    "India": 1, "USA": 2.2, "Europe": 1.8, "Canada": 1.9, "UK": 2.0, "Germany": 1.85, "Australia": 2.1, "Remote": 1.6
}
stage_adjustment = {"Fresher": 0.8, "Junior": 1.0, "Mid-level": 1.2, "Career Switcher": 0.9}
multiplier = location_multiplier[location] * stage_adjustment[career_stage]

info = skill_info[skill]
salary = int(info["base_salary"] * multiplier)
roi = round(salary / info["learn_time"], 2)
weeks = int(info["learn_time"] * 4)

st.metric("💰 Salary Potential (LPA)", f"{salary} LPA")
st.metric("⏱️ Learning Time", f"{info['learn_time']} months")
st.metric("📈 ROI Score", roi)

# Verdict
if roi >= 6:
    verdict = "🔥 High ROI Skill – Top Career Investment"
elif roi >= 4:
    verdict = "💼 Solid Choice – Great Potential"
elif roi >= 2.5:
    verdict = "⚠️ Moderate ROI – Upskill Recommended"
else:
    verdict = "🔍 Niche Skill – Consider Bundling"
st.markdown(f"### 🔮 Clairvoyra Verdict:\n**{verdict}**")

# Career Paths
st.markdown("### 💼 Career Role Suggestions:")
st.write(", ".join(f"`{r}`" for r in info["roles"]))

st.markdown("### 📦 Recommended Skill Bundle:")
st.write(", ".join(f"`{b}`" for b in info["bundle"]))

st.markdown("### 🗺️ Learning Timeline:")
st.success(f"Start learning **{skill}** now and be job-ready in **{weeks} weeks**.")
# -------------------------------
# 🔍 Filter Skills by Role & Learning Time
# -------------------------------
st.markdown("## 🔍 Filter Skills by Role & Learning Time")

selected_role = st.selectbox("🎯 Select a career role to filter by:", sorted({r for v in skill_info.values() for r in v['roles']}))
max_learn_time = st.slider("⏳ Maximum learning time (in months):", min_value=1, max_value=6, value=3)

filtered_skills = []
for skill_name, details in skill_info.items():
    if selected_role in details['roles'] and details['learn_time'] <= max_learn_time:
        filtered_skills.append((skill_name, details['learn_time'], details['base_salary']))

if filtered_skills:
    st.success(f"🔎 Found {len(filtered_skills)} skills for '{selected_role}' under {max_learn_time} months:")
    for skill_name, time, salary in sorted(filtered_skills, key=lambda x: x[1]):
        st.markdown(f"- **{skill_name}** — Learn Time: `{time} months`, Base Salary: `{salary} LPA`")
else:
    st.warning("No skills match this filter. Try increasing the max learning time or choosing a different role.")
# -------------------------------
# 🔁 Alternate Career Routes Generator
# -------------------------------
st.markdown("## 🔁 Alternate Career Routes Generator")

career_routes = {
    "Python": {
        "Safe": ["Learn Python", "Get Data Analyst Internship", "Become Mid-level Analyst"],
        "Growth": ["Learn Python", "Master ML + MLOps", "Become AI Infrastructure Engineer"],
        "Creative": ["Learn Python", "Explore Game Development (Pygame)", "Launch Indie Game"]
    },
    "SQL": {
        "Safe": ["Learn SQL", "Become BI Analyst", "Promote to Data Analyst"],
        "Growth": ["SQL + Data Warehousing", "ETL + Big Data", "Data Engineer"],
        "Creative": ["SQL + Web Dev", "Build Dashboards", "Freelance Developer"]
    },
    "JavaScript": {
        "Safe": ["Learn JS", "Frontend Internship", "Frontend Developer"],
        "Growth": ["JS + React + Node", "Full Stack Developer", "Tech Lead"],
        "Creative": ["JS + Creative Coding", "Generative Art", "Creative Technologist"]
    }
}

selected_skill = st.selectbox("🌀 Choose a skill for alternate career routes:", list(career_routes.keys()))
if selected_skill:
    st.markdown("### 🛣️ Your Career Routes:")
    for path in ["Safe", "Growth", "Creative"]:
        st.markdown(f"**{path} Route**: {' → '.join(career_routes[selected_skill][path])}")
# -------------------------------
# 📅 Career Calendar – 12 Weeks of Growth
# -------------------------------
st.markdown("## 📅 Career Calendar – 12 Weeks of Growth")

resources = {
    "Python": ["FreeCodeCamp Python", "Automate Boring Stuff", "Python for Everybody"],
    "SQL": ["Mode SQL Tutorial", "Khan Academy SQL", "LeetCode SQL"],
    "JavaScript": ["JS.info", "FreeCodeCamp JS", "Eloquent JavaScript"],
}

challenges = [
    "Build a mini project",
    "Write a blog post",
    "Teach the concept to someone",
    "Join a coding group",
    "Review past work",
    "Take a mock interview"
]

bonus_tips = [
    "Follow 5 tech leaders on LinkedIn",
    "Build a portfolio website",
    "Contribute to open source",
    "Write a career blog post"
]

start_date = datetime.today()
st.markdown("### 📆 12-Week Growth Calendar")
for week in range(12):
    skill = random.choice(list(resources.keys()))
    res = random.choice(resources[skill])
    role = random.choice(["Frontend Dev", "Data Analyst", "DevOps Engineer", "Mobile Dev"])
    challenge = random.choice(challenges)
    bonus = bonus_tips[week // 4] if week % 4 == 0 else None

    st.markdown(f"**Week {week+1} – Start: {(start_date + timedelta(days=week*7)).strftime('%Y-%m-%d')}**")
    st.write(f"- 🔧 Skill: {skill}")
    st.write(f"- 📚 Resource: {res}")
    st.write(f"- 🎯 Role Goal: {role}")
    st.write(f"- 💪 Challenge: {challenge}")
    if bonus:
        st.success(f"🎁 Bonus Tip: {bonus}")
    st.markdown("---")
# -------------------------------
# 🧠 Domain-based Skill Recommendations
# -------------------------------
st.markdown("## 🧠 Explore Skills by Domain")

domain_skills = {
    "Data Analysis": ["Python", "SQL"],
    "Business Intelligence": ["Power BI", "Tableau"],
    "Frontend Development": ["HTML & CSS", "React", "JavaScript"],
    "Backend Development": ["Node.js", "Django", "Java"],
    "Full Stack Development": ["JavaScript", "MongoDB", "Express.js"],
    "Cloud Engineering": ["AWS", "Terraform"],
    "DevOps": ["Docker", "CI/CD", "Jenkins"],
    "Machine Learning": ["Python", "Scikit-learn"],
    "Deep Learning": ["TensorFlow", "Keras"],
    "Mobile App Development": ["Flutter", "Dart"],
    "Cybersecurity": ["Linux", "Networking"],
    "Data Engineering": ["Spark", "Airflow"],
    "AI Integration": ["Prompt Engineering", "LangChain"],
    "Blockchain": ["Solidity", "Ethereum"],
    "Game Development": ["Unity", "C#"],
    "Web3": ["Smart Contracts", "IPFS"],
    "Embedded Systems": ["C", "C++"],
    "System Administration": ["Linux", "Bash"],
    "Site Reliability Engineering": ["Monitoring", "SRE"],
    "QA Testing": ["Selenium", "Postman"],
    "Agile Management": ["Scrum", "Kanban"],
    "Product Management": ["Figma", "Jira"],
    "UI/UX Design": ["Figma", "Adobe XD"],
    "Robotic Process Automation": ["UiPath", "Blue Prism"],
    "Big Data": ["Hadoop", "Hive"],
    "Data Science": ["Pandas", "NumPy"],
    "Computer Vision": ["OpenCV", "YOLO"],
    "NLP": ["SpaCy", "NLTK"],
    "Digital Marketing": ["Google Ads", "SEO"],
    "E-commerce Engineering": ["Magento", "Shopify"],
    "Cloud Security": ["IAM", "Firewall"],
    "Fintech Development": ["Python", "API Integration"],
    "HealthTech AI": ["ML", "Image Processing"],
    "IoT Development": ["MQTT", "Raspberry Pi"],
    "Sustainable Tech": ["Green IT", "Energy Efficiency"],
    "Storage Engineering": ["SAN", "NAS"],
    "Legacy Systems": ["COBOL", "JCL"],
    "ETL Engineering": ["Informatica", "Talend"],
    "Data Warehousing": ["Snowflake", "Redshift"],
    "Visualization": ["Looker", "Power BI"],
    "Mobile Security": ["App Hardening", "Code Obfuscation"],
    "AI for Coding": ["Copilot", "CodeWhisperer"],
    "Information Retrieval": ["Elasticsearch", "Lucene"],
    "CRM Systems": ["Salesforce", "Zoho"],
    "BPM Systems": ["Camunda", "Bizagi"],
    "Voice AI": ["Speech Recognition", "TTS"],
    "AR/VR Development": ["Unreal Engine", "3D Modeling"],
    "SaaS Tools": ["Notion", "Zapier"],
    "Low Code Platforms": ["OutSystems", "Mendix"],
    "Open Source Contribution": ["Git", "Documentation"]
}
# Domain selector
selected_domain = st.selectbox("🌐 Select a domain to discover relevant skills:", sorted(domain_skills.keys()))

if selected_domain:
    skills = domain_skills[selected_domain]
    st.markdown(f"### 🚀 Recommended Skills for **{selected_domain}**:")
    for s in skills:
        st.markdown(f"- 🔧 **{s}**")
