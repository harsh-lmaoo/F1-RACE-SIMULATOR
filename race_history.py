from pathlib import Path
from datetime import datetime
FILE=Path("data/race_history.txt")

class RaceHistory:
    def save(self,result):
        FILE.parent.mkdir(parents=True,exist_ok=True)
        winner=result[0]
        fastest=next((r for r in result if r["fastest_lap"]),None)
        dnfs=[r["name"] for r in result if r["dnf"]]
        with FILE.open("a",encoding="utf-8") as f:
            f.write("="*70+"\n")
            f.write(f"DATE: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            f.write(f"WINNER: {winner['name']} ({winner['team']})\n")
            f.write(f"FASTEST LAP: {fastest['name'] if fastest else 'N/A'}\n")
            f.write(f"DNF: {', '.join(dnfs) if dnfs else 'None'}\n")

    def show(self):
        print("\nRACE HISTORY")
        if not FILE.exists() or not FILE.read_text().strip():
            print("No completed races yet."); return
        print(FILE.read_text())
