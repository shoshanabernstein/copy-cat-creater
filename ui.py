import app
import streamlit as st

st.set_page_config(
        page_title="Copy-Cat Creater",
        page_icon="🍟",
        layout="wide",
    )

st.title("_Copy-Cat_ :red[Creater]", text_alignment="center")
filtered_foods = app.sidebar()
# st.markdown("### Quick Guide")
# st.markdown("""
# 1. **Bold** your headers for clarity.
# 2. Use :orange[color] to highlight **key variables**.
# 3. Use :red-background[**Critical Errors**] for things that need immediate attention.
# 4. Try the :rainbow[Rainbow Effect] for fun titles!
# """)
app.tab_card(filtered_foods)

for food in filtered_foods:
    app.food_card(food)



