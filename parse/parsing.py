from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('parse/chromedriver.exe')
driver.get('http://site.fibaorganizer.com/armfed/league/34175/')


# REGULAR TABLE ELEMENTS
n1 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[1]')
reg_team1 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[2]')
reg_team1_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[3]')
reg_team1_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[4]')

n2 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[1]')
reg_team2 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[2]')
reg_team2_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[3]')
reg_team2_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[4]')

n3 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[1]')
reg_team3 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[2]')
reg_team3_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[3]')
reg_team3_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[4]')

n4 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[1]')
reg_team4 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[2]')
reg_team4_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[3]')
reg_team4_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[4]')

n5 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[1]')
reg_team5 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[2]')
reg_team5_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[3]')
reg_team5_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[4]')

n6 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[1]')
reg_team6 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[2]')
reg_team6_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[3]')
reg_team6_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[4]')

n7 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[9]/td[1]')
reg_team7 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[9]/td[2]')
reg_team7_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[9]/td[3]')
reg_team7_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[9]/td[4]')

n8 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[10]/td[1]')
reg_team8 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[10]/td[2]')
reg_team8_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[10]/td[3]')
reg_team8_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[10]/td[4]')

reg_list = [[n1.text,reg_team1.text,reg_team1_wl.text,reg_team1_point.text],[n2.text,reg_team2.text,reg_team2_wl.text,reg_team2_point.text],[n3.text,reg_team3.text,reg_team3_wl.text,reg_team3_point.text],[n4.text,reg_team4.text,reg_team4_wl.text,reg_team4_point.text],[n5.text,reg_team5.text,reg_team5_wl.text,reg_team5_point.text],[n6.text,reg_team6.text,reg_team6_wl.text,reg_team6_point.text],[n7.text,reg_team7.text,reg_team7_wl.text,reg_team7_point.text],[n8.text,reg_team8.text,reg_team8_wl.text,reg_team8_point.text]]

# SEMIFINAL TABLE ELEMENTS
sem_team1 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[13]/td[2]')
sem_team1_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[13]/td[3]')
sem_team1_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[13]/td[4]')

sem_team2 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[14]/td[2]')
sem_team2_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[14]/td[3]')
sem_team2_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[14]/td[4]')

sem_team3 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[15]/td[2]')
sem_team3_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[15]/td[3]')
sem_team3_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[15]/td[4]')

sem_team4 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[16]/td[2]')
sem_team4_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[16]/td[3]')
sem_team4_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[16]/td[4]')

sem_team5 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[17]/td[2]')
sem_team5_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[17]/td[3]')
sem_team5_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[17]/td[4]')

sem_team6 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[18]/td[2]')
sem_team6_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[18]/td[3]')
sem_team6_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[18]/td[4]')

sem_team7 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[19]/td[2]')
sem_team7_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[19]/td[3]')
sem_team7_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[19]/td[4]')

sem_team8 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[20]/td[2]')
sem_team8_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[20]/td[3]')
sem_team8_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[20]/td[4]')

sem_list = [[n1.text,sem_team1.text,sem_team1_wl.text,sem_team1_point.text],[n2.text,sem_team2.text,sem_team2_wl.text,sem_team2_point.text],[n3.text,sem_team3.text,sem_team3_wl.text,sem_team3_point.text],[n4.text,sem_team4.text,sem_team4_wl.text,sem_team4_point.text],[n5.text,sem_team5.text,sem_team5_wl.text,sem_team5_point.text],[n6.text,sem_team6.text,sem_team6_wl.text,sem_team6_point.text],[n7.text,sem_team7.text,sem_team7_wl.text,sem_team7_point.text],[n8.text,sem_team8.text,sem_team8_wl.text,sem_team8_point.text]]




