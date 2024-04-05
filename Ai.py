import random
import logging

# Setup logging
logging.basicConfig(filename='login_attempts.log', level=logging.INFO)

# Simulate user accounts with weak passwords
user_accounts = {
    "user1": "password1",
    # Add more user accounts here
}

# Simulate login attempts
def simulate_login_attempts(num_attempts):
    for _ in range(num_attempts):
        username = random.choice(list(user_accounts.keys()))
        password = random.choice(["password", "123456", "qwerty", "letmein"])  # Common passwords
        if user_accounts.get(username) == password:
            logging.info(f"Successful login attempt: {username}")
        else:
            logging.warning(f"Failed login attempt: {username}")

# Simulate 100 login attempts
simulate_login_attempts(100
