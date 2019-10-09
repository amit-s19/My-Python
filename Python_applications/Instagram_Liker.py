from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def CloseSession(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        username_field = driver.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        password_field = driver.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_picture(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        # searching for all the pictures within the scroll limit
        links = driver.find_elements_by_tag_name('a')
        picture_links = [elem.get_attribute('href') for elem in links]
        picture_links = [elem for elem in picture_links if '/p/' in elem]
        print(hashtag + ' Pictures : ' + str(len(picture_links)))
        for href in picture_links:
            driver.get(href)
            try:
                like = driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                time.sleep(5)
            except Exception as e:
                time.sleep(2)



#Test = InstagramBot('__i.am.666__', 'blade dl1ch8686')
#Test.login()
#hashtags = ['fitness', 'gym']
#for elem in hashtags :
#    Test.like_picture(elem)


print(''' INSTAGRAM BOT ''')
Username = str(raw_input('Enter the username : '))
Password = str(raw_input('Enter the password : '))
print(''' What do you want to do?
          1. Like posts
          2. Comment on posts
          3. Follow Unfollow
          ''')
Valid_inputs= [1, 2, 3]

choice = input('Enter your choice : ')
if choice not in Valid_inputs :
    print("Not a valid choice!")
else :
    User = InstagramBot(Username, Password)
    User.login()
    if choice == 1:
        Hashtags = []
        print("Enter the hashtags(press 0 to stop) :")
        while(True):
            hashtag = raw_input()
            if hashtag == '0' :
                break
            else :
                Hashtags.append(hashtag)

        for elem in Hashtags:
            print("Liking pictures in hashtag {}........ ".format(elem))
            User.like_picture(elem)
