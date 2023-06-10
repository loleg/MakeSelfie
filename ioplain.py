#!/usr/bin/env python
import PySimpleGUI as sg
import imageio.v3 as iio


def main():

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ]]

    # create the window and show it without the plot
    window = sg.Window('Webcam',
                       layout, location=(800, 400))

    # set up webcam using imageio
    #camera = iio.get_reader("<video0>")

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    recording = False

    while True:
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Record':
            recording = True

        elif event == 'Stop':
            recording = False

        if recording:
            frame = iio.imread("<video0>", index=0, size=(640, 480))
            video_bytes = iio.imwrite("<bytes>", frame, extension=".gif")
            window['image'].update(data=video_bytes)


main()