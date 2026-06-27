from youtube_transcript_api import YouTubeTranscriptApi

video_id = "F0GQ0l2NfHA"

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id)

with open("genai_course.txt", "w", encoding="utf-8") as f:
    for snippet in transcript:
        f.write(snippet.text + "\n")

print("Transcript saved successfully!")