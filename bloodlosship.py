# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:50:38 2024

@author: user
"""

import streamlit as st 
import pickle
import base64


def add_local_backgound_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
     
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url(data:files/
                                  {"jpg"};base64,{encoded_string.decode()});
        background-size: cover
            }}
        </style>
                """,
      unsafe_allow_html=True
                 )

add_local_backgound_image_('files/smsk.jpg')









filename = "modelbloodloss.pickle"
loaded_model = pickle.load(open(filename, "rb"))


st.markdown("<h1 style='text-align: center; color: black ; font-size: 25px ;'>Blood Loss Assessment by Samutsakhon Tool (BLAST)</h1>", unsafe_allow_html=True)


q1 = st.radio("**เพศ**", ["ชาย" , "หญิง"],  horizontal = True)
if q1 == "ชาย" :
    a = int(1)
else :
    a = int(0)
    
q2 = st.radio("**ผู้ป่วยเป็นโรคไตหรือไม่**" , ["ไม่เป็น" , "เป็น"],  horizontal = True)
if q2 == "ไม่เป็น" :
    b = int(0)
else :
    b = int(1)
    
q3 = st.radio("**ผู้ป่วยเป็นโรคหัวใจขาดเลือดหรือไม่**" , ["ไม่เป็น" , "เป็น"],  horizontal = True)
if q3 == "ไม่เป็น" :
    c = int(0)
else :
    c = int(1)
    
q4 = st.radio("**การผ่าตัดนี้ใส่ cementหรือไม่**" , ["ไม่ใส่" , "ใส่"],  horizontal = True)
if q4 == "ไม่ใส่" :
    d = int(0)
else :
    d = int(1)
    
    
st.markdown(

"""
ให้ท่านประเมิน ASA Clsss ของผู้ป่วย โดย
- ASA Class I หมายความว่า ผู้ป่วยแข็งแรงดีไม่มีโรคประจำตัว
- ASA Class II หมายความว่า ผู้ป่วยที่มีโรคประจำตัวอยู่ในระดับรุนแรงน้อยและควบคุมได้ดี
- ASA Class III หมายความว่า ผู้ป่วยมีโรคประจำตัวอยู่ในระดับปานกลางถึงรุนแรง ควบคุมได้ไม่ดี
- ASA Class IV หมายความว่า  ผู้ป่วยที่มีโรคประจำตัวที่มีอาการรุนแรง มีอัตราเสี่ยงต่อการเสียชีวิตสูง
- ASA Class V หมายความว่า ผู้ป่วยในระยะสุดท้ายที่มีโอกาสตายได้ภายใน 24 ชั่วโมง
ไม่ว่าจะได้รับการผ่าตัดหรือไม่
"""

)
    

q5 = st.radio("**ผู้ป่วยเป็น ASA Classใด**" , ["I" , "II", "III", "IV", "V"],  horizontal = True)
if q5 == "I" :
    e = int(1)
elif q5 == "II" :
    e = int(2)    
elif q5 == "III" :
    e = int(3) 
elif q5 == "IV" :
    e = int(4)
else :
    e = int(5)  
    

    
if st.button('**ประเมินความเสี่ยง**'):
    s=[a,b,c,d,e]
    array = loaded_model.predict([s])
    k=loaded_model.predict_proba([s]).round(2)
    if array[0] == 0: 
           st.write(f":green[ผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด ควรจองเลือดไม่เกิน 1 U ค่าความเชื่อมั่น {k[0][0]*100}%]")
    else:
           st.write(f":red[ผู้ป่วยมีความเสี่ยงที่จะเสียเลือด ควรจองเลือด 2 U ขึ้นไป ค่าความเชื่อมั่น {k[0][1]*100}%]")

           