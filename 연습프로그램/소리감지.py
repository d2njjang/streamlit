import streamlit as st
import numpy as np
import sounddevice as sd

# 설정값
THRESHOLD_DB = 70  # 소음 기준 (데시벨)
DURATION = 1  # 측정 간격 (초)
SAMPLERATE = 44100  # 샘플링 레이트

# 데시벨 계산 함수
def calculate_decibels(audio_data):
    rms = np.sqrt(np.mean(np.square(audio_data)))
    db = 20 * np.log10(rms) if rms > 0 else 0
    return round(db, 2)

# 마이크에서 소리 감지
def get_microphone_volume():
    recording = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=1, dtype='float32')
    sd.wait()  # 녹음 완료 대기
    audio_data = recording.flatten()
    return calculate_decibels(audio_data)

# Streamlit UI
st.title("📢 소음 감지 알람 앱")
st.write("마이크에서 입력되는 소리를 감지하여 70dB 이상이면 경고 메시지를 표시합니다.")

if st.button("측정 시작"):
    st.write("🎤 소리를 감지하는 중...")
    
    while True:
        volume = get_microphone_volume()
        st.write(f"현재 소리 크기: {volume} dB")

        if volume >= THRESHOLD_DB:
            st.error(f"🚨 경고! 소음 수준 초과: {volume} dB")
            break