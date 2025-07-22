## Entropheus

Entropheus is a CLI-based advanced password strength analyzer and custom wordlist generator designed for real-time usage in cybersecurity testing, auditing, and training environments.

It combines zxcvbn scoring, entropy calculations, pattern detection, and intelligent wordlist generation — all wrapped in a stylish terminal interface.

## Features

- CLI interface inspired by tools like Zphisher
- Password strength analysis using:
  - zxcvbn scoring system
  - Entropy-based bit strength
- Feedback engine that detects weak patterns (e.g., "1234", "qwerty", no special characters)
- Auto wordlist generation using user input (name, date of birth, pet name, etc.)
- Leetspeak and combination logic
- Exported wordlist in .txt format usable with tools like Hydra or JohnTheRipper
- Session logging with timestamped crack estimates

## Technologies Used

- Python 3.10+
- [zxcvbn-python](https://github.com/dwolfhub/zxcvbn-python)
- `math`, `itertools`, `os`, `rich` for CLI styling

## Project Structure

Entropheus/
├── main.py
├── modules/
│ ├── strength_checker.py
│ ├── feedback_engine.py
│ └── wordlist_generator.py
├── wordlists/
│ └── generated.txt
├── results/
│ └── session_log.txt
├── screenshots/
└── README.md


## How to Run

1. Clone this project or copy the Entropheus folder.
2. Install the dependencies:

bash
pip install zxcvbn-python rich

Run the tool:
    python3 main.py

Usage
Option 1: Analyze a password

  Input a password to check its strength score, entropy, and estimated crack time

  Receive warnings and improvement suggestions

  Results are logged in results/session_log.txt

Option 2: Generate a custom wordlist

  Enter your name, DOB, pet name

  Tool will automatically generate 1000–5000 wordlist entries with mutations

  Output saved as wordlists/generated.txt

Output Examples

  results/session_log.txt contains:

  P@ssw0rd123 | Score: 3 | Entropy: 58.9 | Crack: 1 day

  wordlists/generated.txt contains:

  @ruN2024
  2003T1g3r
  BrUn0@123
  ArunTiger2025

Author

Made as part of a real-time internship project.

License

This project is intended for educational and ethical use only.


---
