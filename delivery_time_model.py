# delivery_time_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load datasets
base_path = r"C:\Users\yashp\Downloads\Week 6 - Dependencies\Dependencies\data"
orders = pd.read_csv(f"{base_path}\\olist_orders_dataset.csv")
items = pd.read_csv(f"{base_path}\\olist_order_items_dataset.csv")
products = pd.read_csv(f"{base_path}\\olist_products_dataset.csv")

# Merge datasets
df = pd.merge(orders, items, on='order_id')
df = pd.merge(df, products, on='product_id')

# Remove rows with missing dates
df = df.dropna(subset=['order_delivered_customer_date', 'order_approved_at'])

# Convert to datetime
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])

# Calculate delivery time in days
df['delivery_time_days'] = (df['order_delivered_customer_date'] - df['order_approved_at']).dt.days

# Drop any negative or zero delivery time values
df = df[df['delivery_time_days'] > 0]

# Select features
df_model = df[['product_category_name', 'price', 'freight_value', 'delivery_time_days']].dropna()

# Encode categorical feature
le = LabelEncoder()
df_model['product_category_encoded'] = le.fit_transform(df_model['product_category_name'])

# Features and label
X = df_model[['product_category_encoded', 'price', 'freight_value']]
y = df_model['delivery_time_days']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model and scaler
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("Model training complete and saved.")
