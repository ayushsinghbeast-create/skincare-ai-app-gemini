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
    This is a placeholder for the login and registration function.
    A full implementation would require a backend database like Firebase or a similar service to handle user authentication.
    """)
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")
    st.markdown("---")
    st.header("New User?")
    st.button("Register")

def show_skincare_analyzer():
    st.markdown("<h1 class='main-header'>Skincare Pro Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("Upload a clear photo and enter your health and lifestyle details to analyze your skin.")
    
    st.header("Upload Photo")
    uploaded_file = st.file_uploader("Drag and drop a file here or click to browse", type=["jpg", "jpeg", "png"])
    
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
    st.markdown("Follow these essential daily tips to stay on top of your skincare routine.")
    
    st.subheader("Morning Routine:")
    st.markdown("- **Tip 1:** Wash your face with a gentle cleanser to remove overnight impurities.")
    st.markdown("- **Tip 2:** Apply a Vitamin C serum to protect against environmental damage.")
    st.markdown("- **Tip 3:** Always finish with a broad-spectrum sunscreen of at least SPF 30.")
    
    st.subheader("Evening Routine:")
    st.markdown("- **Tip 1:** Double cleanse your face to effectively remove makeup and sunscreen.")
    st.markdown("- **Tip 2:** Use a treatment product like a Retinol or AHA/BHA serum.")
    st.markdown("- **Tip 3:** Lock in moisture with a rich moisturizer to help your skin repair overnight.")

def show_chatbot():
    st.title("AI Skincare Chatbot")
    st.markdown("Click on a question to reveal the answer.")
    
    qa_pairs = {
        "What is the best way to get rid of blackheads?": "Blackheads can be effectively removed by using products with salicylic acid (BHA) or by incorporating a clay mask into your routine. Gentle exfoliation is key.",
        "How can I reduce redness and irritation on my skin?": "To reduce redness, look for calming ingredients like Centella Asiatica (Cica), Niacinamide, or Green Tea extract. Avoid harsh scrubs and fragrances.",
        "What is the difference between AHA and BHA?": "AHAs (Alpha Hydroxy Acids) like glycolic acid work on the skin's surface. BHAs (Beta Hydroxy Acids) like salicylic acid penetrate deeper into pores to clear oil and debris.",
        "Is it necessary to use a toner?": "A toner is not always necessary, but it can be a great addition. Hydrating toners can prep the skin for serums, while exfoliating toners can aid in cell turnover.",
        "Can diet affect my skin?": "Yes, diet plays a significant role. Foods rich in antioxidants, healthy fats, and vitamins can improve skin health, while high-sugar or processed diets can contribute to acne.",
        "What is a serum and how do I use it?": "A serum is a concentrated formula with active ingredients to target specific concerns. Apply it after cleansing and toning, and before moisturizing.",
        "How do I choose the right sunscreen?": "Choose a broad-spectrum sunscreen with at least SPF 30. For sensitive skin, look for mineral sunscreens with zinc oxide or titanium dioxide.",
        "What are the benefits of using a face mask?": "Face masks can provide a concentrated dose to address specific concerns like hydration, radiance, or oil control. Use them 1-2 times per week.",
        "Should I use an eye cream?": "Eye creams are specifically formulated for the delicate skin around the eyes. They can help with fine lines, puffiness, and dark circles.",
        "What is the importance of moisturizing?": "Moisturizing is crucial for all skin types as it helps maintain the skin's protective barrier, preventing water loss and protecting it from environmental irritants.",
        "How can I prevent premature aging?": "The best way to prevent premature aging is to use sunscreen daily, apply antioxidants like Vitamin C, and incorporate a retinoid into your nighttime routine.",
        "What is the best way to treat acne scars?": "Acne scars can be treated with products containing retinoids, Vitamin C, or AHAs. For more severe scars, professional treatments like microneedling or laser therapy may be necessary.",
        "Why is my skin suddenly breaking out?": "Breakouts can be caused by various factors including hormonal changes, stress, diet, using a new product, or environmental factors like humidity.",
        "What are ceramides and why are they important?": "Ceramides are lipids that help form the skin's barrier. They are essential for retaining moisture and protecting the skin from external irritants. They are great for all skin types, especially dry or sensitive skin.",
        "How do I determine my skin type?": "To determine your skin type, wash your face and wait an hour without applying any products. If your skin feels tight and flaky, it's dry. If it's shiny, it's oily. If it's a mix, it's combination. If it feels balanced, it's normal."
    }
    
    for question, answer in qa_pairs.items():
        with st.expander(question):
            st.markdown(f"**Answer:** {answer}")

def show_skin_comparator():
    st.title("Skin Health Comparator")
    st.markdown("Compare your skin's report to an ideal report and discover your areas for improvement.")
    
    st.header("Upload Your Skin Report")
    uploaded_file = st.file_uploader("Upload your previous skin report here (PNG, JPG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        st.subheader("Your Report:")
        st.image(uploaded_file, use_column_width=True)
        
        st.markdown("---")
        
        st.subheader("Ideal Skin Report (Reference):")
        st.markdown("""
        <div class="comparison-container">
            <h4>Ideal Skin Report</h4>
            <ul>
                <li><strong>Hydration Level:</strong> Excellent</li>
                <li><strong>Texture:</strong> Very smooth</li>
                <li><strong>Pores:</strong> Small and clear</li>
                <li><strong>Radiance:</strong> Very glowing</li>
                <li><strong>Acne/Spots:</strong> None</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.header("Comparative Analysis")
        st.markdown("The main differences between your report and the ideal report are highlighted below:")

        defects = {
            "Texture": "Some roughness and uneven texture",
            "Hydration": "Dryness and dehydration",
            "Pores": "Some visible and clogged pores",
        }
        
        for flaw, description in defects.items():
            st.error(f"**{flaw} Defect:** {description}")

        st.markdown("---")
        st.header("Product Recommendations")
        st.markdown("Products specifically recommended to address your deficiencies:")
        
        st.info("**Texture & Unevenness:** Use an AHA/BHA serum like Glycolic Acid or Salicylic Acid.")
        st.info("**Hydration:** Use a Hyaluronic Acid or Ceramide-infused moisturizer.")
        st.info("**Pores:** Try a clay mask or a Niacinamide serum to deeply cleanse your pores.")
        

def show_voice_assistant():
    st.title("Voice Assistant (Coming Soon)")
    st.info("This feature will require text-to-speech (TTS) and speech-to-text (STT) APIs to function. This is a placeholder for future development.")
    st.markdown("Imagine being able to ask questions about your skincare routine and getting an answer in a human voice.")

def show_skin_prediction_ai():
    st.title("Skin Prediction AI")
    st.markdown("Answer a few questions about your habits to predict your skin's future.")

    questions = [
        "Do you drink more than 2 liters of water per day?",
        "Do you sleep for at least 7 hours every night?",
        "Do you exercise regularly?",
        "Do you apply sunscreen on your face daily?",
        "Do you eat fruits and vegetables daily?",
        "Do you practice stress management techniques?",
        "Do you wash your face daily (morning and evening)?",
        "Do you clean your makeup brushes every week?",
        "Do you apply an anti-pollution serum before going out?",
        "Do you remove your makeup before sleeping at night?",
        "Do you moisturize your face daily?",
        "Do you consume a lot of sugary and processed foods?",
        "Do you spend a lot of time in direct sunlight?",
        "Do you consume alcohol or smoke?",
        "Do you touch your face many times during the day?"
    ]

    st.markdown("---")
    
    with st.form("prediction_form"):
        user_answers = {}
        for i, question in enumerate(questions):
            answer = st.radio(question, ("Yes", "No"), key=f"q_{i}")
            user_answers[question] = answer
        
        submitted = st.form_submit_button("View Prediction")
    
    if submitted:
        st.markdown("---")
        with st.spinner('Analyzing your skin\'s future...'):
            time.sleep(3)

        good_habits = 0
        bad_habits = 0

        # Scoring logic
        for q, a in user_answers.items():
            if q in questions[0:11]: # Positive habits
                if a == "Yes":
                    good_habits += 1
                else:
                    bad_habits += 1
            else: # Negative habits
                if a == "No":
                    good_habits += 1
                else:
                    bad_habits += 1

        total_score = good_habits - bad_habits
        
        st.header("Your Skin's Future (in the next 6 months)")
        if total_score >= 8:
            st.success("Your skin will look very good and healthy in the next 6 months.")
            st.image("https://placehold.co/600x400/0000FF/FFFFFF?text=Healthy+Skin+Future", use_column_width=True)
            st.markdown("""
            Your good habits are very impactful. Your skin will look clear, radiant, and youthful. Continue with your routine.
            """)
        elif 3 <= total_score < 8:
            st.warning("Your skin will look good, but there's room for improvement.")
            st.image("https://placehold.co/600x400/FFA500/000000?text=Improving+Skin", use_column_width=True)
            st.markdown("""
            You have a mix of good and bad habits. Your skin can become even better by eliminating some of the bad habits.
            """)
        else:
            st.error("Your skin may face some challenges, but you can still improve it.")
            st.image("https://placehold.co/600x400/FF0000/FFFFFF?text=Challenging+Skin", use_column_width=True)
            st.markdown("""
            You need to change some habits to improve your skin's condition. Take your skincare routine seriously.
            """)

def show_skincare_gamification():
    st.title("Skincare Gamification (Coming Soon)")
    st.info("This feature will include daily challenges, points, and badges to make your skincare routine more fun and engaging. This is a placeholder for future development.")
    st.markdown("Earn points by completing your daily routine tasks and unlock new features or rewards!")

def show_hyper_personalized_advice():
    st.title("Hyper-Personalized Advice")
    st.markdown("Fill out this detailed questionnaire to get a custom routine for your skin.")
    
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
    st.markdown("A list of high-impact tips with their benefits and product recommendations.")
    
    tips = [
        ("Hydrate from Within", "Drinking enough water keeps your skin plump and hydrated, improving elasticity and overall health.", "Hydrating Cleanser, Hyaluronic Acid Serum"),
        ("Double Cleanse at Night", "The first cleanse removes makeup and sunscreen, while the second cleanse deeply purifies your pores, preventing breakouts.", "Oil-based Cleanser, Water-based Cleanser"),
        ("Exfoliate Regularly", "Exfoliating 1-2 times per week removes dead skin cells, giving you a brighter complexion and helping products absorb better.", "AHA/BHA Exfoliant, Exfoliating Toner"),
        ("Don't Skip the Sunscreen", "Sunscreen protects your skin from harmful UV rays, which cause premature aging, dark spots, and skin cancer.", "Broad-spectrum SPF 30+ Sunscreen"),
        ("Use a Vitamin C Serum", "Vitamin C is a powerful antioxidant that protects skin from free radicals, brightens the complexion, and stimulates collagen production.", "Vitamin C Serum"),
        ("Moisturize, Moisturize, Moisturize", "Moisturizing helps to maintain your skin's protective barrier, keeping it soft and supple.", "Moisturizer for your skin type"),
        ("Incorporate Retinol", "Retinol increases cell turnover, which helps to reduce wrinkles, fine lines, and acne. Start slowly and use it at night.", "Retinol Serum or Cream"),
        ("Treat Your Neck and Chest", "These areas are just as susceptible to aging as your face. Extend your skincare routine to your neck and chest.", "Any face serum or cream"),
        ("Check the Ingredients", "Knowing what is in your products helps you avoid irritants and find ingredients that address your specific concerns.", "Ingredient Checker (like this app!)"),
        ("Don't Over-Exfoliate", "Over-exfoliating can damage your skin's barrier, leading to irritation, redness, and breakouts.", "Limit exfoliation to 1-2 times per week"),
        ("Use a Gentle Cleanser", "Harsh cleansers can strip your skin of its natural oils, leading to dryness or excessive oil production.", "Mild, pH-balanced Cleanser"),
        ("Pat, Don't Rub", "Patting your skin dry with a towel is gentler and prevents unnecessary friction and irritation.", "Soft face towel"),
        ("Change Your Pillowcases", "Pillowcases can accumulate bacteria and oil, which can lead to breakouts. Change them at least once a week.", "Silk or satin pillowcases are a bonus"),
        ("Get Enough Sleep", "Sleep is when your skin repairs itself. A lack of sleep can lead to a dull complexion and under-eye bags.", "Eye Cream"),
        ("Manage Your Stress", "High stress levels can trigger skin issues like acne, psoriasis, and eczema.", "Stress management techniques"),
        ("Clean Your Phone Screen", "Your phone screen can transfer bacteria and dirt to your face, causing breakouts on your cheeks and jawline.", "Alcohol wipes"),
        ("Stay Away from Hot Water", "Hot water can strip your skin of its natural oils. Use lukewarm water for cleansing instead.", "Lukewarm water"),
        ("Protect Your Hands", "The skin on your hands can show signs of aging quickly. Use hand cream and sunscreen regularly.", "Hand cream with SPF"),
        ("Listen to Your Skin", "Pay attention to how your skin reacts to products and environmental changes. Adjust your routine accordingly.", "Knowledge and patience"),
        ("Use a Humidifier", "A humidifier can help add moisture to the air in dry environments, keeping your skin hydrated.", "Humidifier"),
        ("Incorporate an Antioxidant", "Antioxidants like Vitamin E, Ferulic Acid, and Green Tea protect your skin from environmental aggressors.", "Antioxidant Serum"),
        ("Try a Face Massage", "Regular face massages can help improve blood circulation and lymphatic drainage, giving your skin a healthy glow.", "Face roller or Gua Sha"),
        ("Be Patient", "Skincare is a marathon, not a sprint. Give new products at least 4-6 weeks to show results.", "Patience"),
        ("Avoid Touching Your Face", "Touching your face can transfer dirt and bacteria, leading to breakouts.", "Conscious effort"),
        ("Wash Your Makeup Brushes", "Dirty brushes can be a breeding ground for bacteria, causing breakouts. Wash them once a week.", "Makeup brush cleanser")
    ]
    
    for i, (tip, benefit, product) in enumerate(tips):
        st.markdown(f"""
        <div class="tip-container">
            <h4 style="color: #4A90E2;">{i+1}. {tip}</h4>
            <p><strong>Benefit:</strong> {benefit}</p>
            <p><strong>Product Recommendation:</strong> {product}</p>
        </div>
        """, unsafe_allow_html=True)

def show_daily_routine_checker():
    st.title("Daily Routine Checker")
    st.markdown("Mark the tasks you completed today to earn points for your score.")
    
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
    
    pages = {
        "Skincare Pro Analyzer": show_skincare_analyzer,
        "Daily Routine Checker": show_daily_routine_checker,
        "AI Skincare Chatbot": show_chatbot,
        "Daily Skincare Tips": show_daily_tips,
        "Hyper-Personalized Advice": show_hyper_personalized_advice,
        "25 Skincare Tips": show_25_tips,
        "Skin Prediction AI": show_skin_prediction_ai,
        "Login / Register": show_login_register,
        "Skin Health Comparator": show_skin_comparator,
        "Voice Assistant": show_voice_assistant,
        "Skincare Gamification": show_skincare_gamification,
    }
    
    if 'points' not in st.session_state:
        st.session_state.points = 0
    
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))
    
    if 'current_page' not in st.session_state or st.session_state.current_page != selected_page:
        st.session_state.current_page = selected_page
        st.session_state.points += 5
    
    st.sidebar.markdown(f"<div class='points-display'>Points: {st.session_state.points}</div>", unsafe_allow_html=True)
    
    pages[selected_page]()

if __name__ == "__main__":
    main()
