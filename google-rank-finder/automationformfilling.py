#pip install mechanize
import re
from mechanize import Browser

name="ratantata"
web="https://en.wikipedia.org/wiki/Ratan_Tata"
br = Browser()

# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a user-agent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

br.open("https://a-serchengine.herokuapp.com/form/").read().decode('UTF-8')
#br.select_form(ls_form='fb-init')
br.select_form(method='post')
br.form[ 'name' ] = name
br.form[ 'web' ] = web
br.submit()