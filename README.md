# FileSender
FileSender is a python programming for sending files from a certain directory to a certain database, it's using socket library. I make it because I've implemented it to my raspberry pi for saving sensor data. FileSender contains three programs:

a. sender.py -> Program for sending data, you can edit the address to connect with receiver and filename what you         want to send 

b. receiver.py -> Program for receiving data, you can edit the address to connect with sender.py.

c. database.py -> Program for implementing data from receiver.py to database. You can edit the database address, tables and coloumns name. It runs as monitoring program.

You can adjust these programs based what you want and you can develop these.

For the program can run well, first install some libraries.

1. pandas

2. SQLAlchemy

3. pathlib

4. mmap
