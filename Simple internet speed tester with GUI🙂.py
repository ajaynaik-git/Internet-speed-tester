# Author & Source code details

# Author - Ajay A Naik
# About code - the code checks your network speed and output is given in a GUI.
# If you enjoyed using the code & want to DM me just drop a message @ Linkedin (available in my git hub profile section)🙂



#pip install tkinter
#pip install speedtest
#if tkinter & speedtest modules are not present in your computer type above commands in CMD 

# note- if speedtest is not working uninstall it by typing pip uninstall speedtest & try pip install speedtest-cli this will solve the issue.
 
from tkinter import * #importing tkinter module
from speedtest import Speedtest #importing speedtest module

#main function
def update_text(): 
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)#made the value to be rounded because it displays at long float value & also divides by 10 to the power 6
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps") 


#GUI Config
root = Tk()
#Giveing a title which will be displayed at top of dialog box
root.title("AJAY'S INTERNET SPEED TESTER ")
#Adjust the size as per requried
root.geometry('420x250+250+150')
#backgroud color is an optional sclect as per your wish
root.config(background='black')
#this is for creating button and i have added a name for button , adjust the width of the button , here comes the main point "COMMAND" goes to main function and fetches the updated data
button = Button(root, text="Click Here To Know Your Internet Speed \n Please wait for 1min ", width=50, command=update_text,background = '#49A')
#closeing button workflow
button.pack()
#label is been created for displaying download speed result same for upload also
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()



root.mainloop()
