from Course_StrefaKursow_Level_II import Person

Person1 = Person("Tim", "Brown", "timms13")
Person1.printPersonInformation()
print("")
Person2 = Person("Joes", "Brown", "dunny48")
Person2.printPersonInformation()
Person3 = Person1
print("")
print(Person1 == Person2)
print(id(Person1), id(Person2))
print("")
print(Person1 == Person3)
print(id(Person1), id(Person3))


