

import tkinter as tk


root = tk.Tk()
root.title("Fibonacci Series Generator")
root.geometry("400x400")


instruction_label = tk.Label(root, text="Enter the number of terms:")
instruction_label.pack(pady=10)
 
entry = tk.Entry(root)
entry.pack(pady=5)


def generate_fibonacci():
    
    n = int(entry.get())
    
    
    fib_series = [0, 1]
    
    
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
     
    result_label.config(text="Fibonacci Series: " + str(fib_series))

  

generate_button = tk.Button(root, text="Generate Fibonacci Series", command=generate_fibonacci)
generate_button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
