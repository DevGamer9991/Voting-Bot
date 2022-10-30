from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

firstClr = False

options = Options()

options.add_argument('--log-level=3')
options.add_argument("--window-size=1920,1080")
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

counter = 1

url = "https://okc.vypeok.com/2022/10/25/vote-now-okc-area-private-schools-miss-volleyball-presented-by-community-builders-poll-ends-11-1/"

while True:
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options, service_log_path='NULL')
    
    if (firstClr == False):
        os.system("cls")
        firstClr = True

    print(f"\nOpening URL For the {counter} time.\n")
    counter += 1
    driver.get(url)

    try: 
        inputEl = driver.find_element(By.ID, "PDI_answer51314002")
        voteButton = driver.find_element(By.ID, "pd-vote-button11227721")

        inputEl.click()
        driver.implicitly_wait(1)
        voteButton.click()

        voteTitle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "question-top-11227721")))

        voterWrapper = driver.find_element(By.ID, "pds-results")

        voters = voterWrapper.find_elements(By.TAG_NAME, "li")

        votes = 0
        place = 1
        for voter in voters:
            name = voter.find_element(By.TAG_NAME, "label").find_element(By.TAG_NAME, "span").text
            if (name == "Natalie French – Christian Heritage"):

                votes = voter.find_element(By.XPATH, "//label/span/span[@class='pds-feedback-votes']").text
                votes = votes.split("(")[1]
                votes = votes.split(")")[0]
                votes = votes.split(" votes")[0]

                placeString = ""
                if (place == 1):
                    placeString = "1st"
                elif (place == 2):
                    placeString = "2nd"
                elif (place == 3):
                    placeString = "3rd"
                else:
                    placeString = place + "th"

                print(f"Natalie Has { votes } votes! And She is in { placeString } place!")
                
                break
            else:
                place += 1

        driver.close()
    except Exception as e:
        print("Error Occured!")
        print(e)
        driver.close()
        continue