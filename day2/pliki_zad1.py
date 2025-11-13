# działania z plikami
# context manager
# with - kontekst manager w pythonie
#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', "w", encoding="utf8") as f:  # filehandler
    f.write("Powitanie\n")
    f.write("Kolejny\n")
    f.write("Jeszcze jedno\n")

# x
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', "x", encoding="utf8") as f:  # filehandler
#     f.write("Powitanie\n")
#     f.write("Kolejny\n")
#     f.write("Jeszcze jedno\n")
with open('test.log', "w", encoding="utf8") as f:  # filehandler
    f.write("Powitanie2\n")
    f.write("Kolejny2\n")
    f.write("Jeszcze jedno2\n")

# a
with open('test.log', "a", encoding="utf8") as f:  # filehandler
    f.write("Powitanie2\n")
    f.write("Kolejny2\n")
    f.write("Jeszcze jedno2\n")
    f.write("Dośdane\n")

# r
with open('test.log', "r", encoding="utf8") as file:
    lines = file.read()

print(lines)
