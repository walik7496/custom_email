# Email Sender Application

## Installation

1. **Install Python 3.x**: Download Python from the official website.

2. **Install the required Python libraries**:

    ```bash
    pip install tkinter
    ```

## Usage

1. **Run** the `email_sender.py` script.

2. In the GUI, fill out the following fields:
    - **Email**: Your email address.
    - **Password**: Your email account password.
    - **To**: The recipient's email address.
    - **Subject**: The subject of your email.
    - **Body**: The content of your email.

3. Click **"Send"** to send the email. If there are any errors, a notification will appear at the bottom of the window.

4. If you need to clear all fields, click the **"Reset"** button.

## Code Explanation

- **Tkinter GUI**: Provides a simple form to fill in the email details.
- **SMTP**: Sends the email using Python's built-in `smtplib` library.
- **Error Handling**: Displays notifications if fields are missing or if there's an issue sending the email.

## Troubleshooting

- **Missing Fields**: Ensure all fields (Email, Password, To, Subject, Body) are filled before sending the email.
- **SMTP Server**: The script uses Gmail's SMTP server (`SMTP.gmail.com`) and port 587. Ensure your email provider supports SMTP and check if the account requires an app-specific password.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

If you have any questions or need further assistance, feel free to open an issue or reach out directly to the repository owner.
