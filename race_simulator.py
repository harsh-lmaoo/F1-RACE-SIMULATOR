import random

LAPS=20
POINTS={1:25,2:18,3:15,4:12,5:10,6:8,7:6,8:4,9:2,10:1}
TYRES={"Soft":(-0.32,7),"Medium":(0,10),"Hard":(0.22,14)}

def run_race(grid):
    print("\n"+"="*78+"\nGRAND PRIX RACE\n"+"="*78)
    weather=random.choice(["Dry","Dry","Dry","Light Rain"])
    print(f"Weather: {weather} | Laps: {LAPS}")

    state={}
    for d in grid:
        state[d["name"]]={
            "driver":d,"total":0.0,"tyre":random.choice(["Soft","Medium","Hard"]),
            "age":0,"stops":0,"dnf":False,"pits":[],"fastest":False
        }

    safety=set(random.sample(range(4,LAPS),2)) if random.random()<.60 else set()
    rain=set(random.sample(range(8,LAPS),3)) if weather=="Light Rain" else set()
    if safety: print("⚠️ Safety Car:",sorted(safety))
    if rain: print("🌧️ Rain:",sorted(rain))

    fastest=(999,None)
    for lap in range(1,LAPS+1):
        for s in state.values():
            if s["dnf"]: continue
            d=s["driver"]; modifier,life=TYRES[s["tyre"]]
            s["age"]+=1
            degradation=max(0,s["age"]-life)*.08
            rain_penalty=random.uniform(.8,1.5) if lap in rain and s["tyre"]!="Intermediate" else 0
            safety_factor=.55 if lap in safety else 1
            current=(d["pace"]+modifier+degradation+random.uniform(-.22,.35)+rain_penalty)*safety_factor
            s["total"]+=current
            if current<fastest[0]: fastest=(current,d["name"])

            if s["age"]>=life and s["stops"]<2:
                s["stops"]+=1; s["pits"].append(lap); s["total"]+=20
                choices=["Soft","Medium","Hard"]
                choices.remove(s["tyre"])
                s["tyre"]=random.choice(choices); s["age"]=0

            if random.random()<.004: s["dnf"]=True

    finishers=sorted([s for s in state.values() if not s["dnf"]],key=lambda x:x["total"])
    dnfs=[s for s in state.values() if s["dnf"]]
    result=[]

    for pos,s in enumerate(finishers,1):
        fastest_flag=s["driver"]["name"]==fastest[1]
        pts=POINTS.get(pos,0)+(1 if fastest_flag and pos<=10 else 0)
        result.append({"position":pos,"name":s["driver"]["name"],"team":s["driver"]["team"],
            "grid":s["driver"]["grid"],"points":pts,"stops":s["stops"],
            "tyre":s["tyre"],"fastest_lap":fastest_flag,"dnf":False})

    for s in dnfs:
        result.append({"position":len(result)+1,"name":s["driver"]["name"],
            "team":s["driver"]["team"],"grid":s["driver"]["grid"],"points":0,
            "stops":s["stops"],"tyre":s["tyre"],"fastest_lap":False,"dnf":True})

    print("\nFINAL CLASSIFICATION")
    print("-"*95)
    for r in result:
        status="DNF" if r["dnf"] else ("FASTEST LAP" if r["fastest_lap"] else "FINISHED")
        print(f"P{r['position']:2} {r['name']:<22} {r['team']:<18} Grid {r['grid']:2} "
              f"Stops {r['stops']} Pts {r['points']:2} {status}")
    print(f"\n🏆 WINNER: {result[0]['name']}")
    print(f"⚡ FASTEST LAP: {fastest[1]} ({fastest[0]:.3f})")
    return result
