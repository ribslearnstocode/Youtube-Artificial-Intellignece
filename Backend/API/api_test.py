from langdetect import detect
from youtube_transcript_api import YouTubeTranscriptApi



print(YouTubeTranscriptApi.list_transcripts("eIrMbAQSU34"))
print(detect("это компьютерный портал для гиков"))