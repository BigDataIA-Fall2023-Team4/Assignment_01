import requests
import spacy

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
    
def text_summarize(text):
    try:
        # Load the English language model
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        sentence_scores = {}
        for sentence in doc.sents:
            sentence_scores[sentence] = len(sentence)
        
        # Seting 10% of the original text to retain in the summary
        desired_percentage = 10

        # Calculate the number of sentences to include in the summary
        total_sentences = list(doc.sents)
        N = int(len(total_sentences) * (desired_percentage / 100))

        # Ensure N is at least 1 to avoid an empty summary
        N = max(1, N)

        summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:N]
        summary = " ".join(str(sentence) for sentence in summary_sentences)

        return summary
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    

