import json, requests
import billboard

def search_youtube(keyword): # keyword로 유튜브 검색 후 검색결과 가져오기
    api_key = 'strawberry-cream-frappuccino'
    url = (
        'https://www.googleapis.com/youtube/v3/search?part=snippet&q='
        + keyword + '&maxResults=5' + '&key='
        + api_key
    )
    # print(url)
    data = json.loads(requests.get(url).text)
    results = int(data['pageInfo']['resultsPerPage'])
    # print('n : ' + str(results))
    # print('q : ' + str(keyword) + '\n')
    video_data_list = []
    for idx in range(results):
        try:
            video_data = []
            # 비디오 id, 제목, 채널, 썸네일 순 리스트
            video = data['items'][idx]
            video_data.append(str(video['id']['videoId']))
            # print('id : ' + str(video['id']['videoId']))
            video_data.append(str(video['snippet']['title']))
            # print('title : ' + str(video['snippet']['title']))
            video_data.append(str(video['snippet']['channelTitle']))
            # print('channel : ' + str(video['snippet']['channelTitle']))
            video_data.append(str(video['snippet']['thumbnails']['default']['url']))
            # print('thumbnail : ' + str(video['snippet']['thumbnails']['default']['url']) + '\n')
            video_data_list.append(video_data)
        except:
            continue
    return video_data_list

def get_video_data(videoid): # video id로 동영상 세부 정보 가져오기
    api_key = 'strawberry-cream-frappuccino'
    url = (
        'https://www.googleapis.com/youtube/v3/videos?part=snippet&id='
        + videoid + '&key=' + api_key
    )
    data = json.loads(requests.get(url).text)
    video_data = []
    try:
        # 비디오 id, 제목, 채널, 썸네일 순 리스트
        video = data['items'][0]
        video_data.append(str(video['id']))
        # print('id : ' + str(video['id']['videoId']))
        video_data.append(str(video['snippet']['title']))
        # print('title : ' + str(video['snippet']['title']))
        video_data.append(str(video['snippet']['channelTitle']))
        # print('channel : ' + str(video['snippet']['channelTitle']))
        video_data.append(str(video['snippet']['thumbnails']['default']['url']))
        # print('thumbnail : ' + str(video['snippet']['thumbnails']['default']['url']) + '\n')
    except:
        return None
    return video_data

def get_billboard_chart(top):
    # top decides list size(int type, max 100), for example top==10 returns top 10 songs in chart
    chart = [
        [str(song.title), str(song.artist)]
        for song in billboard.ChartData('hot-100')[:int(top)]
    ]
    # list containing [title, artist]
    return chart

if __name__ == '__main__':
    # print(get_video_data(search_youtube('playlist')[0][0]))
    # print(search_youtube('playlist'))
    print(get_billboard_chart(10))
