# Discord CTF BOT

This is a Discord bot that fetches and displays CTF (Capture The Flag) events from the CTFtime API. The bot allows users to query CTF events based on a specified date range and displays the results in a formatted table.

## Features

- Fetch and display CTF events from the CTFtime API.
- Command to query CTF events within a specified date range.

## Features

1. **Python 3.x**
2. **Dependencies**: Install the required Python packages listed in `requirements.txt`.

## Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. **Create a Virtual Environment (optional but recommended):**

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Replace Token: Replace your discord bot token to the `.env` file.**

```makefile
DISCORD_TOKEN=your_discord_bot_token
```

5. **Run the Bot:**

```bash
python bot.py
```

## Commands

- /ctf: Fetches and displays CTF events within the specified data range. Usage:

```css
/ctf [start_date] [end_date]
```

- - `start_date` and `end_date` should be in the format DD-MM-YYYY. If no dates are provided, it defaults to the current date and one month from the current date.

## Example

To fetch CTF events from September 1,2024, to October 1, 2024:

```bash
/ctf 01-09-2024 01-10-2024
```
