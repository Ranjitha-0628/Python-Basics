#While Loops

i = 1
while i <= 10:
    print(i)
    i += 1

#Odd numbers from 1 to 20
i = 1
while i <= 20:
    if i%2 != 0:
        print(i, end=' ')
        i += 1
   
#Bus ticket Booking Simulation 

seats = 8
booking_number = 0
while seats > 0:
    booking_number += 1
    seats -= 1
    print(f"Booking #{booking_number}: Seat booked. Seats remaining: {seats}")

print("All seats are booked.")

i = 10
while i > 0:
    print(i)
    i -= 1
print("Happyyyy new year!!!")