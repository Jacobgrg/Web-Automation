import re
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

class main:

    def __init__(self):
        self.init()

    def init(self):
        driver.get("https://jiness.hk/a/login")
        driver.maximize_window()
        self.login()
        self.search()
        self.page_has_loaded()
        self.description()



    def login(self):
        username = ("Enter your Email")
        password = ("Enter your Password")
        user = driver.find_element("name", "user-name")
        user.send_keys(username)

        user = driver.find_element("name", "user-password")
        user.send_keys(password)
        user.submit()

    def search(self):
        # btn = driver.find_element("class","btn btn-info")
        btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div/button")
        btn.click()
            

        src = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/input[1]")
        src.send_keys("programmer")

        deadline = Select(driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[2]/div/div[4]/select'))
        deadline.select_by_index(2)
        print("Selection sucess")
        btn = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div/button')
        btn.click()

    def page_has_loaded(self):
        _timeout = 10  # ⚠ don't forget to set a reasonable timeout
        WebDriverWait(driver, _timeout).until(
            expected_conditions.presence_of_element_located(
                # we can wait by any selector type like element id:
                (By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/input[1]")
            )
        )
        print("Success")

   

    def description(self):
        #  int=driver.find_elements(By.XPATH,("//*[@id='joblist_tab_current']"))
         elements = driver.find_elements(By.XPATH,("//div[@id='joblist_tab_current']/div"))
         num= len(elements)
         z=0
        #  print (int.size)
         print(f"------------------------------------- int{num} ------------------------------------------------------")
         for i in range(1,num+1):

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div/div/div/div/div[1]/div/div[4]/div/div/div/div[{i}]"))).click()        
             # Gets the Company Details
            Company = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/div[1]/div/div[4]/div/div/div/div[{i}]/div[1]/h5").text
            print(Company)
            #  Click on the Close button 
            close = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div/div[4]/button")

            driver.execute_script("arguments[0].scrollIntoView();", close)
            _timeout = 10  # ⚠ don't forget to set a reasonable timeout
            WebDriverWait(driver, _timeout).until(
                expected_conditions.presence_of_element_located(
                # we can wait by any selector type like element id:
                (By.XPATH, "html/body/div/div/div/div/div[7]/div/div/div[4]/button")
            ))

            # Sleep is kept here so that the content can load
            time.sleep(3)
            try:
                Email= driver.find_element(By.CSS_SELECTOR,("a[href*='@']"))
                print(Email.text)
            except NoSuchElementException as exception:
                self.cleaning()
            print("------------------------")
            
            # Click finish button
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "html/body/div/div/div/div/div[7]/div/div/div[4]/button"))).click()

         print("Finish")

    def cleaning(self):
         text = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div/div[2]/form/div/div[3]/div[9]").text
         match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
         print("ELO")
         
         print(match)
        
Object = main()








 



















