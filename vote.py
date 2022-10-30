from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from threading import Thread

options = Options()

options.add_argument('--log-level=3')
options.add_argument("--window-size=1920,1080")
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

counter = 1

url = "https://okc.vypeok.com/2022/10/25/vote-now-okc-area-private-schools-miss-volleyball-presented-by-community-builders-poll-ends-11-1/"

def bot(counter, url):
    while True:
        driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options, service_log_path='NULL')

        print(f"Started New Vote")
        counter += 1
        driver.get(url)

        try: 
            inputEl = driver.find_element(By.ID, "PDI_answer51314002")
            voteButton = driver.find_element(By.ID, "pd-vote-button11227721")

            inputEl.click()
            driver.implicitly_wait(.50)
            voteButton.click()

            voteTitle = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "question-top-11227721")))

            voterWrapper = driver.find_element(By.ID, "pds-results")

            voters = voterWrapper.find_elements(By.TAG_NAME, "li")

            votes = 0
            place = 1
            for voter in voters:
                name = voter.find_element(By.TAG_NAME, "label").find_element(By.TAG_NAME, "span").text
                if (name == "Natalie French – Christian Heritage"):

                    votes = voter.find_element(By.TAG_NAME, "label").find_element(By.CLASS_NAME, "pds-feedback-result").find_element(By.CLASS_NAME, "pds-feedback-votes").text
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
                if (name == "Gracie Maschmeier – Crossing Christian"):
                    votes = voter.find_element(By.TAG_NAME, "label").find_element(By.CLASS_NAME, "pds-feedback-result").find_element(By.CLASS_NAME, "pds-feedback-votes").text
                    votes = votes.split("(")[1]
                    votes = votes.split(")")[0]
                    votes = votes.split(" votes")[0]

                    print(f"Gracie Has { votes } votes!")

            driver.quit()
        except Exception as e:
            print("Error Occured!")
            driver.quit()
            continue

t1 = Thread(target=bot, args=(counter, url))
t2 = Thread(target=bot, args=(counter, url))
t3 = Thread(target=bot, args=(counter, url))
t4 = Thread(target=bot, args=(counter, url))
t5 = Thread(target=bot, args=(counter, url))
t6 = Thread(target=bot, args=(counter, url))
t7 = Thread(target=bot, args=(counter, url))
t8 = Thread(target=bot, args=(counter, url))
t9 = Thread(target=bot, args=(counter, url))
t10 = Thread(target=bot, args=(counter, url))
t11 = Thread(target=bot, args=(counter, url))
t12 = Thread(target=bot, args=(counter, url))
t13 = Thread(target=bot, args=(counter, url))
t14 = Thread(target=bot, args=(counter, url))
t15 = Thread(target=bot, args=(counter, url))
t16 = Thread(target=bot, args=(counter, url))
t17 = Thread(target=bot, args=(counter, url))
t18 = Thread(target=bot, args=(counter, url))
t19 = Thread(target=bot, args=(counter, url))
t20 = Thread(target=bot, args=(counter, url))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t20.start()