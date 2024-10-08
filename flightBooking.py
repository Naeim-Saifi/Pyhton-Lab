class FlightBooking:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = {}  
        self.available_seats = [f"{row}{seat}" for row in range(1, total_seats//6 + 1)
                                for seat in 'ABCDEF']  
        

    def assign_seat(self, passenger_name, seat_number):

        if seat_number in self.available_seats:
            self.booked_seats[seat_number] = passenger_name
            self.available_seats.remove(seat_number)
            print(f"\nSeat {seat_number} assigned to {passenger_name}.")
        else:
            print(f"\nSeat {seat_number} is already booked or does not exist!")



    def display_available_seats(self):

        if self.available_seats: #Check Dict is empty or not
            print("\nAvailable seats:", self.available_seats)
        else:
            print("\nNo seats available.")


    def handle_overbooking(self):
        if len(self.booked_seats) >= self.total_seats:
            print("\nOverbooking detected! All seats are booked.")
            print("\nPlease contact customer service to handle this overbooking.")
        else:
            print("\nSeats are still available. No overbooking detected.")



flight = FlightBooking("AI101", 30) 
flight.display_available_seats()


flight.assign_seat("Naeim Saifi", "1A")
flight.assign_seat("Piyush Sharma", "1B")

flight.display_available_seats()


flight.assign_seat("Jobanjit", "1A")


flight.handle_overbooking()


for i in range(2, 8):
    flight.assign_seat(f"Passenger{i}", f"{i}C")
    

flight.handle_overbooking()
