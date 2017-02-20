"""Constants """

DEBUG = True
BASE_URL = 'https://www.packtpub.com'
LOOKUP_URL = BASE_URL + '/packt/offers/free-learning'
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36',
           'Accept': 'text/html'}

LOGIN_DATA = {
    'op': 'Login',
    'form_build_id': 'form-73ba86bbfb2a50719049129632c84810 ',
    'form_token': '2f1d586bf7df196b77d0761709d03199',
    'form_id': 'packt_user_login_form'
}
