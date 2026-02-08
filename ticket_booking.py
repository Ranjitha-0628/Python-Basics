"""
Simple bus ticket booking simulation.
The bus has 8 seats. Each booking decreases available seats.
When no seats remain the program prints "All seats are booked." and exits.
"""

def main():
    seats = 8
    booking_number = 0

    while seats > 0:
        booking_number += 1
        seats -= 1
        print(f"Booking #{booking_number}: Seat booked. Seats remaining: {seats}")

    print("All seats are booked.")


if __name__ == "__main__":
    main()
