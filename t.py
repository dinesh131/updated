import os
import saythanks

is_test_run = 'TEST' in os.environ

if __name__ == '__main__' and not is_test_run:
#    saythanks.app.run(ssl_context='adhoc')
	saythanks.app.run(port = 5000, host='saythanks.kgisl.com')
