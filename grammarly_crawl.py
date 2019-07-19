from selenium import webdriver
from time import sleep
import os
import logging
from selenium.webdriver.common.keys import Keys

"""
Grammaly는 문법 교정 사이트 입니다.
본 소스코드는 총 2가지 역할로 사용하실 수 있습니다.
1. Grammaly 자동화 테스트기능
2. Grammaly 예문 크롤링 기능


Grammaly is a Grammar Error Correction System.
This source code can be used in two roles in total.
1. Grammaly automated test
2. Grammaly crawler
"""

##############################################################################################
#본인의 Grammaly ID와 비밀번호를 입력해주세요.
#Please Write your Grammaly ID and PW
ID="YOUR_ID"
PW="YOUR_PW"

#크롬드라이버를 OS에 맞게 설치한 후 경로를 입력해주세요.
# chrome driver PATH 
#Please Install the chromedriver.exe  / Check your Chrome Version.
driver_path = r'/home/chanjun/Desktop/Grammarly_Crawl/chromedriver'
##############################################################################################


# log
log = logging.getLogger('log_grammaly')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='weblio_log', filemode='w')


#grammaly url
url = 'https://www.grammarly.com/signin?allowUtmParams=true'

# driver Option
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36")


driver = webdriver.Chrome(driver_path)

driver.implicitly_wait(10)


# Login by gmail
def login_google(email, password):
    try:
        driver.get(url)
        window_before = driver.window_handles[0] # grammarly window
        google_login_button = driver.find_element_by_class_name('_1ycFJ-_-_-_-_-_-client-components-new_funnel-social_signup-google--google-googleButton') # google 로그인버튼
        sleep(5)
        driver.execute_script("arguments[0].click();", google_login_button) # click the google login. Oauth2
        window_after = driver.window_handles[1] # google login window
        driver.switch_to.window(window_after) # change the window google login to grammaly
        sleep(5)
        driver.find_element_by_name('identifier').send_keys(email + Keys.ENTER) # ID 
        sleep(5)
        driver.find_element_by_name('password').send_keys(password + Keys.ENTER) # PW 
        driver.switch_to.window(window_before) # change the window google login to grammaly
        sleep(5)
        new_file_botton = driver.find_element_by_class_name('_758e07ad-document_item-add') # Insert the sentence
        driver.execute_script("arguments[0].click();", new_file_botton) # click the button
        sleep(5)
        f=open('test.txt','r',encoding='utf-8') #test file
        line=f.read() 
        sentence = line
        driver.find_element_by_xpath('//div[@class="_9c5f1d66-denali-editor-editor ql-editor ql-blank"]').send_keys(sentence) # Insert sentence
        sleep(5)
        wrongs = driver.find_elements_by_xpath('//div[@class="_c265ffae-typography-base _89c0e071-base-contentWrapper"]') 
        #tag_words = driver.find_elements_by_xpath('//span[@data-mark-id]') #error list
        #for i in range(len(tag_words)):
        #    tag_word = tag_words[i].text # error word
        #    tag = '[{0}]'.format(i+1) # number tag
        #    sentence_list = sentence.split('\n') 
        #    tag_sentence = sentence_list[i].replace(tag_word, tag + tag_word) # tag + sentence
        #    with open('tag_sentence.txt', 'a+', encoding='utf-8') as ts_f: # write the file
        #        ts_f.write(tag_sentence + '\n')
        sleep(5)

        for i,wrong in enumerate(wrongs):
            wrong.click() # click the error button
            content = driver.find_element_by_xpath('//div[@class="_c265ffae-typography-base _090fff83-full-shortDescription _6c1eef76-full-description"]').text
            button = driver.find_element_by_xpath('//div[@class="_6a9d14b7-replacements_labels-itemInsert _d6699f4b-replacements_labels-item _c9042367-button-button"]') # 수정할 부분 버튼
            driver.execute_script("arguments[0].click();", button) # edit button
            new_sen = driver.find_element_by_xpath('//div[@class="_9c5f1d66-denali-editor-editor ql-editor"]').text # edit sentence
            sleep(5)
            with open('tag.txt', 'a+', encoding='utf-8') as f_w2:  # write the file
                f_w2.write('[{0}]'.format(i+1) + content +'\n')
        with open('result.txt', 'a+', encoding='utf-8') as f_w: # write the file
            f_w.write(new_sen)
            sleep(5)
    except Exception as e:
        print(e)
    finally:
        f.close()
        driver.close()
        driver.quit()
        #sys.exit()

# Login by email
def login_ect(email, password):
    try:
        driver.get(url)
        sleep(3)
        driver.find_element_by_xpath('//input[@type="email"]').send_keys(email) 
        sleep(5)
        driver.find_element_by_xpath('//input[@type="password"]').send_keys(password + Keys.ENTER) 
        sleep(10)
        new_file_botton = driver.find_element_by_class_name('_758e07ad-document_item-add') 
        driver.execute_script("arguments[0].click();", new_file_botton) 
        sleep(10)
        f=open('test.txt','r',encoding='utf-8') # Check the PATH
        line=f.read() 
        sentence = line.strip()
        driver.find_element_by_xpath('//div[@class="_9c5f1d66-denali-editor-editor ql-editor ql-blank"]').send_keys(sentence) 
        sleep(10)
        wrongs = driver.find_elements_by_xpath('//div[@class="_c265ffae-typography-base _89c0e071-base-contentWrapper"]') 
        #tag_words = driver.find_elements_by_xpath('//span[@data-mark-id]')
        #for i in range(len(tag_words)):
        #    tag_word = tag_words[i].text 
        #    tag = '[{0}]'.format(i+1) 
        ##    sentence_list = sentence.split('\n') 
        #    tag_sentence = sentence_list[i].replace(tag_word, tag + tag_word) 
        #    with open('tag_sentence.txt', 'a+', encoding='utf-8') as ts_f:
        #        ts_f.write(tag_sentence + '\n')
        sleep(10)
        for wrong in wrongs:
            wrong.click() 
            button = driver.find_element_by_xpath('//div[@class="_6a9d14b7-replacements_labels-itemInsert _d6699f4b-replacements_labels-item _c9042367-button-button"]') # 수정할 부분 버튼
            driver.execute_script("arguments[0].click();", button) 
            new_sen = driver.find_element_by_xpath('//div[@class="_9c5f1d66-denali-editor-editor ql-editor"]').text 
            sleep(3)
            with open('result.txt', 'w', encoding='utf-8') as f_w: 
                f_w.write(new_sen)
            sleep(5)
    except Exception as e:
        print(e)
        pass
    finally:
        f.close()
        driver.close()
        driver.quit()
        #sys.exit()

def main(email, password):
    if '@gmail.com' in email:
        login_google(email, password)
        print('done')
    else:
        login_ect(email, password)
        print('done')


if __name__ == "__main__":
    email = ID
    password = PW
    main(email, password)



