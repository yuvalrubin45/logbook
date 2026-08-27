# logbook

**Live:** [tubular-chaja-14116c.netlify.app](https://tubular-chaja-14116c.netlify.app)

A tiny, self-contained journal app that runs entirely in the browser — no build step, no server, no account.

- Writes entries with timestamps, grouped by day
- Simple `task +` / `task -` lines double as an open-tasks list, with a "tomorrow" button to push a task (or all open tasks at once) a day out — it stays out of the active list, shown separately as "scheduled", until then
- Recurring tasks fire automatically on a weekday schedule you pick
- Chapter dividers mark sections within a log, and are collapsible — tap one to hide everything until the next chapter
- Right-to-left scripts (e.g. Hebrew) are detected automatically per line and aligned/punctuated correctly
- Every entry is saved on-device (IndexedDB) as you type, on any browser or platform — no file needs to be linked for the app to work
- On Chrome/Edge on desktop, you can additionally link a real file on disk (via the File System Access API) that mirrors everything you write, and import a previously-exported `.txt` log to merge it back in
- Works as an installable app (Add to Home Screen) with its own icon

## Usage

Open `index.html` in any modern browser and start typing — everything is saved locally right away. Open the file menu if you also want to mirror your log to a real file on disk (Chrome/Edge desktop) or share/export a copy.

## License

MIT — see [LICENSE](LICENSE).
