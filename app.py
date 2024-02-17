from flask import Flask, render_template, request, redirect, send_file
from src.utils import thumbnail
from src.transcript import api



app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        id = request.form.get('id')
        return redirect("/video?id=" + id)
    
    return render_template('index.html')

@app.route('/video')
def video():
    id = request.args.get('id')
    if 'youtube.com' in id:
        url = id
    elif 'youtu.be' in id:
        url = "https://www.youtube.com/watch?v=" + id.split('/')[-1]
        print(url)
    else:
        url = "https://www.youtube.com/watch?v=" + id



    
    scraper = thumbnail.Scraper(url)
    try:
        data = scraper.get_data()
        print(data)
        return render_template('video.html', title=data[0], thumbnail=data[1], date=data[2], url=url)
    except Exception:
        return render_template('error.html')

@app.route('/transcript', methods=['GET'])
def transcript():
    video_url = request.args.get('url')

    if not video_url:
        return redirect('/')  
    try:
        transcriber = api.Transcriber(video_url.split('?v=')[1])
        return render_template('transcript.html', t = transcriber.get_transcript())
    except Exception as e:
        return render_template('error.html')
        print(e)
    
        

    except Exception as e:
        return f"Error: {e}"
    

if __name__ == '__main__':
    app.run()   