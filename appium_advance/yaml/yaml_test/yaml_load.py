import yaml

file=open('familyInfo.yaml')
data=yaml.load(file)

print(data)

print(data['spouse'])

print(data['children'][1]['name'])

data['children'][1]['name'] = 'Sunly'
print(data['children'][1]['name'])
print('-----')
#将python数据类型转化为yaml数据类型
slogan = ['welcome','to','51zxw']
website = {'url':'www.51zxw.com'}

print(slogan)
print(website)
print('======')
print(yaml.dump(slogan))
print(yaml.dump(website))