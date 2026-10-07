# Project_on_Restaurant_Bill_Generator
# 🍽️ Restaurant Bill Generator

A simple and beginner-friendly restaurant billing application built using **Python and Streamlit**.

The application allows users to select food items, enter quantities, apply discounts and GST, and generate a clean restaurant bill.

## 🚀 Features

* 🍔 Select food items
* 🔢 Enter quantities
* 🧾 Calculate item-wise cost
* 💸 Apply discounts
* 🧮 Calculate GST
* 💰 Display subtotal
* 💰 Display grand total
* 👤 Enter customer name
* 📅 Display bill date and time
* 📱 Mobile-friendly Streamlit interface
* ✨ Simple and clean user interface
* ✅ Input validation

## 🛠️ Technologies Used

* Python
* Streamlit

## 📁 Project Structure

```text
restaurant-bill-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Run the Project Locally

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project

```bash
cd restaurant-bill-generator
```

### Step 3: Install Streamlit

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

Usually the local address is:

```text
http://localhost:8501
```

## 🧮 Bill Calculation

The application follows these calculations:

### Subtotal

```text
Subtotal = Sum of all item costs
```

### Discount

```text
Discount Amount = Subtotal × Discount Percentage / 100
```

### Amount After Discount

```text
Amount After Discount = Subtotal - Discount Amount
```

### GST

```text
GST Amount = Amount After Discount × GST Percentage / 100
```

### Grand Total

```text
Grand Total = Amount After Discount + GST Amount
```

## 🧪 Testing

The application should be tested using the following cases:

### Test Case 1: No customer name

Expected result:

```text
Please enter the customer name.
```

### Test Case 2: No food item selected

Expected result:

```text
Please select at least one food item.
```

### Test Case 3: One item

Select one food item with quantity 1.

Expected result:

* Correct item price
* Correct subtotal
* Correct GST
* Correct grand total

### Test Case 4: Multiple items

Select multiple food items with different quantities.

Expected result:

* Each item appears in the bill
* Each item total is calculated correctly
* Subtotal is correct

### Test Case 5: Discount

Enter a discount such as:

```text
10%
```

Expected result:

```text
Discount = Subtotal × 10%
```

### Test Case 6: Different GST

Test:

```text
0%
5%
12%
18%
```

The GST amount should change accordingly.

### Test Case 7: Mobile testing

Open the deployed application on a mobile browser and verify:

* Menu is readable
* Quantity controls work
* Buttons are visible
* Bill is readable
* Grand total is visible
* No horizontal scrolling is required

## 🚀 GitHub

The project can be uploaded to GitHub using Git.

```bash
git init
git add .
git commit -m "Initial commit - Restaurant Bill Generator"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with GitHub.
4. Create a new app.
5. Select this GitHub repository.
6. Select the `main` branch.
7. Select `app.py` as the main file.
8. Deploy the application.

After deployment, Streamlit will provide a public application URL.

## 📱 Mobile Testing

Open the deployed Streamlit URL on a smartphone.

Test:

* Customer name input
* Food selection
* Quantity selection
* GST
* Discount
* Generate Bill button
* Grand total
* Different screen sizes

## 🎯 Future Improvements

Possible future features include:

* 🖨️ Print bill
* 📄 Download bill as PDF
* 🧾 Generate invoice number
* 🍕 Add/remove menu items
* 💳 Payment method selection
* 📊 Daily sales dashboard
* 💾 Store previous bills
* 🔐 Admin login

## 👨‍💻 Author

Restaurant Bill Generator project built using Python and Streamlit.

---

⭐ If you find this project useful, consider giving the repository a star!
