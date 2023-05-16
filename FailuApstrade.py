# Failu atvēršana, nolasīšana

with open("Fails.txt") as file:
    # persons = file.readlines() #readlines izveido masīvu kur kats elements ir līnija

    # words = []

    # for person in persons:
    #     words += person.split(" ")

    # print(persons)
    # for i in range(len(persons)):
    #     persons[i] = persons[i].replace("\n", "")

    
    # print(persons)

    # persons.sort(reverse=True)

    # print(persons)

    with open("new.txt", "w") as file: #w
        file.write("sis ir jauns fails")
