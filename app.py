import PySimpleGUI as sg
import re, sys

sg.theme("black")
display = ""

def calculator(command):
    try:
        result = float(eval(command))
        if result.is_integer():
            result = int(result)
            return str(result)
        
        else:
            return str(result)
    except Exception as e:
        return str("Err...")
        sys.exit(0)



layout = [
    [sg.Multiline("", size=(17, 3), key="-display-", justification="r", font="digit 20", no_scrollbar=True)],
    [sg.Button("clear", size=(5,3)), sg.Button("(", size=(5,3)), sg.Button(")", size=(5,3)), sg.Button("/", size=(5,3))],
    [sg.Button("7", size=(5,3)), sg.Button("8", size=(5,3)), sg.Button("9", size=(5,3)), sg.Button("*", size=(5,3))],
    [sg.Button("4", size=(5,3)), sg.Button("5", size=(5,3)), sg.Button("6", size=(5,3)), sg.Button("-", size=(5,3))],
    [sg.Button("1", size=(5,3)), sg.Button("2", size=(5,3)), sg.Button("3", size=(5,3)), sg.Button("+", size=(5,3))],
    [sg.Button("0", size=(5,3)), sg.Button(".", size=(5,3)), sg.Button("%", size=(5,3)), sg.Button("=", size=(5,3))]
]

window = sg.Window("CALCULADOR", layout=layout, element_justification="center")

while True:
    
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", "-", "+", "(", ")"):
        display += event

    if event == "clear":
        display = ""

    if event == "=":
        command = values["-display-"]
        display = calculator(command)

    if event == "%":
        

        expressao_matematica = values["-display-"]
        resultado = re.search(r"\d+\s*$", expressao_matematica)
        if resultado:
            agrupamento_numerico = resultado.group()
            display = display.replace(agrupamento_numerico, str(int(agrupamento_numerico)/100))



    window["-display-"].update(display)

window.close

