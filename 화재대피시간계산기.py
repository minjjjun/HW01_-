def calculate_evacuation_time(total_population, total_exits):
    try:
        if total_exits == 0:
            return "Error: Total exits should not be zero."
        else:
            return total_population / total_exits
    except ZeroDivisionError:
        return "Error: Total exits should not be zero."

def main():
    while True:
        print("\nSafety Engineering Calculator - Evacuation Time Calculator")
        print("1. Calculate Minimum Evacuation Time")
        print("2. Exit")
        choice = input("Select an option (1/2): ")

        if choice == '1':
            try:
                total_population = int(input("Enter total population in the building: "))
                total_exits = int(input("Enter total number of exits: "))

                evacuation_time = calculate_evacuation_time(total_population, total_exits)
                if isinstance(evacuation_time, str):
                    print(evacuation_time)
                else:
                    print(f"Minimum Evacuation Time: {evacuation_time} minutes")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '2':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
