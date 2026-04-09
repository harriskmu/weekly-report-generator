# Weekly Report Generator

A Python tool that takes raw notes, bullet points, or messy updates and turns them into 
a clean, formatted weekly status report.

Built this because writing the same report every Friday is a waste of time. 
Now it takes about 30 seconds.

---

## What it does

- Takes raw input (bullet points, notes, numbers — whatever you have)
- Structures it into a professional weekly report format
- Sections include: summary, accomplishments, blockers, and next week's priorities
- Output is clean markdown you can paste anywhere

---

## Setup

1. Clone the repo
2. Install dependencies

```bashpip install -r requirements.txt

3. Add your OpenAI API key to a `.env` fileOPENAI_API_KEY=your_key_here

4. Add your raw notes to `input.txt`

5. Run it

```bashpython main.py

---

## Example input
finished the dashboard redesign
met with ops team about automation rollout
SQL pipeline is still broken, waiting on IT
need to prep Q3 presentation next week
onboarded two new vendors


## Example outputWeekly Status Report — Week of [date]Summary
Strong week overall with key progress on the dashboard and vendor onboarding.
One open blocker with the SQL pipeline pending IT support.Accomplishments

Completed dashboard redesign
Met with ops team to align on automation rollout timeline
Successfully onboarded two new vendors
Blockers

SQL pipeline issue unresolved — awaiting IT response
Next Week

Prepare and finalize Q3 presentation
Follow up with IT on pipeline fix


---

## File structureweekly-report-generator/
├── main.py
├── generator.py
├── input.txt
├── requirements.txt
├── .env.example
└── README.md

---

## Notes

- Works best when your input is honest and specific — garbage in, garbage out
- You can pipe the output to a `.md` file if you want to save it
- Designed for weekly team reporting but works for any recurring update format

---

## Requirements

- Python 3.9+
- OpenAI API key
