
from selenium import webdriver
import os

# below command Provide current working directory path which we can see top of PyCharm editor
dir = os.path.dirname(__file__)
print(dir)

IE_driver_path = dir + "\IEDriverServer.exe"
chrome_driver_path = dir + "\chromedriver.exe"

# Create a new IE/Crome/Firefox driver instant
# Ie and chrome driver instant can be done at any of two ways mention below

# first method
#driver = webdriver.Ie("C:\\Users\\pratik.t.patel\\PycharmProjects\\unittest\\Practice\\IEDriverServer.exe")
#driver = webdriver.Chrome("C:\\Users\\pratik.t.patel\\PycharmProjects\\unittest\\Practice\\chromedriver.exe")

# Second Method
#driver = webdriver.Ie(IE_driver_path)
#driver = webdriver.Chrome(chrome_driver_path)

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to application Url
driver.get("https://www.amazon.in/")

# Find Search box on webapp, do data entry and sumbit that dta using submit() method
driver.find_element_by_id("twotabsearchtextbox").clear()
driver.find_element_by_id("twotabsearchtextbox").send_keys("phones")
driver.find_element_by_id("twotabsearchtextbox").submit()
#driver.find_element_by_id("nav-search-submit-text").click()

#Find element by link tesxt and click on it
#elem = driver.find_element_by_link_text("Xiaomi Redmi Note Prime (White, 16 GB)").click()
elem = driver.find_element_by_id("s-results-list-atf")
elem1 = list();
elem1 = elem.find_elements_by_tag_name("h2")

for ele in elem1:
   print (ele.text)




#numbers = [0,10]
#for number in numbers:
#xpath ="//*[@id="result_+"number"]/div/div/div/div[2]/div[2]/a/h2"
#temp ="//*[@id="result_"+str(number)+"]/div/div/div/div[2]/div[2]/a/h2"
#xpath ="//*[@id="result_"+number+"]/div/div/div/div[2]/div[2]/a/h2"


