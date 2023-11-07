from selenium import webdriver
import requests
import time
import bs4

username = '' #input your facebook username here
password ='' # input your password here
userID= 'ravi.uma.54379236'


webpage= webdriver.chrome()
webpage.get('https://web.facebook.com')
email= webpage.find_element(by="id",value="email") 
passcode= webpage.find_element(by="id",value="pass")
email.send_keys(username)
passcode.send_keys(password)
webpage.find_element(by="name",value="login").click()

time.sleep(10)

#webpage.get(f"https://mbasic.facebook.com/{userID}")
#pageContentt= webpage.page_source
#soup = bs4.BeautifulSoup(pageContentt, 'html.parser')

webpage.get(f"https://mbasic.facebook.com/{userID}")
pageContent= webpage.page_source
soup = bs4.BeautifulSoup(pageContent, 'html.parser')

image_element = soup.find_all('img')
image= image_element[2]
url = image['src']

time.sleep(3)

picture= requests.get(url)

if picture.status_code == 200:
    with open('profile_picture.jpg','wb') as p:
        p.write(picture.content)
        print('Profile picture has been saved')
else:
    print('Profile picture could not be saved')

webpage.quit()


