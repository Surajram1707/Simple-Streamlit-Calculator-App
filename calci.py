import streamlit as st


st.set_page_config(page_title='CALCULATOR APP', layout = 'centered', initial_sidebar_state = 'auto')
st.title("Calculator")

num1 = st.text_input("Enter the first number","0")
num2 = st.text_input("Enter the second number","0")

oper = st.selectbox("Select an operation",["Select","Addition","Subtraction","Multiplication","Division","Modulo","Power"])

button = st.button("Perform Operation")

if button:
    if oper == "Addition":
        res = int(num1)+int(num2)
        st.success(f"Result of Addition is {res}")
    elif oper == "Subtraction":
        res = int(num1)-int(num2)
        st.success(f"Result of Subtraction is {res}")
    elif oper =="Multiplication":
        res = int(num1)*int(num2)
        st.success(f"Result of Multiplication is {res}")
    elif oper=="Division":
        res = int(num1)/int(num2)
        st.success(f"Result  of Division is {res}")
    elif oper=="Modulo":
        res = int(num1)%int(num2)
        st.success(f"Result of Modulo is {res}")
    elif oper == "Power":
        res = int(num1)**int(num2)
        st.success(f"Result of Power is {res}")
    else:
        st.error("Please Select an Operation")
