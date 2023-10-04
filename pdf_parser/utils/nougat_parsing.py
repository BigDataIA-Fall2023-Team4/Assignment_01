import requests

def parse_pdf_with_nougat(file_address, api_address):
    url = api_address + "/predict/"
    payload = {}
    files=[
    ('file',('filefromweb.pdf',open(file_address,'rb'),'application/pdf'))
    ]

    headers = {}
    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        response.raise_for_status()
        content = response.text
        # print(type(content))
        # print(content)
        return content
        
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None
