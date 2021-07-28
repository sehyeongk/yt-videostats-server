from sqlalchemy import Column, Integer, String, Date, DateTime, BigInteger, Float, Enum, Index
from sqlalchemy.dialects.mysql import MEDIUMTEXT, SMALLINT

from database import Base


class Channel(Base):
    __tablename__ = 'private_channels'
    __table_args__ = (
                        Index('id', 'channel_id', 'created_at'),
    )

    id = Column(Integer, primary_key=True)
    channel_id = Column(String(24), primary_key=True)
    created_at = Column(Date, primary_key=True)
    title = Column(String(255), nullable=True)
    thumbnail = Column(String(255), nullable=True)
    status = Column(String(50), nullable=True)
    linked_at = Column(DateTime, nullable=True)
    published_at = Column(DateTime, nullable=True)
    leaved_at = Column(Date, nullable=True)
    cms = Column(String(50), nullable=True)
    company = Column(String(50), nullable=True)
    strike = Column(SMALLINT, nullable=True)
    total_views = Column(BigInteger, nullable=True)
    total_videos = Column(BigInteger, nullable=True)
    total_subscribers = Column(BigInteger, nullable=True)


class Video(Base):
    __tablename__ = 'private_videos'

    id = Column(String(50), primary_key=True)
    channel_id = Column(String(50), nullable=True)
    title = Column(String(255), nullable=True)
    status = Column(Enum('PUBLIC', 'PRIVATE', 'UNLISTED', 'DELETED'), nullable=True)
    description = Column(MEDIUMTEXT, nullable=True)
    thumbnail =  Column(String(255), nullable=True)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)


class VideoStat(Base):
    __tablename__ = 'private_videos_stat'
    __table_args__ = (
                        Index('id', 'video_id', 'stat_type'),

    )

    id = Column(Integer, primary_key=True)
    video_id = Column(String(50)) #
    stat_type = Column(Enum('THREEDAYS', 'ONEWEEK', 'TWOWEEKS', 'ONEMONTH'))
    from_date = Column(DateTime, nullable=True)
    to_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    impressions = Column(BigInteger, nullable=True)
    impression_click_rate = Column(Float, nullable=True)
    views = Column(BigInteger, nullable=True)
    views_subs = Column(BigInteger, nullable=True)
    views_unsubs = Column(BigInteger, nullable=True)
    views_red = Column(BigInteger, nullable=True)
    avg_per_viewed = Column(Float, nullable=True)
    avg_per_viewed_subs = Column(Float, nullable=True)
    avg_per_viewed_unsubs = Column(Float, nullable=True)
    avg_per_viewed_red = Column(Float, nullable=True)
    avg_view_duration = Column(Integer, nullable=True)
    video_length = Column(Integer, nullable=True)
    watch_time = Column(Float, nullable=True)
    watch_time_red = Column(Float, nullable=True)
    subs_gain = Column(Integer, nullable=True)
    subs_lost = Column(Integer, nullable=True)
    subs = Column(Integer, nullable=True)
    likes = Column(Integer, nullable=True)
    dislikes = Column(Integer, nullable=True)
    comment = Column(Integer, nullable=True)
    sharing = Column(Integer, nullable=True)
    playlist_add = Column(Integer, nullable=True)
    playlist_remove = Column(Integer, nullable=True)
    end_screen_shown = Column(BigInteger, nullable=True)
    end_screen_click = Column(BigInteger, nullable=True)
    click_per_end_screen_shown = Column(Float, nullable=True)
    card_shown = Column(BigInteger, nullable=True)
    card_click = Column(BigInteger, nullable=True)
    card_click_rate = Column(Float, nullable=True)
    est_partner_rev = Column(Integer, nullable=True)
    est_partner_ad_rev = Column(Integer, nullable=True)
    est_partner_red_rev = Column(Integer, nullable=True)
    est_partner_super_rev = Column(Integer, nullable=True)
    ad_impressions = Column(BigInteger, nullable=True)
    est_monetized_playbacks = Column(BigInteger, nullable=True)
    cpm = Column(Float, nullable=True)
    cpm_playback_base = Column(Float, nullable=True)
    unique_viewer = Column(BigInteger, nullable=True)