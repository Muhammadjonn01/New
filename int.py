# class Restaurant:
#     def __init__(self):
#         self.menu_items = []
#         self.book_table = []
#         self.customer_orders = []

#     def add_item_to_menu(self, item):
#         self.menu_items.append(item)

#     def book_tables(self, table):
#         self.book_table.append(table)

#     def customer_order(self, order):
#         self.customer_orders.append(order)

#     def print_menu(self):
#         print("Menu Items:")
#         for item in self.menu_items:
#             print(item)

#     def print_table_reservations(self):
#         print("Booked Tables:")
#         for table in self.book_table:
#             print(table)

#     def print_customer_orders(self):
#         print("Customer Orders:")
#         for order in self.customer_orders:
#             print(order)

# import functools
# import time

# def retry(func):
#     MAX_ATTEMPTS = 3

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         attempts = 0
#         while attempts < MAX_ATTEMPTS:
#             try:
#                 return func(*args, **kwargs)
#             except:
#                 print("Function failed. Retrying...")
#                 attempts += 1
#                 time.sleep(1)
#         print("Function failed after multiple attempts.")
#         return None

#     return wrapper

# @retry
# def example_func():
#     # Function code that may fail
#     pass

# example_func()

