import streamlit as st
st.title("language picker")
st.subheader("ur fav language")
st.text("think about ur fav language")
st.write("did u get it")
lang=st.selectbox("select one ",['python','java','css'])
st.write(f"your {lang} is the best choice")
if st.button("open lang"):
    st.success("all the best")
st.radio("select one ",['python','java','css'])
st.slider("how much do you know about lang",1,2,3)
st.number_input("enter how many joins this tutorial",max_value=10,min_value=1,step=1)
dob=st.date_input("enter ur dob")
if dob:
    st.write("ur dob")