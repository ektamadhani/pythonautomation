from selenium import webdriver
def WaitForElement(self,locator,locatortype="id",timeout=10,pollfrequency=0.5):
    element=None
    try:
        bytype=self.getBytype(locatortype)
        wait=webdriverwait(self.driver,timeout,pollfrequency)
        element=wait.until(Ec.element_to_be_clickable(bytype,locator))
    except:
        print("got into expectations")
    return element


