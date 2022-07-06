from student import Student
from Node import Node


def main():
    maksym = Student("Maksym", "Pelyshko", "11", 2003 , 82)
    olya = Student("Olya", "Rybenchuk", "12", 2004, 45)
    danylo = Student("Danylo", "Kovalchuk","13" , 2002, 50)
    sofia = Student("Sofia", "Rokun", "14", 2004, 87)

    root = Node(Student("Bohdan","Drahan", "14", 2003, 72))
    root.insert(maksym)
    root.insert(olya)
    root.insert(danylo)
    root.insert(sofia)
    root.print()
    print("==========================", "delete the students of the 14th group:")

    root.delete_by_group("14")
    root.print()
    print("==========================", "withdrawal of students with a rating above 47")
    root.print_by_rating(47)

if __name__ == "__main__":
    main()








