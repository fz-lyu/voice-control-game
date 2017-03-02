from pyaudio import PyAudio, paInt16
import time
import struct
import config
pa = PyAudio()
data = list()
data.append(1)
sampling_rate = int(pa.get_device_info_by_index(0)['defaultSampleRate'])
print("collecting data")
stream = pa.open(format=paInt16, channels=1, rate=sampling_rate, input=True, frames_per_buffer=1000)
init_time = time.time()
while (time.time() - init_time) <= 3:
    string_audio_data = stream.read(1000)
    volume = max(struct.unpack('1000h', string_audio_data))
    data.append(int(volume))
    time.sleep(0.5)
noise_level = sum(data) / len(data)
print(noise_level)
print("data collected")
config.sensitivity = noise_level

