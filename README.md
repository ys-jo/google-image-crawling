# google-image-crawling

### How to use 
1. download chromedriver.exe  
   https://chromedriver.chromium.org/downloads
2. modify code in main.py
```python
driver = webdriver.Chrome('./chromedriver.exe') #Modify the downloaded chromedriver path

dir = "./results" + "\\" + name #Modify result folder path

if count >= 260: # Edit as many images as user wants
    break

searchs = ["chairs"] # edit to the word user wants
```
3. execute main.py