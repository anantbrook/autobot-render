"""
main.py — Entry point for the Auto Channel Bot (Render-ready)
"""
import asyncio
import logging
import sys
import os

# ── Render: log to stdout only (no file — use Render's log panel) ─────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("main")


def validate_config():
    from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID
    errors = []
    if not TELEGRAM_BOT_TOKEN:
        errors.append("❌ TELEGRAM_BOT_TOKEN env var not set")
    if not TELEGRAM_CHANNEL_ID:
        errors.append("❌ TELEGRAM_CHANNEL_ID env var not set")
    if errors:
        print("\n" + "="*55)
        print("  MISSING ENV VARIABLES — Set them in Render Dashboard")
        print("  Service → Environment → Add Environment Variable")
        print("="*55)
        for e in errors:
            print(f"  {e}")
        print()
        sys.exit(1)
    print("✅ Config validated")


async def main():
    validate_config()

    print("""
╔══════════════════════════════════════════════════════╗
║        AUTO CHANNEL BOT — Starting Up               ║
║  Deals • Free Courses • Jobs • Affiliate Income     ║
╚══════════════════════════════════════════════════════╝
    """)

    # Ensure /data directory exists (Render persistent disk)
    from config import DB_PATH
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    from database.db import init_db
    init_db()

    from publisher.telegram_publisher import send_welcome_message
    await send_welcome_message()

    from scheduler.tasks import run_initial_scrape, setup_schedule, scheduler
    await run_initial_scrape()

    from publisher.telegram_publisher import publish_queued_posts
    logger.info("📨 Sending first posts...")
    await publish_queued_posts("deals", limit=1)
    await asyncio.sleep(3)
    await publish_queued_posts("courses", limit=1)
    await asyncio.sleep(3)
    await publish_queued_posts("jobs", limit=1)

    setup_schedule()
    scheduler.start()

    logger.info("🤖 Bot is LIVE on Render! Scheduler running...")
    for job in scheduler.get_jobs()[:6]:
        logger.info(f"   📅 {job.id} → {job.next_run_time}")

    try:
        while True:
            await asyncio.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        logger.info("🛑 Shutting down...")
        scheduler.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
