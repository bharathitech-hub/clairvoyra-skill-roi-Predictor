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
# --- Expanded Career Goal Selection (50 Roles) ---
goal = st.selectbox("🎯 What's your career goal?", [
    "Data Analyst", "Data Scientist", "Data Engineer", "AI Engineer", "ML Engineer",
    "Frontend Developer", "Backend Developer", "Full Stack Developer", "DevOps Engineer", "Cloud Engineer",
    "Mobile App Developer", "Game Developer", "Cybersecurity Specialist", "Blockchain Developer", "UI/UX Designer",
    "Business Analyst", "Product Manager", "Tech Support Engineer", "QA Engineer", "Embedded Systems Engineer",
    "Robotics Engineer", "Big Data Engineer", "AR/VR Developer", "Site Reliability Engineer", "Solutions Architect",
    "Database Administrator", "IT Support Specialist", "Network Engineer", "System Administrator", "Digital Marketing Analyst",
    "SEO Specialist", "Data Architect", "MLOps Engineer", "Security Analyst", "Penetration Tester",
    "Computer Vision Engineer", "NLP Engineer", "Prompt Engineer", "ETL Developer", "Firmware Engineer",
    "Web Designer", "No-Code Developer", "Low-Code Platform Engineer", "CRM Developer", "Salesforce Developer",
    "Test Automation Engineer", "Agile Coach", "Scrum Master", "IoT Engineer", "Tech Evangelist"
])

goal_skills = {
    "Data Analyst": ["Python", "SQL", "Power BI"],
    "Data Scientist": ["Python", "Pandas", "Scikit-learn"],
    "Data Engineer": ["SQL", "Spark", "Airflow"],
    "AI Engineer": ["Python", "Django", "Prompt Engineering"],
    "ML Engineer": ["Python", "Scikit-learn", "MLOps"],
    "Prompt Engineer": ["Prompt Engineering", "LLMs", "LangChain"],
    "Frontend Developer": ["HTML & CSS", "JavaScript", "React"],
    "Backend Developer": ["Java", "Node.js", "Django"],
    "Full Stack Developer": ["JavaScript", "React", "Node.js"],
    "DevOps Engineer": ["Git", "Docker", "CI/CD"],
    "Cloud Engineer": ["AWS", "Terraform", "Kubernetes"],
    "Cybersecurity Specialist": ["Linux", "Cybersecurity", "Networking"],
    "Mobile App Developer": ["Flutter", "Dart", "Firebase"],
    "UI/UX Designer": ["Figma", "Adobe XD", "HTML & CSS"],
    "Product Manager": ["Jira", "Scrum", "Figma"],
    "Business Analyst": ["Excel", "Power BI", "SQL"],
    "BI Developer": ["Power BI", "Tableau", "SQL"],
    "QA Engineer": ["Selenium", "Postman", "CI/CD"],
    "SRE Engineer": ["Monitoring", "SRE", "Linux"],
    "ETL Engineer": ["Informatica", "Talend", "SQL"],
    "Data Architect": ["SQL", "Redshift", "Data Modeling"],
    "MLOps Engineer": ["Docker", "MLflow", "CI/CD"],
    "Big Data Engineer": ["Hadoop", "Hive", "Spark"],
    "Computer Vision Engineer": ["OpenCV", "YOLO", "TensorFlow"],
    "NLP Engineer": ["SpaCy", "NLTK", "Transformers"],
    "IoT Developer": ["MQTT", "Raspberry Pi", "Python"],
    "Blockchain Developer": ["Solidity", "Ethereum", "Smart Contracts"],
    "Game Developer": ["Unity", "C#", "Pygame"],
    "Web3 Developer": ["Smart Contracts", "IPFS", "Solidity"],
    "Digital Marketing Engineer": ["Google Ads", "SEO", "Analytics"],
    "Tech Support Engineer": ["Linux", "Networking", "Troubleshooting"],
    "Embedded Systems Engineer": ["C", "Microcontrollers", "RTOS"],
    "Robotics Engineer": ["Python", "ROS", "Computer Vision"],
    "AR/VR Developer": ["Unity", "3D Modeling", "Unreal Engine"],
    "Site Reliability Engineer": ["Monitoring", "SRE", "Linux"],
    "Solutions Architect": ["Cloud Architecture", "DevOps", "System Design"],
    "Database Administrator": ["SQL", "Backup & Recovery", "Redshift"],
    "IT Support Specialist": ["Windows Admin", "Ticketing Tools", "Networking"],
    "Network Engineer": ["Networking", "Cisco", "Firewalls"],
    "System Administrator": ["Linux", "Bash", "Virtualization"],
    "Digital Marketing Analyst": ["Google Ads", "SEO", "Analytics"],
    "SEO Specialist": ["SEO", "Keyword Research", "Google Analytics"],
    "Security Analyst": ["Cybersecurity", "SIEM", "Incident Response"],
    "Penetration Tester": ["Ethical Hacking", "Metasploit", "Burp Suite"],
    "ETL Developer": ["Informatica", "SQL", "Data Warehousing"],
    "Firmware Engineer": ["Embedded C", "RTOS", "Microcontrollers"],
    "Web Designer": ["HTML & CSS", "Adobe XD", "Figma"],
    "No-Code Developer": ["Bubble", "Zapier", "Airtable"],
    "Low-Code Platform Engineer": ["OutSystems", "Mendix", "API Integration"],
    "CRM Developer": ["Salesforce", "CRM Workflows", "Apex"],
    "Salesforce Developer": ["Salesforce", "Apex", "Visualforce"],
    "Test Automation Engineer": ["Selenium", "CI/CD", "TestNG"],
    "Agile Coach": ["Scrum", "Kanban", "Jira"],
    "Scrum Master": ["Scrum", "Agile", "Jira"],
    "IoT Engineer": ["MQTT", "Raspberry Pi", "Python"],
    "Tech Evangelist": ["Public Speaking", "Tech Writing", "Open Source"]
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
    "Git": {"learn_time": 1, "base_salary": 5, "bundle": ["GitHub", "CI/CD"], "roles": ["Version Control Specialist"]},
    "Adobe XD": {"learn_time": 1.5, "base_salary": 4, "bundle": ["Figma", "UI Design"], "roles": ["UI/UX Designer"]},
    "Airflow": {"learn_time": 2, "base_salary": 7, "bundle": ["Python", "ETL"], "roles": ["Data Engineer"]},
    "Analytics": {"learn_time": 2, "base_salary": 6, "bundle": ["Excel", "Power BI"], "roles": ["Business Analyst"]},
    "C#": {"learn_time": 3, "base_salary": 7, "bundle": [".NET", "Unity"], "roles": ["Game Developer"]},
    "CI/CD": {"learn_time": 2, "base_salary": 8, "bundle": ["Jenkins", "GitHub Actions"], "roles": ["DevOps Engineer"]},
    "Dart": {"learn_time": 2, "base_salary": 6, "bundle": ["Flutter", "Firebase"], "roles": ["Mobile App Developer"]},
    "Data Modeling": {"learn_time": 2, "base_salary": 7, "bundle": ["ER Diagrams", "SQL"], "roles": ["Data Architect"]},
    "Ethereum": {"learn_time": 2.5, "base_salary": 9, "bundle": ["Solidity", "Smart Contracts"], "roles": ["Blockchain Developer"]},
    "Excel": {"learn_time": 1, "base_salary": 4, "bundle": ["Power BI", "Pivot Tables"], "roles": ["Business Analyst"]},
    "Figma": {"learn_time": 1.5, "base_salary": 5, "bundle": ["UI Principles", "Adobe XD"], "roles": ["UI/UX Designer"]},
    "Firebase": {"learn_time": 2, "base_salary": 6, "bundle": ["Firestore", "Dart"], "roles": ["Mobile App Developer"]},
    "Google Ads": {"learn_time": 1.5, "base_salary": 5, "bundle": ["SEO", "Analytics"], "roles": ["Digital Marketing Analyst"]},
    "Hadoop": {"learn_time": 3, "base_salary": 8, "bundle": ["Hive", "Spark"], "roles": ["Big Data Engineer"]},
    "Hive": {"learn_time": 2, "base_salary": 7, "bundle": ["Hadoop", "SQL"], "roles": ["Big Data Engineer"]},
    "IPFS": {"learn_time": 2, "base_salary": 8, "bundle": ["Blockchain", "Smart Contracts"], "roles": ["Web3 Developer"]},
    "Informatica": {"learn_time": 2.5, "base_salary": 8, "bundle": ["ETL", "SQL"], "roles": ["ETL Developer"]},
    "Jira": {"learn_time": 1, "base_salary": 4, "bundle": ["Agile", "Scrum"], "roles": ["Product Manager"]},
    "LangChain": {"learn_time": 2, "base_salary": 10, "bundle": ["LLMs", "Prompt Engineering"], "roles": ["AI Engineer"]},
    "MLOps": {"learn_time": 2.5, "base_salary": 9, "bundle": ["CI/CD", "Docker"], "roles": ["ML Engineer"]},
    "MLflow": {"learn_time": 2, "base_salary": 8, "bundle": ["Tracking", "MLOps"], "roles": ["ML Engineer"]},
    "MQTT": {"learn_time": 1.5, "base_salary": 6, "bundle": ["IoT", "Raspberry Pi"], "roles": ["IoT Developer"]},
    "Monitoring": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Grafana", "Prometheus"], "roles": ["SRE"]},
    "NLTK": {"learn_time": 2, "base_salary": 7, "bundle": ["Text Processing", "SpaCy"], "roles": ["NLP Engineer"]},
    "OpenCV": {"learn_time": 2.5, "base_salary": 8, "bundle": ["YOLO", "Computer Vision"], "roles": ["CV Engineer"]},
    "Pandas": {"learn_time": 2, "base_salary": 7, "bundle": ["Python", "NumPy"], "roles": ["Data Scientist"]},
    "Postman": {"learn_time": 1, "base_salary": 4, "bundle": ["API Testing", "Swagger"], "roles": ["QA Engineer"]},
    "Pygame": {"learn_time": 2, "base_salary": 6, "bundle": ["Python", "Game Dev"], "roles": ["Game Developer"]},
    "Raspberry Pi": {"learn_time": 2, "base_salary": 6, "bundle": ["Python", "IoT"], "roles": ["IoT Engineer"]},
    "Redshift": {"learn_time": 2, "base_salary": 8, "bundle": ["SQL", "Data Modeling"], "roles": ["Data Architect"]},
    "SEO": {"learn_time": 1.5, "base_salary": 5, "bundle": ["Google Ads", "Analytics"], "roles": ["SEO Specialist"]},
    "SRE": {"learn_time": 2, "base_salary": 8, "bundle": ["Monitoring", "Linux"], "roles": ["Site Reliability Engineer"]},
    "Scikit-learn": {"learn_time": 2, "base_salary": 8, "bundle": ["ML Models", "Python"], "roles": ["ML Engineer"]},
    "Scrum": {"learn_time": 1, "base_salary": 4, "bundle": ["Jira", "Agile"], "roles": ["Scrum Master"]},
    "Selenium": {"learn_time": 2, "base_salary": 6, "bundle": ["Python", "CI/CD"], "roles": ["QA Engineer"]},
    "Smart Contracts": {"learn_time": 2, "base_salary": 9, "bundle": ["Solidity", "Blockchain"], "roles": ["Blockchain Developer"]},
    "Solidity": {"learn_time": 2.5, "base_salary": 9, "bundle": ["Smart Contracts", "Ethereum"], "roles": ["Blockchain Developer"]},
    "SpaCy": {"learn_time": 2, "base_salary": 7, "bundle": ["NLP", "Text Mining"], "roles": ["NLP Engineer"]},
    "Spark": {"learn_time": 3, "base_salary": 9, "bundle": ["Scala", "Hadoop"], "roles": ["Big Data Engineer"]},
    "Tableau": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Power BI", "SQL"], "roles": ["BI Developer"]},
    "Talend": {"learn_time": 2, "base_salary": 7, "bundle": ["ETL", "Informatica"], "roles": ["ETL Developer"]},
    "TensorFlow": {"learn_time": 3, "base_salary": 9, "bundle": ["Keras", "Deep Learning"], "roles": ["AI Engineer"]},
    "Terraform": {"learn_time": 2, "base_salary": 8, "bundle": ["Cloud Infra", "AWS"], "roles": ["DevOps Engineer"]},
    "Transformers": {"learn_time": 2.5, "base_salary": 10, "bundle": ["LLMs", "NLP"], "roles": ["NLP Engineer"]},
    "Unity": {"learn_time": 3, "base_salary": 7, "bundle": ["C#", "Game Physics"], "roles": ["Game Developer"]},
    "YOLO": {"learn_time": 2.5, "base_salary": 8, "bundle": ["Object Detection", "OpenCV"], "roles": ["Computer Vision Engineer"]}
     "3D Modeling": {"learn_time": 2, "base_salary": 6, "bundle": ["Unity", "Unreal Engine"], "roles": ["AR/VR Developer"]},
     "API Integration": {"learn_time": 1.5, "base_salary": 6, "bundle": ["REST APIs", "OAuth"], "roles": ["Low-Code Platform Engineer"]},
     "Agile": {"learn_time": 1, "base_salary": 5, "bundle": ["Scrum", "Kanban"], "roles": ["Scrum Master"]},
     "Airtable": {"learn_time": 1, "base_salary": 4, "bundle": ["Zapier", "No-Code Tools"], "roles": ["No-Code Developer"]},
     "Apex": {"learn_time": 2, "base_salary": 7, "bundle": ["Salesforce", "Visualforce"], "roles": ["Salesforce Developer"]},
     "Backup & Recovery": {"learn_time": 1.5, "base_salary": 6, "bundle": ["SQL", "Disaster Recovery"], "roles": ["Database Administrator"]},
     "Bash": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Linux", "Shell Scripting"], "roles": ["System Administrator"]},
     "Bubble": {"learn_time": 1.5, "base_salary": 5, "bundle": ["No-Code", "Workflows"], "roles": ["No-Code Developer"]},
     "Burp Suite": {"learn_time": 1.5, "base_salary": 6, "bundle": ["OWASP", "Web Security"], "roles": ["Penetration Tester"]},
     "C": {"learn_time": 2, "base_salary": 6, "bundle": ["Embedded C", "Microcontrollers"], "roles": ["Embedded Systems Engineer"]},
     "CRM Workflows": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Salesforce", "Zoho CRM"], "roles": ["CRM Developer"]},
     "Cisco": {"learn_time": 2, "base_salary": 7, "bundle": ["Networking", "Routing Protocols"], "roles": ["Network Engineer"]},
     "Cloud Architecture": {"learn_time": 3, "base_salary": 10, "bundle": ["AWS", "DevOps"], "roles": ["Solutions Architect"]},
     "Computer Vision": {"learn_time": 2.5, "base_salary": 8, "bundle": ["YOLO", "OpenCV"], "roles": ["Computer Vision Engineer"]},
     "Data Warehousing": {"learn_time": 2.5, "base_salary": 8, "bundle": ["Redshift", "Snowflake"], "roles": ["ETL Developer"]},
     "DevOps": {"learn_time": 2.5, "base_salary": 9, "bundle": ["CI/CD", "Terraform"], "roles": ["DevOps Engineer"]},
     "Embedded C": {"learn_time": 2, "base_salary": 6, "bundle": ["RTOS", "Microcontrollers"], "roles": ["Firmware Engineer"]},
     "Ethical Hacking": {"learn_time": 2, "base_salary": 8, "bundle": ["Kali Linux", "Metasploit"], "roles": ["Security Analyst"]},
     "Firewalls": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Network Security", "Configuration"], "roles": ["Network Engineer"]},
     "Analytics": {"learn_time": 2, "base_salary": 6, "bundle": ["Power BI", "Google Analytics"], "roles": ["Digital Marketing Analyst"]},
     "Incident Response": {"learn_time": 2, "base_salary": 7, "bundle": ["SIEM", "Security Tools"], "roles": ["Security Analyst"]},
     "Kanban": {"learn_time": 1, "base_salary": 5, "bundle": ["Agile", "Jira"], "roles": ["Agile Coach"]},
     "Keyword Research": {"learn_time": 1.5, "base_salary": 5, "bundle": ["SEO", "Google Ads"], "roles": ["SEO Specialist"]},
     "LLMs": {"learn_time": 2.5, "base_salary": 10, "bundle": ["Transformers", "Prompt Engineering"], "roles": ["AI Engineer"]},
     "Mendix": {"learn_time": 2, "base_salary": 7, "bundle": ["Low-Code", "API Integration"], "roles": ["Low-Code Platform Engineer"]},
     "Metasploit": {"learn_time": 1.5, "base_salary": 7, "bundle": ["Penetration Testing", "Kali Linux"], "roles": ["Penetration Tester"]},
     "Microcontrollers": {"learn_time": 2, "base_salary": 6, "bundle": ["C", "Embedded Systems"], "roles": ["Firmware Engineer"]},
     "Networking": {"learn_time": 2, "base_salary": 6, "bundle": ["Linux", "Cisco"], "roles": ["Network Engineer"]},
     "Open Source": {"learn_time": 1, "base_salary": 5, "bundle": ["Git", "Documentation"], "roles": ["Tech Evangelist"]},
     "OutSystems": {"learn_time": 2, "base_salary": 7, "bundle": ["Low-Code Tools", "Mendix"], "roles": ["Low-Code Platform Engineer"]},
     "Public Speaking": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Storytelling", "Slide Design"], "roles": ["Tech Evangelist"]},
     "ROS": {"learn_time": 2, "base_salary": 7, "bundle": ["Python", "Robotics"], "roles": ["Robotics Engineer"]},
     "RTOS": {"learn_time": 2, "base_salary": 6, "bundle": ["Embedded C", "Microcontrollers"], "roles": ["Embedded Systems Engineer"]},
     "SIEM": {"learn_time": 2, "base_salary": 7, "bundle": ["Security Monitoring", "Incident Response"], "roles": ["Security Analyst"]},
     "Salesforce": {"learn_time": 2, "base_salary": 8, "bundle": ["CRM", "Apex"], "roles": ["CRM Developer"]},
     "System Design": {"learn_time": 3, "base_salary": 10, "bundle": ["Architecture", "Scalability"], "roles": ["Solutions Architect"]},
     "Tech Writing": {"learn_time": 1.5, "base_salary": 5, "bundle": ["Markdown", "Open Source"], "roles": ["Tech Evangelist"]},
     "TestNG": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Selenium", "JUnit"], "roles": ["Test Automation Engineer"]},
     "Ticketing Tools": {"learn_time": 1, "base_salary": 4, "bundle": ["Jira", "ServiceNow"], "roles": ["IT Support Specialist"]},
     "Troubleshooting": {"learn_time": 1.5, "base_salary": 5, "bundle": ["Windows Admin", "Network Basics"], "roles": ["Tech Support Engineer"]},
     "Unreal Engine": {"learn_time": 2.5, "base_salary": 7, "bundle": ["3D Modeling", "VR Development"], "roles": ["AR/VR Developer"]},
     "Visualization": {"learn_time": 1.5, "base_salary": 6, "bundle": ["Tableau", "Power BI"], "roles": ["BI Developer"]},
     "Visualforce": {"learn_time": 1.5, "base_salary": 7, "bundle": ["Salesforce", "Apex"], "roles": ["Salesforce Developer"]},
     "Windows Admin": {"learn_time": 1.5, "base_salary": 5, "bundle": ["Active Directory", "Troubleshooting"], "roles": ["IT Support Specialist"]},
     "Zapier": {"learn_time": 1, "base_salary": 4, "bundle": ["No-Code", "Automation"], "roles": ["No-Code Developer"]}

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