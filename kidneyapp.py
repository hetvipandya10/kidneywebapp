import streamlit as st

st.title("Welcome to kidney App")

age=st.slider("Select age=",6,83)
bp=st.slider("Select bp=",50,110)
sg=st.slider("Select sg=",1.005,1.025)
al=st.slider("Select al=",0,4)
su=st.slider("Select su=",0,5)
rbc=st.slider("Select rbc=",0,1)
pc=st.slider("Select Pc=",0,1)
pcc=st.slider("Select pcc=",0,1)
ba=st.slider("Select ba=",0,1)
bgr=st.slider("Select bgr=",70,490)
bu=st.slider("Select bu=",10.0,15.2)
sc=st.slider("Select sc=",0.4,15.2)
sod=st.slider("Select sod=",111,150)
pot=st.slider("Select pot=",2.5,47.0)
hemo=st.slider("Select hemo=",3.1,17.8)
pcv=st.slider("Select pcv=",9,54)
wc=st.slider("Select wc=",3800,26400)
rc=st.slider("Select rc=",2.1,8.0)
htn=st.slider("Select htn=",0,1)
dm=st.slider("Select dm=",0,1)
cad=st.slider("Select cad=",0,1)
appet=st.slider("Select appet=",0,1)
pe=st.slider("Select pe=",0,1)
ane=st.slider("Select ane=",0,1)

import pickle
model=pickle.load(open("kidney.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]])
    st.success("The kidney is "+ prd[0])

