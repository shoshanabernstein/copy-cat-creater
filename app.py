import streamlit as st
from database import get_food_restaurant, filter_foods, get_categories_by_restaurant
import pandas as pd
import altair as alt

# from ai import recreate_recipe_ai_bot

def sidebar():
    with st.sidebar:
        st.header("🔍Search")

        # Choose restaurant radio button
        chosen_restaurant = st.radio("Pick A Restaurant", get_food_restaurant())

        # Choose calorie button
        chosen_calories = st.slider("Calories", 0, 800, 300, step=50)

        # Choose categores dropdown
        chosen_category = st.selectbox("Category", get_categories_by_restaurant(chosen_restaurant))


        filtered_foods = filter_foods(chosen_restaurant, chosen_calories, chosen_category)

    if not filtered_foods:
        st.warning("⚠️ No results found...",)

        
    return filtered_foods

def chart(filtered_foods):
    chart_data = []
    for food in filtered_foods:
        chart_data.append(
            {"Name": food['food_name'], "Calories": food['food_calories'], 
                "Type": food['food_category']})
    df = pd.DataFrame(chart_data)
    top_30_df = df.sort_values('Calories', ascending=False).head(30)
    st.area_chart(top_30_df, x='Name', x_label="Food Item Name", 
                  y='Calories', y_label="Calories in Food", 
                  color='Type', height='stretch', width='stretch')
    st.line_chart(top_30_df, x='Type', y='Calories')

def food_card(food):
    with st.expander(food['food_name']):
        
        st.header(food['food_name'])
        badge(food['food_calories'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(food['food_category'])
            st.image(food['food_logo'], width='content')

        with col2:
            st.link_button("Nutrition Info", food['food_link'])

        with col3:
            col3.metric(":bolt: **Calories**", food['food_calories'])

        
            #st.write(recreate_recipe_ai_bot(food))

def food_card_grid(filtered_foods):
    cols_per_rows = 4
    for i in range(0, len(filtered_foods), cols_per_rows):
        cols = st.columns(cols_per_rows)

        for col, food in zip(cols, filtered_foods[i:i+cols_per_rows]):
            with col:
                food_card(food)


def tab_card(filtered_foods):
    tab1, tab2,  = st.tabs(["📋 Menu", " 📈 Chart"])


    with tab1:
        ...
    with tab2:
        st.header("_Restaraunt_ :red[Charts]")
        with st.popover("Restaraunts"):
            restaurant_select_box = st.selectbox("Choose a Restaraunt:", options=get_food_restaurant())
            filter_food_by_restaurant = filter_foods(restaurant=restaurant_select_box)
        chart(filter_food_by_restaurant)

def badge(food_calories):
    if food_calories > 1000:
        return st.info("Very High Calorie") 
    elif food_calories > 750:
        return st.warning("High Calorie")
    elif food_calories > 300:
        return st.success("Medium Calorie")
    else:
        return st.success("Low Calorie")


