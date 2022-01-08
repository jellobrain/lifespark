#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import connection
import PySimpleGUI as Sg
import results
import imports
import codes
import members
import admissions


def main():
    layout = [[Sg.Text("It is expected that at a minimum you have a local database engine installed, "
                       "python3 installed, and an empty database called 'lifespark'.")], [Sg.Button("OK")]]

    # Create the window
    window = Sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == Sg.WIN_CLOSED:
            home()
            window.close()


def home():
    layout = [[Sg.Text("Please select what you would like to do:")], [Sg.Button("Import CSV")],
              [Sg.Button("Get Results")], [Sg.Button("Exit")]]

    # Create the window
    window = Sg.Window("Home", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Import CSV":
            window.close()
            leimports()

        elif event == "Get Results":
            window.close()
            leresults()

        elif event == "Exit" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


def leimports():
    layout = [[Sg.Text("If you have an empty database with no tables already in it, "
                       "please choose to undeergo the fullmonty.  If you already have data in the tables, \n"
                       "but want to add or change them, select a table you would like to import.  "
                       "Make sure you include your username and password.")],
              [Sg.Text('Username'), Sg.Input()],
              [Sg.Text('Password'), Sg.Input()],
              [Sg.Button('Import Full Monty')],
              [Sg.Button('Reimport Members')],
              [Sg.Button('Reimport Codes')],
              [Sg.Button('Import additional Admissions')],
              [Sg.Button('Home')],
              [Sg.Button('Exit')]]

    # Create the window
    window = Sg.Window("Imports", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Import Full Monty" and values[0] and values[1]:
            window.close()
            imports.fullmonty(values[0], values[1])

        elif event == "Reimport Members" and values[0] and values[1]:
            window.close()
            members.members(values[0], values[1])

        elif event == "Reimport Codes" and values[0] and values[1]:
            window.close()
            codes.codes(values[0], values[1])

        elif event == "Import additional Admissions" and values[0] and values[1]:
            window.close()
            admissions.admissions(values[0], values[1])

        elif event == "Home":
            window.close()
            home()

        elif event == "Exit" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


def leresults():
    layout = [[Sg.Text("Before getting any results, you will need to have run the 'Full Monty' at least once "
                       "because it brings in important views that are essential for these results to compute.")],
              [Sg.Text('Username'), Sg.Input()],
              [Sg.Text('Password'), Sg.Input()],
              [Sg.Button('Run All Results')],
              [Sg.Button('Top 10 Costing Members')],
              [Sg.Button('Admission Costs and Counts per Week')],
              [Sg.Button('Readmissions')],
              [Sg.Button('Top 10 Longest Admissions')],
              [Sg.Button('Home')],
              [Sg.Button('Exit')]]

    # Create the window
    window = Sg.Window("Results", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button

        if event == "Run All Results" and values[0] and values[1]:
            window.close()
            results.fullmonty(values[0], values[1])

        elif event == "Top 10 Costing Members" and values[0] and values[1]:
            window.close()
            results.costmembers(values[0], values[1])

        elif event == "Admission Costs and Counts per Week" and values[0] and values[1]:
            window.close()
            results.admcostcount(values[0], values[1])

        elif event == "Readmissions" and values[0] and values[1]:
            window.close()
            results.readmissions(values[0], values[1])

        elif event == "Top 10 Longest Admissions" and values[0] and values[1]:
            window.close()
            results.admlongest(values[0], values[1])

        elif event == "Home":
            window.close()
            home()

        elif event == "Exit" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
