# Automatic Birthday mail sending with Python

Automating routine tasks like sending birthday wishes can indeed streamline our lives, ensuring that we maintain meaningful connections without the risk of oversight or forgetfulness. With a Python script tailored to this purpose, you can effortlessly extend warm greetings to your friends at the stroke of midnight, regardless of your schedule. This sophisticated solution not only showcases your thoughtfulness but also underscores your commitment to nurturing relationships in the digital age. By harnessing the power of automation, you can infuse a touch of elegance into your interactions, leaving a lasting impression on your friends while freeing up valuable time for other pursuits. Embrace the efficiency and convenience of modern technology, and let your Python script become the silent orchestrator of heartfelt birthday wishes, ensuring that no celebration goes unnoticed or unacknowledged.

## The first thing we do is install six libraries: 

- pandas
- datetime
- smtplib
- time
- requests
- win10toast
- Apart from this, Also create an Excel sheet for containing records like this: Name, Email, Contact, Birthday, and Year. (Already file is created)

Install all at once: Write in terminal `pip install -r requirements.txt`

## Approach:


1. **Define Functions for Email and SMS:**
   - Create a function `send_email()` to start a Gmail session, send the email, and quit the session. You will need to get fast2sms account and get API key from it.
   - Implement a function `send_sms()` which verifies the API key and sends SMS using the fast2sms.com service.

2. **Read Data and Check Birthdays:**
   - Read the data from the Excel sheet containing birthday information.
   - Compare today's date with the birthdays in the dataset.

3. **Sending Wishes:**
   - If there is a match between today's date and a birthday in the dataset:
     - Call the `send_email()` function to send birthday wishes via email.
     - Utilize the `send_sms()` function to send birthday wishes via SMS.
     - Add the current year to the Excel sheet to mark that wishes have been sent for this year.

4. **Desktop Notifications:**
   - Use the `ToastNotifier` from the win10toast library to display desktop notifications upon successful sending of email and SMS.
