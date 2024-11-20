#first pip install the tabulate 
from tabulate import tabulate

text = input("Input your password ")
t_w_u_e = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
data = []

for i in text:
    index = t_w_u_e.find(i)
    if index != -1:  # Check if character is in t_w_u_e
        new_index = (index + 2) % len(t_w_u_e)
        new_char = t_w_u_e[new_index]
        data.append([i, new_char])
    else:
        data.append([i, i])  # If character is not in t_w_u_e, keep it as is

table = tabulate(data, headers=["Char", "New Char"], tablefmt="grid")
print(table)
