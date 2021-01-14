#!/usr/bin/env python3 
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas.pack()

label = tk.Label(root, text='CS2', bg='azure3')
label.config(font=('helvetica', 20))
canvas.create_window(150, 60, window=label)
