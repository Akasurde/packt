"""
Program to download free ebook from Packtpub site
"""

import ConfigParser
import os
import re
import requests
import const
from lib import info, debug, sysexit


def parser_cfg():
    """
    Helper function to parser configuration file
    """
    config_file = "packt_config.ini"
    config_path = os.path.join(os.path.expanduser('~'), config_file)
    config = ConfigParser.ConfigParser()
    if not os.path.exists(config_path):
        info("Trying local configuration file")
        config_path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(config_path):
            sysexit("Unable to find configuration file {0}".format(config_path))

    if const.DEBUG:
        debug("Using configuration file from {0}".format(config_path))

    config.read(config_path)
    return dict(config.items('packt'))


def main():
    """ Main function """

    cfg = parser_cfg()
    const.LOGIN_DATA['email'] = cfg['username']
    const.LOGIN_DATA['password'] = cfg['password']
    # Start Requests session
    session = requests.Session()
    session.headers.update(const.HEADERS)
    info("Login into [{0}]".format(const.BASE_URL))
    session.post(const.BASE_URL, data=const.LOGIN_DATA)
    info("Looking for new ebook [{0}]".format(const.LOOKUP_URL))
    lookup = session.get(const.LOOKUP_URL)
    claim_url = ""
    for line in lookup.iter_lines():
        match_obj = re.match(r'.*(freelearning-claim/[0-9]+/[0-9]+)', line)
        if match_obj:
            claim_url = const.BASE_URL + "/" + match_obj.group(1)
            break

    info("Claiming ebook from [{0}]".format(claim_url))
    session.get(claim_url)
    book_code = claim_url.split("/")[-2]
    download_url = const.BASE_URL + "/ebook_download/" + book_code + "/pdf"
    info("Downloading ebook from [{0}]".format(download_url))
    download_ebook = session.get(download_url)
    with open("{0}.pdf".format(book_code), "wb") as pdfile:
        pdfile.write(download_ebook.content)
    sysexit("Done", color='green')

if __name__ == "__main__":
    main()
