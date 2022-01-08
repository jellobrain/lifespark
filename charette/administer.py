#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
import imports
import results
import members
import codes
import admissions


def main():
    sg.Window(title="Welcome to the Importer and Report Builder for this exercise.",
              layout=[[]], margins=(100, 50)).read()
    intro = [[sg.Text("In order to proceed, you must have an EMPTY instance of a database up on your localhost "
                      "called 'lifespark'.  It is also assumed you have python3 installed.  I used MySQL on my "
                      "localhost, and it should also work with other database engines.")],
             [sg.Button("OK")], [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Welcome", intro)

    # Create an event loop
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            home()

        elif event == "Close" or event == sg.WIN_CLOSED:
            break

    window.close()

def home():
    sg.Window(title="Home Screen", layout=[[]], margins=(100, 50)).read()
    choosesection = [[sg.Text("Is the database empty or does it already have existing tables with data in them?  "
                     "Alternatively, you can choose 'Generate Reports' if you just want to run some reports.")],
                     [sg.Button("Existing data")], [sg.Button("Empty database")], [sg.Button("Run reports")],
                     [sg.Button("Close")]]


    # Create the window
    window = sg.Window("Home", choosesection)
    while True:
        event, values = window.read()
        if event == "Empty database":
            emptydb()

        elif event == "Existing data":
            existingdata()

        elif event == "Run reports":
            runreports()

        elif event == "Close" or event == sg.WIN_CLOSED:
            break

    window.close()


def emptydb():
    sg.Window(title="Empty Database", layout=[[]], margins=(100, 50)).read()
    empty = [[sg.Text("Please chill while we perform a quick and complete installation of the data.")],
                 [sg.Button("OK")], [sg.Button("Back Home")], [sg.Button("Close")]]


    # Create the window
    window = sg.Window("Empty Database", empty)

    while True:
        event, values = window.read()
        if event == "OK":
            imports.fullmonty()

        if event == "Back Home":
            home()

        elif event == "Close" or event == sg.WIN_CLOSED:
            break

    window.close()

def existingdata():
    sg.Window(title="Existing Data", layout=[[]], margins=(100, 50)).read()
    existing = [[sg.Text("Please choose one from the following types of information you would like to import.")],
                [sg.Button("Members")], [sg.Button("Codes")], [sg.Button("Admissions")],
                [sg.Button("Run Reports")], [sg.Button("Close")]]


    # Create the window
    window = sg.Window("Add Data", existing)

    while True:
        event, values = window.read()
        if event == "Members":
            members.members()

        elif event == "Codes":
            codes.codes()

        elif event == "Admissions":
            admissions.admissions()

        elif event == "Run reports":
            runreports()

        elif event == "Back Home":
            home()

        elif event == "Close" or event == sg.WIN_CLOSED:
            break

    window.close()


def runreports():
    sg.Window(title="Run Reports", layout=[[]], margins=(100, 50)).read()
    choosereport = [[sg.Text("Which report would you like to run?")],
                    [sg.Button("Top Highest Costing Members")], [sg.Button("Admissions Cost and Count")],
                    [sg.Button("Readmissions")], [sg.Button("10 Longest Admissions")], [sg.Button("All")],
                    [sg.Button("Back Home")], [sg.Button("Close")]]


    # Create the window
    window = sg.Window("Run Reports", choosereport)

    while True:
        event, values = window.read()
        if event == "Top Highest Costing Members":
            results.costmembers()

        elif event == "Admissions Cost and Count":
            results.admcostcount()

        elif event == "Readmissions":
            results.readmissions()

        elif event == "10 Longest Admissions":
            results.admlongest()

        elif event == "All":
            results.fullmonty()

        elif event == "Back Home":
            home()

        elif event == "Close" or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == '__administer__':
    main()