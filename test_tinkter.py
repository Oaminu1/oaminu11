#!/usr/bin/env python3

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Tkinter Check")
    label = tk.Label(root, text="Tkinter is working!", padx=20, pady=20)
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()

