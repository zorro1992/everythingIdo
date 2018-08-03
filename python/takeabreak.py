import webbrowser
import time
#This opens a Youtube Browser every 10 sec 3 times 
total_break = 0

while(total_break<=3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=3jUSDLtRd9s")
    total_break = total_break+1

