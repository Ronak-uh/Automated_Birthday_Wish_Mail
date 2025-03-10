Personalized Birthday Wish Automation 🎉

This is a Python-based Birthday Wish Automation Project that automatically sends personalized birthday emails to your contacts. It reads the contact details (Name, Email, Birthday) from a CSV file, checks if anyone’s birthday matches today’s date (excluding the year), and sends a customized birthday email with a random birthday wish.

The project also includes a Tkinter GUI (Graphical User Interface) that allows you to:
✅ Add New Contacts
✅ Display Contact List
✅ Send Birthday Wishes Automatically
✅ Go Back to Main Menu

🚀 Features

✅ 1. Automatic Birthday Emails
	•	The script automatically checks if anyone’s birthday matches today’s date (ignoring the year).
	•	If a match is found, a personalized email is sent using SMTP (Gmail).
	•	It uses random birthday wishes from a predefined list, making the emails feel personal.

✅ 2. Contact Management with CSV File
	•	The project uses a CSV file (contacts.csv) to store contact details like:
	•	Name
	•	Email
	•	Birthday (in YYYY-MM-DD format)
	•	You can add new contacts directly from the GUI, and the contact will be saved in the CSV file.

✅ 3. Random Birthday Wishes
	•	The project contains multiple birthday wish templates.
	•	Every time a birthday email is sent, it randomly selects a wish and sends it.
	•	This ensures that emails do not feel repetitive.

✅ 4. Dark Golden Theme GUI
	•	The project comes with a modern, dark-golden-themed GUI built using Tkinter.
	•	The interface includes:
	•	Main Menu with options to Add Contact or Display Data.
	•	Add Contact Window with input fields for Name, Email, and Birthday.
	•	Display Data Window showing all contacts in a tabular format.

💌 How the Email Works

The project uses Gmail SMTP Server to send emails. You need to:
	1.	Enable Less Secure Apps Access in your Gmail account.
	2.	Provide your Email and Password in the config.py file.
	3.	The script will automatically log in and send emails to the contacts.

📅 How the Birthday Date Works
	•	The script only checks Month and Day (MM-DD) from the Birthday field.
	•	This allows it to send birthday emails every year without changing the year in the CSV.
	•	Example: If the birthday is 2001-03-06, it will send an email on March 6th every year.

💻 Folder Structure

📂 Birthday Wish Automation

├── 📄 main.py         # Main Python script with GUI and email functionality

├── 📄 config.py       # Contains your email and password for SMTP

├── 📄 contacts.csv    # Stores contact information

├── 📄 README.md       # Project documentation

🔧 How to Run the Project

✅ Step 1: Clone the repository

git clone https://github.com/Ronak-uh/Birthday-Wish-Automation.git
cd Birthday-Wish-Automation

✅ Step 2: Install required libraries

pip install tkinter

✅ Step 3: Create a Config File (config.py)

You need to create a file named config.py in the root folder.
This file will contain your email and password for the SMTP server.

Inside the config.py file, add the following code:

EMAIL = "your-email@gmail.com"
PASSWORD = "your-password"

💡 Note:
	•	If you have 2-factor authentication (2FA) enabled, you need to create an App Password in Gmail.
	•	If you don’t have 2FA, you can enable Less Secure Apps Access from your Gmail settings.

✅ Step 4: Create a Contact File (contacts.csv)
	•	Inside the project folder, you need to create a CSV file named contacts.csv.
	•	The file should contain the following headers:

Name,Email,Birthday

	•	Example Data:

John Doe,johndoe@gmail.com,2000-03-06
Alice Smith,alicesmith@gmail.com,1999-12-15

	•	You can also add contacts from the GUI, but initially, you must have a CSV file.

✅ Step 5: Run the Script

Run the Python file using:

python main.py

The GUI will open, and you can:
	•	✅ Add new contacts.
	•	✅ Display existing contacts.
	•	✅ Automatically send birthday emails.

✅ Step 6: Test the Email (Optional)

If you want to test the email functionality without waiting for a birthday, simply uncomment this line in main.py:

# email_send("your-email@gmail.com", "Test", "This is a test email.")

Then run the script, and you should receive a test email.

📂 config.py (for Email Credentials)

If you haven’t created the config.py file yet, create it now and paste the following code:

EMAIL = "your-email@gmail.com"
PASSWORD = "your-password"

💡 Note: If you have 2-factor authentication (2FA) enabled, you will need to generate an App Password from your Gmail settings.

✅ How to Test the Email

If you want to test if the email works without waiting for a birthday, simply uncomment this line in main.py:

email_send("your-email@gmail.com", "Test", "This is a test email.")

Then run the script, and you should receive a test email.

🎁 Future Improvements
	•	✅ Add Email Scheduling with Cron Jobs
	•	✅ Add Email Custom Templates
	•	✅ Implement Notification System
	•	✅ Connect with Google Calendar API

💬 Contributing

Feel free to fork this repository, make changes, and create pull requests. Contributions are always welcome! 🚀

📜 License

This project is licensed under the MIT License.

💖 Show Some Support

If you liked the project or found it helpful, feel free to ⭐ star the repository or follow me for more projects like this. 🎂🎉

💌 Made by Ronak Chavhan.
