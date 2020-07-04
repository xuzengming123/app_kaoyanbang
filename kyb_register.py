from capability import driver
import random
#进入注册界面并选择设置头像
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
# #点击头像
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_usecheader').click()
# #获取所有图片
# images= driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
# #选择第十个图片
# images[10].click()
# #点击保存
# driver.find_element_by_id('com.tal.kaoyan:id/save').click()

#注册信息填写
username = 'zxw2018' + 'FLY' + str(random.randint(1000,9000))
print('username: %s'%username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

password = 'zxw' + str(random.randint(10000000,90000000))
print('password: %s'%password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

email = '51xzw' + str(random.randint(1000,9000)) + '@163.com'
print('email: %s'%email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

#院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
#选择省份
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
#选择具体院校--同济大学
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()


#专业选择
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
#选择经济学类-统计学-经济统计学
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()

#点击进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()