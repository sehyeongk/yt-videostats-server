from flask import Flask

from controller import search_video_by_title, get_videos_info


def create_app():

    app = Flask(__name__)

    app.add_url_rule('/videos', view_func=search_video_by_title, methods=['GET'])
    app.add_url_rule('/video', view_func=get_videos_info, methods=['GET'])

    return app