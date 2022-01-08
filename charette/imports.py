#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
from datetime import datetime
import connection
import main


def fullmonty(user, password):
    conn = connection.connect(user, password)
    # We are assuming here that when a person runs this complete import, they are starting from scratch.
    # The code assumes that there is an empty database called 'lifespark'.

    # Create the members table.
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE members (member_id int, first_name varchar(100) not null, '
                   'last_name varchar(100) not null, dob date null, gender char(10) null, PRIMARY KEY (member_id))')
    conn.commit()

    # Create the codes table.
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE codes (id int, code varchar(10) not null, cost int(20) not null, '
                   'code_desc varchar(255) null, PRIMARY KEY (id))')
    conn.commit()

    # Create the admissions table.
    # I am creating a primary key called 'record_id'.
    # This facilitates the easy upload of new data into that table in the future.
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE admissions (record_id int AUTO_INCREMENT, id int, member_id int, '
                   'first_name varchar(100), last_name varchar(100), dob date, gender char(10), code varchar(10), '
                   'admission_date datetime, discharge_date datetime, magic varchar(255) null, '
                   'PRIMARY KEY (record_id, member_id))')
    conn.commit()

    # Now we start working with the attached csv files.  The first is members.
    # First we use Pandas to bring in the data.
    mdata = pd.read_csv('../members.csv', header=0, sep=',')
    # Then we create a dataframe.
    mdataframe = pd.DataFrame(data=mdata)

    # Using the dataframe, we want to first work with the DOB column to make sure it is formatted as a date.
    mdataframe["dob"] = pd.to_datetime(mdataframe["dob"], format="%m/%d/%Y")
    mdataframe["dob"] = mdataframe["dob"].dt.strftime("%Y-%m-%d")

    # Now we move through each row, and import the data into the table.
    for row in mdataframe.values:
        if not isinstance(row[0], int):
            pass
        else:

            cursor = conn.cursor()
            sql = 'INSERT INTO members (member_id, first_name, last_name, dob, gender) ' \
                  'VALUES (%s, %s, %s, %s, %s)'

            val = (row[0], row[1], row[2], row[3], row[4])

            cursor.execute(sql, val)

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
            # If the first column is not a numerical value, then move on.
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

                # Might come in handy later
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

    # To make data retrieval a bit easier later on, I am going to create some views:
    # The permember_cost view has all of the members with their total costs.
    cursor = conn.cursor()
    cursor.execute("CREATE VIEW permember_cost AS SELECT DISTINCT a.member_id, SUM(c.cost) AS 'total_cost' "
                   "FROM admissions a, codes c WHERE a.code = c.code GROUP BY a.member_id ORDER BY a.member_id")
    # The peradmission_time view has each admission with length of stay calculations.
    cursor.execute("CREATE VIEW peradmission_time AS SELECT DISTINCT record_id, member_id, admission_date, "
                   "TIME_TO_SEC(TIMEDIFF(discharge_date, admission_date))  AS 'length_stay' FROM admissions;")
    conn.commit()

    main.home()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
