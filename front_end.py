import streamlit as st
import pandas as pd

raw_data = st.beta_container()
confirmed = st.beta_container()
recovered = st.beta_container()
deceased = st.beta_container()

with raw_data:
    st.title("Daily State-Wise Data")
    st.text("We update this data on a daily basis with help of API provided by https://www.covid19india.org")

    data_r = pd.read_csv("state_wise_daily.csv")
    st.write(data_r)

    selected_state = st.selectbox("Choose the state whose data you want to see", options=['Delhi (DL)',
                                                                                          'Andaman and Nicobar Islands (AN)',
                                                                                          'Andhra Pradesh (AP)',
                                                                                          'Arunachal Pradesh (AR)',
                                                                                          'Assam (AS)',
                                                                                          'Bihar (BR)',
                                                                                          'Chandigarh (CH)',
                                                                                          'Chhattisgarh (CT)',
                                                                                          'Dadra and Nagar Haveli and Daman and Diu (DN)',
                                                                                          'Goa (GA)',
                                                                                          'Gujrat (GJ)',
                                                                                          'Haryana (HR)',
                                                                                          'Himachal Pradesh (HP)',
                                                                                          'Jammu and Kashmir (JK)',
                                                                                          'Jharkhand (JH)',
                                                                                          'Karnataka (KA)',
                                                                                          'Kerela (KL)',
                                                                                          'Ladakh (LA)',
                                                                                          'Lakshadweep (LD)',
                                                                                          'Madhya Pradesh (MP)',
                                                                                          'Maharashtra (MH)',
                                                                                          'Manipur (MN)',
                                                                                          'Meghalaya (ML)',
                                                                                          'Mizoram (MZ)',
                                                                                          'Nagaland (NL)',
                                                                                          'Odisha (OR)',
                                                                                          'Puducherry (PY)',
                                                                                          'Punjab (PB)',
                                                                                          'Rajasthan (RJ)',
                                                                                          'Sikkim (SK)',
                                                                                          'State Unassigned (UN)',
                                                                                          'Tamil Nadu (TN)',
                                                                                          'Telangana (TG)',
                                                                                          'Tripura (TR)',
                                                                                          'Uttar Pradesh (UP)',
                                                                                          'Uttarakhand (UK)',
                                                                                          'West Bengal (WB)'], index=0)
    state = selected_state[-3:-1]

with confirmed:
    st.title("Confirmed Patients")
    st.text("The daily trends of confirmed COVID-19 patients in the state")

    lis_col1, graph_col1 = st.beta_columns(2)
    data1 = pd.read_excel("confirmed.xlsx")
    lis_col1.write(data1[['Date',state]])

with recovered:
    st.title("Recovered Patients")
    st.text("The daily trends of patients recovered from COVID-19 in the state")

    lis_col2, graph_col2 = st.beta_columns(2)
    data2 = pd.read_excel("recovered.xlsx")
    lis_col2.write(data2[['Date',state]])

with deceased:
    st.title("Deceased Patients")
    st.text("The daily trends of deceased patients of COVID-19 in the state")

    lis_col3, graph_col3 = st.beta_columns(2)
    data3 = pd.read_excel("deceased.xlsx")
    lis_col3.write(data3[['Date',state]])
