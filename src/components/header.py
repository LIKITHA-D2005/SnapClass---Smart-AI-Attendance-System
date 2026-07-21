import streamlit as st


def header_home():

    logo_url = "https://img.freepik.com/premium-vector/student-pictogram_764382-145835.jpg?w=996"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:150px;' />
            <h1 style='text-align:center; color:#C5B3D3'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True) #allows html rendering


def header_dashboard():

    logo_url = "https://img.freepik.com/premium-vector/student-pictogram_764382-145835.jpg?w=996"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#C5B3D3'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)