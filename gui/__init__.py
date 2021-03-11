import PySimpleGUI as sg

class Gui:

    def __init__( self ):
        pass

    def getMainWindow( self ):
        layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

        # Create the window
        window = sg.Window("Demo", layout)

        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "OK" or event == sg.WIN_CLOSED:
                break

        window.close()

    def getStockWindow( self ):
        pass

    def getMarketWindow( self ):
        pass

    def getDisclaimerWindow( self ):
        pass