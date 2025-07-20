# main.py
import os
import time
from modules.strength_checker import analyze_password
from modules.feedback_engine import check_patterns
from modules.wordlist_generator import generate_wordlist
from rich.console import Console
from rich.panel import Panel
from rich import print

console = Console()

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Panel.fit("[bold cyan]Entropheus[/bold cyan]\n[green]Advanced Password Strength Analyzer + Wordlist Generator[/green]", border_style="bright_blue"))

def menu():
    banner()
    print("[1] Analyze a password")
    print("[2] Generate custom wordlist")
    print("[3] Exit")

    choice = input("\n[?] Choose an option: ")
    if choice == '1':
        analyze()
    elif choice == '2':
        generate()
    else:
        print("\n[red]Exiting...[/red]")
        exit()

def analyze():
    banner()
    pw = input("🔑 Enter a password to analyze: ")
    result = analyze_password(pw)
    flags = check_patterns(pw)

    console.rule("[bold yellow]Analysis Report")
    print(f"[bold]Password:[/bold] {pw}")
    print(f"[bold]zxcvbn Score:[/bold] {result['zxcvbn_score']} / 4")
    print(f"[bold]Entropy:[/bold] {result['entropy_bits']} bits")
    print(f"[bold]Crack Time:[/bold] {result['crack_time']}")
    
    if flags:
        print("[red]Warnings:[/red]")
        for f in flags:
            print(" -", f)

    if result['feedback']['warning']:
        print(" - zxcvbn: ", result['feedback']['warning'])

    with open("results/session_log.txt", "a") as log:
        log.write(f"{pw} | Score: {result['zxcvbn_score']} | Entropy: {result['entropy_bits']} | Crack: {result['crack_time']}\n")

    input("\nPress Enter to return to menu...")
    menu()

def generate():
    banner()
    name = input("👤 Name: ")
    dob = input("📅 Date of Birth (YYYY): ")
    pet = input("🐾 Pet Name: ")

    words = generate_wordlist(name, dob, pet)
    with open("wordlists/generated.txt", "w") as f:
        for word in words:
            f.write(word + "\n")

    print(f"\n[green]Wordlist generated! Saved to wordlists/generated.txt ({len(words)} entries)[/green]")
    input("\nPress Enter to return to menu...")
    menu()

if __name__ == "__main__":
    menu()
