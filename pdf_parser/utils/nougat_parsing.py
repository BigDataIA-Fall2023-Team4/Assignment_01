import requests

def parse_pdf_with_nougat(file_address, api_address):
    url = api_address + "/predict/"
    payload = {}
    pdf_response = requests.get(file_address)
    if pdf_response.status_code != 200:
            print(f"Failed to download PDF from {file_address}. Status code: {pdf_response.status_code}")
            return None
    
     # Extract the PDF content
    pdf_content = pdf_response.content

    files=[
    ('file',('filefromweb.pdf',pdf_content,'application/pdf'))
    ]
    
    headers = {}
    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        response.raise_for_status()
        content = response.text
        return content
        
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None
