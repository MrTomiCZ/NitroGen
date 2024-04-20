import requests
import string
import random
import time

print ("===================================================================================")
print ("                                Made by kubalinh3")
print ("  Official Discord: http://nitrogen.xf.cz/discord or https://discord.gg/MguNCfUe53")
print ("===================================================================================")

# Configure your Discord webhooks URLs
SUCCESS_WEBHOOK_URL = "YOUR-WEBHOOK-HERE"
FAILURE_WEBHOOK_URL = "YOUR-WEBHOOK-HERE"

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_to_discord_webhook(url, message):
    data = {"content": message}
    response = requests.post(url, json=data)
    print(response.text)  # Print the response content for debugging purposes

def send_get_request(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code

def main():
    while True:
        # Generate a random alphanumeric string with 18 characters
        generated_code = generate_random_string(18)

        # Send a GET request to the specified URL
        status_code = send_get_request(generated_code)

        # Check if the status code is 200
        if status_code == 200:
            # If the status code is 200, send the code to the success webhook
            send_to_discord_webhook(SUCCESS_WEBHOOK_URL, f"Valid Code: {generated_code}")
        else:
            # If the status code is not 200, send the code to the failure webhook
            send_to_discord_webhook(FAILURE_WEBHOOK_URL, f"Invalid Code: {generated_code}, Status Code: {status_code}")

        # Sleep for a while before generating the next string
        time.sleep(1)

if __name__ == "__main__":
    main()