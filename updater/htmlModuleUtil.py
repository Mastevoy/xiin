
__version__     = '2011.07.10-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from HTMLParser import HTMLParser

class HtmlModuleUtil(HTMLParser):
# http://stackoverflow.com/questions/1699634/how-to-retrieve-a-directory-of-files-from-a-remote-server
    """
    Custom/extended HTMLParser.
    """

    remoteList = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    ext = value.split('.')[1]
                    if ext == 'py' and value not in '__init__.py':
                        self.remoteList.append(value)
    #end

    def get_list(self):
        """
        Returns the server list of files.
        """
        return self.remoteList

#end