import getpass
import time
import pyfiglet
import random
import sys
import colorama
from colorama import Fore
from colorama import Style



#function to print the pattern
def pattern(n):
    
    for i in range(0, n):
        for j in range(0, i+1):
            
            print(Style.DIM + '*', end=' ')
              
            # adding two second of time delay
            time.sleep(0.01)
        print(' ')

#main function
if __name__ == '__main__':
    
    # taking range from the user
    num = 15
    print(Fore.BLUE + "loggar in")
      
    # calling function to print the pattern
    pattern(num)
print(Style.NORMAL + "")

#File: captch.py
print("""
       _
      / )
|||| / /
||||/ /
\__(_/
 ||//
 ||/
 ||
(||
 ""
""")
name = input("Vad heter du?\n" + Fore.MAGENTA)






if name == ("ben") or name == ("ebbe") or name == ("alvin") or name == ("anders"):
  print("loggar ut!!")
  repeats = "..fuck you..\n" * 40
  print(Fore.RED + repeats)
  exit()
else:
  print(Fore.BLUE + "Hej " + name + ", det här är min kaffe butik!")


time.sleep(2.4)
print("      {")
print("   {   }")
print("    }_{ __{")
print(" .-{   }   }-.")
print("(   }     {   )")
print("|`-.._____..-'|")
print("|             ;--.")
print("|            (__  \ ")
print("|    MILLE   ,| )  )")
print("|    WEBER    |/  /")
print("|             /  /")
print("|            (  /")
print("\             y'")
print(" `-.._____..-'" + Fore.MAGENTA + Style.BRIGHT)
#meny
 


# function to print the pattern
def pattern(n):
    
    for i in range(0, n):
        for j in range(0, i+1):
            
            print('$', end=' ')
              
            # adding two second of time delay
            time.sleep(0.1)
        print(' ')
  

      
# main function
if __name__ == '__main__':
    
    # taking range from the user
    num = 6
    print("laddar menyn")
      
    # calling function to print the pattern
    pattern(num)

  

print("$$$$$$\$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\ ")
print("$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ |  $$ |")
print("$$ / $$ / $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |")
print("$$ | $$ | $$ |$$   ____|$$ |  $$ |$$ |  $$ |")
print("$$ | $$ | $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ |")
print("\__| \__| \__| \_______|\__|  \__| \____$$ |")
print("                                  $$\   $$ |")
print("                                  \$$$$$$  |")
print("                                   \______/ ")


print("  .-=-.")
print(" ,|`~'| 20kr kaffe")
print(" `|   |")
print("   `~'")


print("  .-~~-.")
print(",|`-__-'|")
print("||      | 40kr espresso")
print("`|      |")
print("  `-__-'")


print("  .=%%=.")
print(",|`=%%='|")
print("||      | 30kr latte")
print("`|      |")
print("  `-__-'")



#vilken
dryck = input(Fore.BLUE + "Vilken vill du köpa?\n" + Fore.MAGENTA)

if dryck == "kaffe":
  price = 20

elif dryck == "espresso":
  price = 40

elif dryck == "latte":
  price = 30
else:
  print("Vi har inte det på våran meny")
  exit()

manga = input(Fore.BLUE + "Hur många?\n" + Fore.MAGENTA)

#tråkig matte
total = price * int(manga)
#summa
print(Fore.BLUE + "det blir " + str(total) + " kr tack!\n")

password = getpass.getpass()
#all information och avslutning
print("\nTack " + name + " dina " + str(manga) + " " + dryck + ",s är klara om en stund ;) tryck enter ")

input()
print(Fore.RED + Style.BRIGHT + " ")


print("$ tack för koden " + name + ". Ditt bank konto är tomt nu $\n")
print("$ Du får ingen " + dryck + " $")

print("""
                                  .
     .              .   .'.     \   /
   \   /      .'. .' '.'   '  -=  o  =-
 -=  o  =-  .'   '              / | \
   / | \                          |
     |                            |
     |                            |
     |                      .=====|
     |=====.                |.---.|
     |.---.|                ||=o=||
     ||=o=||                ||   ||
     ||   ||                ||   ||
     ||   ||                ||___||
     ||___||                |[:::]|
     |[:::]|                '-----'
     '-----'
""")
for i in range(7):
     
    # using sleep() to hault execution
    time.sleep(1)
    print(i)
  
print("ALLA PENGAR ÄR ÖVERFÖRDA")

print(Fore.GREEN + """
   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
""")

print(Fore.RED + "replit repl process died unexpectedly: exit status 255")

hämlig = input()
if hämlig == "1213":
  print(name + ",s lösenord är " + password)


print("""
    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
""")
exit()
