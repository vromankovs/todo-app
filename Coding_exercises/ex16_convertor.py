import FreeSimpleGUI as sg
from conventers import convert

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window(title="Convertor",
                   layout = [[label1, input1],
                             [label2, input2],
                             [convert_button]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()