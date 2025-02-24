class Car:
    def __init__(self,licensePlate,model,parkingTime):
        self.licensePlate = licensePlate
        self.model = model
        self.parkingTime= parkingTime
    
    def getLicensePlate(self):
        return self.licensePlate

    def getModel(self):
        return self.model
    
class ParkingLot:
    def __init__(self,lst):
        self.parkedCars = lst

    def parkCar(self,Car):
        self.parkedCars.append(Car)

    def removeCar(self,licensePlate):
        for ele in self.parkedCars[:]:
            if ele.licensePlate == licensePlate:
                del ele
                return True
        return False
    
    def displayCars(self):
        return self.parkedCars


def main():
    # Create car objects
    car1 = Car("ABC123", "Toyota Camry", "10:00 AM")
    car2 = Car("XYZ789", "Honda Accord", "10:15 AM")

    car3 = Car("LMN456", "Ford Focus", "10:30 AM")
    lot = ParkingLot([])
    # Test parking multiple cars
    lot.parkCar(car1)
    lot.parkCar(car2)
    lot.parkCar(car3)
    if len(lot.displayCars()) != 3:
        print("Error: Not all cars parked.")
    # Validate each car's license plate and model
    print("Parked cars:")
    for c in lot.displayCars():
        print(f"{c.getLicensePlate()} - {c.getModel()}")
    # Test removing an existing car
    removed = lot.removeCar("ABC123")
    print("Car ABC123 removed:", removed)
    # Attempt to remove non-existent car
    removed_nonexistent = lot.removeCar("ZZZ999")
    print("Non-existent car removal:", removed_nonexistent)
    # Final state of parked cars
    print("Remaining cars:")
    for c in lot.displayCars():
        print(c.getLicensePlate())
if __name__ == '__main__':
    main()