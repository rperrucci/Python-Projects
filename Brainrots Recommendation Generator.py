#init
#Robert
import webbrowser

url = ["https://static.wikitide.net/italianbrainrotwiki/f/fa/Tung_tung_tung_sahur.png?20260104084952",
       "https://static.wikitide.net/italianbrainrotwiki/thumb/e/e0/Tralalelo_tralala.png/599px-Tralalelo_tralala.png?20250718174343",
        "https://static.wikitide.net/italianbrainrotwiki/thumb/c/cb/U_Din_Din_Din_Din_Dun_Ma_Din_Din_Din_Dun2.webp/300px-U_Din_Din_Din_Din_Dun_Ma_Din_Din_Din_Dun2.webp.png",
        "https://static.wikitide.net/italianbrainrotwiki/thumb/5/50/Chimpanzini_Bananino.png/600px-Chimpanzini_Bananino.png?20250509140541"]


#Functions
def brainrot():
    print("Hello! Today I will be recommending you a brainrot based on your preferences.")
    pick = input("Do you prefer baseball or swimming?: ")
    if pick == "baseball":
        print("I belive that Tung Tung Tung Sahur, a baseball bat wielding brainrot, is the right choice for you.")
        webbrowser.open(url[0])
    if pick == "swimming":
            print("I believe that Tralalelo Tralala, a shark possesing shoes on all 4 of his legs, is the right choice for you.")
            webbrowser.open(url[1])
    rec = input("Do you want another brainrot recommendation? (Y/N): ").upper()
    if rec == "Y":
         fruit = input("Do you prefer oranges or bananas?: ")
         if fruit == "oranges":
              print("I believe that Odin Din Din Dun, a walking orange with huge muscles, is the right choice for you.")
              webbrowser.open(url[2])
         if fruit == "bananas":
              print("I believe that Chimpanzini Bananini, a hopping banana with a chimpanzi for a head, is the right choice for you.")
              webbrowser.open(url[3])
    if rec == "N":
         print("Have a good day!")

#main
brainrot()






#Picture of Tung Tung Tung Sahur
#Website Name: Italian Brainrot Wiki
#Url: https://italianbrainrot.miraheze.org/wiki/File:Tung_tung_tung_sahur.png
#Author Name: Noxa
#Date: 14:32, 7 May 2025
#Article Title: Tung Tung Tung Sahur

#Picture of Tralalelo Tralala
#Website Name: Italian Brainrot Wiki
#Url: https://italianbrainrot.miraheze.org/wiki/File:Tralalelo_tralala.png
#Author Name: @eZburger401, @amoamimandy.1a, and @elchino1246
#Date: 17:35, 29 April 2025
#Article Title: Tralalelo Tralala

#Picture of Odin Din Din Dun
#Website Name: Italian Brainrot Wiki
#Url: https://italianbrainrot.miraheze.org/wiki/U_Din_Din_Din_Din_Dun_Ma_Din_Din_Din_Dun
#Author Name:Noxa (deleted due to copyright infringement), Italian Brainrot Animals (re-upload), ReisonBS (ReisonBS), Low Brainrot (V3), SebasMZ (V4)
#Date: 00:56, 10 May 2025
#Article Title: U Din Din Din Din Dun Ma Din Din Din Dun

#Picture of Chimpanzini Bananini
#Website Name: Italian Brainrot Wiki
#Url: https://italianbrainrot.miraheze.org/wiki/Chimpanzini_Bananini
#Author Name: alexey_pigeon
#Date: 14:05, 9 May 2025
#Article Title: Chimpanzini Bananini
