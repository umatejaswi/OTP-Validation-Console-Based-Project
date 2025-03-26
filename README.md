# OTP-Validation-Console-Based-Project
Here's a `README.md` file description for your GitHub repository:

---

# OTP Validation Console-Based Project

## Overview
This is a **Console-Based OTP Validation Application** written in Python. The program generates a random 4-digit OTP and sends it via email for verification. The user is then prompted to enter the received OTP, and the system validates it.

## Features
- Generates a **random 4-digit OTP**.
- Sends OTP via **SMTP (email)**.
- Accepts user input to verify the OTP.
- Displays **success** or **failure** messages based on validation.

## Requirements
- Python 3.x
- `smtplib` for sending emails
- `email.mime` for formatting email messages

## Setup Instructions
1. Install Python (if not already installed).
2. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/your-repository.git
   ```
3. Navigate to the project directory:
   ```sh
   cd your-repository
   ```
4. Run the script:
   ```sh
   python OTP-Validation-Console-Based-Project.py
   ```

## Configuration
- Update the sender's email and **SMTP credentials** in the script.
- Add recipient emails to the `n` list.

## Security Note
⚠️ **Do not hardcode credentials (like email passwords) in your script.** Instead, use environment variables or a configuration file.

