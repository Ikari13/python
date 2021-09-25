import json
import requests
headers = {'Authorization':'Bearer ya29.a0ARrdaM-x4GDxbAE4x0tVGcgYZKCATVHiAxQl6D9RrrHVQ9wAYqRqEQGaIS8q5eEsX3wVD2PWpbnCRxYIx6t2dNxeGzr-Xt5JfwumwadPICe_jVr_PmUdFxHfW9CV_7qbQEi7gIeLjEHdh89srBZKO-P90BS0'}
param = {
    'name': 'MyImage',
    'parents':['1BfItZqDS_WDHCBP2zv5Uc6soh-MSliFW']
}


files = {
    'data': ('metadata', json.dumps(param), 'application/json; charset=UTF-8'),
    'file': ('application/jpg',open("C:/Users/jared/Desktop/Folders/python/01.jpg", "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)