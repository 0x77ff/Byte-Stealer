import sys

def save_variables_to_file(webhook_url, copy_to_startup, btc_wallet):
    try:
        with open("saved_variables.txt", "w") as file:
            file.write(f"Webhook URL: {webhook_url}\n")
            file.write(f"Copy to startup?: {copy_to_startup}\n")
            file.write(f"BTC wallet: {btc_wallet}\n")
    except Exception as e:
        print("Error occurred while writing to the file:", e)


if __name__ == '__main__':
 if len(sys.argv) >= 4:
    # Extract the command-line arguments from sys.argv
    webhook_url = sys.argv[1]
    copy_to_start_up = sys.argv[2]
    btc_wallet = sys.argv[3]
    save_variables_to_file(webhook_url, copy_to_start_up, btc_wallet)
 else:
    pass