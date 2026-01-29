import streamlit as st

st.header("b.shivaram ")

#title
st.title("welcome")

#subheader
st.subheader("login now")

#horizantal line
st.markdown("---------------------------------------------------------")

st.text(" this app is to allow u to make ")

st.write("Hello shivaram")
st.write(234)
#st.write(we can use dict also)

st.markdown("### ###")
st.markdown("**bold text**")
st.markdown("*italic one*")
st.markdown("- team1 \n- team2")

st.caption("shivaram this is caption")
st.code("""
def add(a,b):
        return a+b
        """, language="python")

# latex is used to display math functions

st.latex(r'''
a^2 + b^2 = c^2''')

#divider method is used to separate sessions
st.divider()

#button
if st.button("click done"):
    st.write("ur done!")
    st.balloons()
else:
    st.error("conn error!")
st.divider()

# input num
id = st.text_input("Name: " ) 
if st.button("done"):
    if id=="":
        st.warning("name cannot be empty")
    elif not id.isalpha() :
        st.error("invalid input")
    else:
        st.write(f"hello{id}")       
st.divider()
feedback=st.text_area("give feedback:")
st.divider()
if st.checkbox(" i agree "):
    st.write("thank u for agreeing")
st.divider()

gen = st.radio("Choose Operation", [" male", " female"," other", " Read"])
st.write(f"your choice :{gen}")
st.divider()
y=st.selectbox("select ur country:",("ind","aus","dub"))
st.write(f" u selected: { y}")
st.divider()
#slider method to create a slider
age = st.slider("select your age:", 0,100,25)
st.write(f"ur {age}")
st.divider()
#to upload file use "file_uploader()"

up= st.file_uploader("choose a flie")
if up is not None:
    st.success("file up success!")
    st.write(f"filename:")

st.divider()

#form method
with st.form("my_form"):
    name= st.text_input("Name: ")
    age=st.number_input("age:")
    submit=st.form_submit_button("submit")

if submit:
    st.balloons()
    st.write("ur done!")
st.divider()

with st.form("login_form"):
    id= st.text_input("username: ")
    password=st.text_input("pass:",type="password")
    login=st.form_submit_button("login")

if login:
    st.balloons()
    st.write("ur done!")   

st.divider()
#col method 

col1,col2,col3=st.columns(3)
with col1:
    st.subheader("col1")
    st.write("this is col1")    
with col2:
    st.subheader("col2")
    st.write("this is col2") 

with col3:
    st.subheader("col3")
    st.write("this is col3")         
st.divider()
    
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)    
st.divider()

st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
