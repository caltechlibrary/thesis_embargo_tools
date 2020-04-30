import email
import html
from html.parser import HTMLParser

class StripperHTMLParser (HTMLParser):
    _plain_text = []
    def handle_data(self, data):
        self._plain_text.append(html.unescape(data))
    def get_text(self):
        return ''.join(self._plain_text)

def strip_html_markup(src):
    stripper = StripperHTMLParser()
    stripper.reset()
    stripper.feed(src)
    return stripper.get_text()
    

def get_name_from_subject(src):
    if 'Embargo Request for ' in src: 
        [ junk, name ] = src.split('Embargo Request for ', 2)
        if (name != None) and (name != ''):
            return name
    return ''

def get_value(prefix, src, default):
    value = default
    if src.startswith(prefix):
        [ junk, value ] = src.split(': ', 2)
    return value.replace('<br />', '').replace('</p>', '')
     
def unwrap_lines(src):
    # NOTE: We need to join our lines that are forced wrapped at
    # column 80.
    lines = src.split('\n')
    n = []
    for line in lines:
        if line.endswith('='):
            line = f'{line[0:-1]}'
            n.append(line)
        else:
            n.append(line)
            n.append('\n')
    return ''.join(n).split('\n')

    

def get_object_from_payload(src):
    obj = {
        'embargo_reason': '',
        'requestor_name': '',
        'requestor_email': '',
        'thesis_author': '',
        'thesis_title': '',
        'grad_year': '',
        'advisor_name': '',
        'advisor_email': '',
        'division': '',
        'request': '',
    }
    lines = unwrap_lines(src)
    # iterate through the document and populate
    # our object.
    for i, line in enumerate(lines):
        if line.startswith('<p>Reason for Requesting Embargo: '):
            obj['embargo_reason'] = get_value('<p>Reason for Requesting Embargo: ', line, '')
        if line.startswith('Requestor Name: '):
            obj['requestor_name'] = get_value('Requestor Name: ', line, '')
        if line.startswith('Requestor Email: '):
            obj['requestor_email'] = get_value('Requestor Email: ', line, '')
        if line.startswith('Thesis Author: '):
            obj['thesis_author'] = get_value('Thesis Author: ', line, '')
        if line.startswith('Thesis Title: '):
            obj['thesis_title'] = get_value('Thesis Title: ', line, '')
        if line.startswith('Graduation Year: '):
            obj['grad_year'] = get_value('Graduation Year: ', line, None)
        if line.startswith('Advisor Name: '):
            obj['advisor_name'] = get_value('Advisor Name: ', line, '')
        if line.startswith('Advisor Email: '):
            obj['advisor_email'] = get_value('Advisor Email: ', line, '')
        if line.startswith('Division: '):
            obj['division'] = get_value('Division: ', line, '')
        if line.startswith('Request: '):
            obj['request'] = get_value('Request: ', line, '')
    return obj


def get_name_and_object(src):
    '''Take a str version of the EMail message, parse, return a touple of name and message'''
    msg = email.message_from_string(src)
    subject = msg.get('Subject')
    name = get_name_from_subject(subject)
    payload = msg.get_payload()
    if type(payload) is list:
        #Handle multiple payloads from outlook
        payload = payload[0].get_payload()
    obj = get_object_from_payload(payload)
    return name, obj


def process_email(filename):
    with open(filename) as f:
      raw_message = f.read()
    return get_name_and_object(raw_message)

