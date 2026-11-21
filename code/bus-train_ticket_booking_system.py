seats = list(range(1, 11))
bookings = {}
fare = 500


def view_seats():
    print("Booked seats:", bookings)
    print("Available seats:", seats)


def book_seat():
    seat = int(input("Enter seat number: "))

    if seat < 1 or seat > 10:
        print("Invalid seat. Choose a seat from 1 to 10.")

    elif seat not in seats:
        print("Seat", seat, "is already booked.")

    else:
        name = input("Enter passenger name: ")
        bookings[seat] = name
        seats.remove(seat)

        print("Seat", seat, "booked for", name)
        print("Fare:", fare)
        print("Seats left:", len(seats))

        if len(seats) == 0:
            print("Bus is now full.")


def view_bookings():
    if len(bookings) == 0:
        print("No bookings found.")

    else:
        for seat, name in bookings.items():
            print("Seat:", seat, "Passenger:", name)


def cancel_booking():
    seat = int(input("Enter seat number to cancel: "))

    if seat in bookings:
        del bookings[seat]
        seats.append(seat)
        seats.sort()

        refund = fare * 80 / 100

        print("Booking for seat", seat, "cancelled.")
        print("Refund:", int(refund))

    else:
        print("No booking found for this seat.")


while True:
    print("\n----- BUS TICKET BOOKING SYSTEM -----")
    print("1. View seats")
    print("2. Book seat")
    print("3. View bookings")
    print("4. Cancel booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_seats()

    elif choice == "2":
        book_seat()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        cancel_booking()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
