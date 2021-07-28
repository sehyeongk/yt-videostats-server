from sqlalchemy import select
from sqlalchemy.orm import Session

from flask import request, jsonify
from database import engine
from models import Video


def search_video_by_title():
    try:
        title = request.args.get('title', None)
        if not title:
            return jsonify('Enter the title to search for'), 400

        statement = select(Video).filter(Video.title.like(f'%{title}%')).limit(20)
        with Session(engine) as session:
            videos = session.execute(statement)

        result = []
        for row in videos:
            video = row['Video']
            result.append(
                {
                    'id': video.id,
                    'channel_id': video.channel_id,
                    'title': video.title,
                    'status': video.status,
                    'description': video.description,
                    'thumbnail': video.thumbnail,
                    'published_at': video.published_at,
                    'created_at': video.created_at,
                    'updated_at': video.updated_at,
                    'deleted_at': video.deleted_at
                }
            )

        return jsonify(result), 200

    except Exception as e:
        return jsonify(e), 400


def get_videos_info():
    pass
