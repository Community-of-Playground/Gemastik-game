import tkinter as tk

def send_message():
    message = entry.get()
    messages.insert(tk.END, "You: " + message)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("WhatsApp Clone Chat App")
root.geometry("400x600")

messages_frame = tk.Frame(root)
messages_frame.pack(pady=10)

messages = tk.Listbox(messages_frame, width=50, height=20)
messages.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar = tk.Scrollbar(messages_frame, orient=tk.VERTICAL, command=messages.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
messages.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()