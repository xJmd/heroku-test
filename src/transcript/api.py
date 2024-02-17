from youtube_transcript_api import YouTubeTranscriptApi as yta
from src.transcript.formater import Formater

class Transcriber:

    def __init__(self, video_id):
        self.id = video_id

    def get_transcript(self):
        data = yta.get_transcript(self.id)
        transcript = ''
        for value in data:
            for key, val in value.items():
                if key == 'text':
                    transcript += val + " "  # adding a space so the words in different {text: } aren't stuck to each other
        starting_t = transcript.splitlines()
        transcript = " ".join(starting_t)
        
        formater = Formater(transcript)

        return formater.update()


