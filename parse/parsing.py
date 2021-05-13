from selenium import webdriver
from time import sleep

# It is for windows
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('parse/chromedriver.exe', options=options)
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

reg_list = [[n1.text, reg_team1.text, reg_team1_wl.text, reg_team1_point.text],
            [n2.text, reg_team2.text, reg_team2_wl.text, reg_team2_point.text],
            [n3.text, reg_team3.text, reg_team3_wl.text, reg_team3_point.text],
            [n4.text, reg_team4.text, reg_team4_wl.text, reg_team4_point.text],
            [n5.text, reg_team5.text, reg_team5_wl.text, reg_team5_point.text],
            [n6.text, reg_team6.text, reg_team6_wl.text, reg_team6_point.text],
            [n7.text, reg_team7.text, reg_team7_wl.text, reg_team7_point.text],
            [n8.text, reg_team8.text, reg_team8_wl.text, reg_team8_point.text]]

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

sem_list = [[n1.text, sem_team1.text, sem_team1_wl.text, sem_team1_point.text],
            [n2.text, sem_team2.text, sem_team2_wl.text, sem_team2_point.text],
            [n3.text, sem_team3.text, sem_team3_wl.text, sem_team3_point.text],
            [n4.text, sem_team4.text, sem_team4_wl.text, sem_team4_point.text],
            [n5.text, sem_team5.text, sem_team5_wl.text, sem_team5_point.text],
            [n6.text, sem_team6.text, sem_team6_wl.text, sem_team6_point.text],
            [n7.text, sem_team7.text, sem_team7_wl.text, sem_team7_point.text],
            [n8.text, sem_team8.text, sem_team8_wl.text, sem_team8_point.text]]

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

vb_list = [[vb_n1.text, vb_team1.text, vb_team1_games.text, vb_team1_total.text],
           [vb_n2.text, vb_team2.text, vb_team2_games.text, vb_team2_total.text],
           [vb_n3.text, vb_team3.text, vb_team3_games.text, vb_team3_total.text],
           [vb_n4.text, vb_team4.text, vb_team4_games.text, vb_team4_total.text],
           [vb_n5.text, vb_team5.text, vb_team5_games.text, vb_team5_total.text],
           [vb_n6.text, vb_team6.text, vb_team6_games.text, vb_team6_total.text],
           [vb_n7.text, vb_team7.text, vb_team7_games.text, vb_team7_total.text],
           [vb_n8.text, vb_team8.text, vb_team8_games.text, vb_team8_total.text]]

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

mad_pl = [[pl_1.text, pl_1_games.text, pl_1_min.text, pl_1_total.text, pl_1_permin.text, pl_1_perg.text],
          [pl_2.text, pl_2_games.text, pl_2_min.text, pl_2_total.text, pl_2_permin.text, pl_2_perg.text],
          [pl_3.text, pl_3_games.text, pl_3_min.text, pl_3_total.text, pl_3_permin.text, pl_3_perg.text],
          [pl_4.text, pl_4_games.text, pl_4_min.text, pl_4_total.text, pl_4_permin.text, pl_4_perg.text],
          [pl_5.text, pl_5_games.text, pl_5_min.text, pl_5_total.text, pl_5_permin.text, pl_5_perg.text],
          [pl_6.text, pl_6_games.text, pl_6_min.text, pl_6_total.text, pl_6_permin.text, pl_6_perg.text],
          [pl_7.text, pl_7_games.text, pl_7_min.text, pl_7_total.text, pl_7_permin.text, pl_7_perg.text],
          [pl_8.text, pl_8_games.text, pl_8_min.text, pl_8_total.text, pl_8_permin.text, pl_8_perg.text],
          [pl_9.text, pl_9_games.text, pl_9_min.text, pl_9_total.text, pl_9_permin.text, pl_9_perg.text],
          [pl_10.text, pl_10_games.text, pl_10_min.text, pl_10_total.text, pl_10_permin.text, pl_10_perg.text],
          [pl_11.text, pl_11_games.text, pl_11_min.text, pl_11_total.text, pl_11_permin.text, pl_11_perg.text]]

# Les Vbet Women's Regular

driver.get('http://site.fibaorganizer.com/armfed/league/41501/')

wm_n1 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[1]')
wm_team1 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[2]')
wm_team1_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[3]')
wm_team1_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[3]/td[4]')

wm_n2 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[1]')
wm_team2 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[2]')
wm_team2_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[3]')
wm_team2_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[4]/td[4]')

wm_n3 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[1]')
wm_team3 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[2]')
wm_team3_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[3]')
wm_team3_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[5]/td[4]')

wm_n4 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[1]')
wm_team4 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[2]')
wm_team4_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[3]')
wm_team4_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[6]/td[4]')

wm_n5 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[1]')
wm_team5 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[2]')
wm_team5_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[3]')
wm_team5_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[7]/td[4]')

wm_n6 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[1]')
wm_team6 = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[2]')
wm_team6_wl = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[3]')
wm_team6_point = driver.find_element_by_xpath('//*[@id="283-300-standings-container"]/table/tbody/tr[8]/td[4]')

wom_list = [[wm_n1, wm_team1, wm_team1_wl, wm_team1_point], [wm_n2, wm_team2, wm_team2_wl, wm_team2_point],
            [wm_n3, wm_team3, wm_team3_wl, wm_team3_point], [wm_n4, wm_team4, wm_team4_wl, wm_team4_point],
            [wm_n5, wm_team5, wm_team5_wl, wm_team5_point], [wm_n6, wm_team6, wm_team6_wl, wm_team6_point], ]
# Les Foxes Players

driver.get('http://site.fibaorganizer.com/armfed/41501/team/4725329/#mbt:283-200$t&0=7')

les_pl_1 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[2]')
les_pl_1_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[3]')
les_pl_1_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[4]')
les_pl_1_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[5]')
les_pl_1_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[6]')
les_pl_1_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[2]/td[7]')

les_pl_2 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[2]')
les_pl_2_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[3]')
les_pl_2_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[4]')
les_pl_2_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[5]')
les_pl_2_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[6]')
les_pl_2_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[3]/td[7]')

les_pl_3 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[2]')
les_pl_3_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[3]')
les_pl_3_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[4]')
les_pl_3_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[5]')
les_pl_3_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[6]')
les_pl_3_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[4]/td[7]')

les_pl_4 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[2]')
les_pl_4_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[3]')
les_pl_4_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[4]')
les_pl_4_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[5]')
les_pl_4_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[6]')
les_pl_4_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[5]/td[7]')

les_pl_5 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[2]')
les_pl_5_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[3]')
les_pl_5_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[4]')
les_pl_5_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[5]')
les_pl_5_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[6]')
les_pl_5_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[6]/td[7]')

les_pl_6 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[2]')
les_pl_6_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[3]')
les_pl_6_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[4]')
les_pl_6_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[5]')
les_pl_6_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[6]')
les_pl_6_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[7]/td[7]')

les_pl_7 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[2]')
les_pl_7_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[3]')
les_pl_7_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[4]')
les_pl_7_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[5]')
les_pl_7_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[6]')
les_pl_7_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[8]/td[7]')

les_pl_8 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[2]')
les_pl_8_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[3]')
les_pl_8_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[4]')
les_pl_8_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[5]')
les_pl_8_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[6]')
les_pl_8_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[9]/td[7]')

les_pl_9 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[2]')
les_pl_9_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[3]')
les_pl_9_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[4]')
les_pl_9_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[5]')
les_pl_9_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[6]')
les_pl_9_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[10]/td[7]')

les_pl_10 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[2]')
les_pl_10_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[3]')
les_pl_10_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[4]')
les_pl_10_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[5]')
les_pl_10_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[6]')
les_pl_10_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[11]/td[7]')

les_pl_11 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[2]')
les_pl_11_games = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[3]')
les_pl_11_min = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[4]')
les_pl_11_total = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[5]')
les_pl_11_permin = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[6]')
les_pl_11_perg = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[12]/td[7]')

les_pl = [[les_pl_1.text, les_pl_1_games.text, les_pl_1_min.text, les_pl_1_total.text, les_pl_1_permin.text,
           les_pl_1_perg.text],
          [les_pl_2.text, les_pl_2_games.text, les_pl_2_min.text, les_pl_2_total.text, les_pl_2_permin.text,
           les_pl_2_perg.text],
          [les_pl_3.text, les_pl_3_games.text, les_pl_3_min.text, les_pl_3_total.text, les_pl_3_permin.text,
           les_pl_3_perg.text],
          [les_pl_4.text, les_pl_4_games.text, les_pl_4_min.text, les_pl_4_total.text, les_pl_4_permin.text,
           les_pl_4_perg.text],
          [les_pl_5.text, les_pl_5_games.text, les_pl_5_min.text, les_pl_5_total.text, les_pl_5_permin.text,
           les_pl_5_perg.text],
          [les_pl_6.text, les_pl_6_games.text, les_pl_6_min.text, les_pl_6_total.text, les_pl_6_permin.text,
           les_pl_6_perg.text],
          [les_pl_7.text, les_pl_7_games.text, les_pl_7_min.text, les_pl_7_total.text, les_pl_7_permin.text,
           les_pl_7_perg.text],
          [les_pl_8.text, les_pl_8_games.text, les_pl_8_min.text, les_pl_8_total.text, les_pl_8_permin.text,
           les_pl_8_perg.text],
          [les_pl_9.text, les_pl_9_games.text, les_pl_9_min.text, les_pl_9_total.text, les_pl_9_permin.text,
           les_pl_9_perg.text],
          [les_pl_10.text, les_pl_10_games.text, les_pl_10_min.text, les_pl_10_total.text, les_pl_10_permin.text,
           les_pl_10_perg.text],
          [les_pl_11.text, les_pl_11_games.text, les_pl_11_min.text, les_pl_11_total.text, les_pl_11_permin.text,
           les_pl_11_perg.text]]

# Mad team leaders

driver.get('http://site.fibaorganizer.com/armfed/34175/team/4730677/')

m_scorer = driver.find_element_by_xpath(
    '/html/body/div[5]/div/div[1]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a')
m_scorer_point = driver.find_element_by_xpath(
    '//*[@id="283-200-tab-container"]/div/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/span/strong')

m_rebounder = driver.find_element_by_xpath(
    '/html/body/div[5]/div/div[1]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/table/tbody/tr[4]/td[2]/a')
m_rebounder_point = driver.find_element_by_xpath(
    '//*[@id="283-200-tab-container"]/div/div[3]/div/div[2]/table/tbody/tr[4]/td[3]/span/strong')

m_assister = driver.find_element_by_xpath(
    '/html/body/div[5]/div/div[1]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/table/tbody/tr[6]/td[2]/a')
m_assister_point = driver.find_element_by_xpath(
    '//*[@id="283-200-tab-container"]/div/div[3]/div/div[2]/table/tbody/tr[6]/td[3]/span/strong')

mad_top = [m_scorer, m_scorer_point, m_rebounder, m_rebounder_point, m_assister, m_assister_point]

# Les team leaders

driver.get('http://site.fibaorganizer.com/armfed/41501/team/4725329/')

l_scorer = driver.find_element_by_xpath(
    '/html/body/div[5]/div/div[1]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/a')
l_scorer_point = driver.find_element_by_xpath(
    '//*[@id="283-200-tab-container"]/div/div[3]/div/div[2]/table/tbody/tr[2]/td[3]/span/strong')

l_rebounder = driver.find_element_by_xpath(
    '/html/body/div[5]/div/div[1]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/table/tbody/tr[4]/td[2]/a')
l_rebounder_point = driver.find_element_by_xpath(
    '//*[@id="283-200-tab-container"]/div/div[3]/div/div[2]/table/tbody/tr[4]/td[3]/span/strong')

l_assister = driver.find_element_by_xpath(
    '/html/body/div[5]/div/div[1]/div/div/div/div/div/div[3]/div/div[3]/div/div[2]/table/tbody/tr[6]/td[2]/a')
l_assister_point = driver.find_element_by_xpath(
    '//*[@id="283-200-tab-container"]/div/div[3]/div/div[2]/table/tbody/tr[6]/td[3]/span/strong')

les_top = [l_scorer, l_scorer_point, l_rebounder, l_rebounder_point, l_assister, l_assister_point]

driver.get('http://site.fibaorganizer.com/armfed/41501/team/4725329/#mbt:283-200$t&0=1')

# Les Last Game
les_last_date = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[1]')
les_last_t1 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[2]')
les_last_t2 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[3]')
les_last_score = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[4]')
les_last_place = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[5]')

les_last_list = [les_last_date, les_last_t1, les_last_t2, les_last_score, les_last_place]

driver.get('http://site.fibaorganizer.com/armfed/34175/team/4730677/#mbt:283-200$t&0=1')
# Mad Last Game
mad_last_date = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[1]')
mad_last_t1 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[2]')
mad_last_t2 = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[3]')
mad_last_score = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[4]')
mad_last_place = driver.find_element_by_xpath('//*[@id="283-200-tab-container"]/div/table/tbody/tr[1]/td[5]')

mad_last_list = [mad_last_date, mad_last_t1, mad_last_t2, mad_last_score, mad_last_place]
