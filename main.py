from generator import generate_report
from datetime import date

input_path = "input.txt"

with open(input_path, "r") as f:
    raw_notes = f.read()

if not raw_notes.strip():
    print("input.txt is empty. Add your notes and try again.")
else:
    week_of = date.today().strftime("%B %d, %Y")
    print(f"\n--- WEEKLY REPORT — Week of {week_of} ---\n")
    generate_report(raw_notes)
