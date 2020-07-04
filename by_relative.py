from capability import driver
#点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
#获取父节点
parent = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
#父节点下的第一个classname
parent.find_element_by_class_name('android.widget.ImageView').click()