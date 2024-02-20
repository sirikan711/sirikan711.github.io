import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP

h = st.header('Diffuser.ai')
b = st.subheader('เว็บไซต์สำหรับแปลงข้อความเป็นภาพ')
p = st.write('เว็บไซต์แลกมาด้วยอาการปวดหลังและแบตเสื่อม')
text = st.text_input('prompt:')

if text:
    dp = DP.from_pretrained('runwayml/stable-diffusion-v1-5',
                            torch_dtype=torch.float16)
    image_data = dp(text).images[0]
    image = Image.fromarray(image_data)
    st.image(image)
    st.image('https://images.unsplash.com/photo-1485617359743-4dc5d2e53c89?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
    b = st.button('จะไปนอน')