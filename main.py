from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

from accuount_info import my_email, my_password , product_list

class AutomatedShopping:
    # for keeping brower open
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
    # to maximize the brower
    driver.maximize_window()


    def sign_in(self):
        self.driver.get('https://www.trendyol.com/giris?cb=%2F')

        time.sleep(3)
        user_name = self.driver.find_element("name", "login email")
        user_name.send_keys(my_email)
        #lonin_btn = self.driver.find_element("name", "btnLogin")
        #lonin_btn.click()
        time.sleep(3)
        
        password =  self.driver.find_element("name", "login-password")
        password.send_keys(my_password)

        time.sleep(3)
        #password_btn = self.driver.find_element("name", "btnEmailSelect")
        #password_btn.click()
        password.send_keys(Keys.ENTER)
        
        
    def add_basket(self, producturl):
        self.driver.get(producturl)
        time.sleep(4)
        add_btn = self.driver.find_element("xpath","/html/body/div[1]/div[5]/main/div/div[2]/div/div[2]/div[2]/div/div[1]/div[6]/button")
        add_btn.click()
        
    def go_basket(self):
        self.driver.get('https://www.trendyol.com/sepet')
        time.sleep(4)
        basket_btn = self.driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/aside/div/div[1]/a")
        basket_btn.click()
        
        
        
    def pyment(self):
        self.driver.get('https://www.trendyol.com/sepetim/odeme')
        apprv_btn = self.driver.find_element("xpath","/html/body/div[1]/div/div[1]/main/div[2]/aside/div/div[1]/button")
        apprv_btn.click()
        time.sleep(4)
        chexk_box = self.driver.find_element("xpath","/html/body/div[1]/div/div[1]/main/div[2]/aside/div/div[2]/section/div/label/span")
        chexk_box.click()
        time.sleep(2)
        cvv = self.driver.find_element("xpath","/html/body/div/div[2]/div[2]/div")
        cvv.send_keys('235')
        time.sleep(2)
        try:
            cart_number = self.driver.find_element("xpath","/html/body/div/div[1]/div[2]/input")
            cart_number.send_keys('1234567891111111')
        except:
            print ('ERROR')
 
        
if __name__ == "__main__":
    
    my_shop = AutomatedShopping()
    my_shop.sign_in()
    time.sleep(4)
    for i in range(2):
        my_shop.add_basket(product_list[i])
        time.sleep(4)
    
    my_shop.go_basket()
    time.sleep(4)
    my_shop.pyment()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    