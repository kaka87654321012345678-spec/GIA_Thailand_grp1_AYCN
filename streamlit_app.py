

import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime


st.set_page_config(page_title="🌱 ASEAN Youth Carbon Network", page_icon="🌱", layout="centered")

st.title("🌱 ASEAN Youth Carbon Network")
st.markdown("""
Welcome to the AYCN Streamlit App!
Please select a feature from the sidebar menu.
""")

# 主選單
menu = st.sidebar.selectbox(
    "選擇功能",
    ["📊 Dashboard", "🌿 Carbon Tracker", "🏆 Challenges", "🗺️ ASEAN Map", "📚 Learn"]
)

if menu == "📊 Dashboard":
    st.header("📊 AYCN PERSONAL DASHBOARD")
    st.markdown("""
    <div style='background: #E8F5E8; padding: 20px; border-radius: 10px; margin: 10px 0;'>
        <h3>👤 Your Sustainability Profile</h3>
        <p>🏆 <strong>Points:</strong> 150</p>
        <p>🌍 <strong>Carbon Reduced:</strong> 45 kg CO₂</p>
        <p>🏙️ <strong>City Rank:</strong> #3 in Jakarta</p>
        <p>📅 <strong>Active Streak:</strong> 7 days</p>
    </div>
    """, unsafe_allow_html=True)
    st.subheader("🚀 QUICK ACTIONS")
    col1, col2, col3 = st.columns(3)
    col1.button("📝 Log Today's Carbon")
    col2.button("🎯 Join Challenge")
    col3.button("📚 Take Eco-Course")
    st.subheader("📈 RECENT ACTIVITY")
    activities = [
        "✅ Biked to work - Saved 2.5 kg CO₂",
        "✅ Used reusable bag - Saved 0.1 kg CO₂",
        "✅ Plant-based lunch - Saved 3.0 kg CO₂",
        "🎯 Joined Green Commute Challenge"
    ]
    for activity in activities:
        st.write(activity)


elif menu == "🌿 Carbon Tracker":
    st.header("🌿 CARBON FOOTPRINT TRACKER")
    st.markdown("Record your carbon footprint, view history, and export your data!")

    # Initialize session state
    if 'carbon_entries' not in st.session_state:
        st.session_state['carbon_entries'] = []

    category = st.selectbox(
        "Category:",
        ['🚗 Transport', '💡 Energy', '🍽️ Lifestyle', '🗑️ Waste']
    )
    activities_dict = {
        '🚗 Transport': ['Car travel', 'Bus travel', 'Train travel', 'Flight'],
        '💡 Energy': ['Electricity use', 'Cooking gas', 'Heating'],
        '🍽️ Lifestyle': ['Beef meal', 'Chicken meal', 'Dairy products', 'Processed food'],
        '🗑️ Waste': ['Plastic waste', 'Food waste', 'Electronic waste']
    }
    units_dict = {'🚗 Transport': 'km', '💡 Energy': 'kWh', '🍽️ Lifestyle': 'meals', '🗑️ Waste': 'kg'}
    activity = st.selectbox("Activity:", activities_dict[category])
    amount = st.number_input("Amount:", min_value=0.0, value=10.0)
    unit = units_dict[category]
    notes = st.text_input("Notes (optional):")
    factors = {
        'Car travel': 0.2, 'Bus travel': 0.08, 'Train travel': 0.05, 'Flight': 0.25,
        'Electricity use': 0.5, 'Cooking gas': 2.5, 'Heating': 2.0,
        'Beef meal': 3.0, 'Chicken meal': 1.5, 'Dairy products': 1.2, 'Processed food': 0.8,
        'Plastic waste': 2.0, 'Food waste': 1.5, 'Electronic waste': 3.0
    }
    st.write(f"Unit: {unit}")

    if st.button("Save Entry"):
        carbon = amount * factors[activity]
        entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'category': category,
            'activity': activity,
            'amount': amount,
            'unit': unit,
            'carbon_kg': carbon,
            'notes': notes
        }
        st.session_state['carbon_entries'].append(entry)
        st.success(f"✅ Entry saved! {activity}: {amount} {unit}, {carbon:.2f} kg CO₂")

    # History
    st.subheader("📊 Carbon Tracking History")
    entries = st.session_state['carbon_entries']
    if entries:
        df = pd.DataFrame(entries)
        st.dataframe(df.tail(10))
        st.write(f"Total entries: {len(df)}")
        st.write(f"Total carbon tracked: {df['carbon_kg'].sum():.2f} kg CO₂")
        st.write(f"Average per entry: {df['carbon_kg'].mean():.2f} kg CO₂")
        # Export CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📄 Download CSV",
            data=csv,
            file_name=f"aycn_carbon_data_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime='text/csv'
        )
    else:
        st.info("No entries yet. Start tracking your carbon footprint! 🌱")

elif menu == "🏆 Challenges":
    st.header("🏆 ASEAN SUSTAINABILITY CHALLENGES")
    challenges = [
        {
            'name': 'Green Commute Week',
            'description': 'Use sustainable transport for 7 days',
            'participants': 150,
            'progress': 75,
            'reward': '100 points + Eco-Badge'
        },
        {
            'name': 'Energy Saving Month',
            'description': 'Reduce electricity consumption by 20%',
            'participants': 89,
            'progress': 45,
            'reward': '150 points + Energy Star'
        },
        {
            'name': 'Plastic Free Challenge',
            'description': 'Avoid single-use plastics for 30 days',
            'participants': 120,
            'progress': 60,
            'reward': '200 points + Plastic Warrior'
        }
    ]
    for i, challenge in enumerate(challenges, 1):
        st.subheader(f"{i}. {challenge['name']}")
        st.write(f"📝 {challenge['description']}")
        st.write(f"👥 {challenge['participants']} participants")
        st.write(f"📊 {challenge['progress']}% complete")
        st.write(f"🎁 Reward: {challenge['reward']}")
        if st.button(f"Join Challenge {i}"):
            st.success(f"🎉 You joined {challenge['name']}! Check your dashboard for progress tracking.")

elif menu == "🗺️ ASEAN Map":
    st.header("🗺️ ASEAN YOUTH CARBON INDEX")
    cities = {
        'Jakarta': {'carbon_reduced': 180, 'participants': 45, 'rank': 1},
        'Singapore': {'carbon_reduced': 150, 'participants': 38, 'rank': 2},
        'Manila': {'carbon_reduced': 120, 'participants': 42, 'rank': 3},
        'Bangkok': {'carbon_reduced': 110, 'participants': 35, 'rank': 4},
        'Kuala Lumpur': {'carbon_reduced': 95, 'participants': 28, 'rank': 5}
    }
    st.subheader("🏆 CITY LEADERBOARD:")
    for city, data in cities.items():
        st.write(f"{data['rank']}. {city}")
        st.write(f"🌱 {data['carbon_reduced']} kg CO₂ reduced")
        st.write(f"👥 {data['participants']} active participants")
    st.markdown("""
    ASEAN CARBON REDUCTION MAP:

    🇹🇭 Bangkok    [██████████] 110 kg
    🇮🇩 Jakarta    [███████████████] 180 kg
    🇲🇾 Kuala Lumpur [████████] 95 kg
    🇵🇭 Manila     [███████████] 120 kg
    🇸🇬 Singapore  [████████████] 150 kg

    █ = 10 kg CO₂ reduced
    """)

elif menu == "📚 Learn":
    st.header("📚 AYCN SUSTAINABILITY LEARNING HUB")
    courses = [
        {
            'title': 'Carbon Footprint Basics',
            'duration': '15 min',
            'level': 'Beginner',
            'description': 'Understand what carbon footprint means and how to calculate it'
        },
        {
            'title': 'Sustainable Transportation',
            'duration': '20 min',
            'level': 'Intermediate',
            'description': 'Learn about eco-friendly travel options in ASEAN cities'
        },
        {
            'title': 'Green Energy Solutions',
            'duration': '25 min',
            'level': 'Advanced',
            'description': 'Explore renewable energy and efficiency practices'
        }
    ]
    for i, course in enumerate(courses, 1):
        st.subheader(f"{i}. {course['title']}")
        st.write(f"⏱️ {course['duration']} | 🎯 {course['level']}")
        st.write(f"📖 {course['description']}")
        if st.button(f"Start Course {i}"):
            st.success(f"🎬 Starting: {course['title']}\n✅ Course completed! +25 points earned! 🎉")
