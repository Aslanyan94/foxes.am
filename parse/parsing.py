from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
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

driver.get('http://site.fibaorganizer.com/armfed/league/37669/teams-statistics/')
# VBET ARMENIAN CUP

vb_n1 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[2]/td[1]')
vb_team1 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[2]/td[2]')
vb_team1_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[2]/td[3]')
vb_team1_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[2]/td[4]')

vb_n2 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[3]/td[1]')
vb_team2 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[3]/td[2]')
vb_team2_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[3]/td[3]')
vb_team2_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[3]/td[4]')

vb_n3 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[4]/td[1]')
vb_team3 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[4]/td[2]')
vb_team3_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[4]/td[3]')
vb_team3_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[4]/td[4]')

vb_n4 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[5]/td[1]')
vb_team4 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[5]/td[2]')
vb_team4_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[5]/td[3]')
vb_team4_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[5]/td[4]')

vb_n5 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[6]/td[1]')
vb_team5 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[6]/td[2]')
vb_team5_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[6]/td[3]')
vb_team5_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[6]/td[4]')

vb_n6 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[7]/td[1]')
vb_team6 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[7]/td[2]')
vb_team6_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[7]/td[3]')
vb_team6_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[7]/td[4]')

vb_n7 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[8]/td[1]')
vb_team7 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[8]/td[2]')
vb_team7_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[8]/td[3]')
vb_team7_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[8]/td[4]')

vb_n8 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[9]/td[1]')
vb_team8 = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[9]/td[2]')
vb_team8_games = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[9]/td[3]')
vb_team8_total = driver.find_element_by_xpath('//*[@id="283-601-tab-container"]/div[4]/div[2]/table/tbody/tr[9]/td[4]')

vb_list = [[vb_n1.text,vb_team1.text,vb_team1_games.text,vb_team1_total.text],[vb_n2.text,vb_team2.text,vb_team2_games.text,vb_team2_total.text],[vb_n3.text,vb_team3.text,vb_team3_games.text,vb_team3_total.text],[vb_n4.text,vb_team4.text,vb_team4_games.text,vb_team4_total.text],[vb_n5.text,vb_team5.text,vb_team5_games.text,vb_team5_total.text],[vb_n6.text,vb_team6.text,vb_team6_games.text,vb_team6_total.text],[vb_n7.text,vb_team7.text,vb_team7_games.text,vb_team7_total.text],[vb_n8.text,vb_team8.text,vb_team8_games.text,vb_team8_total.text]]

# Mad Players

driver.get('http://site.fibaorganizer.com/armfed/37669/team/4730677/#mbt:283-200$t&0=7')

pl_1 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[2]')
pl_1_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[3]')
pl_1_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[4]')
pl_1_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[5]')
pl_1_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[6]')
pl_1_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[7]')

pl_2 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[2]')
pl_2_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[3]')
pl_2_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[4]')
pl_2_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[5]')
pl_2_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[6]')
pl_2_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[7]')

pl_3 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[2]')
pl_3_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[3]')
pl_3_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[4]')
pl_3_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[5]')
pl_3_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[6]')
pl_3_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[7]')

pl_4 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[2]')
pl_4_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[3]')
pl_4_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[4]')
pl_4_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[5]')
pl_4_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[6]')
pl_4_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[7]')

pl_5 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[2]')
pl_5_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[3]')
pl_5_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[4]')
pl_5_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[5]')
pl_5_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[6]')
pl_5_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[7]')

pl_6 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[2]')
pl_6_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[3]')
pl_6_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[4]')
pl_6_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[5]')
pl_6_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[6]')
pl_6_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[7]')

pl_7 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[2]')
pl_7_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[3]')
pl_7_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[4]')
pl_7_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[5]')
pl_7_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[6]')
pl_7_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[7]')

pl_8 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[2]')
pl_8_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[3]')
pl_8_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[4]')
pl_8_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[5]')
pl_8_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[6]')
pl_8_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[7]')

pl_9 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[2]')
pl_9_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[3]')
pl_9_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[4]')
pl_9_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[5]')
pl_9_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[6]')
pl_9_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[7]')

pl_10 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[2]')
pl_10_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[3]')
pl_10_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[4]')
pl_10_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[5]')
pl_10_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[6]')
pl_10_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[7]')

pl_11 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[2]')
pl_11_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[3]')
pl_11_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[4]')
pl_11_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[5]')
pl_11_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[6]')
pl_11_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[7]')

driver.get('http://site.fibaorganizer.com/armfed/37669/team/4730677/#mbt:283-200$t&0=2')

pl1_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[3]')
pl1_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[4]')
pl1_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[6]')

pl2_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[3]')
pl2_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[4]')
pl2_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[6]')

pl3_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[4]/td[3]')
pl3_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[4]/td[4]')
pl3_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[4]/td[6]')

pl4_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[5]/td[3]')
pl4_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[5]/td[4]')
pl4_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[5]/td[6]')

pl5_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[6]/td[3]')
pl5_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[6]/td[4]')
pl5_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[6]/td[6]')

pl6_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[7]/td[3]')
pl6_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[7]/td[4]')
pl6_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[7]/td[6]')

pl7_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[8]/td[3]')
pl7_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[8]/td[4]')
pl7_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[8]/td[6]')

pl8_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[9]/td[3]')
pl8_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[9]/td[4]')
pl8_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[9]/td[6]')

pl9_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[10]/td[3]')
pl9_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[10]/td[4]')
pl9_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[10]/td[6]')

pl10_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[11]/td[3]')
pl10_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[11]/td[4]')
pl10_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[11]/td[6]')

pl11_position = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[12]/td[3]')
pl11_height = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[12]/td[4]')
pl11_birth = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/div[1]/div/div[2]/table/tbody/tr[12]/td[6]')

mad_pl = [[pl_1.text,pl1_position.text,pl_1_games.text,pl_1_min.text,pl_1_total.text,pl_1_permin.text,pl_1_perg.text],[pl_2.text,pl2_position.text,pl_2_games.text,pl_2_min.text,pl_2_total.text,pl_2_permin.text,pl_2_perg.text],[pl_3.text,pl3_position.text,pl_3_games.text,pl_3_min.text,pl_3_total.text,pl_3_permin.text,pl_3_perg.text],[pl_4.text,pl4_position.text,pl_4_games.text,pl_4_min.text,pl_4_total.text,pl_4_permin.text,pl_4_perg.text],[pl_5.text,pl5_position.text,pl_5_games.text,pl_5_min.text,pl_5_total.text,pl_5_permin.text,pl_5_perg.text],[pl_6.text,pl6_position.text,pl_6_games.text,pl_6_min.text,pl_6_total.text,pl_6_permin.text,pl_6_perg.text],[pl_7.text,pl7_position.text,pl_7_games.text,pl_7_min.text,pl_7_total.text,pl_7_permin.text,pl_7_perg.text],[pl_8.text,pl8_position.text,pl_8_games.text,pl_8_min.text,pl_8_total.text,pl_8_permin.text,pl_8_perg.text],[pl_9.text,pl9_position.text,pl_9_games.text,pl_9_min.text,pl_9_total.text,pl_9_permin.text,pl_9_perg.text],[pl_10.text,pl10_position.text,pl_10_games.text,pl_10_min.text,pl_10_total.text,pl_10_permin.text,pl_10_perg.text],[pl_11.text,pl11_position.text,pl_11_games.text,pl_11_min.text,pl_11_total.text,pl_11_permin.text,pl_11_perg.text]]