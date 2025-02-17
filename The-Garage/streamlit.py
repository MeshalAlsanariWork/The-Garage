<<<<<<< HEAD
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display
import pandas as pd

# تحميل البيانات (استبدلها ببياناتك الفعلية)
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Type': ['Corolla', 'Camry', 'Corolla', 'Camry', 'Corolla'],
    'Count': [150, 120, 180, 160, 200]
}

type_by_year_region = pd.DataFrame(data)

# إعداد الخط العربي
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
prop = fm.FontProperties(fname=font_path)

reshaped_title = get_display(arabic_reshaper.reshape('عدد سيارات Toyota حسب النوع والسنة'))
reshaped_xlabel = get_display(arabic_reshaper.reshape('السنة'))
reshaped_ylabel = get_display(arabic_reshaper.reshape('عدد السيارات'))
reshaped_legend = get_display(arabic_reshaper.reshape('نوع السيارة'))

# إضافة الشعار والعنوان في Streamlit
col1, col2 = st.columns([1, 3])
with col1:
    st.image("IMG_4670.png", width=150)
with col2:
    st.title("السعوديين وتويوتا: علاقة أسطورية في سوق المستعمل!")

# إضافة الصورة بعد القسم "📈 شارت ولاء السعوديين لتويوتا"
# المقدمة
st.write(
    """
    لو تدخل أي **سوق سيارات مستعملة** في السعودية، أول شيء يلفت انتباهك؟ **تويوتا مسيطرة بكل مكان!** 🚗  
    بس وش السبب؟ ليش الناس تحب تشتري وتبيع تويوتا بالذات؟
    """
)

# ولاء السعوديين لتويوتا
st.write("### 📈 ولاء السعوديين لتويوتا")
st.image("image.png", width=850)
st.write(
    """
    العلاقة بدأت من أكثر من **45 سنة**، ولا زالت مستمرة لأن سيارات تويوتا تتميز بـ:
    
    ✅ **الاعتمادية الفوق العادة** – تمشي معك سنين وما تخذلك!  
    ✅ **الصيانة السهلة والرخيصة** – أي ورشة تفهم فيها.  
    ✅ **قطع الغيار بكل مكان** – ما تحتاج تدور أو تنتظر شحن.
    """
)

# أكثر السيارات المعروضة للبيع
st.write("### 🚙 شارت أكثر السيارات المعروضة للبيع")
st.image("image copy.png", width=850)

st.write(
    """
        - في **جدة**، الكامري أكثر سيارة معروضة للبيع، يمكن لأن أهلها يحبون السيارات الاقتصادية للكرف اليومي.  
    - في **الرياض**، الاندكروزر متصدر، لأن أهل العاصمة يعشقون الطلعات والبر ويحتاجون سيارة قوية.
    - زاد عدد سيارات **تويوتا** بشكل ملحوظ مع مرور السنوات، خاصة بعد عام 2010، ووصل إلى أعلى مستوياته بين عامي 2016 و2020. بعض الموديلات مثل **لاند كروزر، راف 4، وكامري** كانت الأكثر انتشارًا مقارنةً بالبقية.
    """
)
st.write(
    """
    تويوتا ما خلت أحد، عندها سيارات تناسب **كل الفئات**:
    
    - راعي **بر**؟ أكيد تفكر في **لاندكروزر** 🏜️  
    - طالب جامعي؟ **كامري** أو **كورولا** خيار ممتاز 🎓  
    - تدور سيارة اقتصادية وعملية؟ عندك **يارس** و**هايلكس** 💰
    """
)

# أكثر السيارات بيعًا حسب المناطق
st.write("### 📊 المناطق والسيارات الأكثر بيعًا")
st.image("image copy 2.png", width=850)
st.write(
    """
    - **لاند كروزر** متسيدة السوق 🚙💨
    - **الرياض** متصدرة بفرق كبير، بعدها الدمام، وجدة، وهذا يدل إن الناس يحبونها، خاصة في المدن الكبيرة والمناطق البرية.
    - **الكامري** عليها طلب بعد 🚗🔥
    - جالسة تنافس بقوة في **جدة** والقصيم وعسير، واضح إنها مفضلة عند اللي يدورون سيارات سيدان عملية.
    - **الهيلوكس** و**الكورولا** منتشرين بس مو بقوة 🛻🚘
        - الهيلوكس موجودة في بعض المناطق، يمكن اللي عندهم شغل في البر والمزارع يفضلونها.
        - الكورولا بعد متواجدة بس بشكل أقل، يمكن الناس تفضل السيارات الأكبر.
    """
)


# أكثر فئة مواصفات معروضة للبيع بالسوق السعودي
st.write("### أكثر فئة مواصفات معروضة للبيع بالسوق السعودي")
st.image("image copy 3.png", width=850)
st.write(
    """
    - **الفل كامل** مسيطر 🔥🔵
        - أغلب المناطق تفضل الفل كامل، واضح إن الناس يحبون المواصفات الكاملة وما يبون يتنازلون عن أي ميزة.
    - **السيمي فل** موجود بس مو بنفس القوة 🟠
        - فيه كم منطقة تفضل السيمي فل، يمكن عشان سعره يكون أقل شوي لكنه يعطي بعض المزايا المهمة.
    - **الستاندرد** قليل جداً 🟢
        - عدد قليل جداً من المناطق تفضل الستاندرد، وهذا يدل إن الناس يميلون للسيارات المجهزة بمواصفات أكثر، حتى لو كانت بس سيمي فل.
    """
)


# الخاتمة
st.write(
    """
    **الخلاصة؟** تويوتا في سوق المستعمل مثل الذهب، تمسك سعرها، وتلقى لها زبون بأي وقت! 🚗💰
    """
)

# رسم المخطط
fig, ax = plt.subplots(figsize=(14, 8))
sns.set_style("whitegrid")
sns.set_palette("bright")

hue_order = type_by_year_region['Type'].unique()
=======

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
>>>>>>> 0a6ea4ce5b09ef86c18cf993610f7872b31c581b
