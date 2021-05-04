from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('http://site.fibaorganizer.com/armfed/league/34175/')

mad_standings = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table')
sleep(1)

finaly_parse = mad_standings.text





