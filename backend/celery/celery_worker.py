# backend/celery_worker.py
from app import app
from backend.celery.celery_factory import celery_init_app
from celery.schedules import crontab

# Import the tasks that will be scheduled
from backend.celery.tasks import send_daily_reminders, send_monthly_reports, send_admin_daily_summary
# Create the Celery app instance using the factory
celery_app = celery_init_app(app)

# --- DEFINE THE SCHEDULE DIRECTLY HERE ---
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Sets up the periodic tasks for the Celery beat scheduler.
    """
    # --- Daily Reminder Job ---
    # Executes daily at 7:00 PM (19:00).
    sender.add_periodic_task(
        crontab(hour=19, minute=0),
        send_daily_reminders.s(),
        name='send daily parking reminders'
    )
    sender.add_periodic_task(
        crontab(hour=20, minute=0), # 8:00 PM
        send_admin_daily_summary.s(),
        name='send daily admin summary'
    )

    # --- Monthly Activity Report Job ---
    # Executes at 8:00 AM on the first day of every month.
    sender.add_periodic_task(
        crontab(day_of_month=1, hour=8, minute=0),
        send_monthly_reports.s(),
        name='send monthly activity reports'
    )