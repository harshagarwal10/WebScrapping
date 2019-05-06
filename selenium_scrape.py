from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import time
from bs4 import BeautifulSoup

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

    
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://techolution.app.param.ai/jobs/')


with open('Jobs.csv', mode='w') as jobs_file:
    jobs_writer = csv.writer(jobs_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    jobs_writer.writerow(["name", "Job-type", "location", "experience", "time posted"])

    # browser.get("https://techolution.app.param.ai/jobs/")

    timeout = 5
    # print(browser.page_source)
    print("===============")

    # find_elements_by_xpath returns an array of selenium objects.
    time.sleep(3)

    # Parse HTML, close browser
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print(soup)
    job_lists = soup.find_all('div', class_="job_list_card")

    list = []
    for job in job_lists:
        for child in job.children:
            child1 = child.children
            name = ""
            tpe = ""
            location = ""
            experience = ""
            tme = ""
            for l, ch in enumerate(child1):
                
                try:
                    if l==0:
                        for i,ch2 in enumerate(ch.children):
                            
                            
                            if i==0 :
                                name = ch2.getText().strip()
                                # print(ch2.getText())
                            elif i==2:
                                for k,ch3 in enumerate(ch2):
                                    if k==0:
                                        tpe = ch3.getText().replace("·", "").strip()
                                        # print(tpe)
                                    elif k==2:
                                        location = ch3.getText().replace("·", "").strip()
                                        # print(location)
                                    if k==4:
                                        experience = ch3.getText().replace("·", "").strip()
                                        # print(experience)
                                    # else:
                                        # print(k, ch3)
                        
                    else: 
                        tme = ch.getText()

                except : 
                    pass
            print("name= "+name,"type= "+tpe, "loca= "+ location,"exp= "+    experience, "time = "+ tme)
            jobs_writer.writerow([name, tpe, location, experience, tme])    
        # child2 = child1.children[0]
        # for childs in child2.children:
        #     print(childs)
        print("=========")    
    # use list comprehension to get the actual repo titles and not the selenium objects.

    list.sort()
    for i in range(len(list)):
        print(list[i].name)
    browser.quit()



