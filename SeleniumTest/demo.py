#循环搜索字段
selectModel = driver.find_element_by_css_selector("ul[role = 'listbox']")
allOption = selectModel.find_elements_by_tag_name("li")
for option in allOption:
    #name是想要查找的名字，可以在方法里面传值
    if name in option.text:
        option.click()
        break