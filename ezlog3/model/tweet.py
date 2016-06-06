# -*- coding: utf-8 *-*
import string, random, re
from datetime import datetime as dt

from flask import g,session,jsonify,render_template
from mongoengine import CASCADE
import bleach

from ezlog3.libs.db import db

class Tweet(db.Document):
    content            = db.StringField(required=True)
    type               = db.StringField(default="text")
    create_date        = db.DateTimeField(default=dt.now)
    author             = db.ReferenceField("User", reverse_delete_rule=CASCADE)

    meta = {
        'allow_inheritance': True,
        'index_types': False,
    }

    def get_tweet_by_topic(self, topic):
        pass

    def post_process(self):
        ## parse topic first
        # content
        topics = re.findall(r"#(\w+)\W", self.content)
        for topic_name in topics:
            topic = Topic(name=topic_name, tweet=self)
            topic.save()

    def render(self):
        ## ugly
        content = self.content

        # process topic

        content = re.sub(r"#(\w+)\W", r"<a href='/tweet/get_by_topic/?name=\1'>#\1</a>" ,content)
        # print content
        # process linkify
        file_extension_dict = {
            ## https://en.wikipedia.org/wiki/Comparison_of_web_browsers#Image_format_support
            "image": ("png", "jpg", "jepg", "gif"),
            ## https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats
            "video": ("webm", "mp4", ),
            "music": ("mp3", "ogg"), 
            "website":("youtube.com", "youtu.be"), ## web site link special process
        }

        link_process = {
            "image": [],
            "video": [],
            "music": [],
            "website":[],
        }

        link_render = []

        result = ['<div class="tweet">']
  
        def mycallback(attrs, new=False):
            if not new:
                return attrs
            href = attrs['href']
            for key in file_extension_dict:
                for extension in file_extension_dict[key]:
                    if href.endswith("."+extension):
                        link_process[key].append((href, extension))
                        return None

            attrs['_text'] = "link"
            return attrs

        content = bleach.linkify(content, callbacks=[mycallback])

        ## image 
        for link_tuple in link_process["image"]:
            link, extension = link_tuple
            content = content.replace(link, "")
            link_render.append('<div class="tweet-image"><img src="%s" /></div>'%link)

        for link_tuple in link_process["video"]:
            link, extension = link_tuple
            content = content.replace(link, "")
            link_render.append(''' <video width="100%%" controls>
                          <source src="%s" type="video/%s">
                          Your browser does not support HTML5 video.
                        </video>'''%(link, extension))


        result.append(content)
        result = result + link_render
        result.append('</div>')
        return "".join(result)



class Topic(db.Document):
    name               = db.StringField()
    tweet              = db.ReferenceField("Tweet", reverse_delete_rule=CASCADE)
