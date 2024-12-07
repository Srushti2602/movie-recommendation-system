import pandas as pd
import streamlit as st

# Paths to data
MAPPED_RECOMMENDATIONS_FILE = "new_mapped_recommendations.csv"

# Load recommendations
@st.cache_data
def load_data():
    return pd.read_csv(MAPPED_RECOMMENDATIONS_FILE)

mapped_recommendations = load_data()

# Streamlit Dashboard
st.title("🎥 Movie Recommendation System")
st.sidebar.header("User Input")

# Dropdown for movie selection
movie_list = mapped_recommendations["Title"].tolist()
selected_movie = st.sidebar.selectbox("Select a movie you like:", movie_list)

if st.sidebar.button("Get Recommendations"):
    with st.spinner("Fetching your recommendations..."):
        try:
            # Fetch recommendations for the selected movie
            movie_recommendation = mapped_recommendations[mapped_recommendations["Title"] == selected_movie]
            
            if not movie_recommendation.empty:
                recommended_titles = movie_recommendation.iloc[0]["RecommendedTitles"].split('|')
                st.subheader(f"Top Recommendations for '{selected_movie}':")
                for recommended_title in recommended_titles:
                    st.write(recommended_title)
            else:
                st.warning("No recommendations found for the selected movie.")
        except Exception as e:
            st.error(f"An error occurred: {e}")