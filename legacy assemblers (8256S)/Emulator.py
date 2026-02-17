import tkinter as tk

# Example list of 256 members
memory = [hex(0) for i in range(256)]
pc = 0
a = 0
flags = 0
instruction = 0

def additional_code():
    global memory
    global pc
    global a
    global flags
    global instruction

    # This function will be executed within the Tkinter mainloop
    # Add your desired code here
    instruction = memory[pc]
    pc += 1
    print(instruction)
    print(pc)
    if instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass
    elif instruction[:5] == "lda @":
        pass

    # Call additional_code() again after 1000 milliseconds (1 second)
    window.after(1000, additional_code)

def create_grid(memory):
    global window  # Declare window as a global variable

    # Create a new Tkinter window
    window = tk.Tk()
    window.title("16x16 Grid")

    # Create a frame to hold the grid
    frame = tk.Frame(window)

    # Create a 2D list to hold the label widgets
    labels = []
    for i in range(16):
        row = []
        for j in range(16):
            label = tk.Label(frame, width=8, height=2, relief=tk.SOLID, borderwidth=1)
            label.grid(row=i, column=j, padx=2, pady=2)
            row.append(label)
        labels.append(row)

    # Add some padding to the frame
    frame.pack(padx=10, pady=10)

    # Populate the labels with data from the list
    for i in range(16):
        for j in range(16):
            index = i * 16 + j
            if index < len(memory):
                labels[i][j].config(text=memory[index])

    # Save the window reference to use in additional_code()
    window.after(1000, additional_code)

    # Start the Tkinter event loop
    window.mainloop()

# Call the function to create the grid
create_grid(memory)