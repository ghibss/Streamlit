
import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_multipage import MultiPage
import order_table
import os

def Open(st, **state):
    st.title("Weelcome Maestro")
    st.write("Hai un APP Table Manager per le prenotazioni ed una per stampare il pdf")
def TableManager(st, **state):
    st.title("Table Manager App")
    with st.form("TableBook"):
        st.write("TableBook")
        d = st.date_input(
            "Giorno Pronotazione",
            datetime.date(2023, 2, 15))
        number = st.number_input('Numero Persone',step=1)
        name = st.text_input("Name: ")
        df_tables = pd.read_csv("data/"+f"{d}.csv").dropna()
        df_tables.index = df_tables['Table Id']
        table_free = df_tables[df_tables.State=='Free']

        #table_free = table_free[table_free['N Posti']>=number]
        table_id = st.multiselect('Select Table',table_free.index)
        submitted_B = st.form_submit_button("Book")

    if submitted_B:
        st.write("Here We GO")
        #st.write(table_id)
        for id in table_id:
            #st.write(df_tables.loc[id])
            df_tables.loc[id,'State'] = name
            df_tables.loc[id,'N_persone'] =  number/len(table_id)
            #st.write(df_tables.loc[id])
        with open("data/"+f"{d}.csv", "w", newline="") as f:
            df_tables.to_csv(f,index=False)
        f.close()

    with st.form("Book Delete"):
        st.write("Book Delete")
        d = st.date_input(
            "Giorno Pronotazione",
            datetime.date(2023, 2, 15))

        df_tables = pd.read_csv("data/"+f"{d}.csv").dropna()
        df_tables.index = df_tables['Table Id']
        table_free = df_tables[df_tables.State !='Free']
        table_id = st.multiselect('Select Table',table_free.index)
        submitted_D = st.form_submit_button("Book")

    if submitted_D:
        st.write("Here We GO")
        #st.write(table_id)
        for id in table_id:
            #st.write(df_tables.loc[id])
            df_tables.loc[id,'State'] = "Free"
            df_tables.loc[id,'N_persone'] = 0
            #st.write(df_tables.loc[id])
        with open("data/"+f"{d}.csv", "w", newline="") as f:
            df_tables.to_csv(f,index=False)
        f.close()





def PrintPdf(st, **state):
    st.title("Print Pdf App")
    st.write("Cose da Fare")
    with st.form("my_form"):
        d = st.date_input(
            "Giorno da Stampare",
            datetime.date(2023, 2, 15))
    #name = st.text_input("Your Name: ")
        submitted = st.form_submit_button("Print")
        if submitted:
            df_tables = pd.read_csv("data/"+f"{d}.csv").dropna()
            st.write(df_tables)

app = MultiPage()
app.st = st
tables = pd.read_csv("tables.csv",';')
tables = tables.dropna(axis=1)
#st.write(tables)
app.add_app("Open", Open)
app.add_app("OrderBook", TableManager)
app.add_app("PrintPdf", PrintPdf)


app.run()

