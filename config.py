"""
╔══════════════════════════════════════════════════════════╗
║        AUTO CHANNEL BOT — CONFIG (Render Ready)         ║
║  All secrets come from Render Environment Variables.    ║
║  Set them in: Render Dashboard → Service → Environment  ║
╚══════════════════════════════════════════════════════════╝
"""

import os

# ─────────────────────────────────────────────────────────
# 1. TELEGRAM (REQUIRED)
# ─────────────────────────────────────────────────────────
TELEGRAM_BOT_TOKEN      = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID     = os.environ.get("TELEGRAM_CHANNEL_ID", "")
TELEGRAM_CHANNEL_INVITE = os.environ.get("TELEGRAM_CHANNEL_INVITE", "")

# ─────────────────────────────────────────────────────────
# 2. OPENAI (Optional)
# ─────────────────────────────────────────────────────────
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_MODEL   = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

# ─────────────────────────────────────────────────────────
# 3. AFFILIATE LINKS
# Set each as its own env var in Render dashboard
# ─────────────────────────────────────────────────────────
AFFILIATE_LINKS = {
    "amazon":    os.environ.get("AFFILIATE_AMAZON",    "https://amzn.to/YOURTAG"),
    "udemy":     os.environ.get("AFFILIATE_UDEMY",     "https://www.udemy.com/courses/"),
    "coursera":  os.environ.get("AFFILIATE_COURSERA",  "https://www.coursera.org/"),
    "nordvpn":   os.environ.get("AFFILIATE_NORDVPN",   "https://nordvpn.com/"),
    "hostinger": os.environ.get("AFFILIATE_HOSTINGER", "https://www.hostinger.com/"),
    "canva":     os.environ.get("AFFILIATE_CANVA",     "https://www.canva.com/"),
    "clickbank_general": os.environ.get("AFFILIATE_CLICKBANK", "https://clickbank.com/"),
}

AFFILIATE_PROMOS = [
    "🔧 *Sponsored:* Stay private online → [NordVPN 68% OFF]({nordvpn})",
    "⚡ *Start a website for $1.99/mo* → [Hostinger]({hostinger})",
    "🎨 *Design for free* → [Canva Pro FREE Trial]({canva})",
    "📚 *Learn new skills* → [Udemy Courses]({udemy})",
]

# ─────────────────────────────────────────────────────────
# 4. BITLY TRACKING (Optional)
# ─────────────────────────────────────────────────────────
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", "")

# ─────────────────────────────────────────────────────────
# 5. POSTING SCHEDULE (UTC)
# ─────────────────────────────────────────────────────────
POST_SCHEDULE = {
    "deals":     ["08:00", "13:00", "17:00", "21:00"],
    "courses":   ["09:00", "20:00"],
    "jobs":      ["10:00", "15:00", "19:00"],
    "affiliate": ["12:00", "22:00"],
}

# ─────────────────────────────────────────────────────────
# 6. SCRAPER SETTINGS
# ─────────────────────────────────────────────────────────
SCRAPE_INTERVAL_MINUTES = int(os.environ.get("SCRAPE_INTERVAL", "30"))
MAX_POSTS_PER_BATCH     = int(os.environ.get("MAX_POSTS_PER_BATCH", "5"))
MIN_DEAL_DISCOUNT_PCT   = int(os.environ.get("MIN_DISCOUNT_PCT", "0"))

# ─────────────────────────────────────────────────────────
# 7. DISTRIBUTION
# ─────────────────────────────────────────────────────────
DISTRIBUTION = {
    "telegram_groups": os.environ.get("ENABLE_TG_GROUPS", "false").lower() == "true",
    "twitter":         os.environ.get("ENABLE_TWITTER",   "false").lower() == "true",
    "reddit":          os.environ.get("ENABLE_REDDIT",    "false").lower() == "true",
}

TWITTER_API_KEY       = os.environ.get("TWITTER_API_KEY", "")
TWITTER_API_SECRET    = os.environ.get("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN  = os.environ.get("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET", "")

REDDIT_CLIENT_ID  = os.environ.get("REDDIT_CLIENT_ID", "")
REDDIT_SECRET     = os.environ.get("REDDIT_CLIENT_SECRET", "")
REDDIT_USERNAME   = os.environ.get("REDDIT_USERNAME", "")
REDDIT_PASSWORD   = os.environ.get("REDDIT_PASSWORD", "")
REDDIT_USER_AGENT = "AutoChannelBot/1.0"

REDDIT_TARGETS = {
    "deals":   ["deals", "frugal", "coupons"],
    "courses": ["learnprogramming", "learnpython", "datascience"],
    "jobs":    ["forhire", "remotework", "cscareerquestions"],
}

# ─────────────────────────────────────────────────────────
# 8. TELEGRAM GROUPS TO PROMOTE IN
# In Render env: TG_TARGET_GROUPS = "group1,group2,group3"
# ─────────────────────────────────────────────────────────
_raw_groups = os.environ.get("TG_TARGET_GROUPS", "")
TARGET_TELEGRAM_GROUPS     = [g.strip() for g in _raw_groups.split(",") if g.strip()]
GROUP_PROMO_INTERVAL_HOURS = int(os.environ.get("GROUP_PROMO_HOURS", "72"))

GROUP_PROMO_MESSAGES = [
    "💰 Daily deals, free courses & job alerts here: {invite}",
    "🔥 Free daily deals + job listings 👉 {invite}",
    "🎓 Free courses & remote jobs posted daily → {invite}",
]

# ─────────────────────────────────────────────────────────
# 9. DATABASE PATH — Render Persistent Disk mounts at /data
# ─────────────────────────────────────────────────────────
DB_PATH = os.environ.get("DB_PATH", "/data/bot_data.db")
if not os.path.exists("/data"):
    DB_PATH = os.path.join(os.path.dirname(__file__), "bot_data.db")

# ─────────────────────────────────────────────────────────
# 10. CHANNEL IDENTITY
# ─────────────────────────────────────────────────────────
CHANNEL_NICHE    = os.environ.get("CHANNEL_NICHE", "tech deals, free online courses, and remote job opportunities")
CHANNEL_LANGUAGE = "English"
CHANNEL_HASHTAGS = {
    "deals":   ["#deals", "#sale", "#discount", "#offer", "#save"],
    "courses": ["#freecourse", "#learnfree", "#onlinelearning", "#education"],
    "jobs":    ["#hiring", "#remotejobs", "#jobalert", "#careers"],
}
