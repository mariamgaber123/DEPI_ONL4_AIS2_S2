import os
import pickle
import tkinter as tk
import pandas as pd

# --- Load the trained model from pickle ---
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
root.geometry("750x500")
root.configure(bg="#f0f4f8")

# Fonts
label_font = ("Helvetica", 16)
entry_font = ("Helvetica", 16)
button_font = ("Helvetica", 16, "bold")

# Main Frame
frame = tk.Frame(root, bg="#f0f4f8", padx=30, pady=30)
frame.pack(expand=True)

# --- Labels ---
tk.Label(frame, text="Average Rooms (RM):",
         font=label_font, bg="#f0f4f8").grid(row=0, column=0, padx=15, pady=15, sticky="e")

tk.Label(frame, text="Poverty % (LSTAT):",
         font=label_font, bg="#f0f4f8").grid(row=1, column=0, padx=15, pady=15, sticky="e")

tk.Label(frame, text="Student-Teacher Ratio (PTRATIO):",
         font=label_font, bg="#f0f4f8").grid(row=2, column=0, padx=15, pady=15, sticky="e")

# --- Entries ---
entry_rooms = tk.Entry(frame, font=entry_font, bd=2, relief="groove")
entry_poverty = tk.Entry(frame, font=entry_font, bd=2, relief="groove")
entry_student_teacher = tk.Entry(frame, font=entry_font, bd=2, relief="groove")

entry_rooms.grid(row=0, column=1, padx=15, pady=15)
entry_poverty.grid(row=1, column=1, padx=15, pady=15)
entry_student_teacher.grid(row=2, column=1, padx=15, pady=15)

# Result label
label_result = tk.Label(
    frame,
    text=model_status,
    fg="green" if model else "red",
    font=("Helvetica", 16, "bold"),
    bg="#f0f4f8"
)
label_result.grid(row=4, column=0, columnspan=2, pady=20)


# --- Prediction Function ---
def predict_price():

    if model is None:
        label_result.config(text="Model not loaded!", fg="red")
        return

    rooms = entry_rooms.get()
    poverty = entry_poverty.get()
    stratio = entry_student_teacher.get()

    if not rooms or not poverty or not stratio:
        label_result.config(text="Enter all fields!", fg="red")
        return

    try:
        rooms = float(rooms)
        poverty = float(poverty)
        stratio = float(stratio)

        X_new = pd.DataFrame(
            [[rooms, poverty, stratio]],
            columns=['RM', 'LSTAT', 'PTRATIO']
        )

        prediction = model.predict(X_new)[0]

        label_result.config(
            text=f"Predicted House Price: ${prediction:,.2f}",
            fg="#1f4e79"
        )

    except ValueError:
        label_result.config(text="Please enter valid numeric values!", fg="red")

    except Exception as e:
        label_result.config(text=f"Error: {e}", fg="red")


# --- Reset Function ---
def reset_fields():
    entry_rooms.delete(0, tk.END)
    entry_poverty.delete(0, tk.END)
    entry_student_teacher.delete(0, tk.END)

    label_result.config(
        text=model_status,
        fg="green" if model else "red"
    )


# --- Buttons ---
btn_predict = tk.Button(
    frame,
    text="Predict",
    command=predict_price,
    bg="#4caf50",
    fg="white",
    font=button_font,
    activebackground="#45a049",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=10
)

btn_predict.grid(row=3, column=0, columnspan=2, pady=15)

btn_reset = tk.Button(
    frame,
    text="Refresh / Reset",
    command=reset_fields,
    bg="#f44336",
    fg="white",
    font=button_font,
    activebackground="#e53935",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=10
)

btn_reset.grid(row=5, column=0, columnspan=2, pady=15)

# Grid spacing
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

root.mainloop()