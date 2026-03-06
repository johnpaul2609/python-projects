import os
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from sqlalchemy import (
    create_engine, Column, Integer, String, Numeric, DateTime, ForeignKey, func
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# -----------------------
# Database configuration
# -----------------------
DB_CONFIG = {
    "USERNAME": "root",
    "PASSWORD": "johnpaul%40123",  # change if needed
    "HOST": "localhost",
    "DATABASE": "testdb1",
    "ECHO": True,
}

DATABASE_URL = f"mysql+pymysql://{DB_CONFIG['USERNAME']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}/{DB_CONFIG['DATABASE']}"

engine = create_engine(DATABASE_URL, echo=DB_CONFIG["ECHO"], pool_pre_ping=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# -----------------------
# Models
# -----------------------
class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Numeric(10, 2), nullable=False)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    subtotal = Column(Numeric(12, 2))
    tax_pct = Column(Numeric(5, 2))
    total = Column(Numeric(12, 2))

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    name = Column(String(100))
    unit_price = Column(Numeric(10, 2))
    quantity = Column(Integer)
    line_total = Column(Numeric(12, 2))

    order = relationship("Order", back_populates="items")


Base.metadata.create_all(engine)
def money(v):
    return Decimal(str(v)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
def seed_menu():
    if session.query(MenuItem).count() == 0:
        sample = [
            ("Burger", 120),
            ("Pizza", 350),
            ("Fries", 90),
            ("Coke", 50),
        ]
        for name, price in sample:
            session.add(MenuItem(name=name, price=money(price)))
        session.commit()


seed_menu()
class BillingApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Restaurant Billing System")
        self.geometry("1000x600")
        self.cart = {}
        self.tax_pct = Decimal("5.00")

        self.current_subtotal = Decimal("0.00")
        self.current_tax = Decimal("0.00")
        self.current_total = Decimal("0.00")
        self.create_widgets()
        self.load_menu()

    def create_widgets(self):
        # LEFT - MENU
        left = ttk.Frame(self, padding=10)
        left.place(x=10, y=10, width=450, height=580)

        ttk.Label(left, text="Menu", font=("Arial", 14)).pack(anchor="w")
        self.menu_tree = ttk.Treeview(left, columns=("name", "price"), show="headings")
        self.menu_tree.heading("name", text="Item")
        self.menu_tree.heading("price", text="Price")
        self.menu_tree.column("name", width=280)
        self.menu_tree.column("price", width=120, anchor="e")
        self.menu_tree.pack(fill="both", expand=True, pady=10)

        ttk.Button(left, text="Add Selected").pack(pady=3)
        ttk.Button(left, text="Add New Menu Item").pack(pady=3)

        right = ttk.Frame(self, padding=10)
        right.place(x=480, y=10, width=1000, height=580)

        ttk.Label(right, text="Cart", font=("Arial", 14)).pack(anchor="w")

        self.cart_tree = ttk.Treeview(right, columns=("name", "qty", "price", "total"), show="headings")
        self.cart_tree.heading("name", text="Item")
        self.cart_tree.heading("qty", text="Qty")
        self.cart_tree.heading("price", text="Unit")
        self.cart_tree.heading("total", text="Total")
        self.cart_tree.pack(fill="both", expand=True, pady=10)

        ttk.Button(right, text="Remove Selected").pack()

        self.total_var = tk.StringVar(value="0.00")

        ttk.Label(right, text="Grand Total:", font=("Arial", 12)).pack(anchor="w", pady=5)
        ttk.Label(right, textvariable=self.total_var, font=("Arial", 14, "bold")).pack(anchor="w")

        ttk.Button(right, text="Generate Bill").pack(pady=5)
        ttk.Button(right, text="Save Bill").pack(pady=5)

    def load_menu(self):
        for row in self.menu_tree.get_children():
            self.menu_tree.delete(row)

        items = session.query(MenuItem).order_by(MenuItem.name).all()
        for item in items:
            self.menu_tree.insert("", "end", iid=str(item.id),
                                  values=(item.name, money(item.price)))
if __name__ == "__main__":
    app = BillingApp()
    app.mainloop()

