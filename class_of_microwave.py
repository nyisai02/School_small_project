#I learning about class
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.is_on: bool = False  # Changed variable name to avoid conflict

    def turn_on(self) -> None:
        if self.is_on:
            print(f"Microwave({self.brand}) is already on")
        else:
            self.is_on = True
            print(f"Microwave({self.brand}) is now on.")  # Corrected print statement

    def turn_off(self) -> None:
        if self.is_on:
            self.is_on = False
            print(f"Microwave({self.brand}) is now off.")  # Corrected print statement
        else:
            print(f"Microwave({self.brand}) is already off")

    def run(self, seconds: int) -> None:
        if self.is_on:
            print(f"Microwave({self.brand}) is running for {seconds} seconds.")
        else:
            print(f"A mystical force whispers: 'Turn on your microwave first'.")  # Added space

# Corrected object initialization
smeg = Microwave(brand="Smeg", power_rating="A")
smeg.turn_on()
smeg.run(5)
smeg.turn_off()
  # Calling turn_on method again for testing

