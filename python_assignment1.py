import requests
import json

response1 = requests.get('https://raw.githubusercontent.com/bhargav-velisetti/flink_examples/master/data/cruise_ship_schema.json')

if(response1.status_code == 200):
    json_content1 = response1.json()
    print('Answer for 1st question')
    crew = json_content1.get('crew', False)
    if crew:
        print(crew)
    else:
        print('Not Found')

response2 = requests.get('https://raw.githubusercontent.com/bhargav-velisetti/apache_beam_examples_java/master/data/sample-data.json')

if(response2.status_code == 200):
    json_content2 = response2.text
    print('Answer for 2nd question')
    json_content2 = json_content2.strip().split('\n')
    for item in json_content2:
        json_data = json.loads(item)
        for key, value in json_data.items():
            if key == 'firstName':
                print(key,value)

list_a = [0,1,2,3,4,5,6]
print('Answers 3, 4 and 5')
print(list_a[4])
print(list_a[-3:])
print(len(list_a))

dict_a = {'a':1,'b':2}
print('Answers 6, 7 and 8')
print(dict_a.keys())
print(dict_a.values())
print(dict_a.get('b', 'Not Found'))
