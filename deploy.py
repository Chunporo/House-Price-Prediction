import streamlit as st 
import pickle 

with open('rf_model.h5','rb') as f:
    saved_model = pickle.load(f)

st.header("House Price Prediction",divider = 'rainbow')    
LotArea = st.number_input("Insert lot size in square feet", value=0)
YearBuilt = st.number_input("Insert original construction date",value = 0)
a1stFlrSF = st.number_input("Insert first floor square feet", value = 0)
a2ndFlrSF = st.number_input("Insert second floor square feet", value = 0)
FullBath = st.number_input("Insert full bathrooms above grade", value = 0)
BedroomAbvGr = st.number_input("Insert bedrooms above grade ", value = 0)
TotRmsAbvGrd = st.number_input("Insert total rooms above grade",value = 0)


features = [LotArea,YearBuilt,a1stFlrSF,a2ndFlrSF,FullBath,BedroomAbvGr,TotRmsAbvGrd]
if st.button('Predict',type="primary"):
    st.write('Price',saved_model.predict([features])[0],'USD')