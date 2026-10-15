# Music Data Entry CLI
When you run the script, it first shows a table of example songs made with the `Rich` library. It then asks you to enter your own favorite songs:

| Field | Example |
|---|---|
| `title` | Ditto |
| `artist` | NewJeans |
| `platform` | Spotify |
| `genre` | K-pop |

After you enter a song, the script shows your entry and asks whether it is correct.

- If you type `yes`, the song is saved to `music_data.csv`.
- If you type anything else, you re-enter the song.

You can add as many songs as you want. When you finish, the script prints how many songs were saved and the full path to the CSV file.

## Files

| File | Description |
|---|---|
| `cli_data_entry.py` | The data entry script |
| `requirements.txt` | Python packages needed to run the script |
| `music_data.csv` | Sample data produced by the script |
| `README.md` | This file |

## How to install the requirements

You need Python 3.

1. Open a terminal and move into this folder:
   ```bash
   cd python-libraries
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows, use `.venv\Scripts\activate` instead.
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

## How to run it

With the virtual environment active, run:

```bash
python cli_data_entry.py
```

Then follow the prompts in the terminal. Answer each confirmation question with `yes` or `no`.

The data is saved to `music_data.csv` in the folder where you run the script. If the file already exists, new songs are added to the end. The header row is written only once, when the file is first created.