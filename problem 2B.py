NH1 = open("test.txt", "w")
NH1.write("This is a test for Problem 3 of Programming Assignment 4")


def iswordinfile(fileName, word):
    wordfound = False
    NH1 = open(fileName, "r")
    J=0
    for line in NH1:
        J+=1
        if word in line:
            wordfound = True
            break
    NH1.close()
    print(wordfound)


iswordinfile("test.txt", "is")
print(j)

