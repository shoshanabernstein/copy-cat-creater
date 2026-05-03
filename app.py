"""Main app for the Copy-Cat Creater."""
import streamlit as st
from database import get_food_restaurant, filter_foods, get_categories_by_restaurant
import pandas as pd
from api import get_simplified_nutrition, get_nutrition_data, api_food_nutrition
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
    st.space(size='medium')
    st.line_chart(top_30_df, x='Type', y='Calories')

# Function to create a card for each food item
def food_card(food):
    """Function to create a card for each food item"""
    with st.popover(f":material/fork_spoon: {food['food_name']}", width='content', type='tertiary'):
        with st.container(width=700):
            header_col, logo_col = st.columns([3, 1])
            with logo_col:
                st.image(food['food_logo'], width=60, use_container_width=True)  
                st.link_button("View Nutrition", food['food_link'], use_container_width=True, icon=":material/nutrition:", type='primary')

            with header_col:
                st.title(food['food_name'])
                st.caption(f"{food['food_restaurant']} | {food['food_category']}")      
                st.badge(f"Calories {food['food_calories']}", width='content', color='gray', icon=f":material/bolt: ")

                col1, col2 = st.columns([2, 3])
                with col1:
                    st.space()
                    # Context for ai generation
                    context = st.text_input("Specifications (optional)", key=f"spec_{food['food_id']}")
                    st.space()
                    # Button to generate the recipe using Azure OpenAI
                    if st.button(f"Generate {food['food_name']} Recipe", type="primary", use_container_width=True):
                        with st.spinner("Analyzing Ingredients..."):
                            recipe = recreate_recipe_ai_bot(food, context)
                            st.space()
                            with st.popover(f"{food['food_name']} Recipe"):
                                st.markdown(recipe)
                with col2:
                    food_image_url = food['food_image']
                    if food_image_url:
                        st.image(food['food_image'], use_container_width=True, caption=f"{food['food_name']}", width=50)
                    else:
                        st.image("https://worldfoodtour.co.uk/wp-content/uploads/2013/06/neptune-placeholder-48.jpg", caption="No Image Available")

# Function to create a grid of food cards
def food_card_grid(filtered_foods):
    """Function to create a grid of food cards."""
    cols = st.columns(3, gap="large", width="stretch")

    # Loop through the filtered food items and create a card for each item
    for index, food in enumerate(filtered_foods):
        with cols[index % 3]:
            with st.container(border=True):
                food_card(food)

# Function to get and display food nutrition
def food_nutrition(food_input):
    if st.button(f"Get Official USDA Nutrition for {food_input.title()}", type="primary", key=f"btn_{food_input}"):
        with st.spinner("Fetching..."):
            api_data = api_food_nutrition(food_input)
            nutrition_info = get_simplified_nutrition(api_data)

            if isinstance(nutrition_info, dict):
                with st.container(border=True):
                    st.success(f":material/check_circle: Found {nutrition_info['name'].title()}")
                    st.subheader(nutrition_info['name'].title())
                    st.caption("Values per **100g**")
                    
                    col1, col2 = st.columns(2)
                    col1.metric("Calories", f"{int(nutrition_info['Calories'])} kcal")
                    col2.metric("Protein", f" {nutrition_info['Protein']}g")
                    col1.metric("Fat", f"{nutrition_info['Fat']}g")
                    col2.metric("Carbs", f"{nutrition_info['Carbs']}g")

            else:
                st.warning(":material/warning: Could not find official data for this item.")


# Function to create tabs for the menu and chart    
def tab_card(filtered_foods):
    tab1, tab2, tab3 = st.tabs([":material/menu_open: Menu", ":material/bar_chart_4_bars:  Chart", ":material/fork_chart: Food Facts"])
    with tab1:
        
        if filtered_foods:
            st.header(f"_{filtered_foods[0]['food_restaurant']}_ :red[Menu]")
            food_card_grid(filtered_foods)      
        if not filtered_foods:
            st.warning(":material/error: No results found...",)
    with tab2:
        restaurant_segmented_control = st.segmented_control("Choose a Restaraunt:", options=get_food_restaurant(), default="McDonald's")
        st.header(f"_{restaurant_segmented_control}_ :red[Charts]")
        filter_food_by_restaurant = filter_foods(restaurant=restaurant_segmented_control)
        chart(filter_food_by_restaurant)
    with tab3:
        st.header(f"_Compare_ :red[Foods]")
        col1, col2 = st.columns(2)
        with col1:
            food_input_one = st.text_input("Enter food one:", "Ice Cream")
            food_nutrition(food_input_one)
        with col2:
            food_input_two = st.text_input("Enter food two:", "Apple")
            food_nutrition(food_input_two)

    
