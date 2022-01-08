# Technical Evaluation completed by Ana Willem
## Introduction
1. This repository assumes that you have an empty database setup called 'Lifespark' on a local mysql server.
2. It also assumes the use of Python3.
3. Code is commented out for readability.
4. In connection.py you must set the user/password that need to be configured for the local environment you are working with.  I have commented those areas with the words 'CHANGEME'.
5. To run the files, navigate to the lifespark/charette folder, and type 'python3 main.py', and this should lead you through the different processes.

# Files
The files in the Lifespark repository are the files that I was provided by Lifespark.

The files that do all the magic, are in the lifespark/charette folder.  They are organized into processes:

### main.py
THIS IS THE FILE YOU RUN. 
This is the file that houses the complete GUI for the process of bringing in these files.

### connection.py
This file manages the connections to the database and MUST BE EDITED TO INCLUDE YOUR LOCAL SQL INFORMATION.

### import.py
This is the files that performs all of the imports, and is triggered by selecting certain options in the GUI.
It is important to run this at least once before choosing to run reports, as it adds some database views that will not be added if this is not run.
  
The import.py file takes care of uploading and processing the different csv files into the database.  
It also creates a list of views that will be used later in the 'results.py' file.

This file is complete for all three data sets, but the datasets can also be imported individually using the:
1. members.py
2. codes.py
3. admissions.py

### members.py
This file is only for importing members from the members.csv in to the database.
It truncates the existing table on import, but does not create the table.

### codes.py
This file is only for importing codes from the codes.csv in to the database.
It truncates the existing table on import, but does not create the table.

### members.py
This file is only for importing members from the admissions.csv in to the database.
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
