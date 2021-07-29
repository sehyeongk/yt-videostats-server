# Sandbox Youtube VideoStat API
Sandbox Youtube VideoStat API는 영상 제목 검색과 영상의 3일치 수치를 반환합니다.

## Getting Started

### Prerequisite
Flask Framework 사용하였습니다. SQLAlchemy 사용했습니다.

### Installing
flask와 SQLAlchemy 가 필요합니다. requirements.txt 를 통해 설치할 수 있습니다.
```
pip install -r requirements.txt
```

## APIs

### search video by title

입력값과 제목이 일치하는 영상들과 여러 정보들을 최대 20개까지 반환합니다.

- Request
	- GET /videos
		- parameter
			- title: title

- Response
```
[
    {
        "channel_id": "UCwoUwLNRWS6LBhskZ_E2dtg",
        "created_at": "Thu, 14 May 2020 06:16:51 GMT",
        "deleted_at": null,
        "description": null,
        "id": "_Fw1KmINV8U",
        "published_at": "Fri, 27 Mar 2020 01:09:39 GMT",
        "status": "PUBLIC",
        "thumbnail": "https://i.ytimg.com/vi/_Fw1KmINV8U/maxresdefault.jpg",
        "title": "[모여봐요 동물의 숲 1화] 제빠가 무인도에 갔어요!! 너굴사장의 여행은 힐링이 될까요? 닌텐도 스위치 인기게임 꿀팁 공략 제이제이 게임-JJ game",
        "updated_at": "Thu, 14 May 2020 11:34:34 GMT"
    },

 ...
]
```

### get video stats

video id를 입력받고 해당 영상 업로드 후 3일 간의 조회수, 댓글수 등 부수적인 정보를 출력합니다. DB에 존재하지 않는 video id가 들어온 경우엔 빈 리스트를 반환합니다.

- Request
	- GET / video
		- parameter
			- vid: video id

- Response
```
{
    "ad_impressions": null,
    "avg_per_viewed": 49.1948,
    "avg_per_viewed_red": 53.4296,
    "avg_per_viewed_subs": 52.0964,
    "avg_per_viewed_unsubs": 47.3769,
    "avg_view_duration": 103,
    "card_click": 0,
    "card_click_rate": 0.0,
    "card_shown": 0,
    "channel_id": "UCGNCf6ibX1HWndVRgiChpqw",
    "click_per_end_screen_shown": 2.336,
    "comment": 29,
    "cpm": null,
    "created_at": "Mon, 27 Apr 2020 08:38:13 GMT",
    "deleted_at": null,
    "dislikes": 11,
    "end_screen_click": 949,
    "end_screen_shown": 40625,
    "est_monetized_playbacks": null,
    "est_partner_ad_rev": null,
    "est_partner_red_rev": null,
    "est_partner_rev": null,
    "est_partner_super_rev": null,
    "from_date": "Tue, 21 Apr 2020 00:00:00 GMT",
    "id": "RsHIju44xPI",
    "impressions": null,
    "likes": 631,
    "playlist_add": 578,
    "playlist_remove": 579,
    "sharing": 32,
    "stat_type": "THREEDAYS",
    "subs": 13,
    "subs_gain": 20,
    "subs_lost": 7,
    "title": "양아지 - 너.. 봤구나..?\" 아지쿤의 위험한 취미생활 - [ 트박스 ] 샌드박스 트위치 핫클립\"",
    "to_date": "Thu, 23 Apr 2020 00:00:00 GMT",
    "unique_viewer": null,
    "updated_at": "Fri, 15 May 2020 09:02:03 GMT",
    "video_length": 209,
    "views": 57103,
    "views_red": 11415,
    "views_subs": 21995,
    "views_unsubs": 35108,
    "watch_time": 1630.88,
    "watch_time_red": 354.08
}
```

## Running the tests

개발 단계에서 서버 실행

```
FLASK_DEBUG='True' FLASK_RUN='app.py' flask run
```

## Built with
flask framework, SQLAlchemy
 
## Deployment

## License
