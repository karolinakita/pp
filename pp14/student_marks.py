# Elektroniczny dziennik z ocenami
# - wprowadzanie ocen
# wyświetlanie ocenwraz z wprowadzoną średnią

# students = {"Tomek": [2,3,4], "Agata": [5,5,5]}
def average(marks):
    return sum(marks)/len(marks)

def get_data():
    students = {}
    while True:
        student = input("Enter student name: ")
        if student == "":
            break
        mark = float(input("Enter mark: "))
        if mark <2 or mark >5:
            break
        if student in students:
            marks = students[student]
            marks.append(mark)
        else:
            marks = [mark]
        students.update({student: marks})
    return students

def print_summary(students):
    counter = 1
    for student in sorted(students.keys()):
        marks = students[student]
        print(counter, student, "oceny: ", marks, "średnia: ", average(marks))
        counter += 1

print_summary(get_data())