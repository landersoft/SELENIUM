from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, webbrowser


options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\lander\\Desktop\\Desarrollo\\scrap\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

driver.get('https://www.binance.com/es-LA/pos')

time.sleep(1)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/main/div/div[3]/div/div[1]/div/input')))\
    .send_keys('ADA')
time.sleep(1)   
#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/div[1]/div/main/div/div[3]/div/div[2]/div[3]/div/div[3]/div/button[3]')))\
#    .clic()


'''WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CLASS_NAME,
                                      ' css-si4zlj')))\
    .click()
'''
'''boton = browser.find_elements_by_xpath("button = browser.find_elements_by_xpath("/html/body/div/button")")
button[0].click()'''



button = driver.find_elements_by_xpath('/html/body/div[1]/div/main/div/div[3]/div/div[2]/div[3]/div/div[3]/div/button[3]')
print (button)
button[0].click()

suscribirse90 = []


print("Esto es a 90 dias: ")


## Aca revisa si está disponible en 90 dias
suscribirse90 = driver.find_elements_by_xpath('/html/body/div[1]/div/main/div/div[3]/div/div[2]/div[2]/div[2]/button')
print(suscribirse90)
if (suscribirse90 != []):
    print("Mandar correo")
else:
    print("No disponible aun")









time.sleep(3)

driver.close()

 