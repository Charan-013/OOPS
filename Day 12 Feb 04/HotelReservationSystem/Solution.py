class Reservation:
    def __init__(self, name, roomNo):
        self.name = name
        self.roomNo = roomNo

    def setRoom(self, newRoomNo):
        self.roomNo = newRoomNo

    def setName(self, newName):
        self.name = newName

    def getRoom(self):
        return self.roomNo

    def getName(self):
        return self.name


class Hotel:
    def __init__(self):
        self.rooms = []

    def Hotel(self, numRooms):
        self.rooms = []

    def buildRooms(self, num):
        for i in range(1, num + 1):
            self.rooms.append([])

    def reserveRoom1(self, person):
        if any(self.rooms[i] == [] for i in range(len(self.rooms))):
            for i in range(len(self.rooms)):
                if self.rooms[i] == []:
                    self.rooms[i] = Reservation(person, i + 1)
                    print(f"{person} reserved Room {i+1}")
                    break
        elif all(self.rooms[i] != [] for i in range(len(self.rooms))):
            print(f"Hotel is full. No room available for {person}")
        # print(self.rooms)

    def reserveRoom(self, person, roomNum):
        if self.rooms[roomNum - 1] == []:
            self.rooms[roomNum - 1] = Reservation(person, roomNum)
            print(f"{person} reserved Room {roomNum}")
        else:
            return -1

    def cancelReservation(self, person):
        for i in range(len(self.rooms)):
            if self.rooms[i] != [] and self.rooms[i].getName() == person:
                self.rooms[i] = []
                print(f"Cancelled reservations for {person}")
                break
        

    def printReservations(self):
        print("Current Reservations:")
        count = 0
        for i in range(len(self.rooms)):
            if self.rooms[i] != []:
                print(f"{self.rooms[i].getName()} - Room {i + 1}")
                count += 1
        print(f"Total Reservations: {count}")
        count = 0
        for i in range(len(self.rooms)):
            if self.rooms[i] == []:
                count += 1
        print(f"Available Rooms: {count}")

        


def Hotel_Reservation_System():
    hotel = Hotel()

    init_room = int(input())
    hotel.buildRooms(init_room)
    while True:
        try:
            inp = input().strip()
            if not inp:
                break

            inp = inp.split(" ")
            # print(inp)
            if inp[0] == "reserve" and len(inp) == 2:
                hotel.reserveRoom1(inp[1])
                # print(inp[1])
            elif inp[0] == "cancel" and len(inp) == 2:
                hotel.cancelReservation(inp[1])
            elif inp[0] == "build" and len(inp) == 2:
                hotel.buildRooms(int(inp[1]))
                print(f"Added {int(inp[1])} more rooms.")

            elif inp[0] == "reserve" and len(inp) == 3:
                inp[2] = int(inp[2])
                hotel.reserveRoom(inp[1], inp[2])
            elif inp[0] == "print":
                hotel.printReservations()

        except EOFError:
            break


if __name__ == "__main__":
    Hotel_Reservation_System()
