import PySimpleGUI as sg

sg.theme('Dark2')

home_layout = [
    [sg.Text('Some stuff in home')]
]

tabs = [sg.Tab('Home', home_layout)]

clients = ['Client_1','Client_2','Client_3']

def get_client_tabs(clients):
    for client in clients:
        client_layout = [
            [sg.Text(client)]
        ]
        tabs.append(sg.Tab(client, client_layout))
    return(tabs)

tabs = get_client_tabs(clients)

tab_group = [[
    sg.TabGroup(
        [tabs]
        )]]

#Define Window
window =sg.Window("Tabs",tab_group)

while True:
    event,values=window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Add Connection":
        pass
        # contact_information_array.append([values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-']])
        # window['-TABLE-'].update(values=contact_information_array)
    if event == "Update Database":
        pass
    if event == "Delete Connection":
        pass
window.close()  
