import requests
import os

def download_gh(date, time):
    response = requests.get(f"https://data.gharchive.org/{date}-{time:02}.json.gz")
    if(response.status_code == 200):
        file_name = f"./downloads/{date}-{time:02}.json.gz"
        with open (file_name, 'wb') as file:
            file.write(response.content)
        return os.path.abspath(file_name)
    else:
        return None

#print(download_gh('2023-03-01','10'))

def test_download_gh():
    date, time = '2023-03-01', '10'
    file_return = download_gh('2023-03-01', '10')
    assert file_return is not None
    assert os.path.isfile(file_return)
    print('test successful')

test_download_gh()