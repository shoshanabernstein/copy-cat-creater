"""UI for the Copy-Cat Creater app."""
import app
import streamlit as st

st.set_page_config(
        page_title="Copy-Cat Creator",
        page_icon=":material/menu_book_2:",
        layout="wide",
        
    )

st.title("_Copy-Cat_ Recipe :red[Creator]", text_alignment="center")
filtered_foods = app.sidebar()

app.tab_card(filtered_foods)





