import transcribe_streaming
import recorder

rc = recorder.Recorder()
audio_buffer = rc.record_audio()
sentence = transcribe_streaming.transcribe_streaming(audio_buffer)

print(sentence)