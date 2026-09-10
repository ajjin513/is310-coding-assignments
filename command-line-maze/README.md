# Indie Band Soundstage: A Command Line Maze

**By:** Hong Ju Jin <br><br>
**Group:** A2 on Music & Cultural Data  <br><br>
**Assignment:** IS 310 - Lost & Found in the Cultural Command Line  

---

**Welcome!**
Hi, welcome to my Command Line Maze! 
Your goal is to reach the **Final Stage**, which is the Headliner Stage!

## Useful Command-Line Cheat Sheet & Navigation Keys

To navigate your way from the garage studio all the way to the festival headliner stage, you will need to inspect clues, uncover hidden sounds, and move through the venue directories using only the command line.

### Core Commands

| Command | Action | Example in This Maze |
| :--- | :--- | :--- |
| `pwd` | Check your current venue / studio location | `pwd` |
| `ls` | See what tracks, notes, or doors are in the room | `ls` |
| `ls -a` | Reveal secret riffs and hidden tracks starting with `.` | `ls -a` |
| `cd <dir>` | Step into the next venue or room | `cd underground-club` |
| `cd ..` | Backtrack out of a dead end to the previous room | `cd ..` |
| `cat <file>` | Read demo tapes, setlists, and contracts | `cat demo-tape.txt` |
| `head -n <N> <file>` | Preview the first few lines of a setlist | `head -n 5 setlist.txt` |
| `grep -i "<term>" <file>` | Search for a specific keyword or clue in a note | `grep -i "stage" contract.txt` |

---

### Tips for Navigating the Maze

* **Spotting Hidden Riffs:** Standard `ls` will not show hidden secrets (like `.secret-riff`). Always run `ls -a` when you enter a new room so you don't miss hidden clues!
* **Hit a Dead End?** If a room leads to a `dead-end.txt` or an empty path, don't worry, use `cd ..` to step back one level and check the alternative path.
* **Inspect Every File:** Don't just look at the filenames. Use `cat` to read notes, tapes, and contracts; the text contains directions and hints on where to go next.
* **Terminal Tab Completion:** You don't have to type out long folder names! Type the first few letters (e.g., `cd rec` or `cat dem`) and press `Tab` on your keyboard to auto-complete.

### Note for Windows (PowerShell) Users

Different operating systems handle hidden files differently. Dotfiles (like `.secret-riff`) are hidden by default on Mac/Linux, but not on Windows PowerShell. 

If you are solving this maze on **Windows PowerShell**, please run the following command once you navigate into the unzipped `garage-studio` directory

```powershell
.\hide-dotfiles.ps1
```

**HAVE FUN!**