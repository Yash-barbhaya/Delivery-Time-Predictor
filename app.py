import streamlit as st

# App Title
st.title("🚚 Delivery Time Prediction App")

# UI Elements
st.header("Enter Package Details")

product_category = st.selectbox("Select Product Category", 
                                ["Electronics", "Clothing", "Home & Kitchen", "Books", "Other"])

customer_location = st.selectbox("Choose Customer Location", 
                                 ["Urban", "Suburban", "Rural"])

shipping_method = st.selectbox("Pick a Shipping Method", 
                               ["Standard", "Express", "Same-Day"])

shipping_priority = st.selectbox("Define Shipping Priority", 
                                 ["Normal", "High", "Urgent"])

weather = st.selectbox("Current Weather Conditions", 
                       ["Sunny", "Rainy", "Snowy", "Stormy"])

weight = st.number_input("Enter Package Weight (kg)", min_value=0.1, max_value=100.0, step=0.1)

package_size = st.selectbox("Choose Package Size", 
                            ["Small", "Medium", "Large"])

distance = st.number_input("Enter Distance to Destination (km)", min_value=1, max_value=5000, step=1)

warehouse_available = st.radio("Nearby Warehouse Availability?", 
                               ["Yes", "No"])

delivery_type = st.selectbox("Delivery Type", 
                             ["Residential", "Business"])


# Prediction Logic
if st.button("🚀 Predict Delivery Time"):
    base_time = 0

    if shipping_method == "Standard":
        base_time = 3
    elif shipping_method == "Express":
        base_time = 2
    else:
        base_time = 1  # Same-Day

    if customer_location == "Rural":
        base_time += 2
    if weather in ["Rainy", "Snowy", "Stormy"]:
        base_time += 1
    if weight > 10:
        base_time += 1
    if distance > 1000:
        base_time += 2
    if package_size == "Large":
        base_time += 1
    if warehouse_available == "Yes":
        base_time -= 1
    if delivery_type == "Business":
        base_time -= 1
    if shipping_priority == "Urgent":
        base_time = min(base_time, 2)

    base_time = max(1, base_time)

    st.success(f"Estimated Delivery Time: **{base_time} days**")
