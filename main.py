from fileinput import close
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def make_int(str):
    str = str.strip()
    str = str.replace(',', '')
    str = int(str)

    return str


while True:

    file = open('price_name.txt', 'a')


    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://www.amazon.in/Lenovo-Windows-Graphics-Phantom-82B500BHIN/dp/B08GG8WCW7/ref=sr_1_4?keywords=legion+5&qid=1653715608&sprefix=legio%2Caps%2C723&sr=8-4'
    
    

    try:
        driver.get(url)
        driver.implicitly_wait(10)

        product_title = driver.find_element_by_id('productTitle')
        product_price = driver.find_element_by_xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')

        #printing the price and name on terminal
        print(product_title.text)
        print(product_price.text)
        name = product_title.text
        price = (product_price.text)
        make_int(price)



        #Taking output from the file for previous price
        with open('price_name.txt') as f:
            lines = f.readlines()
            print(lines)

        previous_price = lines[1]

        make_int(previous_price)


        print(previous_price)

        #Writing in the file the price of product
        if price < previous_price:
            file.close()
            file = open('price_name.txt','w')
            file.write(name)
            file.write('\n')
            file.write(price)
            file.write('\n')
            print('file written')
            file.close()

    finally:
        time.sleep(5)
        driver.close()
        time.sleep(15*60)


