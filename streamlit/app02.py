import streamlit as st

h = st.header('My Web Site')
b = st.subheader('เว็บไซต์ของฉัน')
p = st.write('zzZ')
banner = st.image('https://images.unsplash.com/photo-1485617359743-4dc5d2e53c89?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
b = st.button('Click Me')
text = st.text_input('prompt:')
if text:
    st.image('https://images.unsplash.com/photo-1584921467611-9ca705c13ac6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
    b = st.button('จะไปนอนแล้ว')