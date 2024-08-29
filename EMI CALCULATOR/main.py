import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_calculation_window():
    # Hide the start window
    start_window.withdraw()

    # Create the calculation window
    cal_window = tk.Toplevel()
    cal_window.title("EMI Calculator")
    cal_window.geometry("1000x800")

    # Variables
    first_click = [True] * 6
    cal_emi = 0
    history = []

    def on_click(entry, index):
        if first_click[index]:
            first_click[index] = False
            entry.delete(0, "end")

    def validate_numeric(entry_value):
        return entry_value.isdigit() or entry_value == ""

    def def_cal():
        nonlocal cal_emi
        try:
            p = int(e4.get())
            r = float(e5.get())
            n = int(e6.get())
            cal_emi = (
                p * (r / 1200) * ((1 + r / 1200) ** n) / (((1 + r / 1200) ** n) - 1)
            )
            total_payment = cal_emi * n
            total_interest = total_payment - p
            messagebox.showinfo(
                "EMI DETAILS",
                f"Your Monthly Payment: {cal_emi:.2f}\nTotal Payment: {total_payment:.2f}\nTotal Interest: {total_interest:.2f}",
            )
            history.append((p, r, n, cal_emi))
            update_chart(p, total_interest)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    def update_chart(principal, interest):
        # Clear previous chart if it exists
        for widget in f1.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        fig, ax = plt.subplots()
        ax.pie(
            [principal, interest],
            labels=["Principal", "Interest"],
            autopct="%1.1f%%",
            colors=["#4CAF50", "#FFC107"],
        )
        ax.set_title("EMI Breakdown")

        chart = FigureCanvasTkAgg(fig, f1)
        chart.get_tk_widget().pack(side="right", padx=20, pady=20)
        chart.draw()

    def def_PDF():
        # Create a new PDF
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Path to your background image
        background_image_path = "EMI calculator.jpg"

        # Load and add the wide image at the top
        image_width = 100
        image_height = 60
        pdf.image(background_image_path, x=50, y=0, w=image_width, h=image_height)

        # Add text below the image
        pdf.set_font("Arial", size=12)
        pdf.set_y(image_height + 10)
        pdf.set_text_color(0, 0, 0)

        pdf.multi_cell(0, 10, f"Name: {e1.get()}")
        pdf.multi_cell(0, 10, f"Mobile No.: {e2.get()}")
        pdf.multi_cell(0, 10, f"Email Id: {e3.get()}")
        pdf.multi_cell(0, 10, f"Loan Amount: {e4.get()}")
        pdf.multi_cell(0, 10, f"Interest Rate: {e5.get()}")
        pdf.multi_cell(0, 10, f"Period in Months: {e6.get()}")
        pdf.multi_cell(0, 10, f"Calculated EMI: {cal_emi:.2f}")

        # Load and add the pie chart image
        fig, ax = plt.subplots()
        ax.pie(
            [int(e4.get()), cal_emi * int(e6.get()) - int(e4.get())],
            labels=["Principal", "Interest"],
            autopct="%1.1f%%",
            colors=["#4CAF50", "#FFC107"],
        )
        ax.set_title("EMI Breakdown")
        chart_image_path = "emi_chart.png"
        fig.savefig(chart_image_path, format="png", bbox_inches="tight")
        plt.close(fig)

        # Add the chart image below the text
        chart_width = 150
        chart_height = 100
        chart_x = (pdf.w - chart_width) / 2
        chart_y = pdf.get_y() + 10
        pdf.image(chart_image_path, x=chart_x, y=chart_y, w=chart_width, h=chart_height)

        # Save the PDF
        pdf.output("EMI_Calculated.pdf")
        messagebox.showinfo("PDF Status", "PDF Generated and Saved Successfully.")

    def def_details():
        messagebox.showinfo(
            "User Details",
            f"Name: {e1.get()}\nMobile No.: {e2.get()}\nEmail Id: {e3.get()}",
        )

    def reset_fields():
        # Clear all fields
        for entry, default_text in zip(entries, default_texts):
            entry.delete(0, "end")
            entry.insert(0, default_text)

        nonlocal first_click
        first_click = [True] * 6

        # Ensure the frame is updated
        f1.update_idletasks()

    f1 = tk.Frame(cal_window, width=1000, height=800)
    f1.pack(side="top")

    labels_texts = [
        "Name",
        "Mobile No.",
        "Email Id",
        "Loan Amount",
        "Interest Per Annum",
        "Period In Months",
    ]
    default_texts = [
        "Enter Your Name...",
        "Enter Your Contact...",
        "Enter Your Email Id...",
        "Enter Your Loan Amount...",
        "Enter Your Interest Per Annum...",
        "Enter Your Period In Months...",
    ]

    entries = []
    for i, (label_text, default_text) in enumerate(zip(labels_texts, default_texts)):
        label = tk.Label(f1, text=label_text, font=("Arial", 20), fg="brown")
        label.place(x=100, y=140 + i * 70)
        entry = tk.Entry(
            f1, width=30, font=("Arial", 20), bg="light yellow", validate="key"
        )
        entry.insert(0, default_text)
        entry.bind("<FocusIn>", lambda event, idx=i: on_click(event.widget, idx))
        entry["validatecommand"] = (
            (entry.register(validate_numeric), "%P") if i >= 3 else ""
        )
        entry.place(x=350, y=140 + i * 70)
        entries.append(entry)

    e1, e2, e3, e4, e5, e6 = entries

    button_texts = [
        ("CALCULATE EMI", def_cal),
        ("USER DETAILS", def_details),
        ("GENERATE PDF", def_PDF),
        ("RESET", reset_fields),
    ]
    button_colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"]

    for i, (text, cmd) in enumerate(button_texts):
        button = tk.Button(
            cal_window,
            text=text,
            command=cmd,
            font=("Arial", 20),
            bg=button_colors[i],
            fg="white",
            borderwidth=3,
            relief="raised",
        )
        button.place(x=100 + (i % 3) * 300, y=600 + (i // 3) * 65)

    cal_window.mainloop()


def show_start_window():
    global start_window
    start_window = tk.Tk()
    start_window.geometry("1000x800")
    start_window.title("EMI Calculator")

    # Top label
    start1 = tk.Label(
        start_window, text="EMI CALCULATOR", font=("Arial", 50), fg="black"
    )
    start1.place(x=190, y=10)

    # Image on the main window
    path = "EMI.png"
    img1 = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(start_window, image=img1)
    panel.place(x=250, y=85)

    # Created start button
    startb = tk.Button(
        start_window,
        text="START",
        command=show_calculation_window,
        font=("Arial", 30),
        bg="green",
        fg="white",
        borderwidth=3,
        relief="raised",
    )
    startb.place(x=100, y=580)

    # Created EMI button
    emib = tk.Button(
        start_window,
        text="EMI INFO",
        command=lambda: messagebox.showinfo(
            "EMI INFO", "EMI stands for Equated Monthly Installment..."
        ),
        font=("Arial", 30),
        bg="purple",
        fg="white",
        borderwidth=3,
        relief="raised",
    )
    emib.place(x=390, y=580)

    def exit_win():
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            start_window.destroy()

    # Created exit button
    exitb = tk.Button(
        start_window,
        text="EXIT",
        command=exit_win,
        font=("Arial", 30),
        bg="red",
        fg="white",
        borderwidth=3,
        relief="raised",
    )
    exitb.place(x=730, y=580)

    start_window.protocol("WM_DELETE_WINDOW", exit_win)
    start_window.mainloop()


# Start the application
show_start_window()
