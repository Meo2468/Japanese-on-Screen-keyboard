import tkinter as tk

# Create the main application window.
window = tk.Tk()

def main():
    # Declaring the window's title and size.
    window.title("JP_KeyBoard")
    window.geometry("1350x300")

    title = tk.Label(master=window, text="Welcome to JP_KeyBoard")
    title.grid(column=0, row=0)

    display_keyboard()

    window.mainloop() # Start the GUI event loop.


def on_key_press(key, button):
    print(key)
    button.config(bg="lightblue")



def display_keyboard():
    display_first_row()
    display_second_row()
    display_third_row()
    display_fourth_row()
    display_fifth_row()

def display_first_row():
    first_row = [" ~  ` ", " !  1 ", " @  2 ", " #  3 ", " $  4 ", " %  5 ",
                 " ^  6 ", " &  7 ", " *  8 ", " (  9 ", " )  0 ",
                 " _  - ", " +  = "]
    for index, key in enumerate(first_row):
        button = tk.Button(window, text=key, width=5, height=2, command=lambda k=key, b=None: on_key_press(k, b))
        button.grid(column=index, row=1)
        button.config(command=lambda k=key, b=button: on_key_press(k, b))
    button = tk.Button(window, text=" Backspace ⬅ ", width=10, height=2, command=lambda k="Backspace", b=None: on_key_press(k, b))
    button.grid(column=13, row=1, columnspan=2)
    button.config(command=lambda k="Backspace", b=button: on_key_press(k, b))


def display_second_row():
    second_row = [" Q ", " W ", " E ", " R ", " T ", " Y ", 
                  " U ", " I ", " O ", " P ", " {  [ ", " }  ] "]
    button = tk.Button(window, text=" Tab  ↹ ", width=7, height=2)
    button.grid(column=0, row=2, columnspan=1)
    for index, key in enumerate(second_row):
        button = tk.Button(window, text=key, width=5, height=2)
        button.grid(column=index + 1, row=2)
    button = tk.Button(window, text=" |  \\ ", width=7, height=2)
    button.grid(column=13, row=2)


def display_third_row():
    third_row = [" A ", " S ", " D ", " F ", " G ", " H ", 
                 " J ", " K ", " L ", " :  ; ", ' "  \' ']
    button = tk.Button(window, text=" CapsLock ⇪ ", width=9, height=2)
    button.grid(column=0, row=3)
    for index, key in enumerate(third_row):
        button = tk.Button(window, text=key, width=5, height=2)
        button.grid(column=index + 1, row=3)
    button = tk.Button(window, text=" Enter ⏎ ", width=9, height=2)
    button.grid(column=11, row=3, columnspan=4)


def display_fourth_row():
    fourth_row = [" Z ", " X ", " C ", " V ", " B ", " N ", 
                  " M ", " <  , ", " >  . ", " ?  / "]
    button = tk.Button(window, text=" Shift ⇧ ", width=16, height=2)
    button.grid(column=0, row=4)
    for index, key in enumerate(fourth_row):
        button = tk.Button(window, text=key, width=5, height=2)
        button.grid(column=index + 1, row=4, columnspan=1)
    button = tk.Button(window, text=" Shift ⇧ ", width=20, height=2)
    button.grid(column=10, row=4, columnspan=6)


def display_fifth_row():
    button = tk.Button(window, text=" Ctrl ⎈ ", width=7, height=4)
    button.grid(column=0, row=5)
    button = tk.Button(window, text=" Fn ", width=7, height=4)
    button.grid(column=1, row=5)
    button = tk.Button(window, text=" Win ⊞ ", width=7, height=4)
    button.grid(column=2, row=5)
    button = tk.Button(window, text=" Alt ⎇ ", width=7, height=4)
    button.grid(column=3, row=5)
    button = tk.Button(window, text=" Space ", width=40, height=4)
    button.grid(column=4, row=5, columnspan=5)
    button = tk.Button(window, text=" Alt ⎇ ", width=7, height=4)
    button.grid(column=9, row=5)
    button = tk.Button(window, text=" Menu ☰ ", width=7, height=4)
    button.grid(column=10, row=5)
    button = tk.Button(window, text=" Ctrl ⎈ ", width=7, height=4)
    button.grid(column=11, row=5)
    button = tk.Button(window, text=" ← ", width=5, height=4)
    button.grid(column=12, row=5)
    button = tk.Button(window, text=" ↓ ", width=5, height=1)
    button.grid(column=13, row=6)
    button = tk.Button(window, text=" → ", width=5, height=4)
    button.grid(column=14, row=5)
    button = tk.Button(window, text=" ↑ ", width=5, height=1)
    button.grid(column=13, row=4, rowspan=6)


if __name__ == "__main__":
    main()