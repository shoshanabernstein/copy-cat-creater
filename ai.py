"""AI functions for the app."""
import streamlit as st
from openai import AzureOpenAI

openai_api_key = st.secrets["AZURE_OPENAI_API_KEY"]
openai_api_endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]

client = AzureOpenAI(
    api_key=openai_api_key,
    api_version="2024-02-15-preview",
    azure_endpoint=openai_api_endpoint
)

# Function to recreate a copycat recipe using Azure OpenAI
def recreate_recipe_ai_bot(food):
    prompt = f"""
    You are an expert culinary chemist specializing in restaurant "copy-cat" recreations. 
    Your goal is to provide a home-cook recipe for the {food['food_name']} from {food['food_restaurant']}.

    CRITICAL INSTRUCTIONS:
    1. Category: This item is a {food['food_category']}. Ensure the texture and cooking method match this category.
    2. Authenticity: Identify the "secret" seasonings or specific brands (e.g., "Hidden Valley Ranch" or "Old Bay") that define this restaurant's flavor profile.
    3. Formatting: 
   - Use ### Headings for 'Ingredients' and 'Instructions'.
   - Use bold text for key techniques (e.g., **flash-fry**, **marinate for 2 hours**).
   - Include a "Chef's Secret" note at the end explaining one specific trick to make it taste exactly like the original.

    Provide the recipe now:
    """
    response = client.chat.completions.create(
        model=st.secrets["AZURE_OPENAI_MODEL"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content