from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
import time
links=[]
chrome_options =webdriver.ChromeOptions()

##chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")
s=Service(ChromeDriverManager().install())
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
no_of_count=int(input("how many times you report the post"))

chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=s,options=chrome_options)
i=0
# url=input("Enter the url")
while(i<no_of_count):
    url="https://www.facebook.com/photo/?fbid=1713683362203233&set=a.13968787938836932"
    chrome.get(url)
    menu_button=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Actions for this post']")))
    chrome.execute_script("arguments[0].click();", menu_button)
    report=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text (),'Find support or report photo')]")))
    chrome.execute_script("arguments[0].click();", report)
    violence=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text (),'Violence')]")))
    chrome.execute_script("arguments[0].click();", violence)
    violencethreat=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text (),'Violent threat')]")))
    chrome.execute_script("arguments[0].click();", violencethreat)
    try:
     violence1=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text (),'Sexual violence')]")))
     chrome.execute_script("arguments[0].click();", violence1)
    except:
        pass
    try:
     submit=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text (),'Done')]")))
     chrome.execute_script("arguments[0].click();", submit)
    except:
        submit=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text (),'Submit')]")))
        chrome.execute_script("arguments[0].click();", submit)
        
        
    time.sleep(5)
    i+=1 
