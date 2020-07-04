from find_element.capability import driver
#点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
#点击头像
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_usecheader').click()
#获取所有图片
images= driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
#选择第十个图片
images[10].click()
#点击保存
driver.find_element_by_id('com.tal.kaoyan:id/save').click()