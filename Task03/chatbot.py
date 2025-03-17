import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

# Define chatbot responses
pairs = [
    [r"hi|hello|hey", [f"Hello Sujal Anjara! How can I assist you today?", "Hi Sujal!"]],
    [r"what is your name?", ["I am Sujal's personal chatbot created for this internship."]],
    [r"what is python?", ["Python is a versatile programming language used for web development, AI, and more."]],
    [r"how are you?", ["I'm just a bot, but I'm always ready to help you, Sujal!"]],
    [r"bye|goodbye", ["Goodbye Sujal! Have a great day!", "See you later, Sujal!"]],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Function to handle user input
def send_message():
    user_input = user_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
    user_entry.delete(0, tk.END)

    if user_input.lower() == "bye":
        chat_window.insert(tk.END, "🤖 Chatbot: Goodbye Sujal! Have a great day!\n", "bot")
        chat_window.config(state=tk.DISABLED)
        root.quit()
    else:
        response = chatbot.respond(user_input)
        chat_window.insert(tk.END, "🤖 Chatbot: " + response + "\n", "bot")
    
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)  # Auto-scroll to the latest message

# Create GUI window
root = tk.Tk()
root.title("Sujal's AI Chatbot 🤖")
root.geometry("400x500")
root.resizable(False, False)

# Chat Window
chat_window = Text(root, wrap="word", state=tk.DISABLED, font=("Arial", 12))
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(chat_window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_window.yview)

# User Input Field
user_entry = Entry(root, font=("Arial", 12))
user_entry.pack(pady=5, padx=10, fill=tk.X)

# Send Button
send_button = Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# Initial Greeting
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "🤖 Chatbot: Hi Sujal Anjara! Welcome to your AI chatbot. Type 'hi' to start chatting!\n", "bot")
chat_window.config(state=tk.DISABLED)

# Run GUI
root.mainloop()
