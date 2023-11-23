import email
import re
import urllib.parse
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from email.parser import BytesParser

def extract_features_from_email(file_path):
    with open(file_path, 'r') as file:
        email_content = file.read()

    features = {}

    # Analiză adresa de expediere
    msg = BytesParser().parsebytes(email_content.encode('utf-8'))
    sender_address = msg.get('From') or msg.get('Sender')
    features['sender_address'] = sender_address

    # Analiză legături și URL-uri
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                       email_content)
    parsed_links = [urllib.parse.urlparse(link) for link in links]
    features['links'] = parsed_links

    # Procesare limbaj natural (simplificat)
    words = word_tokenize(email_content)
    words = [word.lower() for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    features['word_tokens'] = words

    # Verificare cereri de informații personale
    personal_info_keywords = ['password', 'credit card', 'social security']
    features['personal_info_requests'] = any(keyword in email_content.lower() for keyword in personal_info_keywords)

    return features

file_path = '/data_set/email2.txt'
email_features = extract_features_from_email(file_path)
print(email_features)

