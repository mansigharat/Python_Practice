import json
import random
import string
from pathlib import Path

import streamlit as st

DATABASE = "data.json"


class Bank:
    """Handles all data persistence and account logic. No input() calls,
    no print() calls. Every method takes plain arguments and returns
    (success: bool, message: str, data: dict|None) so the UI layer
    decides how to display things."""

    @staticmethod
    def _load():
        if Path(DATABASE).exists():
            try:
                with open(DATABASE) as fs:
                    return json.loads(fs.read())
            except (json.JSONDecodeError, OSError):
                return []
        return []

    @staticmethod
    def _save(data):
        with open(DATABASE, "w") as fs:
            json.dump(data, fs, indent=2)

    @staticmethod
    def _generate_account_number(existing_accounts):
        # Loop until a unique account number is produced. Your original
        # code never checked for collisions.
        while True:
            alpha = random.choices(string.ascii_letters, k=3)
            num = random.choices(string.digits, k=3)
            spchar = random.choices("!@#$%^&*?", k=1)
            acc_id = alpha + num + spchar
            random.shuffle(acc_id)
            acc_no = "".join(acc_id)
            if not any(a["accountNo"] == acc_no for a in existing_accounts):
                return acc_no

    @classmethod
    def create_account(cls, name, age, email, pin):
        data = cls._load()

        if not name.strip():
            return False, "Name cannot be empty.", None
        if age < 18:
            return False, "You must be 18 or older to open an account.", None
        if not (pin.isdigit() and len(pin) == 4):
            return False, "Pin must be exactly 4 digits.", None
        if not email.strip() or "@" not in email:
            return False, "Enter a valid email.", None

        info = {
            "name": name.strip(),
            "age": age,
            "email": email.strip(),
            "pin": pin,  # stored as string, leading zeros preserved
            "accountNo": cls._generate_account_number(data),
            "balance": 0,
        }
        data.append(info)
        cls._save(data)
        return True, "Account created successfully.", info

    @classmethod
    def _find_account(cls, data, acc_no, pin):
        matches = [a for a in data if a["accountNo"] == acc_no and a["pin"] == pin]
        return matches[0] if matches else None

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        data = cls._load()
        account = cls._find_account(data, acc_no, pin)
        if account is None:
            return False, "No account found with that account number and pin.", None
        if amount <= 0:
            return False, "Deposit amount must be greater than 0.", None
        account["balance"] += amount
        cls._save(data)
        return True, f"Deposited {amount}. New balance: {account['balance']}", account

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        data = cls._load()
        account = cls._find_account(data, acc_no, pin)
        if account is None:
            return False, "No account found with that account number and pin.", None
        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0.", None
        if amount > account["balance"]:
            return False, "Insufficient balance.", None
        account["balance"] -= amount
        cls._save(data)
        return True, f"Withdrew {amount}. New balance: {account['balance']}", account

    @classmethod
    def get_details(cls, acc_no, pin):
        data = cls._load()
        account = cls._find_account(data, acc_no, pin)
        if account is None:
            return False, "No account found with that account number and pin.", None
        return True, "Account found.", account

    @classmethod
    def update_details(cls, acc_no, pin, new_name, new_email, new_pin):
        data = cls._load()
        account = cls._find_account(data, acc_no, pin)
        if account is None:
            return False, "No account found with that account number and pin.", None

        if new_pin and not (new_pin.isdigit() and len(new_pin) == 4):
            return False, "New pin must be exactly 4 digits.", None
        if new_email and "@" not in new_email:
            return False, "New email looks invalid.", None

        if new_name.strip():
            account["name"] = new_name.strip()
        if new_email.strip():
            account["email"] = new_email.strip()
        if new_pin.strip():
            account["pin"] = new_pin.strip()

        cls._save(data)
        return True, "Details updated successfully.", account

    @classmethod
    def delete_account(cls, acc_no, pin):
        data = cls._load()
        account = cls._find_account(data, acc_no, pin)
        if account is None:
            return False, "No account found with that account number and pin.", None
        data.remove(account)
        cls._save(data)
        return True, "Account deleted successfully.", None


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Bank Management System", page_icon="🏦")
st.title("🏦 Bank Management System")

menu = st.sidebar.radio(
    "Choose an action",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "View Details",
        "Update Details",
        "Delete Account",
    ],
)

if menu == "Create Account":
    st.subheader("Create a new account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit pin", max_chars=4, type="password")

    if st.button("Create Account"):
        ok, msg, info = Bank.create_account(name, int(age), email, pin)
        if ok:
            st.success(msg)
            st.json(info)
            st.warning("Save your account number now. It will not be shown again here.")
        else:
            st.error(msg)

elif menu == "Deposit Money":
    st.subheader("Deposit money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Pin", max_chars=4, type="password")
    amount = st.number_input("Amount", min_value=0, step=1)

    if st.button("Deposit"):
        ok, msg, account = Bank.deposit(acc_no, pin, int(amount))
        st.success(msg) if ok else st.error(msg)

elif menu == "Withdraw Money":
    st.subheader("Withdraw money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Pin", max_chars=4, type="password")
    amount = st.number_input("Amount", min_value=0, step=1)

    if st.button("Withdraw"):
        ok, msg, account = Bank.withdraw(acc_no, pin, int(amount))
        st.success(msg) if ok else st.error(msg)

elif menu == "View Details":
    st.subheader("View account details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Pin", max_chars=4, type="password")

    if st.button("View"):
        ok, msg, account = Bank.get_details(acc_no, pin)
        if ok:
            st.success(msg)
            st.json(account)
        else:
            st.error(msg)

elif menu == "Update Details":
    st.subheader("Update account details")
    st.caption("Leave a field empty to keep its current value. Age, account number, and balance cannot be changed here.")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current Pin", max_chars=4, type="password")
    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New Pin (optional)", max_chars=4, type="password")

    if st.button("Update"):
        ok, msg, account = Bank.update_details(acc_no, pin, new_name, new_email, new_pin)
        if ok:
            st.success(msg)
            st.json(account)
        else:
            st.error(msg)

elif menu == "Delete Account":
    st.subheader("Delete account")
    st.caption("This is permanent. There is no undo.")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Pin", max_chars=4, type="password")
    confirm = st.checkbox("I understand this will permanently delete the account")

    if st.button("Delete Account"):
        if not confirm:
            st.error("Check the confirmation box first.")
        else:
            ok, msg, _ = Bank.delete_account(acc_no, pin)
            st.success(msg) if ok else st.error(msg)