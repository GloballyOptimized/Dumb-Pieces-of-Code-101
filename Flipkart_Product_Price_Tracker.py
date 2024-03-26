from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pywhatkit

# Make sure you have whatsapp web logged in .........

driver = webdriver.Chrome()

#.......................................................................................................................
product_link = ''                        #enter product's absolute URL 
search_interval = 300                    #enter search interval between 2 search cycles for price  
total_search_period = 3000               #enter total search time
target_price = 999                       #enter the price you wanna buy the product 
alert_message_number = 7000580565        #enter your number to send whatsapp alert 
price_dropped = False                    #variable to makesure if the price has dropped 
price_html_element = ''                  #enter class name for price element on webpage 
#.......................................................................................................................

total_searchs = int(total_search_period/search_interval)

while total_searchs > 0:

    product = driver.get(product_link)
    price_element = driver.find_element(By.CLASS_NAME,price_html_element)
    current_price = price_element.text

    if target_price <= current_price:  # Alert message when price dropped below target level 
        pywhatkit.sendwhatmsg_instantly(alert_message_number,f'Congratulations the price of your product has dropped below target level ,click here to buy now : {product_link}')
        price_dropped = True
        
    time.sleep(search_interval)

    total_searchs -= 1

#..............................................................................................................................................................................................

if price_dropped == True:  # Alert message when price hasnt dropped 
    pywhatkit.sendwhatmsg_instantly(alert_message_number,f'The search cycle is over and the price hasnt dropped to target level , still wanna buy click here : {product_link}')

#..............................................................................................................................................................................................
