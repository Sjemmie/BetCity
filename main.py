import streamlit as st
import maths

st.set_page_config('wide')
st.title("Reken is dan")

inzet = st.text_input("Wat is je totale inzet?", key='inzet')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write("Quote 1")
with col2:
    quote_1 = st.text_input(label="quote1", label_visibility='collapsed', placeholder='Voer quotering 1 in', key='quote1')
with col3:
    st.write("Bedrag 1")
with col4:
    input_1 = st.text_input(label='input1', label_visibility='collapsed', placeholder='Vul bedrag 1 in', key='input1')

col5, col6, col7, col8 = st.columns(4)
with col5:
     st.write("Quote 2")
with col6:
     quote_2 = st.text_input(label="quote2", label_visibility='collapsed', placeholder='Voer quotering 2 in', key='quote2')
with col7:
    st.write("Bedrag 2")
with col8:
    input_2 = st.text_input(label='input2', label_visibility='collapsed', placeholder='Vul bedrag 2 in', key='input2')

col9, col10, col11, col12 = st.columns(4)
with col9:
    st.write("Quote 3")
with col10:
    quote_3 = st.text_input(label="quote3", label_visibility='collapsed', placeholder='Voer quotering 3 in', key='quote3')
with col11:
    st.write("Bedrag 3")
with col12:
    input_3 = st.text_input(label='input3', label_visibility='collapsed', placeholder='Vul bedrag 3 in', key='input3')

st.markdown("##")
st.markdown("##")

try:
    col13, col14, col15, col16 = st.columns(4)
    with col13:
        st.write("Uitkomst 1")
    with col14:
        quote_1 = float(quote_1)
        input_1 = float(input_1)
        uitkomst_1 = maths.bedrag(quote_1, input_1)
        st.info(uitkomst_1)
    with col15:
        st.write("Je hebt over:")
    with col16:
        inzet = float(inzet)
        totaal_1 = inzet - input_1
        st.write(totaal_1)

    col17, col18, col19, col20 = st.columns(4)
    with col17:
        st.write("Uitkomst 2")
    with col18:
        quote_2 = float(quote_2)
        input_2 = float(input_2)
        uitkomst_2 = maths.bedrag(quote_2, input_2)
        st.info(uitkomst_2)
    with col19:
        st.write("Je hebt over:")
    with col20:
        totaal_2 = totaal_1 - input_2
        st.write(totaal_2)

    col21, col22, col23, col24 = st.columns(4)
    with col21:
        st.write("Uitkomst 3")
    with col22:
        quote_3 = float(quote_3)
        input_3 = float(input_3)
        uitkomst_3 = maths.bedrag(quote_3, input_3)
        st.info(uitkomst_3)
    with col23:
        st.write("Je hebt over:")
    with col24:
        totaal_3 = inzet - (input_1 + input_2 + input_3)
        st.write(totaal_3)
except ValueError:
    st.error("Vul getallen in")
