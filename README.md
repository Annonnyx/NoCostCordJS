# NoCostCord

A Discord bot framework built on python allowing you to host your own bot for 0$... without billing information!

Tired of spending hours searching for a free VPS, setting up a database, and keeping your bot alive? NoCostCord bundles everything together — hosting, persistent storage, and 24/7 uptime — all using free services. A Discord bot framework built on python, with a clean Cog-based architecture. Just clone, configure, and deploy.

>! This framework is specifically coded for the services allowing you to deploy your bot for free therefore using it with different hosting services wont work !

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Cost](https://img.shields.io/badge/Cost-Free-brightgreen)
![Type](https://img.shields.io/badge/Type-Framework-orange)
![Stars](https://img.shields.io/github/stars/ateronCS2/NoCostCord?style=social)
<p align="center">
  <img src="https://github.com/user-attachments/assets/a612011b-7b2a-46fe-9859-b2f669fc5632" width="600">
</p>
---

## 📦 Stack

| Service | Purpose | Cost |
|---|---|---|
| [Render](https://render.com) | Hosting | Free |
| [UptimeRobot](https://uptimerobot.com) | Keep-alive pinging | Free |
| [Supabase](https://supabase.com) | Persistent database | Free |
| [Discord.py](https://discordpy.readthedocs.io) | Bot framework | Free |

---

## 📁 File Structure

```
NoCostCord/
├── main.py           # Bot entry point
├── server.py         # Flask keep-alive server
├── requirements.txt  # Python dependencies
├── render.yaml       # Render deployment configuration
├── cogs/
│   ├── __init__.py
│   └── example.py    # Example cog
├── utils/
│   └── database.py   # Supabase integration
└── cfg/
```

---

## ⚙️ Prerequisites

- Python 3.10+
- A [Discord bot token](https://discord.com/developers/applications)
- A [Render](https://render.com) account
- A [Supabase](https://supabase.com) account *(optional, only if you need persistent storage)*
- A [UptimeRobot](https://uptimerobot.com) account

---

## 🚀 Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/NoCostCord.git
cd NoCostCord
```

### 2. Create your own repository

**Option A — Fork (recommended):**
Click the **Fork** button on the GitHub repository page to create your own copy instantly.

**Option B — Clone and push to a new repo:**
1. Create a new repository on GitHub
2. Clone NoCostCord locally:
```bash
git clone https://github.com/ateronCS2/NoCostCord.git
cd NoCostCord
```
3. Point it to your new repo:
```bash
git remote set-url origin https://github.com/yourusername/your-repo-name.git
git push -u origin main
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables to run locally
Create and add to `cfg/.env`:
```
DISCORD_TOKEN=your_bot_token_here
SUPABASE_URL=your_supabase_url_here      # optional
SUPABASE_KEY=your_supabase_key_here      # optional
```

### 5. Run locally, for testing
```bash
python main.py
```

---

## 🧩 Adding Cogs

Create a new file in the `cogs/` folder:

```python
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Loaded: MyCog')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

Then load it in `main.py`:
```python
await bot.load_extension('cogs.my_cog')
```

---

## ☁️ Deploying on Render

1. Push your code to GitHub
2. Go to [Render](https://render.com) and create a **Web Service**
3. Connect your GitHub repository — build and start commands are automatically configured via `render.yaml`. If Render still asks for them manually, use:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
4. Add your environment variables under **Environment**
5. Click **Deploy**
   
## ⏰ Keeping Your Bot Alive

Render's free tier spins down after inactivity. To prevent this:

1. Go to [UptimeRobot](https://uptimerobot.com) and create a free account
2. Add a new **HTTP(s)** monitor
3. Set the URL to your Render service URL
4. Set the interval to **5 minutes**

**After that your bot will run 24/7 no upkeep needed, you can enable/disable auto deploy on render and it will automatically deploy the latest commit to your repo**

---

## 🗄️ Using Supabase

Import the database utility in any cog:

```python
from utils.database import get_supabase

# Fetch data
result = get_supabase().table('your_table').select('*').execute()

# Insert data
get_supabase().table('your_table').insert({'key': 'value'}).execute()
```

## 🔧 Troubleshooting

**Bot isn't responding to commands**
- Make sure `intents.message_content` is set to `True` in `main.py`
- Verify your bot has the correct permissions in your Discord server
- Check that your command prefix matches what you set in `main.py`

**Environment variables returning `None`**
- Make sure your `.env` file is in the `cfg/` folder when running locally
- Check that the file was saved with UTF-8 encoding and no BOM — use VS Code or create it via Python rather than Notepad
- On Render, make sure variables are set in the **Environment** tab of your service

**Bot goes offline after a few minutes**
- Make sure UptimeRobot is set up and pinging your Render URL every 5 minutes
- Verify your Render service is a **Web Service** and not a background worker

**Render deployment failing**
- Check that `requirements.txt` includes all your dependencies
- Make sure `render.yaml` is in the root of your repository

**Supabase returning `None` or connection errors**
- Verify `SUPABASE_URL` doesn't include `/rest/v1/` at the end — it should be just `https://your-project.supabase.co`
- Make sure `SUPABASE_KEY` is the `anon public` key, not the `service_role` key

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details. Credit is required when using or distributing this framework.

---

## 🙏 Credits

Created by [ateronCS2](https://github.com/ateronCS2)

(yes this README was partly made by AI, the code wasnt!)
