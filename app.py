import pickle
import streamlit as st 


pickle_in = open("logr.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Personal Loan,Securities Account,CD Account,Online,CreditCard):
    prediction=logr.predict([[Age,Experience,Income,Family,CCAvg,Education,Mortgage,Personal Loan,Securities Account,CD Account,Online,CreditCard]])
    print(Personal Loan)
    return Personal Loan

def main():
    st.title("Personal Loan approval")
    Age = st.text_input("Age")
    Experience = st.text_input("Experience") 
    Income = st.text_input("Income")
    Family = st.text_input("Family")
    CCAvg= st.text_input("CCAvg")
    Education = st.text_input("Education")
    Mortgage = st.text_input("Mortgage")
    Personal Loan = st.text_input("Personal Loan")
    Securities Account = st.text_input("Securities Account")
    CD Account = st.text_input("CD Account")
    Online = st.text_input("Online")
    CreditCard = st.text_input("Personal Loan")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Personal Loan,Securities Account,CD                                                               Account,Online,CreditCard)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    
