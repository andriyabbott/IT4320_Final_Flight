def emptySeats(row, column):

    emptyFlight = [["O" for c in range(column)] for r in range(row)]
    return emptyFlight

def initialSeats(flight):

    try:
        file  = open("reservations.txt")
        for data in file:
            reserved = data.split(",")
            row = int(reserved[1].strip())
            column = int(reserved[2].strip())
            flight[row][column] = "X"
            file.close()
    except:
        print("ERROR loading reservation system")

    return flight

def print_flightChart(flight):
    print("\nPrinting Seating Chart...")

    for row in flight:
        print(row)
    print()
    return