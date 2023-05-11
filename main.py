import tkinter as tk
import sqlite3
import os

# 创建窗口对象
window = tk.Tk()

# 设置窗口标题
window.title("Logistics Management System")

# 设置窗口大小
window.geometry("400x300")

# 创建标签对象
label = tk.Label(window, text="Logistics Management System")

# 将标签对象放置在窗口中央
label.pack(pady=50)

# 定义函数，用于展示登录窗口
def show_login_window():
    # 创建一个新的窗口
    login_window = tk.Toplevel(window)

    # 设置窗口标题
    login_window.title("Login")

    # 设置窗口大小
    login_window.geometry("300x150")

    # 创建标签对象
    label1 = tk.Label(login_window, text="Please enter your user ID and password:")
    label1.pack(pady=10)

    # 创建 StringVar 对象
    user_id = tk.StringVar()
    password = tk.StringVar()

    # 创建标签对象
    label2 = tk.Label(login_window, text="ID:")
    label2.pack(side="left", padx=10)

    # 创建文本框对象
    entry1 = tk.Entry(login_window, textvariable=user_id)
    entry1.pack(side="left", padx=10, pady=5)

    # 创建标签对象
    label3 = tk.Label(login_window, text="Password:")
    label3.pack(side="left", padx=10)

    # 创建文本框对象
    entry2 = tk.Entry(login_window, textvariable=password, show="*")
    entry2.pack(side="left", padx=10, pady=5)

    # 定义确认按钮的事件处理函数
    def confirm():
        # 获取文本框中的值
        user_id_value = user_id.get()
        password_value = password.get()

        # 获取当前脚本所在的目录
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 连接数据库
        conn = sqlite3.connect(os.path.join(current_dir, 'IDpassport.db'))
        cursor = conn.cursor()

        # 查询用户名和密码是否匹配
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user_id_value, password_value))
        result = cursor.fetchone()

        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

        if result is not None:
            # 如果匹配，则显示欢迎窗口
            login_window.destroy()
            show_welcome_window()
        else:
            # 如果不匹配，则显示错误消息
            error_label.configure(text="Invalid user ID or password")

    # 创建按钮对象
    button = tk.Button(login_window, text="Confirm", command=confirm)
    button.pack(pady=10)

    # 创建标签对象
    error_label = tk.Label(login_window, text="")
    error_label.pack()

# 定义函数，用于展示欢迎窗口
def show_welcome_window():
    # 创建一个新的窗口
    welcome_window = tk.Toplevel(window)

    # 设置窗口标题
    welcome_window.title("Welcome")

    # 设置窗口大小
    welcome_window.geometry("300x200")

    # 创建标签对象
    label = tk.Label(welcome_window, text="Welcome!")
    label.pack(pady=10)

    # 创建按钮对象
    button1 = tk.Button(welcome_window, text="Receive Order", command=show_receive_order_window)
    button1.pack(pady=5)

    button2 = tk.Button(welcome_window, text="Route Selection", command=show_route_selection_window)
    button2.pack(pady=5)

    button3 = tk.Button(welcome_window, text="Transport", command=show_transport_window)
    button3.pack(pady=5)

    button4 = tk.Button(welcome_window, text="Query", command=show_query_window)
    button4.pack(pady=5)

    button5 = tk.Button(welcome_window, text="Invoice", command=show_invoice_window)
    button5.pack(pady=5)

    button6 = tk.Button(welcome_window, text="Statistics", command=show_statistics_window)
    button6.pack(pady=5)

# 定义函数，用于展示 "Receive Order" 窗口
def show_receive_order_window():
    # 创建一个新的窗口
    receive_order_window = tk.Toplevel(window)

    # 设置窗口标题
    receive_order_window.title("Receive Order")

    # 设置窗口大小
    receive_order_window.geometry("300x150")

    # 创建标签对象
    label1 = tk.Label(receive_order_window, text="Please enter the order number:")
    label1.pack(pady=10)

    # 创建 StringVar 对象
    order_number = tk.StringVar()

    # 创建文本框对象
    entry1 = tk.Entry(receive_order_window, textvariable=order_number)
    entry1.pack(pady=5)

    # 定义确认按钮的事件处理函数
    def confirm():
        # 获取文本框中的值
        order_number_value = order_number.get()

        # 将订单号存储到数据库中
        cursor.execute("INSERT INTO orders (order_number, order_status) VALUES (?, ?)", (order_number_value, "in progress"))
        conn.commit()

        # 关闭窗口
        receive_order_window.destroy()

        # 弹出提示框
        tk.messagebox.showinfo("Success", "Order received successfully.")

    # 创建按钮对象
    button = tk.Button(receive_order_window, text="Confirm", command=confirm)
    button.pack(pady=10)
  # 定义函数，用于展示 "Route Selection" 窗口
def show_route_selection_window():
    # 创建一个新的窗口
    route_selection_window = tk.Toplevel(window)

    # 设置窗口标题
    route_selection_window.title("Route Selection")

    # 设置窗口大小
    route_selection_window.geometry("300x150")

    # 创建标签对象
    label1 = tk.Label(route_selection_window, text="Please enter the order number:")
    label1.pack(pady=10)

    # 创建 StringVar 对象
    order_number = tk.StringVar()

    # 创建文本框对象
    entry1 = tk.Entry(route_selection_window, textvariable=order_number)
    entry1.pack(pady=5)

    # 定义确认按钮的事件处理函数
    def confirm():
        # 获取文本框中的值
        order_number_value = order_number.get()

        # 检查订单号是否存在
        cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number_value,))
        order = cursor.fetchone()
        if order is None:
            tk.messagebox.showerror("Error", "Invalid order number.")
            return

        # 关闭窗口
        route_selection_window.destroy()

        # 定义路线选择按钮的事件处理函数
        def select_route(route):
            # 更新数据库中的路线选择字段
            cursor.execute("UPDATE orders SET route_selection = ? WHERE order_number = ?", (route, order_number_value))
            conn.commit()

            # 弹出提示框
            tk.messagebox.showinfo("Success", "Route selected successfully.")

        # 创建路线选择按钮
        button1 = tk.Button(window, text="Route 1", command=lambda: select_route("Route 1"))
        button2 = tk.Button(window, text="Route 2", command=lambda: select_route("Route 2"))
        button3 = tk.Button(window, text="Route 3", command=lambda: select_route("Route 3"))

        # 将按钮对象放置在窗口中央
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

    # 创建按钮对象
    button = tk.Button(route_selection_window, text="Confirm", command=confirm)
    button.pack(pady=10)
    # 定义函数，用于展示 "Transport" 窗口
def show_transport_window():
    # 创建一个新的窗口
    transport_window = tk.Toplevel(window)

    # 设置窗口标题
    transport_window.title("Transport")

    # 设置窗口大小
    transport_window.geometry("300x150")

    # 创建标签对象
    label1 = tk.Label(transport_window, text="Please enter the order number:")
    label1.pack(pady=10)

    # 创建 StringVar 对象
    order_number = tk.StringVar()

    # 创建文本框对象
    entry1 = tk.Entry(transport_window, textvariable=order_number)
    entry1.pack(pady=5)

    # 定义确认按钮的事件处理函数
    def confirm():
        # 获取文本框中的值
        order_number_value = order_number.get()

        # 检查订单号是否存在
        cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number_value,))
        order = cursor.fetchone()
        if order is None:
            tk.messagebox.showerror("Error", "Invalid order number.")
            return

        # 关闭窗口
        transport_window.destroy()

        # 定义运输方式按钮的事件处理函数
        def select_transport(transport):
            # 更新数据库中的运输方式字段
            cursor.execute("UPDATE orders SET transport_method = ? WHERE order_number = ?", (transport, order_number_value))
            conn.commit()

            # 弹出提示框
            tk.messagebox.showinfo("Success", "Transport method selected successfully.")

        # 创建运输方式按钮
        button1 = tk.Button(window, text="Car", command=lambda: select_transport("Car"))
        button2 = tk.Button(window, text="Plane", command=lambda: select_transport("Plane"))
        button3 = tk.Button(window, text="Train", command=lambda: select_transport("Train"))

        # 将按钮对象放置在窗口中央
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

    # 创建按钮对象
    button = tk.Button(transport_window, text="Confirm", command=confirm)
    button.pack(pady=10)
  # 定义函数，用于展示 "Query" 窗口
def show_query_window():
    # 创建一个新的窗口
    query_window = tk.Toplevel(window)

    # 设置窗口标题
    query_window.title("Query")

    # 设置窗口大小
    query_window.geometry("300x150")

    # 创建标签对象
    label1 = tk.Label(query_window, text="Please enter the order number:")
    label1.pack(pady=10)

    # 创建 StringVar 对象
    order_number = tk.StringVar()

    # 创建文本框对象
    entry1 = tk.Entry(query_window, textvariable=order_number)
    entry1.pack(pady=5)

    # 定义确认按钮的事件处理函数
    def confirm():
        # 获取文本框中的值
        order_number_value = order_number.get()

        # 检查订单号是否存在
        cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number_value,))
        order = cursor.fetchone()
        if order is None:
            tk.messagebox.showerror("Error", "Invalid order number.")
            return

        # 关闭窗口
        query_window.destroy()

        # 创建表格对象
        table = tk.Toplevel(window)
        table.title("Order Information")
        table.geometry("400x200")

        # 创建表格中的标签对象
        label_id = tk.Label(table, text="ID")
        label_order_number = tk.Label(table, text="Order Number")
        label_route_selection = tk.Label(table, text="Route Selection")
        label_transport_method = tk.Label(table, text="Transport Method")
        label_order_status = tk.Label(table, text="Order Status")

        # 将标签对象放置在表格的第一行
        label_id.grid(row=0, column=0, padx=5)
        label_order_number.grid(row=0, column=1, padx=5)
        label_route_selection.grid(row=0, column=2, padx=5)
        label_transport_method.grid(row=0, column=3, padx=5)
        label_order_status.grid(row=0, column=4, padx=5)

        # 查询数据库中的订单信息
        cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number_value,))
        orders = cursor.fetchall()

        # 在表格中显示订单信息
        for i, order in enumerate(orders):
            # 创建标签对象
            label_id = tk.Label(table, text=order[0])
            label_order_number = tk.Label(table, text=order[1])
            label_route_selection = tk.Label(table, text=order[2])
            label_transport_method = tk.Label(table, text=order[3])
            label_order_status = tk.Label(table, text=order[4])

            # 将标签对象放置在表格中
            label_id.grid(row=i+1, column=0, padx=5)
            label_order_number.grid(row=i+1, column=1, padx=5)
            label_route_selection.grid(row=i+1, column=2, padx=5)
            label_transport_method.grid(row=i+1, column=3, padx=5)
            label_order_status.grid(row=i+1, column=4, padx=5)


    # 创建按钮对象
    button = tk.Button(query_window, text="Confirm", command=confirm)
    button.pack(pady=10)
  # 定义函数，用于展示 "Invoice" 窗口
def show_invoice_window():
    # 创建一个新的窗口
    invoice_window = tk.Toplevel(window)

    # 设置窗口标题
    invoice_window.title("Invoice")

    # 设置窗口大小
    invoice_window.geometry("300x150")

    # 创建标签对象
    label1 = tk.Label(invoice_window, text="Please enter the order number:")
    label1.pack(pady=10)

    # 创建 StringVar 对象
    order_number = tk.StringVar()

    # 创建文本框对象
    entry1 = tk.Entry(invoice_window, textvariable=order_number)
    entry1.pack(pady=5)

    # 定义确认按钮的事件处理函数
    def confirm():
        # 获取文本框中的值
        order_number_value = order_number.get()

        # 检查订单号是否存在
        cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number_value,))
        order = cursor.fetchone()
        if order is None:
            tk.messagebox.showerror("Error", "Invalid order number.")
            return

        # 检查订单状态是否为 "in progress"
        if order[4] != "in progress":
            tk.messagebox.showerror("Error", "This order has already been completed.")
            return

        # 更新订单状态为 "completed"
        cursor.execute("UPDATE orders SET order_status = ? WHERE order_number = ?", ("completed", order_number_value))
        conn.commit()

        # 关闭窗口
        invoice_window.destroy()

        # 弹出提示框
        tk.messagebox.showinfo("Success", "Invoice generated successfully.")

    # 创建按钮对象
    button = tk.Button(invoice_window, text="Confirm", command=confirm)
    button.pack(pady=10)
  # 定义函数，用于展示 "Statistics" 窗口
def show_statistics_window():
    # 查询数据库中的所有订单信息
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    # 创建一个新的窗口
    statistics_window = tk.Toplevel(window)

    # 设置窗口标题
    statistics_window.title("Statistics")

    # 设置窗口大小
    statistics_window.geometry("400x200")

    # 创建表格中的标签对象
    label_id = tk.Label(statistics_window, text="ID")
    label_order_number = tk.Label(statistics_window, text="Order Number")
    label_route_selection = tk.Label(statistics_window, text="Route Selection")
    label_transport_method = tk.Label(statistics_window, text="Transport Method")
    label_order_status = tk.Label(statistics_window, text="Order Status")
    label_transport_cost = tk.Label(statistics_window, text="Transport Cost")

    # 将标签对象放置在表格中
    label_id.grid(row=0, column=0, padx=5)
    label_order_number.grid(row=0, column=1, padx=5)
    label_route_selection.grid(row=0, column=2, padx=5)
    label_transport_method.grid(row=0, column=3, padx=5)
    label_order_status.grid(row=0, column=4, padx=5)
    label_transport_cost.grid(row=0, column=5, padx=5)

    total_transport_cost = 0

    # 在表格中显示订单信息
    for i, order in enumerate(orders):
        # 创建标签对象
        label_id = tk.Label(statistics_window, text=order[0])
        label_order_number = tk.Label(statistics_window, text=order[1])
        label_route_selection = tk.Label(statistics_window, text=order[2])
        label_transport_method = tk.Label(statistics_window, text=order[3])
        label_order_status = tk.Label(statistics_window, text=order[4])

        

        # 将标签对象放置在表格中
        label_id.grid(row=i+1, column=0, padx=5)
        label_order_number.grid(row=i+1, column=1, padx=5)
        label_route_selection.grid(row=i+1, column=2, padx=5)
        label_transport_method.grid(row=i+1, column=3, padx=5)
        label_order_status.grid(row=i+1, column=4, padx=5)
        
# 定义函数，用于显示一个消息框，显示指定的文本
def show_message_box(text):
    tk.messagebox.showinfo("Message", text)

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 连接数据库
conn = sqlite3.connect(os.path.join(current_dir, 'IDpassport.db'))
cursor = conn.cursor()

# 创建用户表格
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

# 插入一些测试数据
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("test", "123456"))

# 提交更改
conn.commit()

# 关闭游标和数据库连接
cursor.close()
conn.close()

# 创建按钮对象
button = tk.Button(window, text="Login", command=show_login_window)

# 将按钮对象放置在窗口中央
button.pack()

# 进入消息循环
window.mainloop()