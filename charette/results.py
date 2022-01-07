#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
from datetime import datetime
import mysql.connector

# First configure the connection.
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306, #2433
    user='xxx',         # CHANGEME
    password='xxx',     # CHANGEME
    database='lifespark'
)

# 1. As the VP of Population Health, I’d like to be able to see a list of 10 members that have
# had the highest cost of care from admissions.
cursor = conn.cursor()
mem_cost_query = cursor.execute("SELECT DISTINCT pc.member_id, a.first_name, a.last_name, pc.total_cost "
                          "FROM permember_cost pc, admissions a WHERE pc.member_id = a.member_id "
                          "ORDER BY total_cost desc LIMIT 10")
mem_cost = cursor.fetchall()
df_mem_cost = pd.DataFrame(data=mem_cost)
df_mem_cost.columns = ["member_id","first_name", "last_name", "total_cost"]


# 2. As the CFO I would like to be able to see the total count of admissions and total cost
# broken down by week. The week starts on Sunday and ends on Saturday.
cursor = conn.cursor()
adm_cost_count_query = cursor.execute("SELECT distinct YEAR(a.admission_date) as 'year', "
                                "date_format(a.admission_date, '%U') as 'week', "
                                "count(a.member_id) as 'num_admissions', sum(c.cost) as 'total_cost' "
                                "FROM admissions a, codes c WHERE a.code = c.code group by YEAR(a.admission_date), "
                                "date_format(a.admission_date,'%U') order by YEAR(a.admission_date) desc, week")
adm_cost_count = cursor.fetchall()
df_adm_cost_count = pd.DataFrame(data=adm_cost_count)
df_adm_cost_count.columns = ["year", "week", "num_admissions", "cost_admissions"]

# 3. As the VP of Life Management I would like to see a report of members that have had a
# readmission. A readmission is when someone is admitted to the hospital within 30 days
# of their last admission.
cursor = conn.cursor()
readmission_query = cursor.execute("WITH individual_admissions (member_id, admission_date) as "
                                "(SELECT member_id, admission_date FROM admissions) SELECT a.member_id, "
                                "a.first_name, a.last_name, a.admission_date as 'admision_date1', "
                                "ia.admission_date as 'admission_date2', "
                                "(UNIX_TIMESTAMP(ia.admission_date) - UNIX_TIMESTAMP(a.admission_date)) as 'DIFF' "
                                "FROM admissions a, individual_admissions ia WHERE ia.member_id = a.member_id "
                                "AND (UNIX_TIMESTAMP(ia.admission_date) - UNIX_TIMESTAMP(a.admission_date))<2592000 "
                                "AND UNIX_TIMESTAMP(a.admission_date) < UNIX_TIMESTAMP(ia.admission_date) "
                                "order by a.member_id")
readmission = cursor.fetchall()
df_readmission = pd.DataFrame(data=readmission)
df_readmission.columns = ["member_id", "first_name", "last_name", "admission_date1", "admission_date2",
                          "length_between_seconds"]


# 4. As the VP of Life Management I would like to see a report of the top 10 longest
# admissions.
cursor = conn.cursor()
adm_longest_query = cursor.execute('SELECT DISTINCT pc.member_id, a.first_name, a.last_name, pc.total_cost '
                          'FROM permember_cost pc, admissions a WHERE pc.member_id = a.member_id '
                          'ORDER BY total_cost desc LIMIT 10')
adm_longest = cursor.fetchall()
df_adm_longest = pd.DataFrame(data=adm_longest)
df_adm_longest.columns = ["member_id", "first_name", "last_name", "total_cost"]

# 5. As a data engineer I would like to be able to upload a new list of admissions (see admissions.py).

# Export these data into a csv file.
df_mem_cost.to_csv('../1.10_highest_costing_members.csv')
df_adm_cost_count.to_csv('../2.cost_count_admissions_by_week.csv')
df_readmission.to_csv('../3.readmissions.csv')
df_adm_longest.to_csv('../4.longest_admissions.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/