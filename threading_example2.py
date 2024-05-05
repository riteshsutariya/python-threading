import threading
import requests
import time

def download_file():
    print('starting downloading file')
    response=requests.get('https://www.wikipedia.org/')
    with open('./wikipedia.json', 'wb') as f:
        f.write(response.content)
    print("File downloaded.")
    
print("Starting file download in a thread...")
# Start the download in a new thread.
thread = threading.Thread(target=download_file)
thread.start()

# The main thread continues.
print("The main thread continues while the file is being downloaded.")
time.sleep(2)
print("Main thread completed.")