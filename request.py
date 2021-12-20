import requests

def sendImage(imgUrl:str) :
    test_file = open(f"{imgUrl}", "rb")
    test_url = "http://localhost:8000/uploadfile"

    headers = {
    'accept': 'application/json'
    }

    file_data=[
    ('file',('test2.png',test_file,'application/octet-stream'))
    ]

    test_response = requests.request("POST", test_url, headers=headers, files=file_data)

    if test_response.ok:
        print("Upload completed successfully!")
        print(test_response.text)
    else:
        print("Something went wrong!")

sendImage("Gun.jpg")