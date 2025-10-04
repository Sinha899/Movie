movies = {
    "Avengers Doomsday": {"availableseats": 50, "ticketprice": 25, "rows": 5, "cols": 10, "bookedseats": set()},
    "Avengers Secret Wars": {"availableseats": 40, "ticketprice": 15, "rows": 5, "cols": 8, "bookedseats": set()},
    "Zelda Movie": {"availableseats": 30, "ticketprice": 20, "rows": 5, "cols": 6, "bookedseats": set()},
    "Now You See me 3": {"availableseats": 45, "ticketprice": 19, "rows": 5, "cols": 9, "bookedseats": set()},
    "Mario Movie": {"availableseats": 35, "ticketprice": 15, "rows": 5, "cols": 7, "bookedseats": set()}
}

def display_movies():
    print("\n" + "="*50)
    print("Available Movies")
    print("="*50)
    for index, (movie, details) in enumerate(movies.items(), start=1):
        print(f"{index}. {movie}")
        print(f"   Available seats: {details['availableseats']} | Price: ${details['ticketprice']}")
    print("="*50)

def book_tickets(moviechoice, numtickets):
    moviename = list(movies.keys())[moviechoice - 1]
    availableseats = movies[moviename]["availableseats"]
    ticketprice = movies[moviename]["ticketprice"]
    rows = movies[moviename]["rows"]
    cols = movies[moviename]["cols"]
   
    if availableseats < numtickets:
        print(f"Sorry, only {availableseats} seats available.")
        return 0, 0, moviename, rows, cols
   
    movies[moviename]["availableseats"] -= numtickets
    return numtickets, numtickets * ticketprice, moviename, rows, cols

def display_seats_pattern(rows, cols, bookedseats):
    print("\n" + " " * 10 + "SCREEN")
    print(" " * 10 + "="*cols*2)
    print("\n   ", end="")
    for j in range(cols):
        print(f"{j+1:2}", end="")
    print()
   
    for i in range(rows):
        print(f"{i+1:2} ", end="")
        for j in range(cols):
            if (i, j) in bookedseats:
                print("X ", end="")
            else:
                print("_ ", end="")
        print()
    print()

totalbill = 0

while True:
    display_movies()
    choice = int(input("\nEnter the number of the movie you want to watch (0 to exit): "))
   
    if choice == 0:
        break
   
    if choice not in range(1, len(movies) + 1):
        print("Invalid choice. Please enter a valid movie number.")
        continue
   
    numtickets = int(input("Enter the number of tickets you want to book: "))
   
    if numtickets <= 0:
        print("Please book at least 1 ticket.")
        continue
   
    booked, cost, moviename, rows, cols = book_tickets(choice, numtickets)
   
    if booked == 0:
        continue
   
    totalbill += cost
    bookedseats = movies[moviename]["bookedseats"]
   
    print(f"\nYou've booked {booked} ticket(s) for {moviename}.")
    print(f"Cost: ${cost} | Your total bill so far: ${totalbill}\n")
   
    # Book seats for all tickets
    seats_to_book = booked
    while seats_to_book > 0:
        display_seats_pattern(rows, cols, bookedseats)
        print(f"Seats remaining to select: {seats_to_book}")
       
        try:
            row = int(input(f"Enter row number (1-{rows}): "))
            col = int(input(f"Enter column number (1-{cols}): "))
           
            # Validate input range
            if row < 1 or row > rows or col < 1 or col > cols:
                print(f"Invalid seat! Row must be 1-{rows}, Column must be 1-{cols}")
                continue
           
            # Check if seat is already booked
            if (row - 1, col - 1) in bookedseats:
                print("Sorry, this seat is already booked. Please choose another seat.")
                continue
           
            # Book the seat
            bookedseats.add((row - 1, col - 1))
            seats_to_book -= 1
            print(f"✓ Seat ({row}, {col}) booked successfully!\n")
           
        except ValueError:
            print("Please enter valid numbers.")
            continue

print(f"\n{'='*50}")
print(f"Thank you for booking! Your total bill is ${totalbill}")
print(f"{'='*50}")
print("Enjoy your movie! 🎬")