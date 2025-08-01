import streamlit as st

st.set_page_config(page_title="RIVLux – Luxury Property ROI Calculator", layout="centered")

st.title("🏠 RIVLux – Luxury Property ROI Calculator")
st.subheader("For Elite Real Estate Investors")

st.markdown("Enter your property details below:")

# User Inputs
property_price = st.number_input("Property Price (USD)", min_value=1000.0, value=100000.0, step=1000.0)
monthly_rent = st.number_input("Monthly Rent (USD)", min_value=100.0, value=1000.0, step=50.0)
monthly_expenses = st.number_input("Monthly Expenses (USD)", min_value=0.0, value=200.0, step=50.0)
years = st.slider("Investment Duration (Years)", 1, 30, 5)
exchange_rate = st.number_input("USD to PKR Rate", min_value=50.0, value=280.0)

# Calculations
total_income = monthly_rent * 12 * years
total_expenses = monthly_expenses * 12 * years
net_profit = total_income - total_expenses
roi_percent = (net_profit / property_price) * 100
breakeven = property_price / max((monthly_rent - monthly_expenses), 1)
net_profit_pkr = net_profit * exchange_rate

# Display Results
st.markdown("### 📊 Results")
st.write(f"**Total Rental Income (USD):** ${total_income:,.2f}")
st.write(f"**Total Expenses (USD):** ${total_expenses:,.2f}")
st.write(f"**Net Profit (USD):** ${net_profit:,.2f}")
st.write(f"**ROI:** {roi_percent:.2f}%")
st.write(f"**Breakeven Period:** {breakeven:.1f} months")
st.write(f"**Net Profit (PKR):** Rs. {net_profit_pkr:,.0f}")

st.markdown("—")
st.caption("Powered by RIVLux | Designed for elite property investors")
