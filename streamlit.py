
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px


# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("data_saudi_used_cars.csv")  # Replace with actual file path
    return data

data = load_data()

# Aggregate data by city
city_data = data['city'].value_counts().reset_index()
city_data.columns = ['city', 'listings']

# Mapping Saudi cities to coordinates (for visualization)
city_coordinates = {
    'Riyadh': [24.7136, 46.6753],
    'Jeddah': [21.4858, 39.1925],
    'Dammam': [26.4207, 50.0888],
    'Khobar': [26.2172, 50.1972],
    'Makkah': [21.3891, 39.8579],
    'Madinah': [24.5247, 39.5692],
    'Abha': [18.2164, 42.5046],
    'Taif': [21.4373, 40.5127]
}

# Create base map
m = folium.Map(location=[23.8859, 45.0792], zoom_start=5)

# Add city markers
for city, coords in city_coordinates.items():
    if city in city_data['city'].values:
        folium.Marker(
            location=coords,
            popup=city,
            tooltip=f"{city} - {city_data[city_data['city'] == city]['listings'].values[0]} listings"
        ).add_to(m)

# Streamlit App
st.title("Used Car Market in Saudi Arabia")
st.subheader("Top Cities for Used Car Listings")
folium_static(m)

# City selection
selected_city = st.selectbox("Select a city", city_data['city'].unique())

if selected_city:
    city_specific_data = data[data['city'] == selected_city]
    top_brands = city_specific_data['brand'].value_counts().head(5)
    st.subheader(f"Top Car Brands in {selected_city}")
    st.bar_chart(top_brands)

    selected_brand = st.selectbox("Select a brand", top_brands.index)
    
    if selected_brand:
        brand_specific_data = city_specific_data[city_specific_data['brand'] == selected_brand]
        top_models = brand_specific_data['model'].value_counts().head(3)
        st.subheader(f"Top 3 Models of {selected_brand} in {selected_city}")
        st.write(top_models)
        
        # Price Distribution
        st.subheader("Price Distribution for Selected Brand")
        fig = px.histogram(brand_specific_data, x='price', nbins=20, title=f'Price Distribution of {selected_brand} in {selected_city}')
        st.plotly_chart(fig)
        
        # Feature-Based Price Analysis
        st.subheader("Factors Influencing Price")
        numeric_columns = ['mileage', 'year']
        selected_factor = st.selectbox("Select a factor", numeric_columns)
        
        fig = px.scatter(brand_specific_data, x=selected_factor, y='price', trendline='ols', title=f'Impact of {selected_factor} on Price')
        st.plotly_chart(fig)
        
        # Filter by Year
        selected_year = st.slider("Filter by Car Year", int(data['year'].min()), int(data['year'].max()), (2019, 2022))
        filtered_data = brand_specific_data[(brand_specific_data['year'] >= selected_year[0]) & (brand_specific_data['year'] <= selected_year[1])]
        st.subheader(f"Filtered Cars from {selected_year[0]} to {selected_year[1]}")
        st.write(filtered_data[['model', 'year', 'price', 'mileage']].head(10))
