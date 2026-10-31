# ============================================
#  Expense Tracker (PyQt5) - QUESTION VERSION
#  Write the code yourself by following the steps.
#  Each step gives you the LOGIC and a small EXAMPLE.
#  The examples use different names - adapt them!
# ============================================
#
#  GOAL: A window where the user chooses Income or Expense,
#  types an item and an amount, and clicks "Add".
#  The app shows every transaction in a list, plus
#  Total Income, Total Expense and Saldo (Income - Expense).
#  Transactions are saved to "transactions.txt" and loaded
#  again the next time the app opens.
#
#  Window sketch:
#     Type:   [Income  v]
#     Item:   [__________]
#     Amount: [__________]
#     [        Add       ]
#     +----------------------------+
#     | [+] Salary - 5000000.0     |
#     | [-] Lunch - 25000.0        |
#     +----------------------------+
#     Total Income: 5000000.0
#     Total Expense: 25000.0
#     Saldo: 4975000.0
#
#  File format (transactions.txt), one transaction per line:
#     Income,Salary,5000000.0
#     Expense,Lunch,25000.0
#  (Don't type commas inside the item name!)
# ============================================


# ---------- STEP 1: Imports ----------
# Logic: import sys, and these from PyQt5.QtWidgets:
#   QApplication, QWidget, QLabel, QLineEdit, QPushButton,
#   QListWidget, QVBoxLayout, QMessageBox, QComboBox
# Example:
#   from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QMessageBox, QComboBox
# TODO: write your imports here


# ---------- STEP 2: File name constant ----------
# Logic: store the file name in one variable so it's easy to change.
# Example:
#   SCORE_FILE = "scores.txt"
EXPENSES = "expense.txt"
# TODO


# ---------- STEP 3: Create the window class ----------
# Logic:
#   - Make a class that inherits from QWidget
#   - In __init__: call super().__init__(), set the window title,
#     and create TWO variables that start at 0:
#     one for total income, one for total expense
# Example:
#   class MyApp(QWidget):
#       def __init__(self):
#           super().__init__()
#           self.setWindowTitle("My App")
#           self.wins = 0
#           self.losses = 0
class Appli(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Money Tracker")
        self.input_type = QLabel("Type")
        self.out_in = QComboBox()
        self.out_in.addItems(["Income", "Expense"])
        self.item_type = QLabel("Item")
        self.input_item = QLineEdit()
        self.input_item.setPlaceholderText("Item (e.g. Salary, Lunch)")
        self.amount_type = QLabel("Amount")
        self.input_amount = QLineEdit()
        self.input_amount.setPlaceholderText("Amount (e.g. 25000)")
        self.change = QPushButton("Add")
        self.changes = QListWidget()
        self.total_in = QLabel("Total income:")
        self.total_income = 0
        self.total_out = QLabel("Total expense")
        self.total_outcome = 0
        self.money_rn = QLabel("Saldo")
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_type)
        main_layout.addWidget(self.out_in)
        main_layout.addWidget(self.item_type)
        main_layout.addWidget(self.input_item)
        main_layout.addWidget(self.amount_type)
        main_layout.addWidget(self.input_amount)
        main_layout.addWidget(self.change)
        main_layout.addWidget(self.changes)
        main_layout.addWidget(self.total_in)
        main_layout.addWidget(self.total_out)
        main_layout.addWidget(self.money_rn)
        self.setLayout(main_layout)
        self.change.clicked.connect(self.save_changes)
        self.load_transactions()
# TODO
    def save_changes(self):
        income_expense = self.out_in.currentText()
        item = self.input_item.text().strip()
        amount = self.input_amount.text().strip()
        if item == "" or amount == "":
            QMessageBox.warning(self, "Error", "Item is empty or amount is empty")
            return
        try:
            amount = float(amount)
        except ValueError:
            print("Error, can't be convert!")
        self.show_transaction(income_expense, item, amount)
        with open(EXPENSES, "a", encoding = "UTF-8") as file:
            file.write(f"{income_expense},{item},{amount}\n")
        self.input_amount.clear()
        self.input_item.clear()
# ---------- STEP 4: Create the widgets (inside __init__) ----------
# Logic: you need
#   - 1 QComboBox  (a dropdown with "Income" and "Expense")
#   - 2 QLineEdit  (item input, amount input)
#   - 1 QPushButton ("Add")
#   - 1 QListWidget (shows all transactions)
#   - 3 QLabel ("Total Income: 0", "Total Expense: 0", "Saldo: 0")
#   Tip: use setPlaceholderText() to show a hint inside the input.
# Example:
#   self.color_box = QComboBox()
#   self.color_box.addItems(["Red", "Blue"])
#
#   self.name_input = QLineEdit()
#   self.name_input.setPlaceholderText("Your name")
#   self.save_button = QPushButton("Save")

# TODO


# ---------- STEP 5: Layout (inside __init__) ----------
# Logic:
#   - Create a QVBoxLayout (stacks widgets top to bottom)
#   - Add each widget in the order of the window sketch
#   - You can add a label directly: layout.addWidget(QLabel("Type:"))
#   - Finally: self.setLayout(layout)
# Example:
#   layout = QVBoxLayout()
#   layout.addWidget(self.color_box)
#   layout.addWidget(self.name_input)
#   self.setLayout(layout)

# TODO


# ---------- STEP 6: Connect the button (inside __init__) ----------
# Logic: when the button is clicked, run the method add_transaction.
#   (Do NOT put () after the method name here.)
# Example:
#   self.save_button.clicked.connect(self.save_name)

# TODO


# ---------- STEP 7: Load saved data at start (inside __init__) ----------
# Logic: at the end of __init__, call self.load_transactions()
#   (you will write this method in Step 10)

# TODO

    def show_transaction(self, kind, item, amount):
        if kind == "Income":
            self.changes.addItem(f"[+] {item} - {amount}")
            self.total_income += amount
        elif kind == "Expense":
            self.changes.addItem(f"[-] {item} - {amount}")
            self.total_outcome += amount 
        saldo = self.total_income - self.total_outcome
        self.money_rn.setText("Saldo :"+ str(saldo))
        self.total_in.setText("Income :"+ str(self.total_income))
        self.total_out.setText("Expense :"+ str(self.total_outcome))
# ---------- STEP 8: Method show_transaction(self, kind, item, amount) ----------
# Logic (this method only updates the screen):
#   1. If kind is "Income":
#        - add "[+] item - amount" to the list
#        - add amount to total income
#      Else (Expense):
#        - add "[-] item - amount" to the list
#        - add amount to total expense
#   2. Calculate saldo = total income - total expense
#   3. Update all 3 labels with setText()
# Example:
#   if result == "Win":
#       self.my_list.addItem(f"[W] {team}")
#       self.wins += 1
#   else:
#       self.my_list.addItem(f"[L] {team}")
#       self.losses += 1
#   diff = self.wins - self.losses
#   self.diff_label.setText(f"Difference: {diff}")

# TODO


# ---------- STEP 9: Method add_transaction(self) ----------
# Logic:
#   1. Read the chosen type from the combo box (.currentText())
#   2. Read text from both inputs (use .text().strip())
#   3. If item or amount is empty -> show a warning and return
#   4. Try to convert amount to float
#        if it fails (ValueError) -> show a warning and return
#   5. Call self.show_transaction(kind, item, amount)
#   6. Open the file in APPEND mode "a" and write "kind,item,amount\n"
#   7. Clear both inputs with .clear()
# Examples:
#   color = self.color_box.currentText()
#
#   if name == "":
#       QMessageBox.warning(self, "Error", "Name is empty")
#       return
#
#   try:
#       age = int(age_text)
#   except ValueError:
#       ...
#
#   with open("scores.txt", "a") as f:
#       f.write(f"{color},{name},{score}\n")

# TODO
    def load_transactions(self):
        try:
            with open(EXPENSES, "r") as f:
                for line in f:
                    line = line.strip()
                    parts = line.split(",")
                    kind = parts[0]
                    item = parts[1]
                    amount = float(parts[2])
                    self.show_transaction(kind, item, float(amount))
        except FileNotFoundError:
            pass
# ---------- STEP 10: Method load_transactions(self) ----------
# Logic:
#   1. Open the file in READ mode "r"
#   2. Loop through each line
#   3. Remove the "\n" with .strip(); skip empty lines
#   4. Split the line by comma: parts = line.split(",")
#        parts[0] = kind, parts[1] = item, parts[2] = amount
#   5. Call self.show_transaction(kind, item, float(amount))
#      (do NOT write to the file again here!)
#   6. If the file does not exist yet (FileNotFoundError),
#      just do nothing (pass)
# Example:
#   try:
#       with open("scores.txt", "r") as f:
#           for line in f:
#               line = line.strip()
#               parts = line.split(",")
#               print(parts[0], parts[1], parts[2])
#   except FileNotFoundError:
#       pass

# TODO


# ---------- STEP 11: Run the app ----------
# Logic: create QApplication, create your window, show it, start the loop.
# Example:
#   app = QApplication(sys.argv)
#   window = MyApp()
#   window.show()
#   sys.exit(app.exec_())
app = QApplication(sys.argv)
window = Appli()
window.show()
sys.exit(app.exec_())
# TODO


# ============================================
#  TEST YOUR APP
#  1. Add Income "Salary" / 5000000 -> Total Income and Saldo = 5000000
#  2. Add Expense "Lunch" / 25000 -> Total Expense = 25000,
#     Saldo = 4975000
#  3. Click Add with empty fields -> warning appears
#  4. Type "abc" as amount -> warning appears
#  5. Close the app, open it again -> everything is still there
#  6. Open transactions.txt in a text editor -> check the format
#
#  BONUS CHALLENGES
#  - Show the saldo in red when it is negative
#    (hint: label.setStyleSheet("color: red"))
#  - Add a "Clear All" button that empties the list, resets the
#    totals, and empties the file (open with "w")
#  - Show amounts with no decimals, e.g. 25000 instead of 25000.0
#  - Add a date for each transaction
# ============================================
