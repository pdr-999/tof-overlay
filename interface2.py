#!/usr/bin/env python
import os
import signal
import PySimpleGUI as sg
import string

ON_LONG_COOLDOWN_BACKGROUND_COLOR = '#c1c6d5'
ON_LONG_COOLDOWN_TEXT_COLOR = '#292846'

ON_SHORT_COOLDOWN_BACKGROUND_COLOR = '#f1e986'
ON_SHORT_COOLDOWN_TEXT_COLOR = '#292846'

READY_BACKGROUND_COLOR = '#257051'
READY_TEXT_COLOR = '#fff'


def GetTextSettings(cd: int, readyKey: string):
    if (cd <= 2):
        return {'value': str(cd),
                'background_color': READY_BACKGROUND_COLOR, 'text_color': READY_TEXT_COLOR}
    elif (cd <= 10):
        return {'value': str(cd),
                'background_color': ON_SHORT_COOLDOWN_BACKGROUND_COLOR, 'text_color': ON_SHORT_COOLDOWN_TEXT_COLOR}
    else:
        return {'value': str(cd),
                'background_color': ON_LONG_COOLDOWN_BACKGROUND_COLOR, 'text_color': ON_LONG_COOLDOWN_TEXT_COLOR}


def StatusOutputExample(pid, cooldowns):

    # Create a text element that will be updated with status information on the GUI itself
    # Create the rows

    default_text_settings = {'auto_size_text': False, 'size': (
        3, 1), 'background_color': READY_BACKGROUND_COLOR, 'text_color': READY_TEXT_COLOR, 'justification': 'center', 'font': ('Oxanium', 24)}

    layout = [
        [
            sg.Text('', key='Q', **default_text_settings),
            sg.Text('', key='E', **default_text_settings),
            sg.Text('', key='R', **default_text_settings),
            sg.Button(key='Quit', button_text='X',
                      font=('Oxanium', 8), size=(2, 1), tooltip='Close')
        ],
    ]

    # Layout the rows of the Window and perform a read. Indicate the Window is non-blocking!
    window = sg.Window('Running Timer', layout, disable_minimize=False, disable_close=True,
                       auto_size_text=True, keep_on_top=True, no_titlebar=True, resizable=True, background_color='red', transparent_color='red', alpha_channel=0.8)

    #
    # Some place later in your code...
    # You need to perform a Read on your window every now and then or
    # else it won't refresh.
    #
    # your program's main loop

    while True:
        event, values = window.read(timeout=10)

        window['Q'].update(**GetTextSettings(cooldowns['Q'], 'Q'))
        window['E'].update(**GetTextSettings(cooldowns['E'], 'E'))
        window['R'].update(**GetTextSettings(cooldowns['R'], 'R'))

        if event in ('Quit', None):
            break

    # Broke out of main loop. Close the window.
    window.close()
    os.kill(pid, signal.SIGTERM)


def main(pid, cooldowns):
    StatusOutputExample(pid, cooldowns)


if __name__ == '__main__':
    main()
