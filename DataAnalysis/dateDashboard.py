import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# Page Config
# =============================
st.set_page_config(
    page_title="Pizza Sales Analytics",
    page_icon="🍕",
    layout="wide"
)

# =============================
# Load Data
# =============================
@st.cache_data
def load_data():
    df = pd.read_csv("pizza_sales.csv")
    df["order_date"] = pd.to_datetime(df["order_date"], format="%d-%m-%Y")
    df["hour"] = pd.to_datetime(df["order_time"]).dt.hour

    # Profit calculation
    df["cost"] = df["unit_price"] * df["quantity"] * 0.6
    df["profit"] = df["total_price"] - df["cost"]

    return df

df = load_data()

# =============================
# Sidebar Filters
# =============================
st.sidebar.header("🔍 Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["order_date"].min(), df["order_date"].max()]
)

category = st.sidebar.multiselect(
    "Pizza Category",
    df["pizza_category"].unique(),
    default=df["pizza_category"].unique()
)

size = st.sidebar.multiselect(
    "Pizza Size",
    df["pizza_size"].unique(),
    default=df["pizza_size"].unique()
)

filtered_df = df[
    (df["order_date"] >= pd.to_datetime(date_range[0])) &
    (df["order_date"] <= pd.to_datetime(date_range[1])) &
    (df["pizza_category"].isin(category)) &
    (df["pizza_size"].isin(size))
]

# =============================
# KPIs
# =============================
st.title("🍕 Pizza Sales Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Revenue", f"${filtered_df.total_price.sum():,.2f}")
col2.metric("📦 Orders", filtered_df.order_id.nunique())
col3.metric("🍕 Pizzas Sold", filtered_df.quantity.sum())
col4.metric("📈 Profit", f"${filtered_df.profit.sum():,.2f}")

st.markdown("---")

# =============================
# Row 1 – Sales Trends
# =============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Daily Revenue Trend")
    daily = filtered_df.groupby("order_date")["total_price"].sum()
    fig, ax = plt.subplots()
    daily.plot(ax=ax)
    ax.set_ylabel("Revenue")
    st.pyplot(fig)

with col2:
    st.subheader("⏰ Hourly Sales Distribution")
    hourly = filtered_df.groupby("hour")["total_price"].sum()
    fig, ax = plt.subplots()
    hourly.plot(kind="bar", ax=ax)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Revenue")
    st.pyplot(fig)

# =============================
# Row 2 – Product Insights
# =============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Top 10 Pizzas by Quantity")
    top_pizzas = (
        filtered_df.groupby("pizza_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    fig, ax = plt.subplots()
    top_pizzas.plot(kind="barh", ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("📊 Revenue by Category")
    category_sales = filtered_df.groupby("pizza_category")["total_price"].sum()
    fig, ax = plt.subplots()
    category_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

# =============================
# Row 3 – Size & Profit
# =============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Revenue by Pizza Size")
    size_sales = filtered_df.groupby("pizza_size")["total_price"].sum()
    fig, ax = plt.subplots()
    size_sales.plot(kind="bar", ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("💹 Profit by Category")
    profit_cat = filtered_df.groupby("pizza_category")["profit"].sum()
    fig, ax = plt.subplots()
    profit_cat.plot(kind="bar", ax=ax)
    st.pyplot(fig)

# =============================
# Monthly Trend
# =============================
st.subheader("🗓️ Monthly Sales Trend")
filtered_df["month"] = filtered_df["order_date"].dt.to_period("M")
monthly = filtered_df.groupby("month")["total_price"].sum()

fig, ax = plt.subplots()
monthly.plot(ax=ax)
ax.set_ylabel("Revenue")
st.pyplot(fig)

# =============================
# Data Table
# =============================
with st.expander("📄 View Filtered Data"):
    st.dataframe(filtered_df)

st.markdown("---")
st.markdown("✅ **Advanced Dashboard built using Pandas & Streamlit**")