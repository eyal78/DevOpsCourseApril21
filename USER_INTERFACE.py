from create_user import create_user
import pyfiglet
from termcolor import colored
import time

# App Welcome Sign
welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

# Welcome Message for newly subscribed user
print((colored("Welcome to Youtube Crawler By Noam -Ver. 1.0.1-beta ", 'blue', attrs=['bold'],)))
print("------------------------------------------------------------")
time.sleep(1.2)



# Asking for Username and Creating a User
username = input("Please Enter A Username: ")

# Creating a username for Youtube Crawler
create_user(username)

# Greeting The New User
time.sleep(1.2)
print((colored("Hey there {} lets Start Having Fun!\U0001f60d ".format(username), 'cyan',)))
print("------------------------------------------------------------")
time.sleep(1.2)

# Asking User for a Search String
# If you only want to download a short test video enter ---> youtube-dl test video
search_str = input("Please Enter A Topic To Download: ")
print("------------------------------------------------------------")
time.sleep(1.2)

# Asking User For A Number Of Videos To Download
number = input("Please Enter A Number Of Videos To Download: ")
print("------------------------------------------------------------")
time.sleep(1.2)

# Importing Youtube Downloader And Uploader To AWS S3 Bucket
from youtube_crawler import upload

# Calling Youtube With search_str,search_results,username
upload(username,search_str,number)

# Printing A User A Thank You Note
print("------------------------------------------------------------")
print((colored('Thank You {} for Using Youtube Crawler By Noam \U0001f60d'.format(username), 'blue', attrs=['bold'],)))
print("------------------------------------------------------------")
exit(0)












