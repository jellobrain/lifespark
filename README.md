# Technical Evaluation completed by Ana Willem
## Introduction
1. This repository assumes that you have an empty database setup called 'lifespark' on a local mysql server.
2. It also assumes the use of Python3.
3. Code is commented out for readability.
4. To run the files, navigate to the lifespark/charette folder, and type 'python3 main.py'.

# Files
The files in the lifespark repository are files that I was provided with by lifespark

The files that do all the magic, are in the lifespark/charette folder.  They are organized into processes:

### main.py
THIS IS THE FIRST AND ONLY FILE YOU SHOULD RUN. It runs a GUI that will take you through all of the other procedures.
  
### imports.py
This is the main import file that takes care of the full import of Views, Tables and Data.

### members.py
This file is only for importing members from the members.csv in to the database.
It truncates the existing table on import, but does not create the table.

### codes.py
This file is only for importing codes from the codes.csv in to the database.
It truncates the existing table on import, but does not create the table.

### admissions.py
This file is only for importing new admissions from the admissions.csv in to the database.
It does not truncate the existing table on import, and is able to take new data from other sources and incorporate it.
This file satisfies item number 5 in the use cases on the assignment.

### results.py
This file queries the tables and views in the database, and it brings in the data requested for items 1-4 on the assignment and places the results in the 'lifespark' folder.  These results are numbered by the assignment use case number.

### scratchpad
This is a text files I used to keep track of SQL queries initially.

### video
I am out of time to do my video, and am happy to still complete that part if you feel it is necessary.  My hope is that with what is here with the code and comments and this README, you will have enough to understand how to make this run.

My hope is that we can go over it all next time we speak.

### Cheers!
