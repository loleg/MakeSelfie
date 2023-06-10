import PySimpleGUI as sg
import requests, random


BAR_WIDTH = 50      # width of each bar
BAR_SPACING = 75    # space between each bar
EDGE_OFFSET = 3     # offset from the left edge for first bar
GRAPH_SIZE = DATA_SIZE = (500,500)       # size in pixels

sg.theme('Light brown 1')

# Create the window

layout = [  
            [sg.Text("What's your username?", key='-LABEL1-')],
            [sg.Input('', key='-INPUT-')],
            [sg.Button('OK')],
            [sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE, k='-GRAPH-')],
            [sg.Exit()]
        ]

window = sg.Window('MakeSelfie', layout, finalize=True)

graph = window['-GRAPH-'] # type: sg.Graph

while True:

    graph.erase()
    for i in range(7):
        graph_value = random.randint(0, GRAPH_SIZE[1]-25)       # choose an int just short of the max value to give room for the label
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color='green')
                             # fill_color=sg.theme_button_color()[1])

        graph.draw_text(text=graph_value, location=(i*BAR_SPACING+EDGE_OFFSET+25, graph_value+10), font='_ 14')

    event, values = window.read()


    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'OK':
        username = values['-INPUT-']
        print('Hello', username)

        # Super safe internet request :-P
        r = requests.get('https://now.makezurich.ch/api/user/' + username)

        if r.status_code == 200:
            userdata = r.json()
            print(userdata)
        elif r.status_code == 404:
            print('User not found')
            window['-LABEL1-'].update('User not found, please try again')
        else:  
            print('Houston we have a problem')
            print(r.text)

window.close()

