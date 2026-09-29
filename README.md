# 🏎️ F1 RACE SIMULATOR V2

## VITyarthi Academic Project

A modular Python Formula 1 simulator with qualifying, race strategy, tyres, pit stops, weather, Safety Car, DNFs, fastest lap and championship standings.

### Features
- 20-driver grid
- Q1, Q2 and Q3 qualifying
- Charles Leclerc guaranteed pole for the project demonstration
- 20-lap race simulation
- Soft, Medium and Hard tyres
- Automatic pit stops and tyre degradation
- Light rain events
- Safety Car events
- Mechanical DNF events
- F1-style points
- Fastest-lap bonus
- Driver championship
- Constructor championship
- Persistent race history
- Driver CRUD operations
- File and JSON persistence

### Structure
```text
F1-RACE-SIMULATOR-V2-VITYARTHI/
├── main.py
├── driver_manager.py
├── qualifying.py
├── race_simulator.py
├── championship.py
├── race_history.py
├── README.md
├── statement.md
├── requirements.txt
├── data/
└── docs/
```

### Run
```bash
python main.py
```

No third-party packages are required.

### Points
1st 25 | 2nd 18 | 3rd 15 | 4th 12 | 5th 10 | 6th 8 | 7th 6 | 8th 4 | 9th 2 | 10th 1

### Educational Concepts
Functions, modules, classes, lists, dictionaries, sorting, loops, conditions, randomisation, CRUD, file handling, JSON, exception handling and persistence.

### Limitations
This is an educational simulator, not an official F1 physics/timing model. Pace values and event probabilities are simplified.

### Future Scope
70-lap races, circuit layouts, sector timing, fuel strategy, DRS/overtakes, VSC, red flags, penalties, GUI, live timing API and a full multi-race season.
