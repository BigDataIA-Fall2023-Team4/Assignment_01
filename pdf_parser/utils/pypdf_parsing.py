from pypdf import PdfReader
import requests

def download_pdf_from_url(url, local_filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(local_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return local_filename

def parse_pdf_with_pypdf(local_filename):
    reader = PdfReader(local_filename)
    number_of_pages = len(reader.pages)
    text = ''
    for i in range (number_of_pages):
        page = reader.pages[i]
        text = text + page.extract_text()
    return text, number_of_pages


# https://www.sec.gov/files/exam-brochure.pdf

# https://www.sec.gov/files/form1.pdf
