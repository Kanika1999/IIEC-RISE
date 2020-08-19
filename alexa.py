# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 01:56:29 2020

@author: Kanik
"""

import os
import pyttsx3

pyttsx3.speak("Welcome  to ALEXA")

while True:
    print("chat with me with your requirements : "  , end='')
    p = input()
    # for Social Networking site 
    if ("run" in p)  and  (("facebook" in p) or ("fb" in p)):
        pyttsx3.speak("Opening your facebook")
        os.system("chrome facebook.com") 
    
    elif ("run"in p) and (("mail" in p)or ("gmail" in p)):
        pyttsx3.speak("Opening your Gmail")
        os.system("chrome gmail.com")
        
    elif ("run"in p) and (("utube" in p) or ("youtube" in p)):
        pyttsx3.speak("Opening youtube")
        os.system("chrome youtube.com")
    
    elif (("run" in p) or ("execute " in p)) and (("wssup" in p) or ("whatsapp " in p)):
       pyttsx3.speak("Opening Whatsapp")
       os.system("chrome whatsapp.com") 
       # for accesing coloud services
    elif (("run" in p) or ("execute " in p)) and (("aws" in p) or ("amazon web services " in p)):
       pyttsx3.speak("welcome to AMAZON WEB SERVICES")
       os.system("chrome  aws.com") 
       
    elif (("run" in p) or ("execute " in p)) and (("gcp" in p) or ("Google cloud platform " in p)):
       pyttsx3.speak("welcome to GOOGLE CLOUD PLATFORM")
       os.system("chrome  cloud.googlerun.com") 
    # sites for placement preparation
    elif (("run" in p) or ("execute " in p)) and ("reasoning site" in p):
       pyttsx3.speak("Opening site")
       os.system("chrome indiabix.com") 
    
    elif (("run" in p) or ("execute " in p)) and (("placement" in p) or ("preparation for placemnt " in p)):
       pyttsx3.speak("Opening site")
       os.system("chrome prepinsta.com") 

    #for accesing your own system
    elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
        pyttsx3.speak("welcome to Text Editor")
        os.system("notepad")
    
    elif ("run" in p)  and ("player" in p) or ("media" in p):
       pyttsx3.speak("welcome to Media Player")
       os.system("wmplayer")
         
   
    
    elif (("run" in p) or ("execute " in p)) and (("manager" in p) or ("taskmanager " in p)):
       pyttsx3.speak("Opening Task Manager")
       os.system("taskmgr") 
       
    elif (("run" in p) or ("execute " in p)) and (("cmd" in p) or ("commandprompt " in p)):
       pyttsx3.speak("Opening Command Prompt")
       os.system("cmd") 
     #for online shopping  
    elif (("run" in p) or ("execute " in p)) and (("flipkart" in p) or ("open flipkart " in p)):
       pyttsx3.speak("Opening flipkart")
       os.system("chrome flipkart.com") 
       
    elif (("run" in p) or ("execute " in p)) and (("amazon" in p) or ("open amazon " in p)):
       pyttsx3.speak("Opening Amazon")
       os.system("chrome amazon.com")
    
    elif ("exit" in p)  or ("quit" in p):
       pyttsx3.speak("BYE BYE HAVE A NICE DAY")
       break
    else:
        print("dont support")
