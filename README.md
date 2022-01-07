# Technical Evaluation completed by Ana Willem
## Introduction
1. This repository assumes that you have an empty database setup called 'lifespark' on a local mysql server.
2. It also assumes the use of Python3.
3. Code is commented out for readability.
4. Each of the python files listed below has a connection section of code with specific information about user/password that need to be configured first for the local environment you are working with.  I have commented those areas with the words 'CHANGEME'.
5. To run the files, navigate to the lifespark/charette folder, and type 'python3 <filename>'.

## Next Steps
One thing I though might be helpful is giving an idea of what I would do if there were more time to clean things up.

1. Right now although they are written using python, they aren't set up in a way that capitalized on the objects and classes being thrown around here.  If I were to refactor, the first thing that I would do is to model the code in OOP.  I think it would shorten it, and it would also make it possible to make number 2 happen.

2. The next thing I would do is to create an admin/main landing page from which a person could execute the things needed but through more of a guided user interface that steers you through a process of selecting options instead of running files from the terminal.  

# Files
The files in the lifespark repository are files that I was provided with by lifespark

The files that do all the magic, are in the lifespark/charette folder.  They are organized into processes:

### import.py
THIS IS THE FIRST FILE YOU SHOULD RUN. It adds some database views that will not be added if this is not run.
  
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
