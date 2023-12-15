import PySimpleGUI as sg

layout = [
    [sg.Text("Introduce dos números")],
    [sg.InputText(), sg.InputText()],
    [sg.Button("Sumar"), sg.Button("Restar"), sg.Button("Multiplicar"), sg.Button("Dividir"), sg.Cancel()]
]

window = sg.Window("Calculadora", layout, size=(600, 300))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Cancel"):
        break

    try:
        number1 = int(values[0])
        number2 = int(values[1])

        if event == "Sumar":
            result = number1 + number2
            sg.popup(f"La suma es {result}")

        elif event == "Restar":
            result = number1 - number2
            sg.popup(f"La resta es {result}")

        elif event == "Multiplicar":
            result = number1 * number2
            sg.popup(f"La multiplicación es {result}")

        elif event == "Dividir":
            if number2 != 0:
                result = number1 / number2
                sg.popup(f"La división es {result}")
            else:
                sg.popup("Error: No se puede dividir por cero.")

    except ValueError:
        sg.popup("Error: Ingresa números válidos.")

window.close()
