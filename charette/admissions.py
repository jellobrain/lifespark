#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 5. As a data engineer I would like to be able to upload a new list of admissions.

import pandas as pd
from datetime import datetime
import connection
import main


def admissions(user, password):
    conn = connection.connect(user, password)
    # I am assuming that we will want to bring this information in peice by peice from different providers
    # so I do not wipe the old table.  But I am leaving it for quick access in special circumstances.
    # cursor = conn.cursor()
    # cursor.execute('TRUNCATE TABLE admissions')
    # conn.commit()

    # Admissions csv.
    # First we use Pandas to bring in the data.
    adata = pd.read_csv('../admissions.csv', header=0, sep=',')
    adataframe = pd.DataFrame(data=adata)

    # Using the dataframe, we want to first work with the dob column to make sure it is formatted as a date.
    adataframe["dob"] = pd.to_datetime(adataframe["dob"], format="%m/%d/%Y")
    adataframe["dob"] = adataframe["dob"].dt.strftime("%Y-%m-%d")

    # Using the dataframe, we want to first work with the admission_date column to make sure it is formatted as a date.
    adataframe["admission_date"] = pd.to_datetime(adataframe["admission_date"], format="%m/%d/%Y")
    adataframe["admission_date"] = adataframe["admission_date"].dt.strftime("%Y-%m-%d")

    # We do not need to do this in the same way for the discharge_Date.
    # I am leaving it here for possible use later.
    # adataframe["discharge_date"] = pd.to_datetime(adataframe["discharge_date"], format="%Y/%m/%d %H:%M:%S UTC")
    # adataframe["discharge_date"] = adataframe["discharge_date"].dt.strftime("%Y-%m-%d")

    # Now we move through each row, and import the data into the table.
    for row in adataframe.values:
        # 'magic' is a column I am using to store table column information for fields in the record that were modified
        # on their way in.  So if I have to bring in information that is missing, the column name will appear
        # as a csv in this field.
        magic = ''
        if not isinstance(row[0], int):
            # if the first column is not a numerical value, then move on.
            pass
        else:
            # If admission_date is missing information, we will bring data in from discharge_date.
            if pd.isna(row[7]):
                row[7] = row[8]
                # But we know this information is not accurate entirely, so we make a note of it in the magic table.
                magic = 'admission_date'

            # If discharge_date is already in datetime format, then we can keep going.
            if isinstance(row[8], pd.DatetimeIndex):
                pass
            # But if it is not in that format, we need to modify it from the string form to a date form.
            elif isinstance(row[8], str):
                input_str = row[8]
                # In case some of the discharge_dates come without the hours:minutes:seconds,
                # we process them differently.
                if len(row[8]) > 14:
                    dt_object = datetime.strptime(input_str, '%Y-%m-%d %H:%M:%S UTC')
                    row[8] = dt_object
                else:
                    dt_object = datetime.strptime(input_str, '%Y-%m-%d')
                    row[8] = dt_object
            else:
                print(f'date 8 not string or datetime...? {row[8]}')

            # If admission_date is already in datetime format, then we can keep going.
            if isinstance(row[7], pd.DatetimeIndex):
                pass
            # But if it is not in that format, we need to modify it from the string form to a date form.
            elif isinstance(row[7], str):
                input_str = row[7]
                # In case some of the admission_dates come without the hours:minutes:seconds,
                # we process them differently.
                if len(row[7]) > 14:
                    dt_object = datetime.strptime(input_str, '%Y-%m-%d %H:%M:%S UTC')
                    row[7] = dt_object
                else:
                    dt_object = datetime.strptime(input_str, '%Y-%m-%d')
                    row[7] = dt_object

                # Might need this later.
                # short_str = input_str[0:10]
                # dt_object = datetime.strptime(short_str, '%Y-%m-%d')
                # row[7] = dt_object.strftime("%Y-%m-%d")

            else:
                print(f'date 7 not string or datetime...? {row[7]}')
            # If dob comes in empty on this csv, that information should already be in the member's table,
            # so let's go get it and assign that value to this object.
            if pd.isna(row[4]):
                cursor = conn.cursor()
                sql = 'SELECT dob FROM members WHERE first_name = %s and last_name = %s'
                val = (row[2], row[3])
                cursor.execute(sql, val)
                rqdob = cursor.fetchall()
                rdob = rqdob[0][0]

                # If there is now value in the dob object, let's tell the magic column that you brought it in.
                if not pd.isna(rdob):
                    row[4] = rdob
                    if magic == '':
                        magic = 'dob'
                    else:
                        magic = magic + ', dob'
                else:
                    print('There is no DOB in members.')

            # Now that all the data is ready, we can import it into SQL.
            cursor = conn.cursor()
            sql = 'INSERT INTO admissions (id, member_id, first_name, last_name, dob, gender, code, admission_date, ' \
                  'discharge_date, magic) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], magic)

            cursor.execute(sql, val)

    conn.commit()
    main.home()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
