import csv
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()
console.print("Initial Data here:", style="bold Red")

table = Table(title="Music Data")
table.add_column("Title")
table.add_column("Artist")
table.add_column("Platform")
table.add_column("Genre")
table.add_row("Bailando", "Enrique Iglesias", "youtube music", "Vibe")
table.add_row("Ditto", "NewJeans", "Spotify", "Kpop")
table.add_row("No Me Platiques Mas", "Luis Miguel", "Spotify", "Vibe")
table.add_row("Really like you", "Babymonster", "Melon", "kpop")

console.print(table)
console.print("\nEnter your favorite songs:")

file_path = Path("music_data.csv")
saved_count = 0

more = "yes"
while more == "yes":
    answer = "no"
    while answer != "yes":
        title = input("Enter the song title: ")
        artist = input("Enter the artist: ")
        platform = input("Enter the platform: ")
        genre = input("Enter the genre: ")

        song = {
            "title": title,
            "artist": artist,
            "platform": platform,
            "genre": genre,
        }

        console.print("\nYou entered:")
        console.print(f"  Title: {song['title']}")
        console.print(f"  Artist: {song['artist']}")
        console.print(f"  Platform: {song['platform']}")
        console.print(f"  Genre: {song['genre']}")

        answer = input("Is this your input? yes or no: ")
        if answer != "yes":
            console.print("Try Again.\n")

    is_new_file = not file_path.exists()

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(["title", "artist", "platform", "genre"])
        writer.writerow([song["title"], song["artist"], song["platform"], song["genre"]])

    saved_count = saved_count + 1
    console.print("Saved!")

    more = input("\nDo you want to enter another song? yes or no: ")

console.print(f"\n{saved_count} song is saved.")
console.print(f"File location: {file_path.resolve()}")