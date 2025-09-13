import streamlit as st
import random
import time

# Set a wide page layout
st.set_page_config(
    page_title="Skincare Pro Analyzer",
    page_icon="✨",
    layout="wide"
)

# --- General Styling ---
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    font-weight: bold;
    color: #4A90E2;
    text-align: center;
    margin-bottom: 1rem;
}
.sidebar .sidebar-content {
    background-color: #f0f2f6;
    border-right: 2px solid #e0e0e0;
}
.stButton>button {
    background-color: #4A90E2;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
}
.stButton>button:hover {
    background-color: #357ABD;
}
.stTextInput, .stFileUploader, .stSelectbox, .stMultiselect {
    border-radius: 12px;
    padding: 10px;
}
.tip-container {
    background-color: #f9f9f9;
    border-left: 5px solid #4A90E2;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.question-container {
    background-color: #e6f3ff;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 10px;
}
.points-display {
    text-align: center;
    font-size: 1.5rem;
    font-weight: bold;
    color: #007BFF;
    margin-top: 1rem;
    padding: 10px;
    border: 2px solid #007BFF;
    border-radius: 12px;
    background-color: #e6f3ff;
}
.comparison-container {
    background-color: #f0f8ff;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #cceeff;
}
</style>
""", unsafe_allow_html=True)


# --- Helper Functions for each page ---

def show_login_register():
    st.title("Login / Register")
    st.markdown("""
    यह लॉगिन और पंजीकरण फ़ंक्शन के लिए एक प्लेसहोल्डर है।
    एक पूर्ण कार्यान्वयन के लिए उपयोगकर्ता प्रमाणीकरण को संभालने के लिए फ़ायरबेस जैसे बैकएंड डेटाबेस या इसी तरह की सेवा की आवश्यकता होगी।
    """)
    st.text_input("Username")
    st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state.logged_in = True
        st.experimental_rerun()
    st.markdown("---")
    st.header("New User?")
    st.button("Register")

def show_skincare_analyzer():
    st.markdown("<h1 class='main-header'>Skincare Pro Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("अपनी त्वचा का विश्लेषण करने के लिए एक स्पष्ट तस्वीर अपलोड करें और अपनी स्वास्थ्य और जीवन शैली का विवरण दर्ज करें।")
    
    st.header("Upload Photo")
    uploaded_file = st.file_uploader("यहां फ़ाइल खींचें और छोड़ें या ब्राउज़ करने के लिए क्लिक करें", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Photo', use_column_width=True)
        st.success("Photo uploaded successfully.")
        
        st.markdown("---")
        st.header("Enter Your Health & Lifestyle Details")
        sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
        water_intake = st.slider("Water Intake (Litres/day)", 0.0, 5.0, 2.0, 0.5)
        stress_level = st.slider("Stress Level (1-10)", 1, 10, 6)
        diet_quality = st.slider("Diet Quality (1-10)", 1, 10, 8)
        
        if st.button("Analyze Skin"):
            st.markdown("---")
            st.header("Analysis Report")
            st.subheader("General Assessment:")
            st.markdown(f"""
            - **Estimated Skin Type:** Combination
            - **Primary Concerns:** Mild acne around the jawline, some pigmentation.
            - **Overall Score:** 85/100
            """)
            
            st.subheader("Lifestyle Impact:")
            if sleep_hours < 7:
                st.warning(f"**Sleep Hours:** With only {sleep_hours} hours, your skin's repair process may be compromised.")
            if water_intake < 2:
                st.warning(f"**Water Intake:** Your intake of {water_intake} L is below the recommended amount, which can lead to dullness and dryness.")
            if stress_level > 7:
                st.warning(f"**Stress Level:** High stress can trigger breakouts and inflammation.")
            if diet_quality < 5:
                st.warning(f"**Diet Quality:** A diet with a score of {diet_quality} can contribute to poor skin health.")

def show_daily_tips():
    st.title("Daily Skincare Tips")
    st.markdown("अपनी स्किनकेयर दिनचर्या में शीर्ष पर बने रहने के लिए इन आवश्यक दैनिक युक्तियों का पालन करें।")
    
    st.subheader("Morning Routine:")
    st.markdown("- **Tip 1:** अपनी त्वचा को रात भर की गंदगी से साफ़ करने के लिए एक हल्के क्लींज़र से अपना चेहरा धोएँ।")
    st.markdown("- **Tip 2:** पर्यावरणीय क्षति से बचाने के लिए विटामिन सी सीरम लगाएं।")
    st.markdown("- **Tip 3:** हमेशा कम से कम एसपीएफ 30 वाली एक व्यापक-स्पेक्ट्रम सनस्क्रीन के साथ समाप्त करें।")
    
    st.subheader("Evening Routine:")
    st.markdown("- **Tip 1:** मेकअप और सनस्क्रीन को प्रभावी ढंग से हटाने के लिए चेहरे को दो बार धोएं।")
    st.markdown("- **Tip 2:** रेटिनोल या एएचए/बीएचए सीरम जैसे उपचार उत्पाद का उपयोग करें।")
    st.markdown("- **Tip 3:** रात भर में अपनी त्वचा की मरम्मत के लिए एक समृद्ध मॉइस्चराइजर से नमी को रोकें।")

def show_chatbot():
    st.title("AI Skincare Chatbot")
    st.markdown("उत्तर प्रकट करने के लिए किसी प्रश्न पर क्लिक करें।")
    
    qa_pairs = {
        "What is the best way to get rid of blackheads?": "ब्लैकहेड्स को सैलिसिलिक एसिड (BHA) वाले उत्पादों का उपयोग करके या अपनी दिनचर्या में मिट्टी का मास्क शामिल करके प्रभावी ढंग से हटाया जा सकता है। हल्का एक्सफोलिएशन महत्वपूर्ण है।",
        "How can I reduce redness and irritation on my skin?": "लालिमा को कम करने के लिए, सेंटेला एशियाटिका (Cica), नियासिनमाइड या ग्रीन टी के अर्क जैसे शांत करने वाले अवयवों की तलाश करें। कठोर स्क्रब और सुगंध से बचें।",
        "What is the difference between AHA and BHA?": "एएचए (अल्फा हाइड्रॉक्सी एसिड) जैसे ग्लाइकोलिक एसिड त्वचा की सतह पर काम करते हैं। बीएचए (बीटा हाइड्रॉक्सी एसिड) जैसे सैलिसिलिक एसिड छिद्रों में गहराई तक घुसकर तेल और गंदगी को साफ करते हैं।",
        "Is it necessary to use a toner?": "टोनर हमेशा आवश्यक नहीं होता है, लेकिन एक बेहतरीन अतिरिक्त हो सकता है। हाइड्रेटिंग टोनर सीरम के लिए त्वचा को तैयार कर सकते हैं, जबकि एक्सफोलिएटिंग टोनर कोशिका नवीनीकरण में मदद कर सकते हैं।",
        "Can diet affect my skin?": "हाँ, आहार एक महत्वपूर्ण भूमिका निभाता है। एंटीऑक्सीडेंट, स्वस्थ वसा और विटामिन से भरपूर खाद्य पदार्थ त्वचा के स्वास्थ्य में सुधार कर सकते हैं, जबकि उच्च-शर्करा या प्रसंस्कृत आहार मुंहासों में योगदान कर सकता है।",
        "What is a serum and how do I use it?": "सीरम एक केंद्रित फ़ॉर्मूला है जिसमें विशिष्ट चिंताओं को लक्षित करने के लिए सक्रिय तत्व होते हैं। इसे साफ़ करने और टोनिंग करने के बाद, और मॉइस्चराइजिंग से पहले लगाएं।",
        "How do I choose the right sunscreen?": "कम से कम एसपीएफ 30 वाली एक व्यापक-स्पेक्ट्रम सनस्क्रीन चुनें। संवेदनशील त्वचा के लिए जिंक ऑक्साइड या टाइटेनियम डाइऑक्साइड के साथ मिनरल सनस्क्रीन देखें।",
        "What are the benefits of using a face mask?": "फेस मास्क हाइड्रेशन, चमक, या तेल नियंत्रण जैसी विशिष्ट चिंताओं को दूर करने के लिए केंद्रित खुराक प्रदान कर सकते हैं। सप्ताह में 1-2 बार इनका उपयोग करें।",
        "Should I use an eye cream?": "आई क्रीम विशेष रूप से आंखों के आसपास की नाजुक त्वचा के लिए बनाई जाती हैं। वे महीन रेखाओं, सूजन और काले घेरों में मदद कर सकती हैं।",
        "What is the importance of moisturizing?": "मॉइस्चराइजिंग सभी प्रकार की त्वचा के लिए महत्वपूर्ण है क्योंकि यह त्वचा के सुरक्षात्मक अवरोध को बनाए रखने में मदद करता है, पानी के नुकसान को रोकता है और इसे पर्यावरणीय परेशानियों से बचाता है।",
        "How can I prevent premature aging?": "समय से पहले बूढ़ा होने से रोकने का सबसे अच्छा तरीका रोजाना सनस्क्रीन का उपयोग करना, विटामिन सी जैसे एंटीऑक्सीडेंट लगाना और अपनी रात की दिनचर्या में रेटिनॉइड को शामिल करना है।",
        "What is the best way to treat acne scars?": "मुंहासे के निशानों का इलाज रेटिनॉइड, विटामिन सी, या एएचए वाले उत्पादों से किया जा सकता है। अधिक गंभीर निशानों के लिए, माइक्रोनीडलिंग या लेजर थेरेपी जैसे पेशेवर उपचार आवश्यक हो सकते हैं।",
        "Why is my skin suddenly breaking out?": "मुंहासे विभिन्न कारकों के कारण हो सकते हैं, जिनमें हार्मोनल परिवर्तन, तनाव, आहार, एक नया उत्पाद का उपयोग करना, या आर्द्रता जैसे पर्यावरणीय कारक शामिल हैं।",
        "What are ceramides and why are they important?": "सेरामाइड्स लिपिड हैं जो त्वचा के अवरोध को बनाने में मदद करते हैं। वे नमी बनाए रखने और त्वचा को बाहरी परेशानियों से बचाने के लिए आवश्यक हैं। वे सभी प्रकार की त्वचा के लिए बहुत अच्छे हैं, विशेष रूप से सूखी या संवेदनशील त्वचा के लिए।",
        "How do I determine my skin type?": "अपनी त्वचा का प्रकार निर्धारित करने के लिए, अपना चेहरा धोएं और किसी भी उत्पाद को लगाए बिना एक घंटा प्रतीक्षा करें। यदि आपकी त्वचा में खिंचाव और परतदारपन महसूस होता है, तो यह शुष्क है। यदि यह चमकदार है, तो यह तैलीय है। यदि यह एक मिश्रण है, तो यह संयोजन है। यदि यह संतुलित महसूस होता है, तो यह सामान्य है।"
    }
    
    for question, answer in qa_pairs.items():
        with st.expander(question):
            st.markdown(f"**Answer:** {answer}")

def show_skin_comparator():
    st.title("Skin Health Comparator")
    st.markdown("अपनी त्वचा की रिपोर्ट की तुलना एक आदर्श रिपोर्ट से करें और अपनी कमियों को जानें।")
    
    st.header("Upload Your Skin Report")
    uploaded_file = st.file_uploader("यहाँ अपनी पिछली स्किन रिपोर्ट अपलोड करें (PNG, JPG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        st.subheader("Your Report:")
        st.image(uploaded_file, use_column_width=True)
        
        st.markdown("---")
        
        st.subheader("Ideal Skin Report (Reference):")
        st.markdown("""
        <div class="comparison-container">
            <h4>आदर्श त्वचा रिपोर्ट</h4>
            <ul>
                <li><strong>Hydration Level:</strong> उत्कृष्ट</li>
                <li><strong>Texture:</strong> बहुत चिकनी</li>
                <li><strong>Pores:</strong> छोटे और साफ़</li>
                <li><strong>Radiance:</strong> बहुत चमकदार</li>
                <li><strong>Acne/Spots:</strong> कोई नहीं</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.header("Comparative Analysis")
        st.markdown("आपके रिपोर्ट और आदर्श रिपोर्ट के बीच मुख्य अंतर नीचे दिए गए हैं:")

        defects = {
            "Texture": "कुछ खुरदुरापन और असमान बनावट",
            "Hydration": "रूखापन और निर्जलीकरण",
            "Pores": "कुछ खुले और अवरुद्ध छिद्र",
        }
        
        for flaw, description in defects.items():
            st.error(f"**{flaw} Defect:** {description}")

        st.markdown("---")
        st.header("Product Recommendations")
        st.markdown("आपकी कमियों को दूर करने के लिए विशेष रूप से अनुशंसित उत्पाद:")
        
        st.info("**Texture & Unevenness:** एक AHA/BHA सीरम जैसे ग्लाइकोलिक एसिड या सैलिसिलिक एसिड का उपयोग करें।")
        st.info("**Hydration:** एक हयालूरोनिक एसिड या सेरामाइड युक्त मॉइस्चराइजर का उपयोग करें।")
        st.info("**Pores:** अपने छिद्रों को गहराई से साफ़ करने के लिए एक मिट्टी का मास्क या नियासिनमाइड सीरम आज़माएं।")
        

def show_voice_assistant():
    st.title("Voice Assistant (Coming Soon)")
    st.info("इस सुविधा को कार्य करने के लिए टेक्स्ट-टू-स्पीच (टीटीएस) और स्पीच-टू-टेक्स्ट (एसटीटी) एपीआई की आवश्यकता होगी। यह भविष्य के विकास के लिए एक प्लेसहोल्डर है।")
    st.markdown("सोचिए कि आप अपनी स्किनकेयर रूटीन के बारे में प्रश्न पूछ सकते हैं और एक मानवीय आवाज़ में उत्तर प्राप्त कर सकते हैं।")

def show_skin_prediction_ai():
    st.title("Skin Prediction AI")
    st.markdown("अपनी आदतों के बारे में कुछ सवालों के जवाब देकर अपनी त्वचा के भविष्य का अनुमान लगाएं।")

    questions = [
        "क्या आप दिन में 2 लीटर से ज़्यादा पानी पीते हैं?",
        "क्या आप रोज़ाना कम से कम 7 घंटे सोते हैं?",
        "क्या आप नियमित रूप से एक्सरसाइज़ करते हैं?",
        "क्या आप रोज़ाना चेहरे पर सनस्क्रीन लगाते हैं?",
        "क्या आप रोज़ फल और सब्ज़ियाँ खाते हैं?",
        "क्या आप तनाव को मैनेज करने के लिए तरीके अपनाते हैं?",
        "क्या आप रोज़ाना चेहरे को धोते हैं (सुबह और शाम)?",
        "क्या आप अपने मेकअप ब्रश को हर हफ़्ते साफ़ करते हैं?",
        "क्या आप बाहर जाने से पहले प्रदूषण से बचाने वाला सीरम लगाते हैं?",
        "क्या आप रात में सोने से पहले मेकअप उतार देते हैं?",
        "क्या आप रोज़ाना अपने चेहरे को मॉइस्चराइज़ करते हैं?",
        "क्या आप मीठे और प्रोसेस्ड फ़ूड्स ज़्यादा खाते हैं?",
        "क्या आप बहुत ज़्यादा धूप में रहते हैं?",
        "क्या आप शराब पीते हैं या धूम्रपान करते हैं?",
        "क्या आप दिन में कई बार अपने चेहरे को छूते हैं?"
    ]

    st.markdown("---")
    
    with st.form("prediction_form"):
        user_answers = {}
        for i, question in enumerate(questions):
            answer = st.radio(question, ("हाँ", "नहीं"), key=f"q_{i}")
            user_answers[question] = answer
        
        submitted = st.form_submit_button("भविष्यवाणी देखें")
    
    if submitted:
        st.markdown("---")
        with st.spinner('आपकी त्वचा के भविष्य का विश्लेषण किया जा रहा है...'):
            time.sleep(3)

        good_habits = 0
        bad_habits = 0

        # Scoring logic
        for q, a in user_answers.items():
            if q in questions[0:11]: # Positive habits
                if a == "हाँ":
                    good_habits += 1
                else:
                    bad_habits += 1
            else: # Negative habits
                if a == "नहीं":
                    good_habits += 1
                else:
                    bad_habits += 1

        total_score = good_habits - bad_habits
        
        st.header("आपकी त्वचा का भविष्य (अगले 6 महीनों में)")
        if total_score >= 8:
            st.success("आपकी त्वचा अगले 6 महीनों में बहुत अच्छी और स्वस्थ दिखेगी।")
            st.image("https://placehold.co/600x400/0000FF/FFFFFF?text=Healthy+Skin+Future", use_column_width=True)
            st.markdown("""
            आपकी अच्छी आदतें बहुत प्रभावशाली हैं। आपकी त्वचा साफ़, चमकदार और जवान दिखेगी। अपनी दिनचर्या जारी रखें।
            """)
        elif 3 <= total_score < 8:
            st.warning("आपकी त्वचा अच्छी दिखेगी, लेकिन उसमें सुधार की गुंजाइश है।")
            st.image("https://placehold.co/600x400/FFA500/000000?text=Improving+Skin", use_column_width=True)
            st.markdown("""
            आपके पास अच्छी और बुरी दोनों आदतें हैं। कुछ बुरी आदतों को छोड़ने से आपकी त्वचा और भी बेहतर हो सकती है।
            """)
        else:
            st.error("आपकी त्वचा में कुछ समस्याएँ हो सकती हैं, लेकिन आप अभी भी इसमें सुधार कर सकते हैं।")
            st.image("https://placehold.co/600x400/FF0000/FFFFFF?text=Challenging+Skin", use_column_width=True)
            st.markdown("""
            आपकी त्वचा की स्थिति में सुधार के लिए कुछ आदतों को बदलने की आवश्यकता है। अपनी स्किनकेयर रूटीन को गंभीरता से लें।
            """)

def show_skincare_gamification():
    st.title("Skincare Gamification (Coming Soon)")
    st.info("इस सुविधा में आपकी स्किनकेयर रूटीन को और अधिक मनोरंजक और आकर्षक बनाने के लिए दैनिक चुनौतियाँ, अंक और बैज शामिल होंगे। यह भविष्य के विकास के लिए एक प्लेसहोल्डर है।")
    st.markdown("अपनी दैनिक रूटीन के कार्यों को पूरा करके अंक अर्जित करें और नई सुविधाओं या पुरस्कारों को अनलॉक करें!")

def show_hyper_personalized_advice():
    st.title("Hyper-Personalized Advice")
    st.markdown("अपनी त्वचा के लिए एक विशेष दिनचर्या प्राप्त करने के लिए इस विस्तृत प्रश्नावली को भरें।")
    
    with st.form("personal_advice_form"):
        age = st.slider("Your Age", 15, 80, 25)
        skin_type = st.radio("What is your skin type?", ("Oily", "Dry", "Combination", "Normal", "Sensitive"))
        concerns = st.multiselect("Select your main skin concerns:", ["Acne", "Fine Lines", "Dullness", "Redness", "Dehydration", "Dark Spots", "Uneven Texture"])
        lifestyle = st.text_area("Describe your daily lifestyle (e.g., city pollution, desk job, active outdoors):")
        
        submitted = st.form_submit_button("Get My Personalized Routine")
        if submitted:
            st.markdown("---")
            st.subheader("Your Custom Skincare Routine:")
            st.write(f"**For a {age}-year-old with {skin_type} skin, focusing on {', '.join(concerns)}...**")
            
            st.markdown("### Morning Routine")
            st.markdown("- **Cleanse:** Use a gentle, pH-balanced cleanser to wake up your skin.")
            st.markdown("- **Treat:** Apply a Vitamin C serum to brighten and protect from pollution.")
            st.markdown("- **Moisturize:** A lightweight moisturizer is essential for hydration.")
            st.markdown("- **Protect:** Always finish with a broad-spectrum SPF 30+ sunscreen.")
            
            st.markdown("### Evening Routine")
            st.markdown("- **Cleanse:** Double-cleanse to remove all impurities from the day.")
            st.markdown("- **Treat:** Incorporate a targeted serum with ingredients like Retinol (for fine lines) or Niacinamide (for acne/dullness).")
            st.markdown("- **Moisturize:** Use a richer moisturizer to repair your skin barrier overnight.")

def show_25_tips():
    st.title("25 Essential Skincare Tips")
    st.markdown("उनके लाभ और उत्पाद अनुशंसाओं के साथ उच्च-प्रभाव वाली युक्तियों की एक सूची।")
    
    tips = [
        ("Hydrate from Within", "पर्याप्त पानी पीने से आपकी त्वचा कोमल और हाइड्रेटेड रहती है, जिससे लोच और समग्र स्वास्थ्य में सुधार होता है।", "हाइड्रेटिंग क्लींजर, हयालूरोनिक एसिड सीरम"),
        ("Double Cleanse at Night", "पहला क्लींजर मेकअप और सनस्क्रीन को हटाता है, जबकि दूसरा क्लींजर आपके छिद्रों को गहराई से साफ़ करता है, जिससे मुंहासे नहीं होते हैं।", "तेल-आधारित क्लींजर, पानी-आधारित क्लींजर"),
        ("Exfoliate Regularly", "सप्ताह में 1-2 बार एक्सफोलिएट करने से मृत त्वचा कोशिकाएं हट जाती हैं, जिससे एक चमकदार रंगत मिलती है और उत्पादों को बेहतर ढंग से अवशोषित होने में मदद मिलती है।", "एएचए/बीएचए एक्सफोलिएंट, एक्सफोलिएटिंग टोनर"),
        ("Don't Skip the Sunscreen", "सनस्क्रीन आपकी त्वचा को हानिकारक यूवी किरणों से बचाता है, जिससे समय से पहले बूढ़ा होना, काले धब्बे और त्वचा कैंसर नहीं होता है।", "ब्रॉड-स्पेक्ट्रम एसपीएफ 30+ सनस्क्रीन"),
        ("Use a Vitamin C Serum", "विटामिन सी एक शक्तिशाली एंटीऑक्सीडेंट है जो त्वचा को मुक्त कणों से बचाता है, रंगत को चमकदार बनाता है, और कोलेजन उत्पादन को उत्तेजित करता है।", "विटामिन सी सीरम"),
        ("Moisturize, Moisturize, Moisturize", "मॉइस्चराइजिंग आपकी त्वचा के सुरक्षात्मक अवरोध को बनाए रखने में मदद करता है, जिससे यह नरम और कोमल रहती है।", "अपनी त्वचा के प्रकार के लिए मॉइस्चराइजर"),
        ("Incorporate Retinol", "रेटिनोल कोशिका नवीनीकरण को बढ़ाता है, जिससे झुर्रियां, महीन रेखाएं और मुंहासे कम होते हैं। धीरे-धीरे शुरू करें और इसे रात में उपयोग करें।", "रेटिनोल सीरम या क्रीम"),
        ("Treat Your Neck and Chest", "ये क्षेत्र आपके चेहरे की तरह ही बुढ़ापे के प्रति संवेदनशील होते हैं। अपनी स्किनकेयर रूटीन को अपनी गर्दन और छाती तक बढ़ाएं।", "कोई भी फेस सीरम या क्रीम"),
        ("Check the Ingredients", "अपने उत्पादों में क्या है यह जानने से आपको परेशानियों से बचने और उन सामग्रियों को खोजने में मदद मिलती है जो आपकी विशिष्ट चिंताओं को दूर करती हैं।", "सामग्री जांचकर्ता (इस ऐप की तरह!)"),
        ("Don't Over-Exfoliate", "अत्यधिक एक्सफोलिएशन आपकी त्वचा के अवरोध को नुकसान पहुंचा सकता है, जिससे जलन, लालिमा और मुंहासे हो सकते हैं।", "सप्ताह में 1-2 बार एक्सफोलिएशन सीमित करें"),
        ("Use a Gentle Cleanser", "कठोर क्लींज़र आपकी त्वचा के प्राकृतिक तेलों को छीन सकते हैं, जिससे सूखापन या तेल का अत्यधिक उत्पादन हो सकता है।", "हल्का, पीएच-संतुलित क्लींज़र"),
        ("Pat, Don't Rub", "तौलिए से अपनी त्वचा को थपथपा कर सुखाना अधिक कोमल होता है और अनावश्यक घर्षण और जलन को रोकता है।", "नरम फेस टॉवल"),
        ("Change Your Pillowcases", "तकिए के कवर में बैक्टीरिया और तेल जमा हो सकते हैं, जिससे मुंहासे हो सकते हैं। उन्हें सप्ताह में कम से कम एक बार बदलें।", "सिल्क या साटन तकिए के कवर एक बोनस हैं"),
        ("Get Enough Sleep", "नींद वह समय है जब आपकी त्वचा खुद की मरम्मत करती है। नींद की कमी से सुस्ती और आंखों के नीचे बैग हो सकते हैं।", "आई क्रीम"),
        ("Manage Your Stress", "उच्च तनाव का स्तर मुंहासे, सोरायसिस और एक्जिमा जैसी त्वचा समस्याओं को ट्रिगर कर सकता है।", "तनाव प्रबंधन तकनीक"),
        ("Clean Your Phone Screen", "आपका फोन स्क्रीन बैक्टीरिया और गंदगी को आपके चेहरे पर स्थानांतरित कर सकता है, जिससे आपके गालों और जबड़े पर मुंहासे हो सकते हैं।", "अल्कोहल वाइप्स"),
        ("Stay Away from Hot Water", "गर्म पानी आपकी त्वचा के प्राकृतिक तेलों को छीन सकता है। इसके बजाय साफ़ करने के लिए गुनगुने पानी का उपयोग करें।", "गुनगुना पानी"),
        ("Protect Your Hands", "आपके हाथों की त्वचा पर बुढ़ापे के लक्षण जल्दी दिख सकते हैं। नियमित रूप से हैंड क्रीम और सनस्क्रीन का उपयोग करें।", "एसपीएफ वाली हैंड क्रीम"),
        ("Listen to Your Skin", "ध्यान दें कि आपकी त्वचा उत्पादों और पर्यावरणीय परिवर्तनों पर कैसे प्रतिक्रिया करती है। तदनुसार अपनी दिनचर्या को समायोजित करें।", "ज्ञान और धैर्य"),
        ("Use a Humidifier", "एक ह्यूमिडिफायर सूखे वातावरण में हवा में नमी जोड़ने में मदद कर सकता है, जिससे आपकी त्वचा हाइड्रेटेड रहती है।", "ह्यूमिडिफायर"),
        ("Incorporate an Antioxidant", "विटामिन ई, फेरुलिक एसिड, और ग्रीन टी जैसे एंटीऑक्सीडेंट आपकी त्वचा को पर्यावरणीय हमलावरों से बचाते हैं।", "एंटीऑक्सीडेंट सीरम"),
        ("Try a Face Massage", "नियमित फेस मसाज रक्त परिसंचरण और लसीका जल निकासी में सुधार करने में मदद कर सकते हैं, जिससे आपकी त्वचा को एक स्वस्थ चमक मिलती है।", "फेस रोलर या गुआ शा"),
        ("Be Patient", "स्किनकेयर एक मैराथन है, न कि स्प्रिंट। नए उत्पादों को परिणाम दिखाने के लिए कम से कम 4-6 सप्ताह दें।", "धैर्य"),
        ("Avoid Touching Your Face", "अपने चेहरे को छूने से गंदगी और बैक्टीरिया स्थानांतरित हो सकते हैं, जिससे मुंहासे हो सकते हैं।", "सचेत प्रयास"),
        ("Wash Your Makeup Brushes", "गंदे ब्रश बैक्टीरिया के लिए एक प्रजनन स्थल हो सकते हैं, जिससे मुंहासे होते हैं। उन्हें सप्ताह में एक बार धोएं।", "मेकअप ब्रश क्लींजर")
    ]
    
    for i, (tip, benefit, product) in enumerate(tips):
        st.markdown(f"""
        <div class="tip-container">
            <h4 style="color: #4A90E2;">{i+1}. {tip}</h4>
            <p><strong>लाभ:</strong> {benefit}</p>
            <p><strong>उत्पाद अनुशंसा:</strong> {product}</p>
        </div>
        """, unsafe_allow_html=True)

def show_daily_routine_checker():
    st.title("Daily Routine Checker")
    st.markdown("आज आपके द्वारा पूरे किए गए कार्यों को चिह्नित करें ताकि आपके स्कोर के लिए अंक मिल सकें।")
    
    tasks = [
        "Washed face with cleanser (morning)",
        "Used a Vitamin C serum",
        "Applied a broad-spectrum sunscreen",
        "Drank at least 2 liters of water",
        "Ate a healthy, balanced meal",
        "Washed face with cleanser (night)",
        "Double-cleansed to remove makeup/sunscreen",
        "Used a targeted serum (e.g., Retinol, Niacinamide)",
        "Applied a hydrating moisturizer",
        "Got at least 7 hours of sleep",
        "Avoided touching your face throughout the day",
        "Washed your hands before starting your routine",
        "Did not pick at any blemishes",
        "Changed your pillowcase (if applicable)",
        "Avoided processed foods and sugary drinks"
    ]
    
    st.markdown("---")
    
    score = 0
    with st.form("routine_checker_form"):
        for i, task in enumerate(tasks):
            col1, col2 = st.columns([0.1, 0.9])
            with col1:
                checkbox_val = st.checkbox("", key=f"task_{i}")
            with col2:
                st.write(task)
            if checkbox_val:
                score += 5
            else:
                score -= 5
        
        submitted = st.form_submit_button("Calculate My Score")
    
    if submitted:
        st.markdown("---")
        st.header("Your Daily Score:")
        if score > 0:
            st.success(f"You earned {score} points today! Great job!")
        elif score == 0:
            st.warning(f"Your score is {score}. There's room for improvement!")
        else:
            st.error(f"Your score is {score}. Let's try to improve tomorrow!")


# --- Main App Navigation ---
def main():
    st.sidebar.title("Navigation")
    
    # Define pages with correct order and login-based visibility
    pages = {
        "Login / Register": show_login_register,
        "Skincare Pro Analyzer": show_skincare_analyzer,
        "Daily Routine Checker": show_daily_routine_checker,
        "AI Skincare Chatbot": show_chatbot,
        "Daily Skincare Tips": show_daily_tips,
        "Hyper-Personalized Advice": show_hyper_personalized_advice,
        "25 Skincare Tips": show_25_tips,
        "Skin Prediction AI": show_skin_prediction_ai,
        "Skin Health Comparator": show_skin_comparator,
        "Voice Assistant": show_voice_assistant,
        "Skincare Gamification": show_skincare_gamification,
    }
    
    # Initialize session state for login and points
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'points' not in st.session_state:
        st.session_state.points = 0
    
    # Show login page if not logged in
    if not st.session_state.logged_in:
        selected_page = st.sidebar.radio("Go to", ["Login / Register"])
        show_login_register()
    else:
        # Show all pages after successful login
        selected_page = st.sidebar.radio("Go to", list(pages.keys()))
        
        # Add 5 points for each page view
        if 'current_page' not in st.session_state or st.session_state.current_page != selected_page:
            st.session_state.current_page = selected_page
            st.session_state.points += 5
        
        st.sidebar.markdown(f"<div class='points-display'>Points: {st.session_state.points}</div>", unsafe_allow_html=True)
        
        pages[selected_page]()

if __name__ == "__main__":
    main()
