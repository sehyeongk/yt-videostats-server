from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from flask import request, jsonify
from database import engine
from models import Video, VideoStat, Channel


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
    try:
        video_id = request.args.get('vid', None)
        if not video_id:
            return jsonify('VideoId is needed'), 400

        with Session(engine) as session:
            info = session.query(
                Video.id,
                Video.title ,
                Channel.channel_id,
                VideoStat.stat_type,
                VideoStat.from_date,
                VideoStat.to_date,
                VideoStat.created_at,
                VideoStat.updated_at,
                VideoStat.deleted_at,
                VideoStat.impressions,
                # VideoStat.impression_click_rate,
                VideoStat.views,
                VideoStat.views_subs,
                VideoStat.views_unsubs,
                VideoStat.views_red,
                VideoStat.avg_per_viewed,
                VideoStat.avg_per_viewed_subs,
                VideoStat.avg_per_viewed_unsubs,
                VideoStat.avg_per_viewed_red,
                VideoStat.avg_view_duration,
                VideoStat.video_length,
                VideoStat.watch_time,
                VideoStat.watch_time_red,
                VideoStat.subs_gain,
                VideoStat.subs_lost,
                VideoStat.subs,
                VideoStat.likes,
                VideoStat.dislikes,
                VideoStat.comment,
                VideoStat.sharing,
                VideoStat.playlist_add,
                VideoStat.playlist_remove,
                VideoStat.end_screen_shown,
                VideoStat.end_screen_click,
                VideoStat.click_per_end_screen_shown,
                VideoStat.card_shown,
                VideoStat.card_click,
                VideoStat.card_click_rate,
                VideoStat.est_partner_rev,
                VideoStat.est_partner_ad_rev,
                VideoStat.est_partner_red_rev,
                VideoStat.est_partner_super_rev,
                VideoStat.ad_impressions,
                VideoStat.est_monetized_playbacks,
                VideoStat.cpm,
                # VideoStat.cpm_playback_base,
                VideoStat.unique_viewer
                )\
                    .filter(and_(VideoStat.video_id == video_id, VideoStat.stat_type == 'THREEDAYS'))\
                        .join(Video, Video.id == VideoStat.video_id)\
                            .join(Channel, Channel.channel_id == Video.channel_id).all()

        result = dict(info[0]) if info else []

        return jsonify(result), 200

    except Exception as e:
        return jsonify(e), 400
