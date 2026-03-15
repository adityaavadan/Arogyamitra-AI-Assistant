import streamlit as st
import google.generativeai as genai

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="ArogyaMitra AI",
    page_icon="💊",
    layout="wide"
)

# ------------------------------
# CUSTOM CSS
# ------------------------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#e3f2fd,#ffffff);
}

h1,h2,h3,h4,h5,h6,p,label,div{
color:#000000 !important;
}

/* WHITE STRIP HEADER */

.header-strip{
background:white;
padding:30px;
border-radius:10px;
text-align:center;
margin-bottom:15px;
box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}

.header-title{
font-size:50px;
font-weight:900;
color:#0b5394;
}

/* BUTTON STYLE */

.stButton>button{
background:linear-gradient(90deg,#2E86C1,#48C9B0);
color:white;
border-radius:10px;
padding:10px 25px;
border:none;
font-size:16px;
}

.stButton>button:hover{
background:linear-gradient(90deg,#1B4F72,#17A589);
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR
# ------------------------------
with st.sidebar:

    st.title("ℹ️ About Us")

    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966485.png")

    st.write("""
    **ArogyaMitra AI** is an AI health assistant.

    ✔ Ask health questions  
    ✔ Check BMI  
    ✔ Generate diet plans  
    ✔ Get workout plans  

    ⚠️ This AI gives general health suggestions only.
    """)

# ------------------------------
# GEMINI API
# ------------------------------
genai.configure(api_key="AIzaSyCFxED8TxNJeZeRULctuhr07dcmyaO_bM0")

model = genai.GenerativeModel("models/gemini-3.1-flash-lite-preview")

# ------------------------------
# WHITE STRIP HEADING
# ------------------------------
st.markdown(
"""
<div class="header-strip">
<div class="header-title">ArogyaMitra AI Assistant</div>
</div>
""",
unsafe_allow_html=True
)

# ------------------------------
# BANNER IMAGE
# ------------------------------
st.image(
"https://images.unsplash.com/photo-1576091160550-2173dba999ef",
use_container_width=True
)

# ------------------------------
# TABS
# ------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
"🤖 AI Doctor Chat",
"⚖️ BMI Health Check",
"🥗 Smart Diet Planner",
"💪 Fitness Workout"
])

# ------------------------------
# TAB 1 CHATBOT
# ------------------------------
with tab1:

    st.header("💬 Ask Health Questions")

    user_input = st.text_input("Ask anything about health")

    if user_input:

        prompt = f"You are a helpful health assistant. Answer clearly: {user_input}"

        response = model.generate_content(prompt)

        st.success(response.text)

# ------------------------------
# TAB 2 BMI
# ------------------------------
with tab2:

    st.header("⚖️ BMI Calculator")

    weight = st.number_input("Enter Weight (kg)")
    height = st.number_input("Enter Height (meters)")

    if height > 0:

        bmi = weight / (height ** 2)

        if st.button("Calculate BMI"):

            st.write("Your BMI:", round(bmi,2))

            if bmi < 18.5:
                st.warning("Underweight")
            elif bmi < 25:
                st.success("Normal Weight")
            elif bmi < 30:
                st.warning("Overweight")
            else:
                st.error("Obese")

# ------------------------------
# TAB 3 DIET PLAN
# ------------------------------
with tab3:

    st.header("🥗 AI Diet Plan Generator")

    goal = st.selectbox(
        "Select your goal",
        ["Weight Loss","Weight Gain","Maintain Fitness"]
    )

    if st.button("Generate Diet Plan"):

        prompt = f"Give a simple healthy diet plan for {goal}"

        response = model.generate_content(prompt)

        st.write(response.text)

# ------------------------------
# TAB 4 WORKOUT
# ------------------------------
with tab4:

    st.header("💪 AI Workout Plan")

    fitness_level = st.selectbox(
        "Select your fitness level",
        ["Beginner","Intermediate","Advanced"]
    )

    if st.button("Generate Workout"):

        prompt = f"Create a weekly workout plan for {fitness_level} level"

        response = model.generate_content(prompt)

        st.write(response.text)

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("---")
st.write("Made with ❤️ using Streamlit + Gemini AI")