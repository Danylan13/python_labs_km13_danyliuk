import json

with open("image_info_test2017/image_info_test2017.json") as f:
    data = json.load(f)
print('Кількість фотографій, інформацію про які можна знайти у цьому файлі :', len(data['images']))
print('Кількість категорій у файлі :', len(data['categories']))

print("Посилання на фотографію '000000000001.jpg' :")
for i in data['images']:
    if i['file_name'] == '000000000001.jpg':
        print("Url :", i['coco_url'])
        print("Height :", i['height'])
        print("Width :", i['width'])
        print("Id :", i['id'])