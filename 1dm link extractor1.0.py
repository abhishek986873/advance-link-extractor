import pyperclip
import time
import re

link_count = 0

while True:
    current_clipboard = pyperclip.paste()
    time.sleep(1)  # wait for a short period of time to check the clipboard again

    if current_clipboard != pyperclip.paste():  # check if the clipboard has been updated
        link_count += 1
        link = pyperclip.paste() # get the link from the clipboard
        if "dash" in link:
            link = link.split("dash")[0] + "master.m3u8" # replace all words after "dash" with "master.m3u8"
        pyperclip.copy(link) # copy the updated link back to the clipboard
        print(f"Link {link_count}: {link}") # print the updated link with the index

        # Extract video ID from CloudFront link
        match = re.search(r'd1d34p8vz63oiq\.cloudfront\.net\/([a-z0-9\-]+)\/', link)
        if match:
            video_id = match.group(1)

            # Create 1DM download link
            one_dm_link = f"https://prourl.xyz/1dm?vid={video_id}"
            print(f"1DM download link: {one_dm_link}")

    if pyperclip.paste().lower() == "exit":  # check if the clipboard contains "exit" to quit the program
        break

print("Exiting...")
