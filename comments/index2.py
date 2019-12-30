import time,re,openpyxl
from time import gmtime, strftime
from selenium import webdriver



class Hack_nnu: 
    def __init__(self):
        self.date = None,
        self.last_time = None,
        self.request = None
    def run_program(self):
        chromedriver = 'C:/users/angular_nija_avenger/downloads/chromedriver'
        browser = webdriver.Chrome(chromedriver)
        self.set_time()
        self.set_date()
        self.run_script(browser)

    def set_time(self):
        file = open("c:/Users/angular_nija_avenger/Documents/Nnu_Project/comments/time.txt","r")
        store = file.read()
        self.last_time = store
        file.close()
    def update_time(self,time):
        file = open("c:/Users/angular_nija_avenger/Documents/Nnu_Project/comments/time.txt","w")
        file.write(time)
        file.close()
        print(time,"this is the time here")
    def set_date(self):
        file = open("c:/Users/angular_nija_avenger/Documents/Nnu_Project/comments/date.txt","r")
        store = file.read()
        file.close()
        date = strftime("%B %d, %Y,", gmtime())
        if not date == store:
            file = open("c:/Users/angular_nija_avenger/Documents/Nnu_Project/comments/date.txt","w")
            file.write(date)
            file.close()
            self.update_time("12:02 am")

    def run_script(self,browser):
        try:
            self.login(browser)
            if browser.current_url is not "https://nnu.ng/member/my-account":
                self.login(browser)
                self.go_to_home_page(browser)
                self.read_links(browser,self.get_post_url(browser))
        except:
            return
    def stoped_at(self):
        file = open("c:/Users/angular_nija_avenger/Documents/Nnu_Project/comments/stopped_at.txt","w")
        file.write(new_time)
        file.close()   
    def read_links(self,browser,data):
        counter = 0
        money = None
        new_time = self.last_time
        for i in range(len(data)):
            time_now = data[i][1]
            if i == 0:
                new_time = time_now
                self.request=time_now
            url = data[i][0]
            last_time = self.last_time
            time.sleep(4)
            browser.get(url)
            if len(time_now) == 7:
                x = time_now
                x = list(x)
                x.insert(0,"0")
                x = "".join(x)
                time_now = x
            if time_now == last_time:
                file = open("c:/Users/angular_nija_avenger/Documents/Nnu_Project/comments/time.txt","w")
                file.write("0"+ new_time)
                file.close()    
                browser.quit()
                break           
    def go_to_home_page(self,browser):
        browser.get('https://nnu.ng')
        time.sleep(5)
    def login(self,browser):
        browser.get('https://nnu.ng')
        try:
            time.sleep(6)
            email_field = browser.find_element_by_css_selector("#login-box > form > ul > li:nth-child(2) > input[type=text]")
            email_field.click()
            email_field.send_keys("eguaborbishop1@gmail.com")


            password_field = browser.find_element_by_css_selector("#login-box > form > ul > li:nth-child(3) > input")
            password_field.click()
            password_field.send_keys("Desto424")

            sbumit_field = browser.find_element_by_css_selector("#login-box > form > ul > li:nth-child(3) > button")
            sbumit_field.click()
            time.sleep(6)
        except:
            return
    def get_post_url(self,browser):
        txt = re.compile(r'<li class="yoda"><a href="(.*?)"><span class="time-posted">(.*?)</span>')
        x = txt.findall(browser.page_source,re.IGNORECASE)
        if x:
            return x
        else:
            return None
    def upadate_spread_sheet(self):
        self.check_for_current_date()
# print(Hack_nnu().run_program())