from pathlib import Path
import json
from rich.console import Console
from rich.table import Table

console = Console()


def show_example_data():
    table = Table(title="Recent Music Artists")
    table.add_column("Artist", style="magenta")
    table.add_column("Song", style="cyan")
    table.add_column("Year", justify="center", style="green")

    table.add_row("Olivia Rodrigo", "vampire", "2023")
    table.add_row("SZA", "Kill Bill", "2022")
    table.add_row("Doja Cat", "Paint The Town Red", "2023")
    table.add_row("Billie Eilish", "What Was I Made For?", "2023")

    console.print("\n[bold cyan]Here is some example music data:[/bold cyan]")
    console.print(table)


def get_song_entry():
    console.print("\n[bold yellow]Enter a recent artist and song:[/bold yellow]")

    artist = input("Artist name: ").strip()
    song = input("Song title: ").strip()
    year = input("Release year: ").strip()

    return {
        "artist": artist,
        "song": song,
        "year": year
    }


def confirm_entry(entry):
    table = Table(title="Confirm Your Entry")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")

    for key, value in entry.items():
        table.add_row(key.title(), value)

    console.print(table)

    while True:
        response = input("Is this correct? (yes/no): ").strip().lower()
        if response in ("yes", "y"):
            return True
        elif response in ("no", "n"):
            return False
        else:
            console.print("[red]Please enter yes or no.[/red]")


def save_to_json(data, filename="recent_songs.json"):
    path = Path(filename).resolve()

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return path


def main():
    show_example_data()

    entries = []

    console.print("\n[bold cyan]Add your favorite recent songs:[/bold cyan]")

    while True:
        entry = get_song_entry()

        if confirm_entry(entry):
            entries.append(entry)
            console.print("[green]Entry saved.[/green]")
        else:
            console.print("[red]Let's try again.[/red]")
            continue

        another = input("Add another song? (yes/no): ").strip().lower()

        if another in ("no", "n"):
            if entries:
                path = save_to_json(entries)
                console.print("\n[bold green]Data saved successfully![/bold green]")
                console.print(f"[bold]File location:[/bold] {path}")
            else:
                console.print("[yellow]No data saved.[/yellow]")
            break


if __name__ == "__main__":
    main()
