import tkinter as tk
import numpy as np

class SalayrPredictionApp:
   def __init__(self,root):
      self.root=root
      self.root.title("Depi R4 - machine learing Diploma ")
      self.root.geometry("500x400")

   def create_widget(self):
      header=tk.Label(self.root,text="DEPI",bg="blue",fg="white" ,font=("Arial",28,"bold"))   
      header.pack(fill=tk.X)

if __name__ == "__main__":
   root=tk.Tk()
   app = SalayrPredictionApp(root)
   root.mainloop()   
   