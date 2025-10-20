import imaplib
import email
import urllib
import urllib.parse
import quopri

from bs4 import BeautifulSoup


class EmailManager:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def connect_to_mail(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self.email, self.password)
        mail.select('inbox')
        return mail

    @staticmethod
    def extract_links_from_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href:  # check if href exists
                try:
                    decoded_href = urllib.parse.unquote(href)  # URL decode first
                    decoded_href = quopri.decodestring(decoded_href.encode()).decode('utf-8',errors='ignore')  # Decode quoted-printable
                    if "unsubscribe" in decoded_href.lower():
                        links.append(href)  # append original url to not break the link
                except (UnicodeDecodeError, AttributeError, TypeError):
                    pass
        return links

    def search_for_email(self):
        mail = self.connect_to_mail()
        _, search_data = mail.search(None, '(BODY "unsubscribe")')
        data = search_data[0].split()

        links = []

        for num in data:
            _, data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/html':
                        html_content = part.get_payload(decode=True).decode('iso-8859-1')
                        links.extend(self.extract_links_from_html(html_content))
            else:
                content_type = msg.get_content_type()
                content = msg.get_payload(decode=True).decode('iso-8859-1')
                if content_type == 'text/html':
                    links.extend(self.extract_links_from_html(content))

        mail.logout()
        return links

    @staticmethod
    def save_links(new_links):
        with open('links.txt', 'w') as f:
            f.write('\n'.join(new_links))
