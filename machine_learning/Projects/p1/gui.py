import os
import pickle
import tkinter as tk
from tkinter import ttk
import pandas as pd

# --- Load the trained model ---
model_path = r'Amit\machine_learning\Projects\p1\model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    model_status = "Model loaded successfully!"
else:
    model = None
    model_status = "Model not found!"

# --- GUI Setup ---
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("700x550")
root.configure(bg="#e0f2f1")

# Fonts
label_font = ("Arial", 13, "bold")
entry_font = ("Arial", 13)
button_font = ("Arial", 13, "bold")
result_font = ("Arial", 16, "bold")

# --- Title ---
title = tk.Label(root, text="🏠 House Price Predictor", font=("Arial", 20, "bold"), bg="#e0f2f1", fg="#00695c")
title.pack(pady=15)

# --- Frame for Inputs ---
input_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge", padx=20, pady=20)
input_frame.pack(pady=10, padx=20, fill="x")

# --- Labels & Entries with Cards ---
tk.Label(input_frame, text="Average Rooms (RM):", font=label_font, bg="#ffffff").grid(row=0, column=0, sticky="w", pady=10)
entry_rooms = tk.Entry(input_frame, font=entry_font, bd=2, relief="groove")
entry_rooms.grid(row=0, column=1, pady=10, padx=10)

tk.Label(input_frame, text="Poverty % (LSTAT):", font=label_font, bg="#ffffff").grid(row=1, column=0, sticky="w", pady=10)
entry_poverty = tk.Entry(input_frame, font=entry_font, bd=2, relief="groove")
entry_poverty.grid(row=1, column=1, pady=10, padx=10)

tk.Label(input_frame, text="Student-Teacher Ratio (PTRATIO):", font=label_font, bg="#ffffff").grid(row=2, column=0, sticky="w", pady=10)
entry_student_teacher = tk.Entry(input_frame, font=entry_font, bd=2, relief="groove")
entry_student_teacher.grid(row=2, column=1, pady=10, padx=10)

# --- Result Card ---
result_frame = tk.Frame(root, bg="#b2dfdb", bd=2, relief="ridge", padx=20, pady=20)
result_frame.pack(pady=15, padx=20, fill="x")
label_result = tk.Label(result_frame, text=model_status, font=result_font, bg="#b2dfdb", fg="green" if model else "red")
label_result.pack()

# --- Functions ---
def predict_price():
    if model is None:
        label_result.config(text="Model not loaded!", fg="red")
        return
    try:
        rooms = float(entry_rooms.get())
        poverty = float(entry_poverty.get())
        stratio = float(entry_student_teacher.get())
        X_new = pd.DataFrame([[rooms, poverty, stratio]], columns=['RM','LSTAT','PTRATIO'])
        prediction = model.predict(X_new)[0]
        label_result.config(text=f"Predicted House Price: ${prediction:,.2f}", fg="#004d40")
    except ValueError:
        label_result.config(text="Enter valid numbers!", fg="red")
    except Exception as e:
        label_result.config(text=f"Error: {e}", fg="red")

def reset_fields():
    entry_rooms.delete(0, tk.END)
    entry_poverty.delete(0, tk.END)
    entry_student_teacher.delete(0, tk.END)
    label_result.config(text=model_status, fg="green" if model else "red")

# --- Buttons ---
button_frame = tk.Frame(root, bg="#e0f2f1")
button_frame.pack(pady=10)

btn_predict = tk.Button(button_frame, text="Predict", command=predict_price, bg="#00796b", fg="white",
                        font=button_font, activebackground="#004d40", activeforeground="white", bd=0, padx=20, pady=10)
btn_predict.grid(row=0, column=0, padx=15)

btn_reset = tk.Button(button_frame, text="Reset", command=reset_fields, bg="#c62828", fg="white",
                      font=button_font, activebackground="#8e0000", activeforeground="white", bd=0, padx=20, pady=10)
btn_reset.grid(row=0, column=1, padx=15)

root.mainloop()