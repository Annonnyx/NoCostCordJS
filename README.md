# NoCostCord
A Discord bot framework built on python allowing you to host your own bot for 0$... without billing information!!!. Includes a clean Cog-based architecture, persistent storage via Supabase, and deployment using Render's free web service tier. Just clone, configure, and deploy.

! This framework is specifically coded for the services allowing you to deploy your bot for free !

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Cost](https://img.shields.io/badge/Cost-Free-brightgreen)

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
└── .env          # Local environment variables
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
Fork this repository on GitHub or create a new one and push the cloned files to it. Render requires a GitHub repository to deploy from.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables to run locally
Add to `cfg/.env`:
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

## 🗄️ Using Supabase

Import the database utility in any cog:

```python
from utils.database import get_supabase

# Fetch data
result = get_supabase().table('your_table').select('*').execute()

# Insert data
get_supabase().table('your_table').insert({'key': 'value'}).execute()
```

---

## ☁️ Deploying on Render

1. Push your code to GitHub
2. Go to [Render](https://render.com) and create a **Web Service**
3. Connect your GitHub repository — build and start commands are automatically configured via `render.yaml`
4. Add your environment variables under **Environment**
5. Click **Deploy**
   
## ⏰ Keeping Your Bot Alive

Render's free tier spins down after inactivity. To prevent this:

1. Go to [UptimeRobot](https://uptimerobot.com) and create a free account
2. Add a new **HTTP(s)** monitor
3. Set the URL to your Render service URL
4. Set the interval to **5 minutes**

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details. Credit is required when using or distributing this framework.

---

## 🙏 Credits

Created by [ateronCS2](https://github.com/ateronCS2)

(yes this README was partly made by AI, the code wasnt!)
