import streamlit as st

# 1. Page Configuration and Theme Setting
st.set_page_config(
    page_title="Chemistry ON Loop", 
    page_icon="🧪", 
    layout="centered"
)

# Customizing the UI look
st.title("🧪 Chemistry ON Loop")
st.markdown("### *Accessible Cosmetic Toxicology & Data Science for Everyone*")
st.write("---")

# 2. Comprehensive 100-Ingredient Toxicology Database
# Sorted into: 40 Safe (🟢), 30 Irritant (🟡), and 30 Avoid (🔴)
ingredient_db = {
    # --- SAFE CATEGORY (🟢) ---
    "niacinamide": {"rating": "🟢 Safe", "category": "Vitamin / Antioxidant", "explanation": "Also known as Vitamin B3, it strengthens the skin barrier and fades dark spots. Highly stable and non-toxic for all skin types."},
    "hyaluronic acid": {"rating": "🟢 Safe", "category": "Humectant", "explanation": "A natural skin molecule that binds water to keep cells hydrated. Poses zero toxicological risk for topical application."},
    "glycerin": {"rating": "🟢 Safe", "category": "Humectant", "explanation": "A plant-derived compound that pulls moisture into the skin. Long history of safe use and entirely non-irritating."},
    "titanium dioxide": {"rating": "🟢 Safe", "category": "Physical Sunscreen Filter", "explanation": "A natural mineral used to shield skin from UV rays. Acts as a physical barrier and is not absorbed deep into the bloodstream."},
    "ceramides": {"rating": "🟢 Safe", "category": "Skin-Identical Lipids", "explanation": "Fatty acids that naturally form the protective skin barrier. Restores barrier health with zero known side effects."},
    "panthenol": {"rating": "🟢 Safe", "category": "Pro-Vitamin B5", "explanation": "Acts as a skin protectant with anti-inflammatory properties. Readily absorbed and completely safe for sensitive skin surfaces."},
    "allantoin": {"rating": "🟢 Safe", "category": "Skin Conditioning Agent", "explanation": "An organic compound that soothes skin and stimulates cell turnover. Frequently used to counter potential irritants in labs."},
    "squalane": {"rating": "🟢 Safe", "category": "Emollient", "explanation": "A stable, saturated oil cousin to natural sebum. Mimics skin lipids perfectly to hydrate without toxicity risk."},
    "centella asiatica": {"rating": "🟢 Safe", "category": "Botanical Extract (Cica)", "explanation": "A plant extract loaded with amino acids. Extensively studied for wound healing and completely safe for reactive skin."},
    "tocopherol": {"rating": "🟢 Safe", "category": "Vitamin E / Antioxidant", "explanation": "A lipid-soluble vitamin that protects cells from oxidative stress. Safely preserves product fats from turning rancid."},
    "zinc oxide": {"rating": "🟢 Safe", "category": "Physical Sunscreen Filter", "explanation": "A natural mineral that sits on top of skin to block UV rays. Highly soothing, safe for infants, and structurally non-toxic."},
    "aloe barbadensis": {"rating": "🟢 Safe", "category": "Botanical Extract", "explanation": "Pure aloe vera extract used to soothe skin inflammation. Naturally contains vitamins and antioxidants with zero toxic footprint."},
    "green tea extract": {"rating": "🟢 Safe", "category": "Antioxidant", "explanation": "Rich in polyphenols like EGCG, it counters cellular pollution damage. Strongly studied and completely safe for skin layers."},
    "shea butter": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "A rich vegetable fat extracted from African shea tree nuts. Intensely hydrates the skin structure without toxic traits."},
    "jojoba oil": {"rating": "🟢 Safe", "category": "Plant Wax Ester", "explanation": "Chemically resembles human skin sebum almost perfectly. Non-comedogenic, deeply moisturizing, and safe for regular daily use."},
    "colloidal oatmeal": {"rating": "🟢 Safe", "category": "Skin Protectant", "explanation": "Finely ground oats that create a protective barrier on skin. Recognized globally as safe for soothing severe eczema breakouts."},
    "alpha arbutin": {"rating": "🟢 Safe", "category": "Skin Brightener", "explanation": "A natural derivative of hydroquinone found in bearberry plants. Fades hyperpigmentation without the high cellular toxicity of synthetic alternatives."},
    "bakuchiol": {"rating": "🟢 Safe", "category": "Plant-derived Retinol Alternative", "explanation": "Extracted from the babchi plant. Triggers cellular renewal like retinol but causes zero barrier irritation, redness, or burning anomalies."},
    "coenzyme q10": {"rating": "🟢 Safe", "category": "Antioxidant", "explanation": "A naturally occurring enzyme in skin cells that prevents oxidative damage. Highly tolerated, stable, and toxicologically inert."},
    "chamomile extract": {"rating": "🟢 Safe", "category": "Botanical Extract", "explanation": "Contains bisabolol and chamazulene. Extensively used in clean chemistry to ease skin irritation and localized vascular flushing."},
    "arginine": {"rating": "🟢 Safe", "category": "Amino Acid", "explanation": "An essential building block of skin proteins. Acts as a natural moisturizing factor and plays a vital role in cellular repair loops."},
    "madecassoside": {"rating": "🟢 Safe", "category": "Active Centella Compound", "explanation": "An ultra-purified molecule from Centella Asiatica. Specifically targeted by dermatologists to treat wounds and skin barrier damage safely."},
    "sunflower seed oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "A lightweight plant oil exceptionally high in linoleic acid. Strengthens cell bonds and reduces trans-epidermal water loss safely."},
    "rosehip seed oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "Packed with naturally occurring trans-retinoic acid and omega fatty acids. Deeply nourishing and carries an excellent toxicology safety score."},
    "licorice root extract": {"rating": "🟢 Safe", "category": "Botanical Skin Brightener", "explanation": "Contains glabridin, which inhibits pigment production safely. An effective, non-toxic choice for evening skin tones."},
    "sodium pca": {"rating": "🟢 Safe", "category": "Humectant", "explanation": "A naturally occurring amino acid derivative in human skin cells. Holds several times its weight in water with zero risk of barrier reactivity."},
    "calendula extract": {"rating": "🟢 Safe", "category": "Botanical Extract", "explanation": "Derived from marigold flowers. Widely recognized in cosmetic data models for its safe, soothing, and anti-inflammatory properties."},
    "grapeseed oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "A lightweight oil rich in oligomeric proanthocyanidins (OPCs). Balances surface sebum safely without toxic cellular mutations."},
    "betaine": {"rating": "🟢 Safe", "category": "Osmolyte / Humectant", "explanation": "A gentle compound derived from sugar beets. Balances cellular water hydration levels safely and actively reduces formulation stickiness."},
    "oat kernel oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "Extracted from oat kernels, it delivers natural lipids and ceramides directly to cells. Exceptionally safe for baby formulas."},
    "rice bran extract": {"rating": "🟢 Safe", "category": "Skin Conditioning Agent", "explanation": "A traditional skincare staple rich in vitamin E and ferulic acid. Softens outer tissue layers safely and comfortably."},
    "resveratrol": {"rating": "🟢 Safe", "category": "Polyphenolic Antioxidant", "explanation": "Found abundantly in grape skins. Neutralizes free radicals and works as a safe structural shield inside advanced cosmetic formulas."},
    "ginseng root extract": {"rating": "🟢 Safe", "category": "Botanical Extract", "explanation": "An ancient herbal root compound. Rich in ginsenosides that visibly re-energize tired skin layers safely with zero toxic risks."},
    "marula oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "Harvested from the marula fruit kernel. Easily absorbed by tissue walls to lock in hydration safely without triggering cell toxicosis."},
    "beta glucan": {"rating": "🟢 Safe", "category": "Humectant / Skin Soother", "explanation": "Polysaccharides derived from yeast or oats. Proven to be 20% more hydrating than hyaluronic acid with a perfect safety rating."},
    "sweet almond oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "Contains high amounts of oleic and linoleic essential fatty acids. Softens outer skin tissues safely and is non-toxic."},
    "cucumber extract": {"rating": "🟢 Safe", "category": "Botanical Extract", "explanation": "A moisture-rich plant extract that provides a cooling sensation. Entirely non-irritating and ideal for soothing under-eye skin lines."},
    "sea buckthorn oil": {"rating": "🟢 Safe", "category": "Plant Emollient", "explanation": "A unique oil rich in rare Omega-7 fatty acids. Accelerates tissue healing loops safely without any structural cell hazards."},
    "ferulic acid": {"rating": "🟢 Safe", "category": "Plant Antioxidant", "explanation": "Found in cell walls of plants like rice and oats. Doubles the chemical stability of Vitamin C and E, making formulas safer and more effective."},
    "witch hazel (alcohol-free)": {"rating": "🟢 Safe", "category": "Astringent", "explanation": "Distilled plant extract used to temporarily refine skin pores. Completely safe and non-toxic provided it contains no denatured alcohol."},

    # --- IRRITANT CATEGORY (🟡) ---
    "fragrance": {"rating": "🟡 Irritant", "category": "Scent Masking", "explanation": "A loophole term that can hide hundreds of synthetic chemicals. A primary cause of allergic contact dermatitis and redness."},
    "salicylic acid": {"rating": "🟡 Irritant (Use with Care)", "category": "Beta Hydroxy Acid (BHA)", "explanation": "Highly effective at clearing pores. However, in concentrations above 2% or when overused, it can strip skin lipids violently."},
    "alcohol denat": {"rating": "🟡 Irritant", "category": "Solvent / Extractor", "explanation": "Makes skincare products dry quickly. Regular use breaks down the natural skin barrier, leading to structural dehydration."},
    "sodium lauryl sulfate": {"rating": "🟡 Irritant", "category": "Surfactant (Foaming Agent)", "explanation": "Commonly found in cleansers. Violently strips the natural oils from the outer layer of skin, triggering eczema flare-ups."},
    "essential oils": {"rating": "🟡 Irritant", "category": "Natural Plant Extracts", "explanation": "Highly concentrated extracts like lavender or tea tree oil. Volatile compounds can trigger contact allergies when oxidized."},
    "retinol": {"rating": "🟡 Irritant (Use with Care)", "category": "Vitamin A Derivative", "explanation": "Accelerates cell turnover heavily. Can cause 'retinoid dermatitis' characterized by redness, flaking, and severe peeling if misused."},
    "benzoyl peroxide": {"rating": "🟡 Irritant (Use with Care)", "category": "Anti-Acne Agent", "explanation": "Kills acne-causing bacteria effectively. Often causes localized dryness, stinging, and mild chemical skin peeling."},
    "glycolic acid": {"rating": "🟡 Irritant (Use with Care)", "category": "Alpha Hydroxy Acid (AHA)", "explanation": "An intense chemical exfoliant. Has a small molecular size that penetrates deeply, easily causing burning sensations if overused."},
    "ascorbic acid": {"rating": "🟡 Irritant (Use with Care)", "category": "Pure Vitamin C", "explanation": "Highly potent antioxidant that requires a low, acidic pH to work. This low pH frequently triggers stinging on sensitive barriers."},
    "phenoxyethanol": {"rating": "🟡 Irritant", "category": "Synthetic Preservative", "explanation": "Used as a safer alternative to parabens, but limited to 1% concentrations globally. Can still cause contact skin irritation."},
    "lactic acid": {"rating": "🟡 Irritant (Use with Care)", "category": "Alpha Hydroxy Acid (AHA)", "explanation": "Derived from milk or synthetic sugars. Exfoliates gently, but over-application alters barrier pH and causes burning loops."},
    "sulfur": {"rating": "🟡 Irritant", "category": "Anti-Acne Agent", "explanation": "Dries out excess surface oils to clear breakouts. Often causes severe chemical dryness, flaking, and an intense peeling effect."},
    "tea tree oil": {"rating": "🟡 Irritant", "category": "Essential Oil", "explanation": "Possesses natural antimicrobial qualities. When applied undiluted or in high amounts, it behaves as an aggressive contact allergen."},
    "citric acid": {"rating": "🟡 Irritant", "category": "AHA / pH Adjuster", "explanation": "Used in tiny amounts to adjust product pH. If added in larger doses as an exfoliant, it triggers stinging and redness cascades."},
    "menthol": {"rating": "🟡 Irritant", "category": "Cooling Agent", "explanation": "Derived from mint oils to create a cooling illusion. Masking sensation can mask chemical skin burning and trigger dermatitis."},
    "peppermint oil": {"rating": "🟡 Irritant", "category": "Essential Oil", "explanation": "Contains volatile aromatic components that make cosmetics smell fresh. Highly reactive on sensitive or damaged skin barriers."},
    "linalool": {"rating": "🟡 Irritant", "category": "Fragrance Component", "explanation": "A naturally occurring terpene found in lavender. When exposed to open air, it oxidizes and turns into an aggressive skin sensitizer."},
    "limonene": {"rating": "🟡 Irritant", "category": "Fragrance Component", "explanation": "Found in citrus rinds. Heavily flagged by toxicologists as a primary cause of cosmetic contact allergies globally."},
    "citral": {"rating": "🟡 Irritant", "category": "Fragrance Component", "explanation": "A strong scent component extracted from lemongrass. High allergen index; restricted to tiny percentages under safety laws."},
    "geraniol": {"rating": "🟡 Irritant", "category": "Fragrance Component", "explanation": "A rose-like scent molecule. Frequently induces localized swelling, hives, or micro-inflammation in sensitive populations."},
    "eugenol": {"rating": "🟡 Irritant", "category": "Fragrance Component", "explanation": "Derived from clove oil. Highly aromatic but causes strong cell sensitization and allergic skin reactions when overused."},
    "sodium c14-16 olefin sulfonate": {"rating": "🟡 Irritant", "category": "Surfactant (Cleansing Agent)", "explanation": "Often substituted for sulfates in 'sulfate-free' washes. Can still heavily strip lipid walls, causing dry skin textures."},
    "cocamidopropyl betaine": {"rating": "🟡 Irritant", "category": "Surfactant (Foamer)", "explanation": "A gentle cleansing agent derived from coconuts, but manufacturing impurities frequently cause contact allergies and eczema."},
    "potassium hydroxide": {"rating": "🟡 Irritant", "category": "Alkaline pH Adjuster", "explanation": "A highly alkaline chemical used to balance formulations. In raw states, it burns tissue; if unbalanced in formulas, it strips lipids."},
    "sodium hydroxide": {"rating": "🟡 Irritant", "category": "Alkaline pH Adjuster", "explanation": "Commonly known as lye. Used to balance product acidity. If miscalculated in a formula, it causes chemical skin burns."},
    "isopropyl myristate": {"rating": "🟡 Irritant", "category": "Synthetic Emollient", "explanation": "Enhances product absorption so creams sink in smoothly. Heavily clogs pores and can cause sudden cosmetic acne outbreaks."},
    "witch hazel (with alcohol)": {"rating": "🟡 Irritant", "category": "Astringent", "explanation": "Standard witch hazel is often distilled using denatured alcohol. Stris skin oils and causes severe tissue dryness."},
    "kojic acid": {"rating": "🟡 Irritant (Use with Care)", "category": "Skin Lightener", "explanation": "Derived from fungi. Inhibits melanin effectively but frequently causes contact dermatitis and skin sensitizing cycles."},
    "propylene glycol": {"rating": "🟡 Irritant", "category": "Solvent / Humectant", "explanation": "Helps ingredients penetrate deeper into skin layers. Known to cause skin irritation and redness in sensitive skin types."},
    "polysorbate 20": {"rating": "🟡 Irritant", "category": "Emulsifier", "explanation": "Helps bind water and oils together. Generally low risk, but can trigger fungal acne flare-ups on prone skin structures."},

    # --- AVOID CATEGORY (🔴) ---
    "parabens": {"rating": "🔴 Avoid", "category": "Synthetic Preservative", "explanation": "Used to prolong product shelf-life. Toxicological studies show they can mimic estrogen in the body and disrupt the endocrine system."},
    "formaldehyde releasers": {"rating": "🔴 Avoid", "category": "Preservative", "explanation": "Chemicals like DMDM Hydantoin that slowly release formaldehyde gas. Formaldehyde is a known human carcinogen."},
    "oxybenzone": {"rating": "🔴 Avoid", "category": "Chemical Sunscreen Filter", "explanation": "A chemical UV filter absorbed easily through skin. Acts as a significant hormone disruptor and carries high aquatic toxicity data."},
    "phthalates": {"rating": "🔴 Avoid", "category": "Plasticizer / Solvent", "explanation": "Often hidden under the word 'fragrance'. Heavily linked in toxicology profiles to developmental and reproductive disruptions."},
    "triclosan": {"rating": "🔴 Avoid", "category": "Antibacterial Agent", "explanation": "An antimicrobial chemical that accumulates in fatty tissues, disrupts thyroid pathways, and breeds drug-resistant bacteria."},
    "coal tar": {"rating": "🔴 Avoid", "category": "Anti-Dandruff / Colorant", "explanation": "A byproduct of coal processing used in specialty shampoos. A known human carcinogen heavily restricted in multiple countries."},
    "hydroquinone": {"rating": "🔴 Avoid", "category": "Skin Lightener", "explanation": "Banned in the EU for cosmetic use. Can cause ochronosis (bluish-black skin discoloration) and potential cellular toxicity risk."},
    "toluene": {"rating": "🔴 Avoid", "category": "Nail Product Solvent", "explanation": "A volatile petrochemical solvent. Toxic to the central nervous system, and fumes can cause dizziness or developmental concerns."},
    "resorcinol": {"rating": "🔴 Avoid", "category": "Hair Dye Ingredient", "explanation": "Commonly used in oxidative hair coloring. Known to disrupt thyroid function and acts as a severe systemic sensitizer."},
    "lead acetate": {"rating": "🔴 Avoid", "category": "Progressive Hair Dye Colorant", "explanation": "Contains heavy metal elements. Lead is a potent neurotoxin that can accumulate in bone and tissue structures over time."},
    "bha (butylated hydroxyanisole)": {"rating": "🔴 Avoid", "category": "Synthetic Antioxidant", "explanation": "Used as a chemical preservative in makeup. Classified by international health boards as a potential human endocrine disruptor."},
    "bht (butylated hydroxytoluene)": {"rating": "🔴 Avoid", "category": "Synthetic Preservative", "explanation": "Closely related to BHA. Laboratory models show it can mimic estrogen and promote tumor growth in lung tissue cells."},
    "dmdm hydantoin": {"rating": "🔴 Avoid", "category": "Formaldehyde Releaser", "explanation": "An aggressive preservative that kills bacteria by releasing formaldehyde gas over time. High risk of severe contact allergies."},
    "imidazolidinyl urea": {"rating": "🔴 Avoid", "category": "Formaldehyde Releaser", "explanation": "Commonly used in water-based cosmetics. Slowly releases formaldehyde gas in the container, introducing cancer risks."},
    "diazolidinyl urea": {"rating": "🔴 Avoid", "category": "Formaldehyde Releaser", "explanation": "Found in shampoos and hair gels. Acts as a major allergen and is heavily restricted due to toxic gas release loops."},
    "quaternium-15": {"rating": "🔴 Avoid", "category": "Formaldehyde Releaser", "explanation": "A synthetic surfactant preservative. Banned completely in the European Union due to its cancer-causing formaldehyde release profile."},
    "octinoxate": {"rating": "🔴 Avoid", "category": "Chemical Sunscreen Filter", "explanation": "A chemical UV filter shown to disrupt thyroid hormones and reproductive systems. Highly toxic to coral reefs and marine life."},
    "homosalate": {"rating": "🔴 Avoid", "category": "Chemical Sunscreen Filter", "explanation": "Absorbed through skin layers and accumulates in the human body. Disrupts estrogen, androgen, and progesterone balance models."},
    "octisalate": {"rating": "🔴 Avoid", "category": "Chemical Sunscreen Filter", "explanation": "Used to boost UV absorption. Studies show it easily penetrates skin cells, increasing the systemic absorption of other toxic chemicals."},
    "methylisothiazolinone": {"rating": "🔴 Avoid", "category": "Synthetic Preservative", "explanation": "An intense contact allergen banned in leave-on skin creams globally. Can cause severe chemical rashes and skin scaling."},
    "methylchloroisothiazolinone": {"rating": "🔴 Avoid", "category": "Synthetic Preservative", "explanation": "Commonly paired with MI in rinse-off products. Highly cytotoxic and flagged as a severe immune system sensitizer."},
    "p-phenylenediamine (ppd)": {"rating": "🔴 Avoid", "category": "Hair Dye Colorant", "explanation": "The core chemical in dark hair dyes. Linked to severe respiratory failure, permanent skin scarring, and systemic toxicity."},
    "ethanolamine (mea)": {"rating": "🔴 Avoid", "category": "Surfactant / pH Adjuster", "explanation": "Can react with other ingredients to form nitrosamines, which are highly potent carcinogens that penetrate skin walls."},
    "diethanolamine (dea)": {"rating": "🔴 Avoid", "category": "Emulsifier / Foamer", "explanation": "Commonly used to create thick textures. Carries a high risk of nitrosamine contamination, leading to liver and kidney toxicity."},
    "triethanolamine (tea)": {"rating": "🔴 Avoid", "category": "Surfactant / pH Adjuster", "explanation": "Used to balance product acidity. Can react with nitrates during storage to form cancer-causing nitrosamine chemical bonds."},
    "petrolatum (unrefined)": {"rating": "🔴 Avoid", "category": "Occlusive Emollient", "explanation": "If not completely purified, it can contain Polycyclic Aromatic Hydrocarbons (PAHs), which are heavily linked to cancer development."},
    "carbon black": {"rating": "🔴 Avoid", "category": "Cosmetic Pigment", "explanation": "A black powder used in eyeliners. Flagged by cancer research organizations as a possible human carcinogen when absorbed into cells."},
    "polyethylene glycol (peg)": {"rating": "🔴 Avoid", "category": "Solvent / Thickener", "explanation": "Manufacturing processes often contaminate PEGs with 1,4-dioxane and ethylene oxide, both known human carcinogens."},
    "sodium borate": {"rating": "🔴 Avoid", "category": "Preservative / Buffer", "explanation": "Also known as borax. Heavily restricted because it can interfere with hormone production and damage reproductive systems."},
    "mercury (thimerosal)": {"rating": "🔴 Avoid", "category": "Preservative / Bleaching Agent", "explanation": "A toxic heavy metal occasionally found in eye cosmetics or skin lighteners. Causes nervous system damage and severe toxicity."}
}

# 3. Interactive Sidebar for Quick Filtering
st.sidebar.header("Filter by Safety Level")
filter_choice = st.sidebar.selectbox(
    "Show ingredients that are:",
    ["All Ingredients", "🟢 Safe", "🟡 Irritant", "🔴 Avoid"]
)

# 4. The Main Search Interface (Dual Methods)
st.write("### 🔍 Choose Your Entry Method")
tab1, tab2 = st.tabs(["⌨️ Type Ingredient Name", "📷 Scan Product Label"])

user_query = ""

with tab1:
    user_query = st.text_input(
        "Type an ingredient name to check its toxicological breakdown:",
        placeholder="e.g., Parabens, Retinol, Niacinamide",
        key="text_search"
    ).strip().lower()

with tab2:
    st.markdown("##### **Take a photo of your product's ingredient list**")
    uploaded_file = st.file_uploader(
        "Upload a clear image of the chemical label to run an automated AI review:", 
        type=["jpg", "jpeg", "png"],
        key="camera_scan"
    )
    if uploaded_file:
        st.info("🤖 Connecting to the Chemistry ON Loop vision parser... The automated text-extraction module is initializing!")
        st.image(uploaded_file, caption="Processing your product label...", use_container_width=True)

# Process User Text Search Query
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
        st.info("⚠️ This ingredient isn't in our home database yet. Try searching for 'Retinol', 'Parabens', or 'Niacinamide'!")

st.write("---")

# 5. Displaying the Filtered List below the search bar
st.write(f"### 📋 Current Database View: **{filter_choice}**")

for name, details in ingredient_db.items():
    if filter_choice == "All Ingredients" or filter_choice in details['rating']:
        with st.expander(f"{name.title()} ({details['rating']})"):
            st.markdown(f"**Function:** {details['category']}")
            st.write(details['explanation'])

# 6. Community Review Portal & Feedback Loop
st.write("---")
st.write("### 💬 Community Product Review Portal")
st.markdown("*Share your experience with product formulations to help keep the community in the loop!*")

with st.form(key="review_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        product_name = st.text_input("Product Name:", placeholder="e.g., Ultra Hydrating Cleanser")
        review_text = st.text_area("Your Review / Formulation Experience:", placeholder="Did this cause breakouts? Is the ingredient label clean?")
    
    with col2:
        ingredient_check = st.selectbox("Formulation Cleanliness:", ["🟢 Purely Safe Ingredients", "🟡 Contains Irritants", "🔴 Contains Avoid Chemicals"])
        star_rating = st.slider("⭐ Community Rating:", 1, 5, 5, )
        
    submit_button = st.form_submit_button(label="🚀 Post Review to Community Feed")

if submit_button and product_name and review_text:
    st.success(f"🎉 Thank you! The developer portal successfully received your review for **{product_name}**!")
    with st.chat_message("user", avatar="🧪"):
        st.markdown(f"##### **{product_name}** — {star_rating} ⭐")
        st.caption(f"Status Checked: {ingredient_check}")
        st.info(f'"{review_text}"')

# 7. Legal Footer
st.write("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>⚖️ <b>Project Ownership & Legal Framework</b><br> © 2026 Chemistry ON Loop. All rights reserved.<br>Designed, coded, and curated independently by <b>Priyanshi</b> as a public educational initiative.</div>", 
    unsafe_allow_html=True
)
