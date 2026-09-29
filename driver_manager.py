from pathlib import Path

DATA_FILE = Path("data/drivers.txt")

DEFAULT_DRIVERS = [
("Charles Leclerc","Ferrari",82.0),("Lewis Hamilton","Ferrari",82.3),
("Max Verstappen","Red Bull",82.1),("Yuki Tsunoda","Red Bull",83.7),
("Lando Norris","McLaren",82.2),("Oscar Piastri","McLaren",82.5),
("George Russell","Mercedes",82.8),("Kimi Antonelli","Mercedes",83.1),
("Fernando Alonso","Aston Martin",83.3),("Lance Stroll","Aston Martin",84.2),
("Carlos Sainz","Williams",83.4),("Alex Albon","Williams",83.8),
("Pierre Gasly","Alpine",84.0),("Franco Colapinto","Alpine",84.5),
("Esteban Ocon","Haas",84.1),("Oliver Bearman","Haas",84.3),
("Liam Lawson","Racing Bulls",84.4),("Isack Hadjar","Racing Bulls",84.6),
("Nico Hulkenberg","Audi",84.2),("Gabriel Bortoleto","Audi",84.7)
]

class DriverManager:
    def __init__(self):
        self.drivers = [{"name":n,"team":t,"pace":p} for n,t,p in DEFAULT_DRIVERS]
        self.load()

    def load(self):
        if not DATA_FILE.exists():
            self.save()
            return
        loaded = []
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
            parts = line.split("|")
            if len(parts) == 3:
                try:
                    loaded.append({"name":parts[0],"team":parts[1],"pace":float(parts[2])})
                except ValueError:
                    pass
        if loaded:
            self.drivers = loaded

    def save(self):
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("\n".join(
            f"{d['name']}|{d['team']}|{d['pace']}" for d in self.drivers
        ), encoding="utf-8")

    def get_drivers(self):
        return self.drivers

    def display_drivers(self):
        print("\nDRIVER DATABASE")
        print("-" * 70)
        for i,d in enumerate(self.drivers,1):
            print(f"{i:2}. {d['name']:<22} {d['team']:<18} Pace {d['pace']:.1f}")

    def add_driver(self):
        name=input("Driver: ").strip()
        team=input("Team: ").strip()
        try: pace=float(input("Base pace: "))
        except ValueError:
            print("Invalid pace."); return
        if not name or not team or any(d["name"].lower()==name.lower() for d in self.drivers):
            print("Invalid or duplicate driver."); return
        self.drivers.append({"name":name,"team":team,"pace":pace})
        self.save(); print("Driver added.")

    def update_driver(self):
        self.display_drivers()
        name=input("Driver to update: ").strip()
        for d in self.drivers:
            if d["name"].lower()==name.lower():
                team=input(f"Team [{d['team']}]: ").strip()
                pace=input(f"Pace [{d['pace']}]: ").strip()
                if team: d["team"]=team
                if pace:
                    try: d["pace"]=float(pace)
                    except ValueError: print("Invalid pace; old value kept.")
                self.save(); print("Driver updated."); return
        print("Driver not found.")

    def delete_driver(self):
        self.display_drivers()
        name=input("Driver to delete: ").strip()
        for i,d in enumerate(self.drivers):
            if d["name"].lower()==name.lower():
                self.drivers.pop(i); self.save(); print("Driver deleted."); return
        print("Driver not found.")
