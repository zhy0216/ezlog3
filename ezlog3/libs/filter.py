import re

import bleach

def linkify(text):
    t_text = text + " "
    t_text = bleach.linkify(t_text)
    # change to topic
    # t_text = re.sub(ur"(@([a-zA-Z0-9_\u4e00-\u9fa5]+)) ",r'<a href="/user/nickname/\g<2>">\g<1></a>',t_text)
    return t_text

