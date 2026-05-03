# Copy-Cat Creater

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.44-red.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

**Copy-Cat Creater** is an intelligent web application designed for home cooks who want to recreate their favorite restaurant and fast-food dishes. By combining web scraping, nutritional data from the USDA, and AI-driven recipe generation, users can transform restaurant menu items into manageable home recipes tailored to their specific dietary needs.

---

## Environment Setup & Local Installation

### Prerequisites
* **Python 3.12+**
* **Azure OpenAI API Key** & Endpoint
* **USDA FoodData Central API Key**

### Installation
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/shoshanabernstein/copy-cat-creater.git](https://github.com/shoshanabernstein/copy-cat-creater.git)
   cd copy-cat-creater

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate