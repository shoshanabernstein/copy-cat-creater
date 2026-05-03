# 🍔 Copy-Cat Creater

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.44-red.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Overview

**Copy-Cat Creater** is an intelligent web application that helps users recreate their favorite restaurant and fast-food meals at home.

It combines:
- 🔍 Web scraping of restaurant menu data  
- 🥗 USDA FoodData Central nutritional information  
- 🤖 AI recipe generation  

The result is a smart system that transforms restaurant meals into customizable, home-cooked recipes tailored to dietary preferences.


## ✨ Features

- 🍔 Browse restaurant menus in a clean Streamlit interface  
- 📊 View detailed nutrition data (USDA API integration)  
- 🎚 Filter meals by calories and category  
- 🤖 Generate AI-powered copy-cat recipes  
- ✏️ Customize recipes (low calorie, ingredient removal, etc.)  
- 🧾 Structured output with step-by-step instructions and chef tips  

---

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/shoshanabernstein/copy-cat-creater.git
cd copy-cat-creater
```

### 2. Create Virtual Environment
Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔐 Configuration
Create a file:
```bash
.streamlit/secrets.toml
```
Add the following:
```bash
AZURE_OPENAI_API_KEY = "your_key_here"
AZURE_OPENAI_ENDPOINT = "your_endpoint_here"
```
### 🗄️ Database Setup
Before first run, initialize the database:
```bash
python load_database.py
```
### ▶️ Run the App
```bash 
streamlit run ui.py
```

### 🧭 How It Works
- Select a restaurant from the sidebar

- Filter menu items by category or calories

- Click a food card to view nutrition details

- Press "Recreate" to generate a copy-cat recipe

- Optionally customize dietary preferences

### 🤖 AI System
The AI module (ai.py) functions as a Culinary Chemist.

It:
- Applies user constraints (e.g. low calorie, allergen removal)

- Generates structured recipes including:

   - Ingredients

   - Cooking steps

   - Chef’s tips

### 🧪 Testing
Run tests

```python -m pytest```

Run with coverage

```pytest --cov=.```


### 📦 Tech Stack
- Streamlit — UI framework

- BeautifulSoup & Requests — Web scraping

- Azure OpenAI — AI recipe generation

- Pandas — Data processing

- SQLite — Local database

### ☁️ Deployment
This project is deployment-ready for:

- Streamlit Community Cloud

- GitHub Codespaces