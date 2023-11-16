import tkinter as tk
from random import randint


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(n):
    next_prime = n - 1
    while not is_prime(next_prime):
        next_prime -= 1
    return next_prime

def clicked():
    message = entry.get()

    p = find_next_prime(randint(100, 540))
    q = find_next_prime(randint(100, 540))

    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_next_prime(phi - 1)
    while phi % e == 0:
        e = find_next_prime(e)

    encoded = []

    for letter in message:
        code = ord(letter)
        encoded.append(code ** e % n)
    

    d = e - 1
    while (d * e) % phi != 1:
        d -= 1

    decoded = []
    for i in encoded:
        decode = i ** d % n
        decoded.append(chr(decode))

    string = ''.join(decoded)
    open = f'Public key: {e}, {n}'
    close = f'Private key: {d}, {n}'

    label.configure(text = string)
    label_open.configure(text = open)
    label_close.configure(text = close)

window = tk.Tk()
window.title("RSA encryption")
window.geometry('400x300')

entry = tk.Entry(window)
entry.focus()
entry.pack()

label = tk.Label(window, text="Encrypted message")
label.pack()


label_open = tk.Label(window, text="Public key")
label_open.pack()

label_close = tk.Label(window, text="Private key")
label_close.pack()

button = tk.Button(window, text="Encrypt", command=clicked)
button.pack()

window.mainloop()
