import streamlit as st
from datetime import datetime

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Restaurant Bill Generator",
    page_icon="🍽️",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 25px;
}

.bill-box {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-top: 20px;
}

.total-box {
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    border: 2px solid #333;
    margin-top: 15px;
}

.total-amount {
    font-size: 30px;
    font-weight: 700;
}

.small-text {
    color: #666;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# RESTAURANT DETAILS
# =========================================================

RESTAURANT_NAME = "Tasty Bites Restaurant"

MENU = {
    "Veg Burger": 120,
    "Cheese Pizza": 250,
    "French Fries": 100,
    "Veg Noodles": 180,
    "Paneer Biryani": 220,
    "Masala Dosa": 100,
    "Ice Cream": 80,
    "Cold Drink": 60
}

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🍽️ Tasty Bites</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Restaurant Bill Generator</div>',
    unsafe_allow_html=True
)

# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.subheader("👤 Customer Details")

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter customer name"
)

# =========================================================
# MENU SELECTION
# =========================================================

st.subheader("🍔 Select Food Items")

selected_items = []

for item, price in MENU.items():

    col1, col2, col3 = st.columns([2.5, 1.5, 1])

    with col1:
        st.write(f"**{item}**")
        st.caption(f"₹{price:.2f} per item")

    with col2:
        quantity = st.number_input(
            f"Quantity for {item}",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key=f"quantity_{item}",
            label_visibility="collapsed"
        )

    with col3:
        st.write(f"₹{price * quantity:.2f}")

    if quantity > 0:
        selected_items.append(
            {
                "item": item,
                "price": price,
                "quantity": quantity,
                "total": price * quantity
            }
        )

# =========================================================
# BILL SETTINGS
# =========================================================

st.subheader("💸 Bill Settings")

col1, col2 = st.columns(2)

with col1:
    gst_rate = st.selectbox(
        "GST",
        [0, 5, 12, 18],
        index=1
    )

with col2:
    discount_rate = st.number_input(
        "Discount (%)",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=1.0
    )

# =========================================================
# GENERATE BILL
# =========================================================

if st.button("🧾 Generate Bill", use_container_width=True):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not customer_name.strip():
        st.warning("⚠️ Please enter the customer name.")

    elif not selected_items:
        st.warning("⚠️ Please select at least one food item.")

    else:

        # -------------------------------------------------
        # CALCULATIONS
        # -------------------------------------------------

        subtotal = sum(item["total"] for item in selected_items)

        discount_amount = subtotal * (discount_rate / 100)

        amount_after_discount = subtotal - discount_amount

        gst_amount = amount_after_discount * (gst_rate / 100)

        grand_total = amount_after_discount + gst_amount

        # -------------------------------------------------
        # BILL DISPLAY
        # -------------------------------------------------

        st.success("✅ Bill generated successfully!")

        st.markdown('<div class="bill-box">', unsafe_allow_html=True)

        st.markdown(
            f"""
            <h2 style="text-align:center;">🍽️ {RESTAURANT_NAME}</h2>
            <p style="text-align:center;">
                <b>Customer:</b> {customer_name}
            </p>
            <p style="text-align:center;" class="small-text">
                Date: {datetime.now().strftime("%d-%m-%Y %I:%M %p")}
            </p>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # -------------------------------------------------
        # ITEM-WISE BILL
        # -------------------------------------------------

        st.markdown("### 🧾 Order Details")

        for item in selected_items:

            col1, col2, col3, col4 = st.columns([2.5, 1, 1, 1])

            with col1:
                st.write(item["item"])

            with col2:
                st.write(f"{item['quantity']}")

            with col3:
                st.write(f"₹{item['price']:.2f}")

            with col4:
                st.write(f"₹{item['total']:.2f}")

        st.divider()

        # -------------------------------------------------
        # BILL SUMMARY
        # -------------------------------------------------

        st.markdown("### 💰 Bill Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Subtotal")
            st.write(f"Discount ({discount_rate:.0f}%)")
            st.write(f"GST ({gst_rate}%)")
            st.markdown("### Grand Total")

        with col2:
            st.write(f"₹{subtotal:.2f}")
            st.write(f"- ₹{discount_amount:.2f}")
            st.write(f"₹{gst_amount:.2f}")
            st.markdown(f"### ₹{grand_total:.2f}")

        st.markdown('</div>', unsafe_allow_html=True)

        # -------------------------------------------------
        # GRAND TOTAL
        # -------------------------------------------------

        st.markdown(
            f"""
            <div class="total-box">
                <div>💰 GRAND TOTAL</div>
                <div class="total-amount">₹{grand_total:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">
        <p>🍽️ Thank you for visiting Tasty Bites!</p>
        <p class="small-text">Restaurant Bill Generator • Built with Python & Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)