import api
from flask import Flask, request, render_template

app =Flask(__name__)

@app.route('/')
def index():
    with open('playlist.txt', 'r', encoding='UTF-8') as f:
        playlist = [ api.get_video_data(item.strip()) for item in f.readlines() ]
    playlist = [ [videodata[1], videodata[2], videodata[0] ] for videodata in playlist ]
    return render_template('index.html', playlist=playlist)

@app.route('/find')
def search_engine():
    chart = api.get_billboard_chart(10)
    return render_template('search.html', chart=chart)

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    result_list = api.search_youtube(keyword)
    if result_list == [] or result_list == None:
        return render_template('wrong.html')
    return render_template('result.html', result_list=result_list)

@app.route('/add/<videoid>')
def add(videoid):
    with open('playlist.txt', 'a', encoding='UTF-8') as f:
        f.write(str(videoid) + '\n')
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
