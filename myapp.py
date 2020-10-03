import pyttsx3
import os

print("############################### Welcome to the Service Menu ###############################" )
pyttsx3.speak("Hello user")
pyttsx3.speak("\n\n\n\nWelcome to the Service Menu\n\n\n\n")
pyttsx3.speak("I am jackii your virtual assistant !!")
pyttsx3.speak("And I am here to help you in the following Services !!")
print("\t\t\t>Window based command")
pyttsx3.speak("Window based command")
print()
print("\t\t\t>Email")
pyttsx3.speak("Email")
print()
print("\t\t\t>search engine")
pyttsx3.speak("Search engine ")
print()
print("\t\t\t>virtualization")
pyttsx3.speak("virtualization")
print()
print("\t\t\t>Social media")
pyttsx3.speak("social media")
print()
print("\t\t\t>shopping")
pyttsx3.speak("shopping")
print()
print("\t\t\t>Entertainment")
pyttsx3.speak("Entertainment")
print()
print("\t\t\t>public clouds")
pyttsx3.speak("Public clouds") 

print()
while True:
  print("Hey user what service you want to run:\t",end="")
  pyttsx3.speak("Now ,Type Name of Service that you want to run")
  p=input()
  if(("run" in p or "launch" in p or "open" in p or "execute" in p)and("chrome" in p or "browser" in p)):
    pyttsx3.speak("opening browser")
    print("opening  browser!")
    os.system("chrome")
  elif("hello" in p or "hii" in p or "hey" in p or "hy" in p ):
    pyttsx3.speak("Hello User") 
  elif(("tell" in p and  "about" in p and "yourself" in p) or ("who" in p and "are" in p and "you" in p or "u" in p) ):
    pyttsx3.speak("My name is jackiee, I am your virtual assistant ,and I am here to help you user")
  elif(("run" in p or "launch" in p or "open" in p or "execute" in p)and("media" in p or "player" in p or "song" in p)):
    pyttsx3.speak("opening media player")
    print("opening  media player!")
    os.system("wmplayer")
  elif(("run" in p or "open" in p or "launch" in p or "execute" in p)and("editior" in p or "notepad" in p)):
    pyttsx3.speak("opening text editor")
    print("opening  Text editor!")
    os.system("notepad")
  elif(("open" in p or "launch" in p or "run" in p)and("calculator" in p or "calc" in p)):
    pyttsx3.speak("opening calculator")
    print("opening  Calculator!")
    os.system("calc")	
  elif(("run" in p or "open" in p or "launch" in p )and ("jupyter" in p or "IDE" in p or "ide" in p or"noteook" in p)):
    pyttsx3.speak("opening jupyter IDE")
    print("opening  Jupyter IDE")
    os.system("jupyter noteook")
  elif(("run" in p or "open" in p or "launch" in p  )and ("paint" in p or "drawing" in p )):
    pyttsx3.speak("opening Paint Software")
    print("opening  Paint Software")
    os.system("mspaint")
  elif ("youtube" in p):
    pyttsx3.speak("opening youtube")
    print("opening YoutTube")
    os.system("chrome www.youtube.com")
  elif("linkedin" in p ):
    pyttsx3.speak("opening Linkedin")
    print("opening Linkedin")
    os.system("chrome www.linkedin.com")
  elif("facebook" in p ):
    pyttsx3.speak("opening facebook")
    print("opening Facebook")
    os.system("chrome www.facebook.com")
  elif("spotify" in p ):
    pyttsx3.speak("opening spotify")
    print("opening Spotify")
  elif("gaana music" in p or "gaana" in p ):
    pyttsx3.speak("opening Gaana MUSIC")
    print("opening Gaana ")
    os.system("chrome www.gaana.com")
  elif("instagram" in p ):
    pyttsx3.speak("opening instagram")
    print("opening Instagram")
    os.system("chrome www.instragam.com")
  elif("twitter" in p ):
    pyttsx3.speak("opening twitter")
    print("opening Twitter")
    os.system("chrome www.twitter.com")
  elif ("google" in p and "cloud" in p or "gcp" in p ):
    pyttsx3.speak("opening Google cloud")
    print("opening Google Cloud")
    os.system("chrome cloud.google.com")
  elif ("gmail" in p ):
    pyttsx3.speak("opening Gmail")
    print("opening Gmail")
    os.system("chrome www.gmail.com")
  elif ("yahoo" in p ):
    pyttsx3.speak("opening Yahoo mail")
    print("opening Yahoo mail")
    os.system("chrome www.yahoomail.com") 
  elif ("aws cloud" in p or "aws" in p or "amazon web service" in p or "AWS" in p ):
    pyttsx3.speak("opening Amazon web service")
    print("opening Amazon web service ")
    os.system("chrome aws.amazon.com")   
  elif(("run" in p or "launch" in p or "open" in p)and ("putty" in p)):
    pyttsx3.speak("opening Putty Software")
    print("opening Putty Software")
    os.system("putty")
  elif(("run" in p or "launch" in p or "open" in p or "start" in p)and ("slack" in p)):
    pyttsx3.speak("opening Slack Software")
    print("opening Slack Software")
    os.system("slack")
  elif(("show" in p or "listout" in p or "open" in p or "start" in p)and ("directory" in p)):
    pyttsx3.speak("Listing all the directory")
    print("Listing all the directory ")
    os.system("dir")
  elif( "open" in p or "start" in p)and ("anydesk" in p):
    pyttsx3.speak("opening Anydesk")
    print("Opening Anydesk ")
    os.system("anydesk")
  elif("whatsapp" in p ):
    pyttsx3.speak("opening whatsapp")
    print("opening Whatsapp")
    os.system("chrome web.whatsapp.com")
  elif("amazon" in p ):
    pyttsx3.speak("opening Amazon")
    print("opening Amazon")
    os.system("chrome www.amazon.com")
  elif("flipkart" in p ):
    pyttsx3.speak("opening Flipkart")
    print("opening Flipkart")
    os.system("chrome www.flipkart.com")
  elif("virtualbox" in p or "virtual box" in p or "virtualization" in p or "vm" in p or "VM" in p or "virtual machine" in p):
    pyttsx3.speak("opening Virtualbox")
    print("opening Virtualbox")
    os.system("virtualbox")
  elif("date" in p ):
    pyttsx3.speak("showing todays date")
    print("showing todays date")
    os.system("date")
  elif("time" in p ):
    pyttsx3.speak("Showing current time")
    print("showing current time")
    os.system("time")
  elif("clear" in p and "screen" in p ):
    os.system("cls") 
  elif("exit" in p or "stop" in p or "quit" in p or "bye" in p):
    pyttsx3.speak("We are closing the program !! Hope you like our service, have a nice day !!")
    os.system("exit()")
    break
  else:
    pyttsx3.speak("service not available")
    print(" Service not available")
    





 




