import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def run():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  driver.get("https://comic.naver.com/webtoon")
  sleep(5)

  days = driver.find_elements(by=By.CSS_SELECTOR,
                              value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a')
  for day in days[1:8]:
    driver.execute_script("arguments[0].scrollIntoView(true);", day)
    day.click()

    print(day.text)

  webtoonTitles = driver.find_elements(by=By.CSS_SELECTOR,
                                        value='#content > div:nth-child(1) > ul > li > div > a > span')
  for webtoonTitle in webtoonTitles:
    print(webtoonTitle.text)


def run2():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  driver.get("https://comic.naver.com/webtoon")
  sleep(5)

  days = driver.find_elements(by=By.CSS_SELECTOR,
                              value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a')
  for day in days[1:8]:
    driver.execute_script("arguments[0].scrollIntoView(true);", day)
    day.click()
    print(day.text)
    newWebtoon = driver.find_elements(by=By.CSS_SELECTOR,
                                      value='#container > div.ListSpot__spot_wrap--Iko15 > div.content > div > ul > li > div > a > span')
    for new in newWebtoon:
      print(new.text)


def run3():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://kr.stussy.com/collections/new-arrivals")
  driver.maximize_window()
  sleep(1)

  categories = driver.find_elements(by=By.CSS_SELECTOR, value='#dropdown-menu-1-shop > div > ul > li > a')

  for i in range(len(categories)):
    categories = driver.find_elements(by=By.CSS_SELECTOR, value='#dropdown-menu-1-shop > div > ul > li > a')
    print(f'카테고리: {categories[i].text}')

    driver.execute_script("arguments[0].scrollIntoView(true);", categories[i])
    driver.execute_script("arguments[0].click();", categories[i])
    sleep(0.1)

    items = driver.find_elements(
      by=By.CSS_SELECTOR,
      value='#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li'
    )
    for item in items[:4]:
      itemImg = item.find_element(by=By.CSS_SELECTOR, value='div > a > div > img')
      itemImgSrc = itemImg.get_attribute('src')
      itemName = item.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-of-type(1)')
      nameText = itemName.text
      itemPrice = item.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-of-type(2)')
      priceText = itemPrice.text
      print(f'상품명: {nameText}, 가격: {priceText}, URL: {itemImgSrc}')


def run4():
  products = []

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  driver.get("https://kr.stussy.com/collections/new-arrivals")
  driver.maximize_window()
  sleep(1)

  categoryies = driver.find_elements(
    by=By.CSS_SELECTOR,
    value='#dropdown-menu-1-shop > div > ul > li > a'
  )

  for i in range(len(categoryies)):
    categoryies = driver.find_elements(
      by=By.CSS_SELECTOR,
      value='#dropdown-menu-1-shop > div > ul > li > a'
    )
    categoryName = categoryies[i].text
    print(f"카테고리: {categoryName}")

    categoryDict = {
      "categoryName": categoryName,
      "productList": []
    }

    driver.execute_script("arguments[0].scrollIntoView(true);", categoryies[i])
    driver.execute_script("arguments[0].click();", categoryies[i])
    sleep(0.1)

    productLis = driver.find_elements(
      by=By.CSS_SELECTOR,
      value='#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li'
    )
    # #'#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li:nth-child(4) > div > div'
    for productLi in productLis[:4]:
      productImg = productLi.find_element(by=By.CSS_SELECTOR, value='div > a > div > img')
      productImgSrc = productImg.get_attribute('src')
      productName = productLi.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-of-type(1)')
      productNameText = productName.text
      productPrice = productLi.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-of-type(2)')
      productPriceText = productPrice.text
      print(f'상품명: {productNameText}, 가격: {productPriceText}, url: {productImgSrc}')
      categoryDict["productList"].append({
        "productName": productNameText,
        "productPrice": productPriceText,
        "productImgSrc": productImgSrc,
      })

    products.append(categoryDict)
  with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)