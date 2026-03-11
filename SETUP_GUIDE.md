════════════════════════════════════════════════════════════════
   AUTO CHANNEL BOT — COMPLETE SETUP GUIDE
   Everything you need to do, step by step
════════════════════════════════════════════════════════════════

TOTAL TIME TO SET UP: ~1-2 hours
MONTHLY COST TO RUN: $5–$15/month (can start FREE on your PC)
INCOME POTENTIAL: $100–$8,000+/month (grows with subscribers)

────────────────────────────────────────────────────────────────
BEFORE YOU START — What Platform Does This Run On?
────────────────────────────────────────────────────────────────

This bot runs as a Python program on a SERVER (computer that
stays on 24/7). You have 3 options:

OPTION A — Run on YOUR PC (free, but stops when PC is off)
  → Good for testing only

OPTION B — Run on a VPS/Cloud Server ⭐ RECOMMENDED
  → Hetzner CX11: $3.99/month (best value)
  → DigitalOcean Droplet: $4/month
  → Sign up: https://www.hetzner.com/cloud
  → Sign up: https://www.digitalocean.com
  → Pick Ubuntu 22.04 as the operating system
  → You get a server that runs 24/7 forever

OPTION C — Run for FREE on Railway.app
  → Go to https://railway.app
  → Free tier: 500 hours/month (enough for a bot!)
  → Connect GitHub repo and deploy

════════════════════════════════════════════════════════════════
STEP 1 — CREATE YOUR TELEGRAM CHANNEL AND BOT
════════════════════════════════════════════════════════════════

1a. CREATE YOUR CHANNEL:
    → Open Telegram on your phone
    → Tap the pencil icon → New Channel
    → Give it a name: e.g. "Daily Deals & Free Courses"
    → Set it to PUBLIC
    → Choose a username: e.g. @daily_deals_hub
    → Write it down — you'll need it later

1b. CREATE A BOT:
    → In Telegram, search for: @BotFather
    → Send: /newbot
    → Bot name: e.g. "Daily Deals Poster"
    → Bot username: e.g. @DailyDealsAutoBot
    → BotFather will give you a TOKEN like:
        7512345678:AAFabcXYZ...
    → COPY THIS TOKEN — you need it in config.py

1c. ADD BOT AS ADMIN TO YOUR CHANNEL:
    → Open your channel
    → Tap channel name → Administrators
    → Add Administrator → search for your bot username
    → Enable: "Post Messages" permission
    → Save

1d. GET YOUR CHANNEL ID (if using numeric ID):
    → Forward any message from your channel to @userinfobot
    → It will show the channel ID like: -1001234567890
    → OR just use @your_channel_username directly

────────────────────────────────────────────────────────────────
STEP 2 — SIGN UP FOR AFFILIATE PROGRAMS (EARN MONEY)
────────────────────────────────────────────────────────────────

Sign up for FREE at each of these. It takes 5-15 min each.
After approval, copy your affiliate links into config.py.

  1. AMAZON ASSOCIATES (Most important!)
     URL: https://affiliate-program.amazon.com
     → Create account → Choose "Technology" niche
     → Get your tracking ID (looks like: yourname-20)
     → Your link: https://www.amazon.com/dp/ASIN?tag=yourname-20
     → Commission: 1-10% on everything the person buys

  2. UDEMY AFFILIATE (For free course posts)
     URL: https://www.udemy.com/affiliate
     → Sign up → Get approved (usually instant)
     → Go to Rakuten Advertising → get your link
     → Commission: Up to 45% per course sold

  3. NORDVPN AFFILIATE (Best recurring income)
     URL: https://nordvpn.com/affiliate
     → Sign up → Instant approval
     → Commission: 30-40% recurring monthly!
     → People keep paying → you keep earning

  4. HOSTINGER AFFILIATE (High per-sale)
     URL: https://www.hostinger.com/affiliates
     → Sign up → Get referral link
     → Commission: Up to $150 per sale

  5. CANVA AFFILIATE (Easy to promote)
     URL: https://www.canva.com/affiliates
     → Sign up via Impact.com
     → Commission: $36 per Pro subscriber

  6. CLICKBANK (Digital products, high commission)
     URL: https://www.clickbank.com
     → Sign up free → Browse marketplace
     → Pick products in your niche with 50%+ commission
     → Commission: 50-75% per sale

  AFTER GETTING YOUR LINKS: Open config.py and replace
  the placeholder URLs in AFFILIATE_LINKS with your real ones.

────────────────────────────────────────────────────────────────
STEP 3 — INSTALL THE BOT ON YOUR SERVER/PC
────────────────────────────────────────────────────────────────

If using a VPS (Hetzner/DigitalOcean), SSH into it first:
  ssh root@YOUR_SERVER_IP

Then run these commands ONE BY ONE:

  # Install Python 3.11
  sudo apt update && sudo apt install python3.11 python3-pip git -y

  # Upload the bot files to your server
  # Option A: Copy files via SCP or FileZilla (FTP)
  # Option B: Put files in GitHub, then:
  git clone https://github.com/YOUR_USERNAME/auto-channel-bot.git
  cd auto-channel-bot

  # Install all dependencies
  pip3 install -r requirements.txt

  # That's it! Now configure the bot.

────────────────────────────────────────────────────────────────
STEP 4 — CONFIGURE THE BOT
────────────────────────────────────────────────────────────────

Open config.py in a text editor and fill in:

  TELEGRAM_BOT_TOKEN = "7512345678:AAFabcXYZ..."  ← Your bot token from Step 1b
  TELEGRAM_CHANNEL_ID = "@your_channel_name"       ← Your channel username
  TELEGRAM_CHANNEL_INVITE = "https://t.me/your_channel_name"

  # Paste your affiliate links:
  AFFILIATE_LINKS = {
      "amazon": "https://amzn.to/YOUR_TAG",
      "udemy": "https://...",    ← Your Udemy affiliate link
      "nordvpn": "https://...",  ← Your NordVPN affiliate link
      ...
  }

  SAVE THE FILE.

────────────────────────────────────────────────────────────────
STEP 5 — TEST RUN THE BOT
────────────────────────────────────────────────────────────────

  python3 main.py

  You should see:
  ✅ Config validated
  ✅ Database initialized
  🚀 Running initial scrape...
  ✅ Queued X new deals
  ✅ Queued X new courses
  ✅ Queued X new jobs
  📨 Sending first posts...

  Check your Telegram channel — it should have posts!

  If you see errors, check the TROUBLESHOOTING section below.

────────────────────────────────────────────────────────────────
STEP 6 — RUN BOT 24/7 (KEEP IT ALWAYS ON)
────────────────────────────────────────────────────────────────

On your VPS, use PM2 or screen to keep the bot running forever:

  METHOD A: Using screen (simplest)
    screen -S bot
    python3 main.py
    Press Ctrl+A then D to detach
    → Bot keeps running even if you close the terminal!
    → To check on it: screen -r bot

  METHOD B: Using PM2 (professional, auto-restarts on crash)
    npm install -g pm2
    pm2 start "python3 main.py" --name "channel-bot"
    pm2 startup    ← Makes it start on server reboot
    pm2 save
    → Check logs: pm2 logs channel-bot

  METHOD C: Using Docker (most reliable)
    docker-compose up -d
    → Check logs: docker-compose logs -f bot
    → Restart: docker-compose restart

────────────────────────────────────────────────────────────────
STEP 7 — SET UP AUTO CHANNEL DISTRIBUTION (GROWTH ENGINE)
────────────────────────────────────────────────────────────────

This is how you automatically grow your subscribers:

7a. FIND TELEGRAM GROUPS IN YOUR NICHE:
    → Search Telegram for: "deals", "free courses", "remote jobs"
    → Also search: "tech channel", "student group", "job updates"
    → Find groups with 1,000+ members
    → Note their usernames (e.g. "techdealsgroup")

7b. ADD GROUPS TO config.py:
    TARGET_TELEGRAM_GROUPS = [
        "techdealsgroup",
        "freecourses2024",
        "remotejobshub",
        # Add 20-50 groups for best results
    ]

7c. MANUALLY JOIN THOSE GROUPS with your bot account
    → In Telegram: search for each group → join
    → OR make bot an admin (ask group admins to add your bot)

7d. THE BOT WILL AUTOMATICALLY:
    → Post your channel invite every 72 hours in each group
    → Rotate between different promo messages
    → Skip groups it posted in recently (to avoid spam bans)

7e. ENABLE REDDIT & TWITTER (optional, for more reach):
    → In config.py set DISTRIBUTION["reddit"] = True
    → Follow Reddit API setup: https://www.reddit.com/prefs/apps
    → Add your credentials to config.py

════════════════════════════════════════════════════════════════
STEP 8 — OPTIONAL: ADD AI POST REWRITING (BETTER POSTS)
════════════════════════════════════════════════════════════════

Without AI: bot uses templates (works fine, recommended to start)
With AI: posts sound more natural and engaging (+20-30% more clicks)

  1. Get OpenAI API key: https://platform.openai.com/api-keys
  2. Add to config.py: OPENAI_API_KEY = "sk-..."
  3. The bot will automatically use GPT-4o-mini to rewrite posts
  4. Cost: ~$1-5/month at normal usage

════════════════════════════════════════════════════════════════
STEP 9 — TRACK AFFILIATE CLICKS (OPTIONAL BUT RECOMMENDED)
════════════════════════════════════════════════════════════════

  1. Create a free Bitly account: https://bitly.com
  2. Go to Settings → Developer → API
  3. Create an API token
  4. Add to config.py: BITLY_TOKEN = "your_token"
  5. Now every link in your posts gets shortened & tracked
  6. See click data in your Bitly dashboard

════════════════════════════════════════════════════════════════
MONETIZATION STRATEGY — HOW TO MAKE REAL INCOME
════════════════════════════════════════════════════════════════

Here's exactly how money flows to you:

  1. BOT POSTS A DEAL:
     "Sony headphones $49 (was $99) → [your amazon affiliate link]"
     → User clicks → Buys headphones
     → You earn: $4.90 (10% commission)
     → They buy other items too → You earn on those too!

  2. BOT POSTS FREE COURSE:
     "Get Python bootcamp FREE → [your udemy affiliate link]"
     → User clicks → Enrolls (paid course = $19.99)
     → You earn: $9 (45% commission)
     → These expire quickly = urgency = high conversion!

  3. BOT POSTS JOB WITH FOOTER:
     "...Apply Now → [job link]
     🔧 Boost your resume: Try NordVPN FREE → [affiliate]"
     → User clicks NordVPN → Subscribes ($11.99/mo)
     → You earn: $4.80/month RECURRING (every month they pay!)

  4. PURE AFFILIATE POST (every 4-5 posts):
     "🌐 Start your website for $1.99/mo → [hostinger link]"
     → User clicks → Buys hosting plan
     → You earn: $65-150 flat fee!

  REALISTIC INCOME PROJECTIONS:
  ──────────────────────────────
  500 subscribers:    ~$20-50/month
  2,000 subscribers:  ~$100-300/month
  10,000 subscribers: ~$500-1,500/month
  50,000 subscribers: ~$2,000-8,000/month
  100,000 subscribers: ~$8,000-25,000+/month

  KEY INSIGHT: It's not just about subscriber count.
  It's about ENGAGED subscribers who click links.
  Focus on content quality → high CTR → more income.

════════════════════════════════════════════════════════════════
TROUBLESHOOTING
════════════════════════════════════════════════════════════════

ERROR: "Forbidden" when posting to channel
  FIX: Make sure your bot is an admin in the channel with
       "Post Messages" permission. See Step 1c.

ERROR: "Bad Request: can't parse entities"
  FIX: Post contains special Markdown characters.
       The formatter will handle most cases automatically.

ERROR: No posts being scraped (0 items)
  FIX: Check your internet connection. Some RSS feeds may be
       temporarily down. Check bot.log for specific errors.

ERROR: Import errors when starting
  FIX: Run: pip install -r requirements.txt again

Bot is posting but affiliate links aren't showing
  FIX: Make sure AFFILIATE_LINKS in config.py are filled in
       (not the placeholder values)

Bot posts duplicate content
  FIX: This is handled automatically by the dedup system.
       If it happens, delete bot_data.db and restart.

════════════════════════════════════════════════════════════════
QUICK CHECKLIST BEFORE GOING LIVE
════════════════════════════════════════════════════════════════

  [ ] Created Telegram channel
  [ ] Created Telegram bot via @BotFather
  [ ] Added bot as admin to channel
  [ ] Filled TELEGRAM_BOT_TOKEN in config.py
  [ ] Filled TELEGRAM_CHANNEL_ID in config.py
  [ ] Signed up for at least Amazon + 1 other affiliate program
  [ ] Pasted affiliate links into config.py
  [ ] Ran: pip install -r requirements.txt
  [ ] Tested with: python3 main.py
  [ ] Saw posts appear in your channel ✅
  [ ] Set up server to run 24/7 (Step 6)
  [ ] Added 10+ Telegram groups to TARGET_TELEGRAM_GROUPS

Once all checked = you have a fully automated income machine! 🚀

════════════════════════════════════════════════════════════════
FILES IN THIS PROJECT
════════════════════════════════════════════════════════════════

  config.py                ← ⭐ YOU EDIT THIS — your keys & settings
  main.py                  ← Start the bot: python main.py
  requirements.txt         ← Install deps: pip install -r requirements.txt
  SETUP_GUIDE.md           ← This file

  scrapers/
    deals.py               ← Scrapes deals from Slickdeals, Reddit, etc.
    courses.py             ← Scrapes free Udemy coupons, Coursera, edX
    jobs.py                ← Scrapes RemoteOK, Remotive, WeWorkRemotely

  content/
    formatter.py           ← Turns scraped data into Telegram posts

  affiliate/
    injector.py            ← Injects your affiliate links into posts

  publisher/
    telegram_publisher.py  ← Sends posts to your channel

  distributor/
    auto_distributor.py    ← Promotes channel to groups/Reddit/Twitter

  database/
    db.py                  ← SQLite database (prevents duplicate posts)

  scheduler/
    tasks.py               ← Runs everything on schedule

  docker-compose.yml       ← Run with Docker (optional)
  Dockerfile               ← Docker container config (optional)
