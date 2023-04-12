import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


import unittest

class GoogleSearchTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://credit-auto.qsiconseil.ma/")

    def tearDown(self):
        self.driver.quit()

    def test_FisrtScript(self):
        data = [
            ['rcd', 'acial!rcd2018'],
            ['lcd', 'acial!acd2018'],
            ['gcd', 'acial!gcd2018'],
            ['acd', 'acial!acd2018'],
        ]
        bouton_acces = self.driver.find_element(By.XPATH, '//*[@id="lnkAccesCreditAuto"]').click()
        for i in range(len(data)):
            userfield = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(data[i][0])  # 00
            time.sleep(1)
            passfield = self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(data[i][1])  #01
            time.sleep(1)
            connection_button = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div/div/form/fieldset/button').click()
            time.sleep(1)

            deco = self.driver.find_element(By.XPATH , '/html/body/nav/div/div[3]/a')
            print(deco)
            time.sleep(1)
            deconnection = self.driver.back()
            clear_input = self.driver.find_element(By.XPATH, '//*[@id="username"]').clear()
            clear_pswd = self.driver.find_element(By.XPATH, '//*[@id="password"]').clear()
    
    def test_SecondScropt(self):
        username= "gcd"
        password = "acial!gcd2018"
        montant_achat = 20000
        pourcentage = random.randint(80,100)
        duree  = 36
        categorie  = random.randint(0,1)
        montant_credit =  20000
        bouton_acces = self.driver.find_element(By.XPATH, '//*[@id="lnkAccesCreditAuto"]').click()
        userfield = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)  # 00
        time.sleep(1)
        passfield = self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)  # 01
        time.sleep(1)
        connection_button = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div/div/form/fieldset/button').click()

        simulation_contrat_link = self.driver.find_element(By.XPATH , '//*[@id="lnkSimulation"]').click()
        time.sleep(3)

        input_achat = self.driver.find_element(By.XPATH , '//*[@id="form_simulation_montantAchat"]').send_keys(montant_achat)
        time.sleep(1)
        input_credit = self.driver.find_element(By.XPATH , '//*[@id="form_simulation_montantCredit"]').send_keys(montant_credit)
        time.sleep(1)
        input_duree = self.driver.find_element(By.XPATH ,'//*[@id="form_simulation_duree"]').send_keys(duree)
        time.sleep(1)
        input_categorie = self.driver.find_element(By.XPATH , '//*[@id="form_simulation_categorie"]').click()
        time.sleep(1)
        if categorie == 0 :
            categorie_A = self.driver.find_element(By.XPATH , '//*[@id="form_simulation_categorie"]/option[1]').click()
            time.sleep(1)
        else :
            categorie_B = self.driver.find_element(By.XPATH, '//*[@id="form_simulation_categorie"]/option[2]').click()
            time.sleep(1)

        calculer_credit = self.driver.find_element(By.XPATH , '//*[@id="calcul"]').click()
        time.sleep(2)
        creer_contrat = self.driver.find_element(By.XPATH ,'/html/body/div[2]/form/fieldset/div[1]/a[2]').click()
        time.sleep(2)
        input_clientName = self.driver.find_element(By.XPATH ,'/html/body/div[2]/fieldset/form/div/input[1]').send_keys("duclos")
        input_search = self.driver.find_element(By.XPATH ,'/html/body/div[2]/fieldset/form/div/input[3]').click()
        time.sleep(1)
        # Locate the hidden checkbox
        # Locate the checkbox by its class
        checkbox = self.driver.find_element(By.CSS_SELECTOR,".custom-control-input")

        # Check the checkbox
        checkbox.click()
                
        time.sleep(5)
        #Formuliare AJOUT CLIENT

if __name__ == "__main__":
    
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="report"))