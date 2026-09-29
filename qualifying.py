import random

def qualifying_session(drivers, label, eliminate):
    results=sorted(
        [(d["pace"]+random.uniform(-0.18,0.18),d.copy()) for d in drivers],
        key=lambda x:x[0]
    )
    print(f"\n--- {label} ---")
    for i,(time,d) in enumerate(results,1):
        print(f"{i:2}. {d['name']:<22} {time:.3f}s")
    survivors=[d for _,d in results[:-eliminate]] if eliminate else [d for _,d in results]
    if eliminate:
        print("Eliminated:", ", ".join(d["name"] for _,d in results[-eliminate:]))
    return survivors, results

def run_qualifying(drivers):
    print("\n" + "="*70 + "\nQUALIFYING\n" + "="*70)
    q1,_=qualifying_session(drivers,"Q1 - 20 drivers",5)
    q2,_=qualifying_session(q1,"Q2 - 15 drivers",5)
    _,q3=qualifying_session(q2,"Q3 - 10 drivers",0)

    leclerc=next(x for x in q3 if x[1]["name"]=="Charles Leclerc")
    q3.remove(leclerc)
    q3.insert(0,(min(x[0] for x in q3)-0.25,leclerc[1]))

    grid=[]
    for pos,(time,d) in enumerate(q3,1):
        d["grid"]=pos; d["qualifying_time"]=time; grid.append(d)

    remaining=[d for d in q2 if d["name"] not in {x[1]["name"] for x in q3}]
    # Recover Q2 and Q1 eliminations in a deterministic order.
    all_names={d["name"] for d in grid}
    for d in drivers:
        if d["name"] not in all_names:
            copy=d.copy(); copy["grid"]=len(grid)+1
            copy["qualifying_time"]=copy["pace"]+random.uniform(.3,1.3)
            grid.append(copy)

    print("\nFINAL GRID")
    for d in grid:
        print(f"P{d['grid']:2} {d['name']:<22} {d['team']:<18} {d['qualifying_time']:.3f}s")
    print("\n🏎️ CHARLES LECLERC TAKES POLE POSITION! 😎")
    return grid
