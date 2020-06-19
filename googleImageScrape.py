from selenium import webdriver

# This is the input for your search term
searchterm = input('What are you searching for? ')
searchurl = 'urls_' + searchterm + '.txt'

# Modify path to chromedriver
browser = webdriver.Chrome('{/your_path_to}/chromedriver')

url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser.get(url)
extensions = { "jpg", "jpeg", "png", "gif" }

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

html = browser.page_source.split('["')
imges = []
for i in html:
    if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
        imges.append(i.split('"')[0])

with open(searchurl, 'w') as f:
    for item in imges:
        f.write(item + '\n')
        print(item +  " | added succesfully")

print('Done!')
browser.quit()
