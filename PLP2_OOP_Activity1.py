class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date


    def get_passenger_info(self):
        return f"Name: {self.name} | From: {self.location} To: {self.destination} | Date: {self.date}"


    def get_weight_allowance(self):
        return 20


class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference


    def get_passenger_info(self):
        return f"[Economy] {super().get_passenger_info()} | Seat: {self.seat_preference}"


class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code


    def get_passenger_info(self):
        return f"[Business] {super().get_passenger_info()} | Lounge Pass: {self.lounge_pass_code}"


    def get_weight_allowance(self):
        return 100


class FirstClass(Passenger):
    def __init__(self, name, location, destination, date, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service


    def get_passenger_info(self):
        chauffeur = "Yes" if self.chauffeur_service else "No"
        return f"[First Class] {super().get_passenger_info()} | Suite: {self.suite_number} | Chauffeur: {chauffeur}"


def main():
    print("--- Airline Ticket Booking System ---")
    print("Select Class: [1] Economy, [2] Business, [3] First Class")
    choice = input("Enter choice (1/2/3): ").strip()
    
    if choice not in ['1', '2', '3']:
        print("Error: Invalid menu choice. Exiting.")
        return


    print("\nEnter flight details:")
    name = input("Passenger Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
        
    location = input("Departure Location: ").strip()
    if not location:
        print("Error: Location cannot be empty.")
        return
        
    destination = input("Destination: ").strip()
    if not destination:
        print("Error: Destination cannot be empty.")
        return
        
    date = input("Flight Date (e.g., 2024-12-25): ").strip()
    if not date:
        print("Error: Date cannot be empty.")
        return


    if choice == '1':
        seat = input("Seat Preference (Window/Aisle/Middle): ").strip()
        if not seat:
            print("Error: Seat preference cannot be empty.")
            return
        ticket = Economy(name, location, destination, date, seat)
        
    elif choice == '2':
        lounge = input("Lounge Pass Code: ").strip()
        if not lounge:
            print("Error: Lounge pass code cannot be empty.")
            return
        ticket = Business(name, location, destination, date, lounge)
        
    elif choice == '3':
        suite = input("Suite Number: ").strip()
        if not suite:
            print("Error: Suite number cannot be empty.")
            return
        chauffeur_input = input("Chauffeur Service? (yes/no): ").strip().lower()
        chauffeur = True if chauffeur_input in ['yes', 'y'] else False
        ticket = FirstClass(name, location, destination, date, suite, chauffeur)


    print("\n--- TICKET SUMMARY ---")
    print(ticket.get_passenger_info())
    print(f"Weight Allowance: {ticket.get_weight_allowance()} kg")


if __name__ == "__main__":
    main()
