'''
Created on  : 2023-06-20

@author     : Ananthakrishnan 

source      : https://medium.com/featurepreneur/selenium-c78e87cc8c4a

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
import csv

def startpy():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bestrandoms.com/random-address-in-ca?quantity=20")

    with open('addresses.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Street', 'City', 'State', 'Postal Code'])

        for j in range(5):

            for i in range(1,21):

                street = driver.find_element(By.XPATH,f'//*[@id="main"]/div/div[2]/div[2]/ul/li[{i}]/p[1]/span').text
                city   = driver.find_element(By.XPATH,f'//*[@id="main"]/div/div[2]/div[2]/ul/li[{i}]/p[2]/span').text
                state  = driver.find_element(By.XPATH,f'//*[@id="main"]/div/div[2]/div[2]/ul/li[{i}]/p[3]/span').text
                zipcode= driver.find_element(By.XPATH,f'//*[@id="main"]/div/div[2]/div[2]/ul/li[{i}]/p[5]/span').text

                
                writer.writerow([street[7:], city[5:], state[20:], zipcode[8:]])
                


            # Everytime you refresh you get a new set of addresses
            pag.write(["ctrl", "R"])



if __name__ == '__main__':
    startpy()
        