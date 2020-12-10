import PySimpleGUI as sg
from logic import decimalize, popularity_handler

row1 =[[sg.Button("1")], [sg.Button("1")], [sg.Button("1")]]

# Create the window
window = sg.Window("Demo", row1)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "1" or event == sg.WIN_CLOSED:
        break

window.close()