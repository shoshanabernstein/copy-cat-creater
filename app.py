"""Main app for the Copy-Cat Creater."""
import streamlit as st
from database import get_food_restaurant, filter_foods, get_categories_by_restaurant
import pandas as pd
import altair as alt
from ai import recreate_recipe_ai_bot

# Sidebar for filtering food items
def sidebar():
    """Sidebar for filtering food items."""
    with st.sidebar:
        st.header(":material/search: Search")

        # Choose restaurant radio button
        chosen_restaurant = st.radio(":material/restaurant: Pick A Restaurant", get_food_restaurant())

        # Choose calorie button
        chosen_calories = st.slider(":material/bolt: Calories", 0, 800, 300, step=50)

        # Choose categores dropdown
        chosen_category = st.selectbox(":material/fastfood: Category", get_categories_by_restaurant(chosen_restaurant))


        filtered_foods = filter_foods(chosen_restaurant, chosen_calories, chosen_category)

    if not filtered_foods:
        st.warning(":material/error: No results found...",)

        
    return filtered_foods

# Function to create the chart for the food items
def chart(filtered_foods):
    """Create a chart for the food items."""
    chart_data = []
    # Create a dataframe for the chart
    for food in filtered_foods:
        chart_data.append(
            {"Name": food['food_name'], "Calories": food['food_calories'], 
                "Type": food['food_category']})
    # df is used to create the chart, sorted by calories and only showing the top 30 items
    df = pd.DataFrame(chart_data)
    top_30_df = df.sort_values('Calories', ascending=False).head(30)
    st.area_chart(top_30_df, x='Name', x_label="Food Item Name", 
                  y='Calories', y_label="Calories in Food", 
                  color='Type', height='stretch', width='stretch')
    # line_chart is used to create a line chart, sorted by calories and only showing the top 30 items
    st.line_chart(top_30_df, x='Type', y='Calories')

# Function to create a card for each food item
def food_card(food):
    """Function to create a card for each food item"""
    with st.popover(f":material/fork_spoon: {food['food_name']}", use_container_width=True):
        header_col, logo_col = st.columns([4, 1])
        with header_col:
            st.title(food['food_name'])
            st.caption(f"{food['food_restaurant']} | {food['food_category']}")
        with logo_col:
            st.image(food['food_logo'], width=60)
        
        st.divider()

        # Display calories and link to nutrition information
        col1, col2 = st.columns(2)
        col1.metric(":material/bolt: Calories", food['food_calories'])
        col2.link_button("View Nutrition", food['food_link'], use_container_width=True, icon=":material/nutrition:")
        
        food_image_url = food['food_image']

        if food_image_url:
            st.image(food['food_image'], use_container_width=True, caption="Menu Item")
        else:
            st.image("https://worldfoodtour.co.uk/wp-content/uploads/2013/06/neptune-placeholder-48.jpg", caption="No Image Available")
        
        st.divider()
        
        # Button to generate the recipe using Azure OpenAI
        if st.button(f"Generate {food['food_name']} Recipe", type="primary", use_container_width=True):
            with st.spinner("Analyzing Ingredients..."):
                recipe = recreate_recipe_ai_bot(food)
                st.markdown(recipe)

# Function to create a grid of food cards
def food_card_grid(filtered_foods):
    """Function to create a grid of food cards."""
    cols = st.columns(3)

    # Loop through the filtered food items and create a card for each item
    for index, food in enumerate(filtered_foods):
        with cols[index % 3]:
            with st.container(border=True):
                food_card(food)

# Function to create tabs for the menu and chart    
def tab_card(filtered_foods):
    tab1, tab2,  = st.tabs([":material/menu_open: Menu", ":material/bar_chart_4_bars:  Chart"])


    with tab1:
        food_card_grid(filtered_foods)
    with tab2:
        st.header("_Restaraunt_ :red[Charts]")
        with st.popover("Restaraunts"):
            restaurant_select_box = st.selectbox("Choose a Restaraunt:", options=get_food_restaurant())
            filter_food_by_restaurant = filter_foods(restaurant=restaurant_select_box)
        chart(filter_food_by_restaurant)

# Function to create a badge for the calorie count
def badge(food_calories):
    if food_calories > 1000:
        return st.info("Very High Calorie") 
    elif food_calories > 750:
        return st.warning("High Calorie")
    elif food_calories > 300:
        return st.success("Medium Calorie")
    else:
        return st.success("Low Calorie")


