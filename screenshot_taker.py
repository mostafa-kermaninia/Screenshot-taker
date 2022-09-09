from selenium import webdriver
from io import BytesIO
from PIL import Image
from selenium.webdriver.common.by import By


#input informations
website_link = input('give me the link:')
element = input("give me the element's full xpath")


#introduce the chrome driver
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path = 'chromedriver.exe' , options = options)
driver.get(website_link)
driver.maximize_window()


#full screenshot
S = lambda X : driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width') , S('Height'))
driver.find_element(By.TAG_NAME , 'body').screenshot('fullscreenshot.png')


##table screenshot
#1-find the table element location
element = driver.find_element(By.XPATH , element) 
location = element.location
size = element.size
png = driver.get_screenshot_as_png()
driver.quit()


#2-crop and save the table's pic
im = Image.open(BytesIO(png))

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left , top , right , bottom))
im.save('elementscreenshot.png')
#:)