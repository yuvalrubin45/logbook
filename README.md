# logbook

**Live:** [tubular-chaja-14116c.netlify.app](https://tubular-chaja-14116c.netlify.app)

A tiny, self-contained journal app that runs entirely in the browser — single HTML file, no build step, no server, no dependencies.

- Writes entries with timestamps, grouped by day
- Simple `task +` / `task -` lines double as an open-tasks list. Any task can be pushed 12 hours into the future with a "+12h" button, individually or all at once, and stays out of the active list, shown separately as "scheduled", until then.
- Chapter dividers mark sections within a log
- Right-to-left scripts (e.g. Hebrew) are detected automatically per line and aligned/punctuated correctly
- Saves directly to a local file on disk via the File System Access API (Chrome/Edge), so your log lives in a plain text-ish `.html` file you control

## Usage

Open `index.html` in a browser (Chrome or Edge for full file-saving support). Use "create a new log" or "open an existing log" from the file menu to pick where entries are saved, then just type and press enter.

## License

MIT — see [LICENSE](LICENSE).
