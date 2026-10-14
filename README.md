# Block Schedule

An internal tool for finishing-phase trade schedules. Each trade works through the building one block at a time. The tool works out every trade's start and end date for every block, then prints a calendar for each trade on letter paper.

It's one file, `index.html`. Open it in Chrome, either from the GitHub Pages link or straight from your computer. There's no login and no server.

## What it does

- **Schedule:** every block and every trade, with start and end dates. Click a date to see why it falls where it does, or to shift it.
- **Trade calendars:** one month per page, with the block number on the day the trade starts it. This is the sheet you hand the trade.
- **Lookahead:** which block each trade is in, day by day, one to four weeks at a time.
- **Shifts:** move one trade for one block, later or earlier. Later blocks and every task that follows move with it.
- **Setup:** everything can be changed here: tasks, durations, gaps, what each task follows, number of blocks, workdays, holidays and block labels.
- **Print:** trade calendars, the master schedule and the lookahead, sized for 8.5 × 11 in paper, landscape or portrait. In Chrome's print window, choose "Save as PDF" to make a PDF.

## How dates are worked out

The rules are the same as the 2025 spreadsheet's, applied the same way to every block:

- **End date** = start date + duration, counted in workdays. A duration of 1 ends the next workday.
- A block of a task starts on the **later** of these two dates:
  1. **The task it follows is ready:** that task's end date (or start date) for the same block, plus the gap.
  2. **Its crew is free:** its own end date on the previous block, plus the "next block" gap (normally 1).
- Weekends and the holiday list are skipped.
- Shifts are applied last.

The second rule is the fix over the spreadsheet. In the spreadsheet, blocks 2 and up only waited for the crew, so a fast trade could pass a slow one. With the same inputs, every other date matches the 2025 sheet exactly.

## Where data is kept

Schedules are saved in the browser you use, on that computer only. Nothing is uploaded anywhere.

- To share a schedule with someone, or keep a backup, use **File → Save to file**. That makes a `.schedule.json` file you can put on SharePoint or Teams.
- Anyone can load that file with **File → Open a schedule file**.
- Clearing Chrome's site data deletes the schedules stored in that browser, so save to a file for anything you need to keep.

## Publishing with GitHub Pages

1. Push this repository to GitHub.
2. In the repository, go to **Settings → Pages**.
3. Under "Build and deployment," choose **Deploy from a branch**, then select `main` and `/ (root)`.
4. GitHub gives you a link like `https://<account>.github.io/<repo>/`.

Notes:
- The page tells search engines not to index it.
- A Pages site can be opened by anyone who has the link, even when the repository itself is private. The tool holds no schedule data (that stays in each person's browser and in their saved files), so the link only exposes an empty tool.
- Publishing Pages from a private repository needs a paid GitHub plan.

## Changing the code

The source is in `src/`: `engine.js` holds the date rules, `app.js` the screens and printing, and `styles.css` the styles. After editing, run `python3 build.py` to rebuild `index.html`.
