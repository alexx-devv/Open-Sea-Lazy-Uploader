'''
   ____                            _____                   
  / __ \                          / ____|                  
 | |  | |  _ __     ___   _ __   | (___     ___    __ _    
 | |  | | | '_ \   / _ \ | '_ \   \___ \   / _ \  / _` |   
 | |__| | | |_) | |  __/ | | | |  ____) | |  __/ | (_| |   
  \____/  | .__/   \___| |_| |_| |_____/   \___|  \__,_|   
 | |      | |                                              
 | |      |_|_ _   ____  _   _                             
 | |       / _` | |_  / | | | |                            
 | |____  | (_| |  / /  | |_| |                            
 |______|  \__,_| /___|  \__, |            _               
 | |  | |         | |     __/ |           | |              
 | |  | |  _ __   | |   _|___/  __ _    __| |   ___   _ __ 
 | |  | | | '_ \  | |  / _ \   / _` |  / _` |  / _ \ | '__|
 | |__| | | |_) | | | | (_) | | (_| | | (_| | |  __/ | |   
  \____/  | .__/  |_|  \___/   \__,_|  \__,_|  \___| |_|   
          | |                                              
          |_|                                                                             

Author: Alexx Devv (aka D1G1T) 

Any donation will go to my pizza fund, I love pizza...
ETH: 0x5a7d97C88e9dbBE1748Fb24D5fb7875745d7A152
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import json, time, os, shutil, sys

if "uploaded" not in os.listdir():
    os.mkdir("uploaded")

if "images" not in os.listdir("uploaded"):
    os.mkdir("uploaded/images")

if "metadata" not in os.listdir("uploaded"):
    os.mkdir("uploaded/metadata")

if "images" not in os.listdir():
    os.mkdir("images")

if "metadata" not in os.listdir():
    os.mkdir("metadata")

if len(os.listdir("images")) == 0:
    print("----------------------------------------")
    sys.exit("ERROR: 'images' folder empty.")
 
if len(os.listdir("metadata/")) == 0:
    print("----------------------------------------")
    sys.exit("ERROR: 'metadata' folder empty.")

if len(os.listdir("metadata")) != len(os.listdir("images")):
    sys.exit("ERROR: Amount of images and metadata files need to be the same.")

print("----------------------------------------")
collectionLink = input("Collection link: ")

print("----------------------------------------")
print("Choose your operative system:")
print("Linux    [1]")
print("Windows  [2]")
print("Mac      [3]")
currentOS = input("[1, 2 or 3]: ")

if currentOS == "1":
    # ------- LINUX -------

    # Firefox users
    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Firefox(service=Service("drivers/linux/geckodriver"), options=options)
    driver.execute("INSTALL_ADDON", {"path": f"{os.getcwd()}/metamask/metamask-10.8.0-an+fx.xpi"})
    driver.get("https://opensea.io/login?referrer=%2Faccount")

    # ------- LINUX -------

if currentOS == "2":
    # ------- Windows -------

    # Firefox users
    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Firefox(service=Service("drivers/windows/geckodriver.exe"), options=options)
    driver.execute("INSTALL_ADDON", {"path": f"{os.getcwd()}/metamask/metamask-10.8.0-an+fx.xpi"})
    driver.get("https://opensea.io/login?referrer=%2Faccount")

    # ------- Windows -------

if currentOS == "3":
    # ------- Mac -------

    # Firefox users
    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Firefox(service=Service("drivers/mac/geckodriver"), options=options)
    driver.execute("INSTALL_ADDON", {"path": f"{os.getcwd()}/metamask/metamask-10.8.0-an+fx.xpi"})
    driver.get("https://opensea.io/login?referrer=%2Faccount")

    # ------- Mac -------

# Variables
secretPhrase = json.load(open(f"login-info.json", mode="r"))["phrase"]
password = json.load(open(f"login-info.json", mode="r"))["password"]

driver.switch_to.window(driver.window_handles[1])

# Set up MetaMask

try:
    getStarted = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/button"))
    )
    getStarted.click()
except:
    print("----------------------------------------")
    sys.exit("ERROR: MetaMask didn't load properly")

importWallet = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button")
importWallet.click()

dontSendDataMetaMask = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]")
dontSendDataMetaMask.click()

inputPhrase = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input")
inputPhrase.send_keys(secretPhrase)

inputPassword = driver.find_element(By.XPATH, '//*[@id="password"]')
confirmPassword = driver.find_element(By.XPATH, '//*[@id="confirm-password"]')

inputPassword.send_keys(password)
confirmPassword.send_keys(password)

acceptToS= driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[7]/div")
acceptToS.click()

importWalletLasStep = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/button")
importWalletLasStep.click()

try:
    allDone = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button"))
    )
    allDone.click()
except:
    pass

driver.close()

driver.switch_to.window(driver.window_handles[0])

# OpenSea
connectMetaMask = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[1]/button/div[2]/span")
connectMetaMask.click()

driver.switch_to.window(driver.window_handles[1])
print("----------------------------------------")
input("Tick the address you want to use and press 'Enter': ")

metamaskNext1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]")
metamaskNext1.click()
metamaskConnect = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]")
metamaskConnect.click()

driver.switch_to.window(driver.window_handles[0])
try:
    driver.get(collectionLink)
except:
    print("----------------------------------------")
    sys.exit("ERROR: Collection not found.")

amountImages = len(os.listdir("images/"))
iteracion = 1

for image in sorted(os.listdir("images/")):

    imageUploaded = False
    numberFile = image.split(".")[0]
    metadata_file = open(f"metadata/{numberFile}.json", mode="r")
    metadata = json.load(metadata_file)

    while imageUploaded == False:
        try:
            addItem = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div[1]/span/a"))
            )
            addItem.click()
            imageUploaded = True
        except:
            driver.get(collectionLink)
    
    if iteracion == 1:
        while len(driver.window_handles) == 1:
            time.sleep(1)
            
        driver.switch_to.window(driver.window_handles[1])

        try:
            sign = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/button[2]"))
            )
            sign.click()
        except:
            print(f"MetaMask's 'Sign' button not found, aborting process.")
            driver.quit()

        driver.switch_to.window(driver.window_handles[0])

        iteracion += 1

    dragNdropImage = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="media"]'))
    )
    
    dragNdropImage.send_keys(os.path.abspath(f"images/{image}"))

    nameInput = driver.find_element(By.XPATH, '//*[@id="name"]')
    nameInput.send_keys(metadata["name"])

    descriptionInput = driver.find_element(By.XPATH, '//*[@id="description"]')
    descriptionInput.send_keys(metadata["description"])

    openProperties = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/section/div[2]/form/section/div[1]/div/div[2]/button")
    openProperties.click()

    contador = 1
    posicion = 2
    for attribute in metadata["attributes"]:

        if contador == 1:
            attributeType = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/section/table/tbody/tr/td[1]/div/div/input")
            attributeName = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/section/table/tbody/tr/td[2]/div/div/input")

            attributeType.send_keys(attribute["trait_type"])
            attributeName.send_keys(attribute["value"])
            
            contador += 1

        else:
            addMoreAttributes = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/section/button")
            addMoreAttributes.click()

            attributeType = driver.find_element(By.XPATH, f"/html/body/div[5]/div/div/div/section/table/tbody/tr[{posicion}]/td[1]/div/div/input")
            attributeName = driver.find_element(By.XPATH, f"/html/body/div[5]/div/div/div/section/table/tbody/tr[{posicion}]/td[2]/div/div/input")

            attributeType.send_keys(attribute["trait_type"])
            attributeName.send_keys(attribute["value"])
            
            contador += 1
            posicion += 1
            
    saveAttributes = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/footer/button")
    saveAttributes.click()

    createNFT = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button")
    createNFT.click()

    shutil.move(f"images/{image}", f"uploaded/images/{image}")
    shutil.move(f"metadata/{numberFile}.json", f"uploaded/metadata/{numberFile}.json")

    print("----------------------------------------")
    print(f"{numberFile}/{amountImages} uploaded!")

print("----------------------------------------")
print("Done! feel free to send me some ETH for pizza, I am a hungry dev.")
print("ETH: 0x5a7d97C88e9dbBE1748Fb24D5fb7875745d7A152")
