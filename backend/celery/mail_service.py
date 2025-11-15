import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- Configuration for Local SMTP Debugging Server ---
# This setup is for local development. Emails will be printed to the
# console where the SMTP server is running, not sent over the internet.
SMTP_SERVER_HOST = "localhost"
SMTP_SERVER_PORT = 1025
SENDER_EMAIL = 'no-reply@smartpark.com'
SENDER_PASSWORD = '' # Not needed for local debugging server

def send_email(to_address, subject, html_content):
    """
    Sends an email using the configured SMTP server.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['To'] = to_address
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL

        # Attach the HTML content
        msg.attach(MIMEText(html_content, 'html'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT) as client:
            # No login is required for the local debugging server
            client.send_message(msg)
        
        print(f"Email sent successfully to {to_address}")

    except Exception as e:
        print(f"Error sending email to {to_address}: {e}")