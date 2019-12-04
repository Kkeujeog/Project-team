########구글 이미지 수집 코드###############
################20191202################

import time
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#거미
#집에거미
#spider
url = 'https://www.google.com/search?q=%EC%8C%80%EB%B0%94%EA%B5%AC%EB%AF%B8&tbm=isch&ved=2ahUKEwiY_YTQr5jmAhVVFIgKHWtXC9QQ2-cCegQIABAA&oq=%EC%8C%80%EB%B0%94%EA%B5%AC%EB%AF%B8&gs_l=img.3..0j0i24l6.13106.14029..14171...0.0..0.131.1288.6j6......0....1..gws-wiz-img.......0i131.ahLWu_PzjEk&ei=VcDlXdh-1aigBOuuraAN&bih=916&biw=944&rlz=1C1OKWM_koKR853KR854'
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.get(url)

for i in range(10):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)
    if i == 3:
        driver.find_element_by_xpath('//*[@id="smb"]').click()
        driver.implicitly_wait(3)
#
html = driver.page_source  
soup = BeautifulSoup(html, 'html.parser')

params = []
imglist = soup.find_all("img", class_="rg_ic rg_i") # class는 검색어마다 변경해주어야합니다. 

count = 1
for i in imglist:
    try:
        print(i['src'])
        print(count)
        params.append(i['src'])
        count += 1

    except:
        print(i['data-src'])
        print(count)
        params.append(i['data-src'])
        count += 1

len(params) # 최대 877개 수집 확인

'''
imglist[20]
count = 20
for i in imglist[20:len(imglist)]:
    print(i['data-src'])
    print(count)
    count += 1
    #params.append(i['data-iurl'])
#params
#len(params)
    
imglist[100]
count = 100
for i in imglist[100:len(imglist)]:
    print(i['src'])
    print(count)
    count += 1
    
    
imglist[120]
count = 120
for i in imglist[120:len(imglist)]:
    print(i['data-src'])
    print(count)
    count += 1

imglist[224]
count = 200
for i in imglist[200:len(imglist)]:
    print(i['src'])
    print(count)
    count += 1
'''

x = 1
for p in params:
    req.urlretrieve(p, "c:/sample/ant/"+str(x)+".jpg")
    x += 1

driver.quit()

######################다음##################################
import time # sleep 메소드 사용하려궁
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
    # '바퀴벌레' 검색 하기
url = 'https://search.naver.com/search.naver?where=image'
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.get(url) 
e = driver.find_element_by_id("nx_query")   #1
e.send_keys("바퀴벌레") # 검색어 입력 됨버
e.submit()  # 검색 (enter)

    # 스크래핑 4번하기(마우스를 내리는 행위)
for i in range(1,7):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)
    
driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[8]/a').click()
driver.implicitly_wait(3)
 

    # 웹페이지 내용 저장
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
#soup

params = [] # 이미지 url저장
imglist = soup.find_all("img",class_="_img")
for i in imglist:
    params.append(i['src'])
len(params)
    
    # pc로 이미지 저장
# import urllib.request as req
x = 1
for p in params:
    req.urlretrieve(p,"c:/sample/"+str(x)+".jpg")
    x += 1
driver.quit()

url = "https://search.daum.net/search?w=img"
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.get(url)
e = driver.find_element_by_id("q")
#e.clear()
e.send_keys("집게벌레") #검색창에 입력
e.submit()      #검색

for i in range(1,50):
    driver.find_element_by_tag_name('body').send_keys(Keys.END) 
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="imgColl"]/div[5]/a[1]').click()
    driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup

params = []
imglst = soup.find_all("img", class_="thumb_img")

for i in imglst:
    params.append(i['src'])
params

#c드라이브에 이미지 따와서 sample폴더 만들기
x = 1
for p in params:
    req.urlretrieve(p, "c:/data/project/"+str(x)+".jpg")
    x += 1

driver.quit()

##########################네이버#################################
import time # sleep 메소드 사용하려궁
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
    # '바퀴벌레' 검색 하기
url = 'https://search.naver.com/search.naver?where=image'
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.get(url) 
e = driver.find_element_by_id("nx_query")   #1
e.send_keys("애집개미") # 검색어 입력 됨
e.submit()  # 검색 (enter)
e.clear()
    # 스크래핑 4번하기(마우스를 내리는 행위)
for i in range(1,7):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)
    
driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[8]/a').click()
driver.implicitly_wait(3)
 

    # 웹페이지 내용 저장0
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
#soup

params = [] # 이미지 url저장
imglist = soup.find_all("img",class_="_img")
for i in imglist:
    params.append(i['src'])
len(params)
    
    # pc로 이미지 저장
# import urllib.request as req
x = 723
for p in params:
    req.urlretrieve(p,"c:/sample/ant/"+str(x)+".jpg")
    x += 1
driver.quit()