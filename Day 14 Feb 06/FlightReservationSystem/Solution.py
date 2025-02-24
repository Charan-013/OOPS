class Flight:
    def __init__(self,flightNumber,origin,destination,seatAvailable):
        self.flightNumber = flightNumber 
        self.origin = origin
        self.destination = destination
        self.seatAvailable = seatAvailable

    def reserveSeat(self):
        if self.seatAvailable > 1:
            self.seatAvailable -= 1
            return True
        return False
    
class Reservation:
    def __init__(self,revervationID,flightNumber,passengerName):
        self.revervationID = revervationID 
        self.flightNumber = flightNumber
        self.passengerName = passengerName

    def getReservationDetails(self):
        return f"{self.flightNumber} | {self.passengerName}"

class ReservationManager:
    def __init__(self,flights,reservations):
        self.flights = flights
        self.reservations = reservations

    def makeReservation(self, flightNumber, passengerName):
        flight = None
        for f in self.flights:
            if f.flightNumber == flightNumber:
                flight = f
                break
        
        if flight and flight.reserveSeat():
            reservationID = len(self.reservations) + 1
            reservation = Reservation(reservationID, flightNumber, passengerName)
            self.reservations.append(reservation)
            return reservation
        return None

    def cancelReservation(self, reservationID):
        reservation = None
        for r in self.reservations:
            if r.reservationID == reservationID:
                reservation = r
                break
        
        if reservation:
            for f in self.flights:
                if f.flightNumber == reservation.flightNumber:
                    f.seatAvailable += 1
                    break
            self.reservations.remove(reservation)
            return True
        return False
        



def main():
    # Create a flight with limited seats
    flight = Flight("FL123", "New York", "London", 2)
    # Reserve seats until flight is full
    print("Seat reservation 1:", flight.reserveSeat())
    print("Seat reservation 2:", flight.reserveSeat())
    print("Seat reservation 3 (should fail):", flight.reserveSeat())
    # Create reservations
    reservation1 = Reservation(1, flight.flightNumber, "John Smith")
    reservation2 = Reservation(2, flight.flightNumber, "Jane Doe")
    # Create ReservationManager and add the flight
    rm = ReservationManager([flight], [])
    rm.makeReservation(flight.flightNumber, "John Smith")
    rm.makeReservation(flight.flightNumber, "Jane Doe")
    # Display and cancel reservation
    print("Reservation details for ID 1:", reservation1.getReservationDetails())
    cancelled = rm.cancelReservation(1)
    print("Reservation 1 cancelled:", cancelled)
if __name__ == '__main__':
    main()