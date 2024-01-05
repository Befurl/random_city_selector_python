import pyinputplus, csv, random
# Cities are taken from https://simplemaps.com/data/world-cities


# Chooses a random city from the csv and then removes that city from the csv file
def choose_city():

    # Counts the number of rows in the csv
    # This is used to determine the number of cities remaining
    # It is used to randomly choose a city
    line_num = 0
    with open("worldcities_edited.csv", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            line_num += 1

    # Uses a random number function to select a random row
    line = random.randint(0,line_num-1)

    # The rows aside from the chosen city are saved here
    # This is used to then save them back to the csv without the chosen city
    rows = []

    # Finding and printing the chosen city
    with open("worldcities_edited.csv", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            # Printing the city if the line numbers match
            if reader.line_num == line:
                print("Today's city is " + row[0] + ".")
            # Saving the row to the list of rows if it is not the chosen city
            else:
                rows.append(row)

    # Writing the rows back into the file
    with open("worldcities_edited.csv", "w", encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(rows)


# Adds all cities back into the file
def reload_cities():
    # Grabbing the cities from the original file
    with open("worldcities.csv", encoding='UTF-8') as file:
        contents = file.read()

    # Copying them back into the file used for editing
    with open("worldcities_edited.csv", "w", encoding='UTF-8') as file:
        file.write(contents)


def main():
    # User input
    res = pyinputplus.inputMenu(['Choose next city', 'Reload cities'], numbered=True)
    if res == 'Choose next city':
        choose_city()
    else:
        reload_cities()


if __name__ == '__main__':
    main()
