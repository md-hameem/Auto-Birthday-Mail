import pandas as pd
import datetime
import smtplib
import time
import requests
from win10toast import ToastNotifier

# Your Gmail credentials here
GMAIL_ID = 'your_email_here'
GMAIL_PWD = 'your_password_here'

# For desktop notifications
toast = ToastNotifier()

# Define a function for sending email
def send_email(to, subject, message):
    # Connection to Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
        smtp_server.starttls()  # Start TLS encryption
        smtp_server.login(GMAIL_ID, GMAIL_PWD)  # Login using credentials
        # Send email
        smtp_server.sendmail(GMAIL_ID, to, f"Subject: {subject}\n\n{message}")
    print(f"Email sent to {to} with subject {subject} and message: {message}")
    toast.show_toast("Email Sent!", f"{to} was sent an email", duration=6)

# Define a function for sending SMS
def send_sms(to, message, name, subject):
    url = "https://www.fast2sms.com/dev/bulk" #Need fast2sms.com API key later
    payload = f"sender_id=FSTSMS&message={message}&language=english&route=p&numbers={to}"
    headers = {
        'authorization': "API_KEY_HERE",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    print(f"SMS sent to {to} with subject: {subject} and message: {message}")
    toast.show_toast("SMS Sent!", f"{name} was sent a message", duration=6)

if __name__ == "__main__":
    # Read the Excel sheet containing all the details
    dataframe = pd.read_excel("excelsheet.xlsx")
    # Today's date in format: DD-MM
    today = datetime.datetime.now().strftime("%d-%m")
    # Current year in format: YY
    year_now = datetime.datetime.now().strftime("%Y")
    # List to store indices of processed rows
    processed_indices = []

    for index, row in dataframe.iterrows():
        birthday = row['Birthday'].strftime("%d-%m")  # Strip the birthday in Excel sheet as: DD-MM
        if today == birthday and year_now not in str(row['Year']):
            message = f"Many Many Happy Returns of the day dear {row['NAME']}"
            # Send email
            send_email(row['Email'], "Happy Birthday", message)
            # Send SMS
            send_sms(row['Contact'], message, row['NAME'], "Happy Birthday")
            processed_indices.append(index)  # Store index for updating 'Year' column

    # Update 'Year' column with the current year for processed rows
    for idx in processed_indices:
        current_years = dataframe.loc[idx, 'Year']
        dataframe.loc[idx, 'Year'] = f"{current_years},{year_now}"

    # Write updated data back to the Excel sheet
    dataframe.to_excel('excelBday.xlsx', index=False)
