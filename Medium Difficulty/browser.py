import re
import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Taking Command-line arguments
args = sys.argv
if len(args) < 2:
    directory = "mydir"
else:
    directory = args[1]

# Creating Directory if it does not exist
if not os.path.exists(directory):
    os.mkdir(directory)

# Regex
urlRegex = re.compile(r"(https://)?(.*)")
filenameRegex = re.compile(r"^(https://)?(www.)?(.*)\.(\w\w\w)$")

domain_names = (".org", ".com")
init()  # Colorama Initialise
stack = deque()
currentPage = None

while True:
    mock_url = input()
    mo = urlRegex.search(mock_url)

    # Exit
    if mock_url == "exit":
        exit(0)

    # Back
    elif mock_url == "back":
        if len(stack) == 1 and stack[0] is None:
            pass
        else:
            currentPage = stack.pop()
            print(currentPage)

    # Display Page from internet
    elif mock_url.endswith(domain_names):
        # Adding the https:// part to the url if it does not contain it
        if not mo.group(1):
            mock_url = "https://" + mock_url

        r = requests.get(mock_url)
        if r:
            stack.append(currentPage)
            soup = BeautifulSoup(r.content, features='html.parser')
            lines = []
            soup.script.decompose()
            for soupy in soup.find_all(['p', 'a', 'ul', 'ol', 'li']):
                if soupy.has_attr('href'):
                    print(Fore.BLUE + soupy.get_text().strip())
                    print(Style.RESET_ALL, end="")
                else:
                    print(soupy.get_text().strip())
                lines.append(soupy.get_text().strip())

            mo2 = filenameRegex.search(mock_url)
            filename = mo2.group(3)
            with open(f"{directory}/{filename}.txt", mode="w", encoding=soup.encoding) as f:
                for line in lines:
                    f.write(line + "\n")

        else:
            print("Error: Incorrect URL")

    # Display locally stored Page
    else:
        try:
            with open(f"{directory}/{mock_url}.txt") as f:
                stack.append(currentPage)
                currentPage = f.read()
                print(currentPage)
        except FileNotFoundError:
            print("Error: Incorrect URL")
