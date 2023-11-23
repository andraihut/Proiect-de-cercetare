import unittest
import os
from main import extract_features_from_email
"""
Verifică dacă adresa de expeditor este corect extrasă și are o valoare nenulă.
Verifică dacă lista de link-uri este goală pentru un e-mail legitim.
Verifică dacă procesarea limbajului natural este corectă, comparând lista de cuvinte tokenizate cu o listă așteptată.
Verifică dacă nu există cereri de informații personale în e-mailul legitim
"""
class TestExtractFeatures(unittest.TestCase):
    def test_legitimate_email(self):
        file_path = 'C:\\Users\\User\\Email_verification\\data_set\\email1.txt'
        features = extract_features_from_email(file_path)

        # Aserțiuni pentru adresa de expediere
        self.assertIsNotNone(features['sender_address'])
        self.assertEqual(features['sender_address'], 'legitimate.sender@example.com')

        # Aserțiuni pentru legături și URL-uri
        self.assertEqual(len(features['links']), 0)

        # Aserțiuni pentru procesarea limbajului natural
        expected_word_tokens = ['monthly', 'newsletter', 'exciting', 'updates', 'news', 'best', 'regards', 'legitimate',
                                'sender']
        self.assertEqual(features['word_tokens'], expected_word_tokens)

        # Aserțiuni pentru cereri de informații personale
        self.assertFalse(features['personal_info_requests'])

    def test_phishing_email(self):
        file_path = 'C:\\Users\\User\\Email_verification\\data_set\\email2.txt'
        features = extract_features_from_email(file_path)

        # Aserțiuni pentru adresa de expediere
        self.assertIsNotNone(features['sender_address'])
        self.assertEqual(features['sender_address'], 'legitimate.sender@example.com')

        # Aserțiuni pentru legături și URL-uri
        self.assertEqual(len(features['links']), 0)

        # Aserțiuni pentru procesarea limbajului natural
        expected_word_tokens = ['monthly', 'newsletter', 'exciting', 'updates', 'news', 'best', 'regards', 'legitimate',
                                'sender']
        self.assertEqual(features['word_tokens'], expected_word_tokens)

        # Aserțiuni pentru cereri de informații personale
        self.assertFalse(features['personal_info_requests'])


if __name__ == '__main__':
    unittest.main()
