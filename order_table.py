import streamlit as st



def main(table_number:int):
    col1,col2,col3 = st.columns([2,1,2])
    placeholder = st.container()
    #placeholder_orders = st.expander('Lista Ordini')

    with placeholder:
        st.title('Table '+ str(table_number))
        back = st.button('Go back')
        if back:
            return -1
        with st.form("type"):
            # Every form must have a submit button.
            tipo = st.selectbox('How would you like to be contacted?',
                       ('Email', 'Home phone', 'Mobile phone'))
            submitted_t = st.form_submit_button("submit")
            if submitted_t:
                #with st.form("type"):
                    # Every form must have a submit button.
                    tipo = st.selectbox('2?',
                                        ('Email', 'Home phone', 'Mobile phone'))
                 #   submitted_a = st.form_submit_button("submit")
                    return 1
