# ☕ Cafe Management System

A simple **console-based Cafe Management System built using Python**. This project was developed to practice and understand fundamental Python programming concepts through a practical application.

The system allows users to view the cafe menu, place orders, manage ordered items, and automatically generate an itemized bill.

## 📌 Features

- Display a numbered cafe menu with item prices
- Place an order by selecting item numbers
- Add multiple items in a single ordering session
- Specify quantities for each item
- View the current order and running total
- Update the quantity of an ordered item
- Remove items from the current order
- Generate an automatic itemized bill
- Calculate subtotal and GST
- Display customer name, bill number, date, and time on the receipt
- Handle invalid menu selections and quantity inputs

## 🛠️ Technologies Used

- **Python 3**
- Python built-in `datetime` module

No external libraries or database are required.

## 🧠 Python Concepts Used

This project demonstrates several fundamental Python concepts:

- Variables and data types
- Dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- User input and output
- Exception handling using `try-except`
- String formatting and f-strings
- Dictionary iteration
- Built-in functions
- Python modules
- Date and time handling

## 📂 Project Structure

```text
Cafe-Management-System/
│
├── cafe.py
└── README.md
```

## 🍽️ Sample Menu

| No. | Item | Price |
|---|---|---:|
| 1 | Coffee | Rs.80 |
| 2 | Tea | Rs.40 |
| 3 | Burger | Rs.120 |
| 4 | Sandwich | Rs.100 |
| 5 | Pasta | Rs.150 |
| 6 | Pizza | Rs.200 |

## ⚙️ How the System Works

When the program starts, the user is presented with the following options:

```text
================================
     CAFE MANAGEMENT SYSTEM
================================
1. View Menu
2. Place Order
3. View Current Order
4. Update Item Quantity
5. Remove Item
6. Generate Bill
7. Exit
```

### Placing an Order

The menu displays each item with a number. The customer selects an item using its number and enters the required quantity.

After adding an item, the program asks:

```text
Would you like to order anything else? (yes/no):
```

Entering `yes` allows another item to be added to the same order, while entering `no` completes the ordering process.

### Order Management

Before generating the final bill, the customer can:

- View all ordered items
- Check the current total
- Update the quantity of an item
- Remove an item from the order

### Bill Generation

The system automatically calculates the bill based on the selected items and their quantities.

The receipt contains:

- Bill number
- Customer name
- Date
- Time
- Item names
- Quantity
- Price per item
- Amount per item
- Subtotal
- GST
- Final total

Example:

```text
==================================================
                 BREW & BITE CAFE
              Dehradun, Uttarakhand
==================================================
Bill No. : 183425
Customer : Shaily
Date     : 12-11-2026
Time     : 06:34 PM
--------------------------------------------------
Item              Qty     Price       Amount
--------------------------------------------------
Coffee            2       Rs.80       Rs.160
Burger            1       Rs.120      Rs.120
Pizza             2       Rs.200      Rs.400
--------------------------------------------------
Subtotal:                             Rs.680.00
GST (5%):                              Rs.34.00
--------------------------------------------------
TOTAL:                                Rs.714.00
==================================================
              Thank You! Visit Again!
==================================================
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project folder

```bash
cd Cafe-Management-System
```

### 3. Run the Python program

```bash
python cafe.py
```

Make sure Python 3 is installed on your system.

## 🎯 Purpose of the Project

The main purpose of this project is to apply **Python fundamentals to a practical problem**.

Instead of focusing on frameworks, databases, or external libraries, the project demonstrates how core Python concepts such as dictionaries, functions, loops, conditions, exception handling, and modular programming can be combined to build a complete console-based application.

## 🚀 Possible Future Improvements

The project can later be extended with features such as:

- Graphical User Interface (GUI)
- Database integration
- Multiple customer/order records
- Admin menu management
- Payment method selection
- Persistent bill history
- Login and authentication
- Daily sales reports

## 👩‍💻 Author

**Shaily Sinha**

B.Tech Computer Science  
UPES, Dehradun