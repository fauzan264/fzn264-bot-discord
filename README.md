# 🤖 Discord Bot – Simple Command Bot

This is a basic Discord bot built using `discord.py`. It provides a few simple text-based commands to interact with users in a server.

## 📁 File

* `main.py` — The main script to run the bot.

## 🧠 Features

| Command       | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `!ping`       | Responds with `Pong!` to check if the bot is online.        |
| `!landofdawn` | Mentions specific users (currently the user list is empty). |
| `!indonesia`  | Sends a motivational message about Indonesia.               |
| `!pelayan`    | Replies with “Siap, tuan!”                                  |
| `!kata-kata`  | Loads a quote/message from a file using utils.load_file().  |

## ⚙️ Setup

### 1. Create a `.env` file

Add your Discord bot token in `.env`:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 2. Install dependencies

```bash
pip install -U discord.py python-dotenv
```

## ▶️ How to Run

```bash
python main.py
```

If the token is valid, you should see:

```
Bot aktif sebagai <your_bot_name>
```

## 🔧 Notes

* The `landofdawn` command expects you to populate the `users` list with Discord user IDs:

  ```python
  users = ["123456789012345678", "987654321098765432"]
  ```

<!-- * There's a commented-out section in the script to dynamically load commands from a `cmd` folder. You can enable it to modularize your bot commands. -->
