def emptySeats(row, column):

    emptyFlight = [["O" for c in range(column)] for r in range(row)]
    return emptyFlight

def initialSeats(flight):

    try:
        file  = open("flask_wtforms_tutorial/reservations.txt")
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
    map=""
    for row in flight:
        map+=str(row)
        map+="\n"
        
    return map

#functions that ensures that a seat isn't already taken, output and write the seat selected to reservations.txt
def reserveCheck(name, column, row):
    
    name = first_name
    className = "INFOTC4320" #remember to change all the class names in reservations.txt to this!
    
    #checking
    reserveFileChange = open("flask_wtforms_tutorial/reservations.txt", "a")
    for data in reserveFileChange:
            reserved = data.split(",")
            row = int(reserved[1].strip())
            column = int(reserved[2].strip())
            flight[row][column] = "X"
    reserveFileChange.close()

    if reserveFileChange[row][column] != "X" or "O":
        print ("test")

    #append and re-generate chart somehow
    else:
        return str("This seat is taken")
    
    #BookingID that gets generated 
   
    bookingID = "".join([name[i] + className[i] for i in range(len(name))]) + className[len(name)]
#https://www.geeksforgeeks.org/python-alternate-strings-concatenation/

#output the seat
    #reserveFileChange.write(name + + ", " + str(column) +", " + bookingID )
        

def reserveAdd(firstName, row, column):
    #testing in progress
    #add bookingID here as well
    file = open('/flask_wtforms_tutorial/reservations.txt', 'a')
    #adding a new reservation


    newReserve = '/n' + firstName + ', ' + row + ', ' + column + ', ' + bookingID

    file.write(newReserve)
    file.close()






    #something that updates the chart here
    #why does it not execute? and return to the reservations page? returns to admin for some reason
