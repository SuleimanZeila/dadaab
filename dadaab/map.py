import pandas as pd
import streamlit as st

st.set_page_config(page_title='Dadaab Voters',page_icon="chart_with_upwards_trend")
@st.cache
def dadaab():

	df = pd.read_excel('dertu.xlsx')
	return df

df = dadaab()
#MainMenu {visibility: hidden;}

st.title('Check your Polling Station')
st.subheader('This Application works for Dadaab Registered Voters Only')
with st.form("my_form",clear_on_submit = True):
	col1, col2 ,col3 = st.columns(3)
	lastname = col1.text_input('Please Enter Your Last Name')
	lastname = lastname.upper()
	yob = col2.text_input('Please Enter Your Year of Birth')
	
	sex = col3.selectbox('Select your Gender',['M','F'])


	submitted = st.form_submit_button("Submit")

	if submitted:

		st.write('Your Details Are:')
		df = df[['Identity document type and number','Last Name','First and Middle Name','Date of Birth','Sex','Electoral Number','polling']]

		df = df.loc[(df['Last Name'] == lastname)  ,['Identity document type and number','Last Name','First and Middle Name','Date of Birth','Sex','Electoral Number','polling']]
		df = df.loc[(df['Sex'] == sex)  ,['Identity document type and number','Last Name','First and Middle Name','Date of Birth','Sex','Electoral Number','polling']]

		df = df.loc[(df['Date of Birth'].astype(str) == yob)  ,['Identity document type and number','Last Name','First and Middle Name','Date of Birth','Sex','polling','Electoral Number']]
		st.write(df)
footer="""<style>

footer {visibility: hidden;}
"""
st.markdown(footer,unsafe_allow_html=True)