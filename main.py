import email
from email import policy
from email.parser import BytesParser

# Numele fișierului cu e-mail-ul
nume_fisier_email = "C:\\Users\\User\\Email_verification\\email1.txt"

# Citirea textului e-mail-ului din fișier
with open(nume_fisier_email, 'r', encoding='utf-8') as file:
    email_text = file.read()

# Parsarea textului e-mail-ului
msg = BytesParser(policy=policy.default).parsebytes(email_text.encode('utf-8'))

# Extrage expeditorul (From) și subiectul (Subject)
expeditor = msg.get('From', 'N/A')
subiect = msg.get('Subject', 'N/A')

# Extrage conținutul mesajului
continut_mesaj = msg.get_body(preferencelist=('plain', 'html')).get_content()

# Găsește link-urile din conținutul mesajului
linkuri = []
for cuvant in continut_mesaj.split():
    if cuvant.startswith("http") or cuvant.startswith("www"):
        linkuri.append(cuvant)

# Afiseaza rezultatele
print(f"Expeditor: {expeditor}")
print(f"Subiect: {subiect}")
print(f"Link-uri: {linkuri}")
