#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import connection
import main


def codes(user, password):
    conn = connection.connect(user, password)
    # I am assuming here that when new data is brought into this table, it will be an entire set,
    # so I am first deleting the data from the table.
    cursor = conn.cursor()
    cursor.execute('TRUNCATE TABLE codes')
    conn.commit()

    # Codes csv.
    # First we use Pandas to bring in the data.
    codata = pd.read_csv('../codes.csv', header=0, sep=',')
    codataframe = pd.DataFrame(data=codata)

    # Now we move through each row, and import the data into the table.
    for row in codataframe.values:
        if not isinstance(row[0], int):
            pass
        else:
            cursor = conn.cursor()
            sql = 'INSERT INTO codes (id, code, cost, code_desc) ' \
                  'VALUES (%s, %s, %s, %s)'

            val = (row[0], row[1], row[2], row[3])

            cursor.execute(sql, val)

    conn.commit()

    main.home()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
