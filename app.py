import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import random

# =============================
# Clairvoyra – Skill ROI Predictor
# =============================
# Load pre-trained model and supporting data
model = joblib.load("model.pkl")
df = pd.read_csv("clairvoyra_salary_data.csv")
model_features = joblib.load("clairvoyra_model_features.pkl")

# Skill info database (manually curated for demo)
skill_data = {
    "Python": {"time_to_learn": 3, "bundle": ["Pandas", "SQL", "Streamlit"]},
    "SQL": {"time_to_learn": 2, "bundle": ["Excel", "Power BI"]},
    "JavaScript": {"time_to_learn": 2, "bundle": ["React", "Node.js"]},
    "Java": {"time_to_learn": 3, "bundle": ["Spring", "Maven"]},
    "Power BI": {"time_to_learn": 1.5, "bundle": ["Excel", "DAX"]},
    "React": {"time_to_learn": 2.5, "bundle": ["JS", "Node.js"]},
    "AWS": {"time_to_learn": 3, "bundle": ["EC2", "Lambda"]},
    "Prompt Engineering": {"time_to_learn": 2, "bundle": ["LLMs", "LangChain"]},
    "Cybersecurity": {"time_to_learn": 3.5, "bundle": ["Networking", "Ethical Hacking"]}
}

career_quotes = [
    "The best way to predict your future is to create it. – Abraham Lincoln",
    "Your skills are your superpower. Use them wisely.",
    "Don't just work harder. Work smarter. Learn with purpose.",
    "Big careers are built on small skill choices.",
    "Every great journey starts with learning the right skill."
]

# =============================
# Streamlit App UI
# =============================
st.set_page_config(page_title="Clairvoyra – Skill ROI Predictor", layout="centered")
st.title("🔮 Clairvoyra")
st.subheader("✨ See your future. Learn smarter. Earn stronger.")

# Motivational Quote
st.markdown(f"**💬 Tip of the Day:** _{random.choice(career_quotes)}_")

# Sidebar Skill Selector
selected_skill = st.sidebar.selectbox("Select a tech skill:", list(skill_data.keys()))

# Prepare prediction
X_input = pd.DataFrame([[selected_skill]], columns=["skill"])
X_input_encoded = pd.get_dummies(X_input).reindex(columns=model_features, fill_value=0)
salary_class = model.predict(X_input_encoded)[0]

# ROI Calculation
learn_time = skill_data[selected_skill]['time_to_learn']
roi = round((int(salary_class.strip("₹L+").split("-")[-1]) if "-" in salary_class else int(salary_class.strip("₹L+"))) / learn_time, 2)

# UI Outputs
st.success(f"💰 Predicted Salary Range: {salary_class} LPA")
st.info(f"⏱️ Estimated Learning Time for {selected_skill}: {learn_time} months")
st.metric("📈 ROI Score (Salary ÷ Time to Learn)", f"{roi}")

st.markdown("---")
st.markdown(f"### 💼 Recommended Skill Bundle for {selected_skill}:")
st.markdown(", ".join([f"`{s}`" for s in skill_data[selected_skill]['bundle']]))

# Visualization
st.markdown("---")
st.subheader("📊 Average Salary by Skill")
fig = px.bar(df.sort_values(by="average_salary", ascending=False), x="skill", y="average_salary", color="average_salary", title="Skill vs Average Salary")
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Clairvoyra — built for freshers and professionals to forecast the value of learning before you invest.")
