# System Architecture

```text
                    main.py
                       |
       +---------------+----------------+
       |               |                |
   Qualifying      Race Engine      Driver Manager
    Q1/Q2/Q3      Tyres/Pits/DNF        CRUD
       |               |                |
 Starting Grid      Results          drivers.txt
                       |
             +---------+---------+
             |                   |
       Championship        Race History
       Driver/Team         Persistent File
```

### Modules
- `main.py`: menu/controller
- `driver_manager.py`: driver CRUD
- `qualifying.py`: Q1/Q2/Q3
- `race_simulator.py`: race engine
- `championship.py`: driver/team points
- `race_history.py`: persistent results
