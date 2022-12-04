def timedelta_to_videotime(delta):
  parts = delta.split(":")
  if len(parts[0]) == 1:
    parts[0] = f"0{parts[0]}"
  new_data = ":".join(parts)
  parts2 = new_data.split(".")
  if len(parts2) == 1:
    parts2.append("000")
  elif len(parts2) == 2:
    parts2[1] = parts2[1][:2]
  final_data = ".".join(parts2)
  return final_data

def whisper_segments_to_vtt_data(result_segments):
  data = "WEBVTT\n\n"
  for idx, segment in enumerate(result_segments):
    num = idx + 1
    data+= f"{num}\n"
    start_ = datetime.timedelta(seconds=segment.get('start'))
    start_ = timedelta_to_videotime(str(start_))
    end_ = datetime.timedelta(seconds=segment.get('end'))
    end_ = timedelta_to_videotime(str(end_))
    data += f"{start_} --> {end_}\n"
    text = segment.get('text').strip()
    data += f"{text}\n\n"
  return data

import whisper
import datetime

model = whisper.load_model("large")
result = model.transcribe("audio.wav")
caption_data = whisper_segments_to_vtt_data(result['segments'])
print(caption_data)