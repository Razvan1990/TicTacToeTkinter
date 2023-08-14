import tkinter as tk

# Event handler function for the label click

def run_test():
    def label_clicked(event):
        print("Label clicked!")

    # Create the main window
    window = tk.Tk()
    window.title("PythonExamples.org")
    window.geometry("300x200")

    # Create a label widget
    label = tk.Label(window, text="Hello World!")

    # Bind the click event to the label
    label.bind("<Button-1>", label_clicked)

    # Pack the label widget to display it
    label.pack()

    # Run the application
    window.mainloop()

def run_test2():
    def handle_click(event):
        x = entry.insert(0, "X")
        print(x)

    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack(fill="x")

    entry.bind("<1>", handle_click)

    root.mainloop()