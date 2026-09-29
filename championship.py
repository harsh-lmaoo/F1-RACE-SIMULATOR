from pathlib import Path
import json

FILE=Path("data/championship.json")

class Championship:
    def __init__(self):
        self.driver_points={}; self.team_points={}; self.load()

    def update(self,result):
        for r in result:
            self.driver_points[r["name"]]=self.driver_points.get(r["name"],0)+r["points"]
            self.team_points[r["team"]]=self.team_points.get(r["team"],0)+r["points"]
        self.save()

    def show_driver_standings(self):
        print("\nDRIVER CHAMPIONSHIP")
        rows=sorted(self.driver_points.items(),key=lambda x:x[1],reverse=True)
        if not rows: print("No races completed."); return
        for i,(n,p) in enumerate(rows,1): print(f"{i:2}. {n:<25} {p:3} pts")

    def show_constructor_standings(self):
        print("\nCONSTRUCTOR CHAMPIONSHIP")
        rows=sorted(self.team_points.items(),key=lambda x:x[1],reverse=True)
        if not rows: print("No races completed."); return
        for i,(n,p) in enumerate(rows,1): print(f"{i:2}. {n:<25} {p:3} pts")

    def save(self):
        FILE.parent.mkdir(parents=True,exist_ok=True)
        FILE.write_text(json.dumps({"drivers":self.driver_points,"teams":self.team_points},indent=2))

    def load(self):
        if FILE.exists():
            try:
                data=json.loads(FILE.read_text())
                self.driver_points=data.get("drivers",{}); self.team_points=data.get("teams",{})
            except json.JSONDecodeError: pass

    def reset(self):
        self.driver_points={}; self.team_points={}
        if FILE.exists(): FILE.unlink()
