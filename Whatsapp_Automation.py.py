from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from config import CHROME_DATA_PATH
import os

os.system("taskkill /im chrome.exe /f")
options = webdriver.ChromeOptions()
options.add_argument(CHROME_DATA_PATH)

driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe' , options = options)
driver.get('https://web.whatsapp.com/')
time.sleep(20)


def Send_Mesg(Mobile_No, Message):
    Search_Box = driver.find_element("xpath",'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    Search_Box.send_keys(Mobile_No)
    time.sleep(4)

    driver.find_element("xpath",'//*[@id="pane-side"]/div[1]/div/div/div[1]').click()
    time.sleep(4)

    Mesg_Box = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    Mesg_Box.send_keys(Message)
    Mesg_Box.send_keys(Keys.ENTER)
    time.sleep(5)
    print('"'+ Message +'"send to '+ '+919322******')

def main():
    separator = "="*50
    print(separator)
    print("==============Author Mahesh Pawar ==============")
    print(separator)

    Mobile_No = '+919322*******'
    Message =  'Hello...!, welcome from Mahesh Hello...!'
    Send_Mesg(Mobile_No, Message)
    
if(__name__ == "__main__"):
    main()