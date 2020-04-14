import email
import html
from html.parser import HTMLParser

class StripperHTMLParser (HTMLParser):
    cdata = []
    def handle_data(self, data):
        self.cdata.append(html.unescape(data))
    def get_text(self):
        return ''.join(self.cdata)

def strip_html_markup(src):
    stripper = StripperHTMLParser()
    stripper.feed(src)
    return stripper.get_text()
    

def get_name_from_subject(src):
    [ _, name ] = src.split('Embargo Request for ')
    if (name != None) and (name != ''):
        return name
    return ''

def get_value(prefix, src, default):
    value = default
    if src.startswith(prefix):
        [ _, value ] = src.split(': ')
    return value
     

def get_object_from_payload(src):
    obj = {
        'embargo_reason': '',
        'requestor_name': '',
        'requestor_email': '',
        'thesis_author': '',
        'thesis_title': '',
        'grad_year': None,
        'advisor_name': '',
        'advisor_email': '',
        'division': '',
        'request': '',
    }
    for i, line in enumerate(strip_html_markup(src).split('\n')):
        if line.startswith('Reason for Requesting Embargo: '):
            obj['embargo_reason'] = get_value('Reason for Requesting Embargo: ', line, '')
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
    payload = msg.get_payload()
    name = get_name_from_subject(subject)
    obj = get_object_from_payload(payload)
    return name, obj


def process_email(filename):
    with open(filename) as f:
      raw_message = f.read()
    return get_name_and_object(raw_message)

