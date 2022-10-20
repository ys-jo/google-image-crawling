from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By

"""
download chromedriver.exe
https://chromedriver.chromium.org/downloads
"""


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_img(name):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
    elem = driver.find_element("name", "q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    dir = "./results" + "\\" + name

    createDirectory(dir)
    count = 1
    print(f"total image num: {len(imgs)}")
    for img in imgs:
        print(img)
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute(
                "src")
            path = dir + "\\" + name + "_"
            urllib.request.urlretrieve(imgUrl, path + str(count) + ".jpg")
            count = count + 1
            if count >= 260:
                break
            print(f"download img: {count}")
        except:
            print("Error in Src code!")

    driver.close()
    print("Done")


if __name__ == "__main__":
    searchs = ["chair"]
    for search in searchs:
        crawling_img(search)