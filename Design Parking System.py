class ParkingSystem:
    parkingSpace = dict({})
    def __init__(self, big: int, medium: int, small: int):
        self.parkingSpace[1] = big
        self.parkingSpace[2] = medium
        self.parkingSpace[3] = small

    def addCar(self, carType: int) -> bool:
        if self.parkingSpace[carType] == 0:
            return False
        else:
            self.parkingSpace[carType] -= 1
            return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
