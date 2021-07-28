from flask import Flask

from controller import get_videos_list, get_videos_info


def create_app():

    app = Flask(__name__)

    app.add_url_rule('/videos', view_func=get_videos_list, methods=['GET'])
    app.add_url_rule('/video', view_func=get_videos_info, methods=['GET'])

    return app