output = open("output.txt", "w")
with open('lst14ers.txt') as fers:
    for line in fers:
        output.write("\"" + line.strip() + ", Colorado" + "\", \n")
