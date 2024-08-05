import csv

def grade(mark):
    return "A" if 100 >= mark >= 70 else "B" if mark >= 60 else "C" if mark >= 50 \
        else "D" if mark >= 40 else "E" if mark >= 0 else "Mark out of range"

file = open("marks.csv")
marks = []
csvFile = csv.reader(open("marks.csv"))

marks = [line[1][1:] for line in enumerate(csvFile)][1:]
marks = [[int(x)for x in year] for year in marks]

# marks = [[int(x[0])for x in line[1][1:]] for line in enumerate(csvFile)][1:5]

print("\nTranscript \n" )
for year in range(1, len(marks)):
    print(f"YEAR{year} ")
    for unit in range(len(marks[year])):
        print(f"unit{unit + 1} -> " , marks[year][unit], f" = {grade(marks[year][unit])}")
    print()

    su = sum(marks[year]) ; avg = su/3 ; grad = grade(avg)

    print(f"sum = {su} " , f"avg = {avg :.2f} ",grad if su > 0 else "", "Graduate" if year == 4 and grad != "E" and grad != "Mark out of range" else \
          "pass \n" if grad != "E" and grad != "Mark out of range" else "Fail\n")
file.close()