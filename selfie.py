#!/usr/bin/env python
import PySimpleGUI as sg
import imageio.v3 as iio
import requests, random
import numpy as np

sg.theme('Light blue 1')

layout = [  
            [
                sg.Button('Start', key='Record', size=(10, 1), font='Helvetica 14'),
                sg.Button('CHEESE!', key='Stop', size=(10, 1), font='Helvetica 14'),
                sg.Button('Exit', size=(10, 1), font='Helvetica 14'),
            ],
            [sg.Text("Your MakeZurich username:", key='-LABEL1-')],
            [sg.Input('', key='-INPUT-', size=(10, 1), font='Helvetica 35')],
            [
                sg.Image(filename='', key='logo'),
                sg.Text('', font='Helvetica 35', key='Uscore'),
                sg.Text('', font='Helvetica 14', key='Ustory', size=(40, 5)),
            ],
            [sg.Image(filename='', key='image')],
        ]

window = sg.Window('MakeSelfie', layout, finalize=True)

mzlogo = iio.imread('logo-makezurich-2023.png')
logobytes = iio.imwrite("<bytes>", mzlogo, extension=".gif")
window['logo'].update(data=logobytes)

recording = False

while True:
 
    event, values = window.read(timeout=200)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == 'Record':
        username = values['-INPUT-']
        print('Hello', username)

        # Super safe internet request :-P
        r = requests.get('https://now.makezurich.ch/api/user/' + username)

        if r.status_code == 200:
            userdata = r.json()
            print(userdata)
            window['Ustory'].update(userdata['my_story'])
            window['Uscore'].update(userdata['score'])

        elif r.status_code == 404:
            print('User not found')
            window['-LABEL1-'].update('User not found, please try again')

        else:  
            print('Houston we have a problem')
            print(r.text)

    elif event == 'Stop' and not recording:
        recording = True

    elif event == 'Stop' and recording:

        gray_frames = np.dot(frame, [0.2989, 0.5870, 0.1140])
        gray_frames = np.round(gray_frames).astype(np.uint8)
        gray_frames_as_rgb = np.stack([gray_frames] * 3, axis=-1)
        gray_frames_flip = np.flipud(gray_frames_as_rgb)

        # TODO: combine logo, text etc. into output
        # grey_logo = np.round(mzlogo).astype(np.uint8)
        # grey_logo = np.stack([grey_logo] * 3, axis=-1)
        # merged = np.dstack((gray_frames_flip, grey_logo))

        iio.imwrite('selfie.gif', gray_frames_flip)
        print("Wrote SELFIE.GIF")
        recording = False

    if recording:
        frame = iio.imread("<video0>", index=0, size=(640, 480))
        video_bytes = iio.imwrite("<bytes>", frame, extension=".gif")
        window['image'].update(data=video_bytes)
        

window.close()

