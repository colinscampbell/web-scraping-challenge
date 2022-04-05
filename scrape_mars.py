from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    scraped_data = {}

    browser.visit('https://redplanetscience.com/')
    soup1 = BeautifulSoup(browser.html, 'html.parser')

    browser.visit('https://spaceimages-mars.com')
    soup2 = BeautifulSoup(browser.html, 'html.parser')

    browser.visit('https://galaxyfacts-mars.com')
    soup3 = BeautifulSoup(browser.html, 'html.parser')

    browser.visit('https://marshemispheres.com/schiaparelli.html')
    soup4 = BeautifulSoup(browser.html, 'html.parser')

    browser.visit('https://marshemispheres.com/syrtis.html')
    soup5 = BeautifulSoup(browser.html, 'html.parser')

    browser.visit('https://marshemispheres.com/valles.html')
    soup6 = BeautifulSoup(browser.html, 'html.parser')

    browser.visit('https://marshemispheres.com/cerberus.html')
    soup7 = BeautifulSoup(browser.html, 'html.parser')

    browser.quit()

    titles = soup1.find_all('div', class_='content_title')
    articles = soup1.find_all('div', class_='article_teaser_body')

    imgurl = soup2.find_all('a', class_='showimg fancybox-thumbs')

    table_data = soup3.find_all('tbody')

    hemispheretext1 = soup4.find_all('h2', class_='title')[0].text
    hemisphereimage1 = soup4.find_all('img', class_="wide-image")

    hemispheretext2 = soup5.find_all('h2', class_='title')[0].text
    hemisphereimage2 = soup5.find_all('img', class_="wide-image")

    hemispheretext3 = soup6.find_all('h2', class_='title')[0].text
    hemisphereimage3 = soup6.find_all('img', class_="wide-image")

    hemispheretext4 = soup7.find_all('h2', class_='title')[0].text
    hemisphereimage4 = soup7.find_all('img', class_="wide-image")

    title_array = []
    text_array = []
    large_image = 'https://spaceimages-mars.com/' + imgurl[0]['href']
    table_array = table_data[0]

    for title in titles:
        title_array.append(title.text)

    for text in articles:
        text_array.append(text.text)

    hemispheres_array = []

    dict = {
        "title" : hemispheretext1,
        "img_url" : "https://marshemispheres.com/" + hemisphereimage1[0]['src']
    }
    hemispheres_array.append(dict)

    dict = {
        "title" : hemispheretext2,
        "img_url" : "https://marshemispheres.com/" + hemisphereimage2[0]['src']
    }
    hemispheres_array.append(dict)

    dict = {
        "title" : hemispheretext3,
        "img_url" : "https://marshemispheres.com/" + hemisphereimage3[0]['src']
    }
    hemispheres_array.append(dict)

    dict = {
        "title" : hemispheretext4,
        "img_url" : "https://marshemispheres.com/" + hemisphereimage4[0]['src']
    }
    hemispheres_array.append(dict)


    scraped_data["article_title"] = title_array
    scraped_data["article_text"] = text_array
    scraped_data["large_image"] = large_image
    scraped_data["data_table"] = table_array
    scraped_data["hemisphere_data"] = hemispheres_array

    # Quit the browser
    browser.quit()

    return scraped_data