#!c:\users\a\apoorva\ngo_website\virtual\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyngrok==5.1.0','console_scripts','pyngrok'
__requires__ = 'pyngrok==5.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyngrok==5.1.0', 'console_scripts', 'pyngrok')()
    )
