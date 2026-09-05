import streamlit as st

# 1. Page Configuration and Theme Setting
st.set_page_config(
    page_title="Chemistry on Loop", 
    page_icon="🧪", 
    layout="centered"
)

# Customizing the UI look using basic Streamlit markdown headers
st.title("🌱 Chemistry on Loop")
st.markdown("### *Accessible Cosmetology & Toxicology Data for Everyone*")
st.write("---")

# 2. Comprehensive 15-Ingredient Toxicology Database
# Organized into: Safe, Irritant, and Avoid
ingredient_db = {
    "niacinamide": {
        "rating": "🟢 Safe",
        "category": "Vitamin / Antioxidant",
        "explanation": "Also known as Vitamin B3, it strengthens the skin barrier and fades dark spots. It is highly stable, non-toxic, and incredibly safe for all skin types."
    },
    "hyaluronic acid": {
        "rating": "🟢 Safe",
        "category": "Humectant",
        "explanation": "A naturally occurring molecule in human skin that binds water to keep cells hydrated. It poses zero toxicological risk and is safe for daily topical use."
    },
    "glycerin": {
        "rating": "🟢 Safe",
        "category": "Humectant",
        "explanation": "A simple, plant-derived compound used widely to pull moisture into the skin. It has a long history of safe use and is entirely non-irritating."
    },
    "titanium dioxide": {
        "rating": "🟢 Safe",
        "category": "Mineral Sunscreen",
        "explanation": "A natural mineral used to shield skin from UV rays. Unlike chemical sunscreens, it acts as a physical barrier and is not absorbed deep into the bloodstream, making it highly safe."
    },
    "ceramides": {
        "rating": "🟢 Safe",
        "category": "Skin-Identical Lipids",
        "explanation": "Fatty acids that naturally form the protective layer of your skin. They restore the skin barrier and have absolutely no known side effects or toxic properties."
    },
    "fragrance": {
        "rating": "🟡 Irritant",
        "category": "Scent Masking",
        "explanation": "A generic term on labels that can hide hundreds of synthetic chemicals. It is a leading cause of allergic contact dermatitis, redness, and micro-inflammation."
    },
    "salicylic acid": {
        "rating": "🟡 Irritant (Use with Care)",
        "category": "Beta Hydroxy Acid (BHA)",
        "explanation": "Highly effective at clearing pores and treating acne. However, in concentrations above 2% or when overused, it can strip skin lipids, leading to chemical dryness."
    },
    "alcohol denat": {
        "rating": "🟡 Irritant",
        "category": "Solvent / Extractor",
        "explanation": "Used to make skincare products feel lightweight and dry quickly. Regular use breaks down the natural skin barrier, leading to dehydration and localized irritation."
    },
    "sodium lauryl sulfate": {
        "rating": "🟡 Irritant",
        "category": "Surfactant (Foaming Agent)",
        "explanation": "Commonly found in cleansers to create heavy lather. It strips the natural oils from the outer layer of skin, frequently triggering redness and eczema flare-ups."
    },
    "essential oils": {
        "rating": "🟡 Irritant",
        "category": "Natural Plant Extracts",
        "explanation": "Highly concentrated plant extracts like lavender or tea tree oil. While natural, they contain complex volatile compounds that frequently cause contact allergies when exposed to air."
    },
    "parabens": {
        "rating": "🔴 Avoid",
        "category": "Synthetic Preservative",
        "explanation": "Used to prolong product shelf-life. Toxicological studies show they can mimic estrogen in the body and disrupt the endocrine system, with traces often found in tissue biopsies."
    },
    "formaldehyde releasers": {
        "rating": "🔴 Avoid",
        "category": "Preservative",
        "explanation": "Chemicals (like DMDM Hydantoin) that slowly release formaldehyde to kill bacteria. Formaldehyde is a known human carcinogen and an aggressive skin allergen."
    },
    "oxybenzone": {
        "rating": "🔴 Avoid",
        "category": "Chemical Sunscreen Filter",
        "explanation": "A chemical UV filter that is rapidly absorbed through the skin. It acts as a significant hormone disruptor and is heavily restricted globally due to aquatic and human toxicity data."
    },
    "phthalates": {
        "rating": "🔴 Avoid",
        "category": "Plasticizer / Solvent",
        "explanation": "Often hidden under the word 'fragrance' to make scents last longer. They are heavily linked to developmental toxicological impacts and severe reproductive system disruptions."
    },
    "triclosan": {
        "rating": "🔴 Avoid",
        "category": "Antibacterial Agent",
        "explanation": "An antimicrobial chemical often used in soaps and toothpastes. It accumulates in fatty tissues, disrupts thyroid hormone pathways, and contributes to antibiotic-resistant superbugs."
    }
}

# 3. Interactive Sidebar for Quick Filtering
st.sidebar.header("Filter by Safety Level")
filter_choice = st.sidebar.selectbox(
    "Show ingredients that are:",
    ["All Ingredients", "🟢 Safe", "🟡 Irritant", "🔴 Avoid"]
)

# 4. The Main Search Interface
st.write("### 🔍 Ingredient Search Engine")
user_query = st.text_input(
    "Type an ingredient name to check its toxicological breakdown:",
    placeholder="e.g., Parabens, Niacinamide, Fragrance"
).strip().lower()

# Process User Search Query
if user_query:
    if user_query in ingredient_db:
        data = ingredient_db[user_query]
        st.markdown(f"## **Result:** {data['rating']}")
        st.caption(f"**Chemical Category:** {data['category']}")
        
        if "Safe" in data['rating']:
            st.success(data['explanation'])
        elif "Irritant" in data['rating']:
            st.warning(data['explanation'])
        else:
            st.error(data['explanation'])
    else:
        st.info("⚠️ This ingredient isn't in our home database yet. Try searching for 'Parabens', 'Niacinamide', or 'Fragrance'!")

st.write("---")

# 5. Displaying the Filtered List below the search bar
st.write(f"### 📋 Current Database View: **{filter_choice}**")

for name, details in ingredient_db.items():
    if filter_choice == "All Ingredients" or filter_choice in details['rating']:
        with st.expander(f"{name.title()} ({details['rating']})"):
            st.markdown(f"**Function:** {details['category']}")
            st.write(details['explanation'])


            st.write("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "⚖️ <b>Project Ownership & Legal Framework</b><br>"
    "© 2026 Chemistry in Loop. All rights reserved.<br>"
    "Designed, coded, and curated independently by <b>[Priyanshi]</b> as a public educational initiative."
    "</div>", 
    unsafe_allow_html=True
)
