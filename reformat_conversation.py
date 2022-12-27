import tkinter as tk
import re
import datetime

def reformat_conversation():
    # Get the conversation from the entry field
    conversation = entry.get("1.0", "end-1c")
    # Get the email address from the first line of the conversation
    lines = conversation.split("\n")
    email = lines[0]

    # Split the conversation into a list of lines
    lines = conversation.split("\n")

    # Initialize an empty list for the reformatted conversation
    reformatted = []

    # Iterate through the lines and reformat them
    for line in lines:
        # Replace the specified email address with a single space
        line, replacements = re.subn(email, ' ', line)

        # Add a line break and a line of 40 equal signs above the line if the email address was found in the line
        if replacements > 0:
            reformatted.append("\n" + "=" * 40)
        else:
            line = "\t" + line
        reformatted.append(line)

    # Join the reformatted lines into a single string
    reformatted_conversation = "\n".join(reformatted)

    # Save the reformatted conversation to a new text file with the current date and time as the filename
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    with open(filename, "w") as file:
        file.write(reformatted_conversation)

# Create the main window
root = tk.Tk()
root.title("Conversation Formatter")

# Set the background color to a dark grey
root.configure(bg="#444444")

# Create the button
button = tk.Button(root, text="Reformat", command=reformat_conversation, bg="#333333", fg="white")
button.pack()

# Create the input field
entry = tk.Text(root, bg="#333333", fg="white")
entry.pack(fill=tk.BOTH, expand=True)

# Automatically resize the input and button widgets when the GUI is resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# Set the initial size of the GUI to be smaller
root.geometry("400x300")

# Run the main loop
root.mainloop()
