from driver_manager import DriverManager
from qualifying import run_qualifying
from race_simulator import run_race
from championship import Championship
from race_history import RaceHistory

def main():
    print("=" * 78)
    print("                 F1 RACE SIMULATOR V2 - VITyarthi")
    print("=" * 78)
    manager = DriverManager()
    championship = Championship()
    history = RaceHistory()
    grid = None

    while True:
        print("\n1. View drivers")
        print("2. Run qualifying (Q1/Q2/Q3)")
        print("3. Run full race")
        print("4. Driver championship")
        print("5. Constructor championship")
        print("6. Race history")
        print("7. Add driver")
        print("8. Update driver")
        print("9. Delete driver")
        print("10. Reset championship")
        print("11. Exit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            manager.display_drivers()
        elif choice == "2":
            grid = run_qualifying(manager.get_drivers())
        elif choice == "3":
            if grid is None:
                print("Run qualifying first.")
            else:
                result = run_race(grid)
                championship.update(result)
                history.save(result)
        elif choice == "4":
            championship.show_driver_standings()
        elif choice == "5":
            championship.show_constructor_standings()
        elif choice == "6":
            history.show()
        elif choice == "7":
            manager.add_driver()
        elif choice == "8":
            manager.update_driver()
        elif choice == "9":
            manager.delete_driver()
        elif choice == "10":
            championship.reset()
            print("Championship reset.")
        elif choice == "11":
            print("🏁 Thanks for using F1 Race Simulator V2!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
