# Stremlit

import streamlit as st 

st.set_page_config(page_title="growth mindset projects", page_icon="⭐")
st.title("Growth Maindet Ai Projects: Web App And Streamlit")

st.header("Welcome To your Growth Mindset Journey ⭐")
st.write("Embrance Chellenge,learn from mistakes, and unlock your full potentail. This is Ai power app helps to build growth mindset with reflection,chellenges,and achievement")

# Qoute section 
st.header("Today Growth's Mindset Challenge Quote")
st.write("Success is not final.failure is not fatel it is the courage to continue thats counts windows churchill")


# User inter face
st.header(" What's Your challange today?")
user_input = st.text_input("Describe the challenge you're facing")

# Conditions
if user_input:
    st.seccess(f"you re facing:{user_input}. keep pusing forward towards your goals!")
    
else:
    st.warning("Tell us about your challenge to get started!")


# Reflexcing

st.header("Reflect to your learning")
reflection = st.text_area("Write your reflections here: ")

if reflection:
   st.success(f"Great Insight: Your Reflection: {reflection}")
   
else:
   st.info("Reflecting on past experince help your grow:share your difficulties ")


# Achivements
st.header("Celebrate Your Wins !")
achivement = st.text_input("Share something you're recently accomplished :") 

if achivement:
    st.success(f"🌟 Amazing you achieve: {achivement}")

else:
    st.info("Big or small , every achivement counts ! share one now 😍 ")

# Footer 
st.write("---")
st.write("💡Growth begins the moment you believe you can improve")
st.write("Created By HASSAN KHAN")