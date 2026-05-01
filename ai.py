# import streamlit as st
# from openai import OpenAI

# openai_api_key = st.secrets["OPENAI_API_KEY"]
# openai_api_endpoint = st.secrets["END_POINT"]

# client = OpenAI(
#     api_key=openai_api_key,
#     azure_endpoint=openai_api_endpoint
# )


# def recreate_recipe_ai_bot(food):
#     prompt = f"""
#     Recreate a copycat recipe for 
#     {food['food_name']} from {food['food_restaurant']}. 
    
#     List the ingredients and provide step-by-step instructions.
#     """
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.7
#     )

#     return response.choices[0].message.content