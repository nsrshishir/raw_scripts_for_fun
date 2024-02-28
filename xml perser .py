import base64
import logging
from urllib.parse import urlencode

from hashlib import md5
from werkzeug import urls
import re
import xml.etree.ElementTree as et


xml = '<error xmlns="https://secure.paymarkclick.co.nz/api/" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><errormessage>Authentication error. Username, AccountId and/or Password are incorrect</errormessage><errornumber>3000</errornumber><errortype>AUTHENTICATION</errortype></error>'


def click_xml_parser(xml_string):

    xml_string = re.sub(' xmlns="[^"]+"', '', xml_string, count=1)
    if et.fromstring(xml_string).tag != 'error':
        return {'click_form_url': et.fromstring(xml_string).text}
    else:
        return{
            'error': {
                'errornumber': et.fromstring(xml_string).find('errornumber').text,
                'errortype': et.fromstring(xml_string).find('errortype').text,
                'errormessage': et.fromstring(xml_string).find('errormessage').text,
            }
        }


print(click_xml_parser(xml))