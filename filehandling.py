#File Handling
"""
It used to manipulate the external files from the Python
"""

#Example 1
file=open("example.txt","r")
print(file)
print(file.read())
file.close()


#Example 2
file=open("example.txt","w")
content="Hello World"
file.write(content)
file.close()

#Example 3
file = open("example.txt", "r+")
content = "Hello World"
file.write(content)

file.seek(0)   # move pointer to beginning
reading = file.read()
print(reading)

file.close()
