import re

class twitterClean(object):
    """docstring for twitterClean"""
    def __init__(self):
        super(twitterClean, self).__init__()
        
    def renameUser(corpus):
            _new = []      
            for _temp in corpus:
                _temp =  re.sub( r'(^|[^@\w])@(\w{1,15})\b','',_temp)
                _new.append(_temp)

            return _new

    def removeHashtag(corpus):
        _new = []
        for _temp in corpus:
            _temp = re.sub(r'#(\w+)', '', _temp)
            _new.append(_temp)

        return _new

    def removeURL(corpus):
        _new = []
        for _temp in corpus:
            _temp = re.sub(r'http:\S+', '', _temp, flags=re.MULTILINE)
            _temp = re.sub(r'https:\S+', '', _temp, flags=re.MULTILINE)
            _new.append(_temp)

        return _new

    def removeEmoticon(corpus):
        _new = []
        emoticons_str = r"(?:[:=;B\-][oO\"\_\-]?[\-D\)\]\(\]/\\Op3]{2,3})"
        for _temp in corpus:
            _temp.replace(emoticons_str, '')
            _temp = re.sub(r'[^\x00-\x7F]', '', _temp)
            _new.append(_temp)

        return _new