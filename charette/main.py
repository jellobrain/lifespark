#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as Sg
import imports
import results
import members
import codes
import admissions


def main():
    intro = [[Sg.Text("In order to proceed, you must have an EMPTY instance of a database up on your localhost "
                      "called 'lifespark'.  It is also assumed you have python3 installed.  I used MySQL on my "
                      "localhost, and it should also work with other database engines.")],
             [Sg.Button("OK")], [Sg.Button("Close")]]

    # Create the window
    window = Sg.Window("Welcome", intro)

    # Create an event loop
    while True:
        event, values = window.read()
        if event == "OK" or event == Sg.WIN_CLOSED:
            home()
            window.close()

        elif event == "Close" or event == Sg.WIN_CLOSED:
            window.close()
            quit()
    

def home():
    choosesection = [[Sg.Text("Is the database empty or does it already have existing tables with data in them?  "
                              "Alternatively, you can choose 'Generate Reports' "
                              "if you just want to run some reports.")],
                     [Sg.Button("Existing data")], [Sg.Button("Empty database")], [Sg.Button("Run reports")],
                     [Sg.Button("Close")]]

    # Create the window
    window = Sg.Window("Home", choosesection)
    while True:
        event, values = window.read()
        if event == "Empty database":
            emptydb()
            window.close()

        elif event == "Existing data":
            existingdata()
            window.close()

        elif event == "Run reports":
            runreports()
            window.close()

        elif event == "Close" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


def emptydb():
    empty = [[Sg.Text("What are your database credentials?")],
             [Sg.Text('Database User', size=(30, 1)), Sg.InputText()],
             [Sg.Text('User Password', size=(30, 1)), Sg.InputText()],
             [Sg.Text("Please chill while we perform a quick and complete installation of the data.")],
             [Sg.Button("OK")], [Sg.Button("Back Home")], [Sg.Button("Close")]]

    # Create the window
    window = Sg.Window("Empty Database", empty)

    while True:
        event, values = window.read()
        if event == "OK" and values[0] and values[1]:
            imports.fullmonty(values[0], values[1])
            window.close()

        if event == "Back Home":
            home()
            window.close()

        elif event == "Close" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


def existingdata():
    existing = [[Sg.Text("What are your database credentials?")],
                [Sg.Text('Database User', size=(30, 1)), Sg.InputText()],
                [Sg.Text('User Password', size=(30, 1)), Sg.InputText()],
                [Sg.Text("Please choose one from the following types of information you would like to import.")],
                [Sg.Button("Members")], [Sg.Button("Codes")], [Sg.Button("Admissions")],
                [Sg.Button("Run Reports")], [Sg.Button("Close")]]

    # Create the window
    window = Sg.Window("Add Data", existing)

    while True:
        event, values = window.read()
        if event == "Members" and values[0] and values[1]:
            members.members(values[0], values[1])
            window.close()

        elif event == "Codes" and values[0] and values[1]:
            codes.codes(values[0], values[1])
            window.close()

        elif event == "Admissions" and values[0] and values[1]:
            admissions.admissions(values[0], values[1])
            window.close()

        elif event == "Run reports" and values[0] and values[1]:
            runreports()
            window.close()

        elif event == "Back Home":
            home()

        elif event == "Close" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


def runreports():
    choosereport = [[Sg.Text("What are your database credentials?")],
                    [Sg.Text('Database User', size=(30, 1)), Sg.InputText()],
                    [Sg.Text('User Password', size=(30, 1)), Sg.InputText()],
                    [Sg.Text("Which report would you like to run?")],
                    [Sg.Button("Top Highest Costing Members")], [Sg.Button("Admissions Cost and Count")],
                    [Sg.Button("Readmissions")], [Sg.Button("10 Longest Admissions")], [Sg.Button("All")],
                    [Sg.Button("Back Home")], [Sg.Button("Close")]]

    # Create the window
    window = Sg.Window("Run Reports", choosereport)

    while True:
        event, values = window.read()
        if event == "Top Highest Costing Members" and values[0] and values[1]:
            results.costmembers(values[0], values[1])

        elif event == "Admissions Cost and Count" and values[0] and values[1]:
            results.admcostcount(values[0], values[1])

        elif event == "Readmissions" and values[0] and values[1]:
            results.readmissions(values[0], values[1])

        elif event == "10 Longest Admissions" and values[0] and values[1]:
            results.admlongest(values[0], values[1])

        elif event == "All" and values[0] and values[1]:
            results.fullmonty(values[0], values[1])

        elif event == "Back Home":
            home()

        elif event == "Close" or event == Sg.WIN_CLOSED:
            window.close()
            quit()


if __name__ == '__main__':
    main()
