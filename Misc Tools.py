# URL Shortener
# YouTube Downloader

import Modules.Shorteners.tinyurl as TinyURL
import Modules.Shorteners.bitly as Bitly
import Modules.Downloads.downloader as DL_YT

# Main

list = [
    "\nWelchen Dienst willst du benutzen?\n",
    "1: [URL Shortener] TinyURL",
    "2: [URL Shortener] Bitly (W.I.P)",
    "3: [Downloader]    YouTube\n"
]

for i in list:
    print(i)

generator_chosen = False

while not generator_chosen:
    try:
        chosen_generator = int(input("\nDeine Auswahl (1-3): "))
        
        if 0 < chosen_generator < 4:
            generator_chosen = True
        else:
            raise ValueError

    except ValueError:
        print(f"Bitte gib eine Ganzzahl zwischen 1 und 3 ein.")

url = input("\nBitte gib nun die URL ein: ")

if chosen_generator == 2:
    chosen_generator = 1
    print(f"Gewählten URL Shortener auf 'TinyURL' geändert ...\n")

shortend_url = "Error"

if chosen_generator == 1:
    shortener = TinyURL.Shortener()
    shortend_url = shortener.short_url(url)

elif chosen_generator == 2:
    pass

elif chosen_generator == 3:
    DL_YT.download(url)

if chosen_generator == 1 or chosen_generator == 2:
    print(f"Deine verkürzte URL: '{shortend_url}'")


input("\nZum beenden <Enter> drücken.")