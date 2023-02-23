person = "JOSE"
print(f"my name is {person}")

d = {"a": 123, "b": 234}
print(f"my element is {d['a']}")

myList = [0, 1, 2]
print(f"my index value is {myList[0]}")

library = [("Author", "Topic", "Pages"), ("Twain", "Rafting", 101)]
print(f"{library}")

for author, topic, pages in library:
    # putting a minimum width for better formatting
    print(
        f"{author:{10}} {topic:{40}} {pages:->{10}}"
    )  # put a dash '-' in place of whitespace


from datetime import datetime

today = datetime(year=2019, month=2, day=28)
print(f"\n\n{today:%a %d %Y}")  # strf code for datetime format


myfile = open("/Users/vectoredge/Desktop/work/bihari123/nlp-with-spacy/test.txt")

myfile.read()  # there is a cursoe here, which reads the file all the way till the end and then stays at the end. So then you call the read again, you get nothing
myfile.seek(0)  # resetting the cursor
myfile.read()  # now we can read again

myfile.seek(0)
content = myfile.read()

myfile.seek(0)

contentByLines = myfile.readlines()

for line in contentByLines:
    print(line.split()[0])


myfile = open("/Users/vectoredge/Desktop/work/bihari123/nlp-with-spacy/test.txt", "a+")
myfile.write("my brand new text")

myfile.seek(0)

print(f"{myfile.read()}")

myfile.seek(0)

myfile.close()

with open(
    "/Users/vectoredge/Desktop/work/bihari123/nlp-with-spacy/test.txt"
) as myNewFile:
    myNewVariabl = myNewFile.readlines()
    myNewFile.seek(0)
    print(f"{myNewVariabl}")
