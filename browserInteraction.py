from selenium import webdriver
import time
class Browser:
    driver=None
    @staticmethod
    def launchChrome(self):
        global driver
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
        time.sleep(3)
        return driver
    def maximizeBrowser(self):
        print("Maximize the browser window")
        driver.maximize_window()
    def enterURL(self):
        print("Enter URL to load")
        driver.get("https://learn.letskodeit.com/p/practice")
    def getTitle(self):
        print("Title is "+str(driver.title))
        print("Curremt URL is :"+str(driver.current_url))
    def reloadPage(self):
        print("Page refresh")
        driver.refresh()
        time.sleep(1)
        print("Page refresh alternate way")
        driver.get(driver.current_url)
        time.sleep(1)
    def clickElement(self):
        headers=driver.find_elements_by_xpath("//table[@id='product']//following-sibling::th")
        for i in range(len(headers)):
            print(headers[i].text,end="  ")
        print()
        rowvalues=driver.find_elements_by_xpath("//table[@id='product']//parent::tr//following-sibling::tr//td")
        for i in range(len(rowvalues)):
            print(rowvalues[i].text,end="  ")
            i=i+1
        print()
    def getOtherDetails(self):
        driver.get("https://www.google.com/")
        print("Curremt URL is :"+str(driver.current_url))
        time.sleep(1)
        print("Go one step back in the browser window")
        driver.back()
        time.sleep(1)
        print("Curremt URL is :"+str(driver.current_url))
        driver.forward()
        print("Go one step forward in the browser window")
        time.sleep(1)
        print("Curremt URL is :"+str(driver.current_url))
        #print(driver.page_source)
    def closeTheBrowser(self):
        print("Close the current window")
        driver.close()
        print("Quits the browser")
        driver.quit()
# br=Browser()
# br.launchChrome("")
# br.maximizeBrowser()
# br.enterURL()
# br.getTitle()
# br.reloadPage()
# br.clickElement()
# br.getOtherDetails()
# br.closeTheBrowser()
