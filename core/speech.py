# core/speech.py

import edge_tts
import tempfile
import os
import platform
from playsound import playsound

VOICE = "pt-BR-AntonioNeural"
SPEED = "+50%"  # Velocidade 1.5x aproximadamente

async def speak(text):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_path = temp_audio.name

        communicate = edge_tts.Communicate(text, VOICE, rate=SPEED)
        await communicate.save(temp_path)

        playsound(temp_path)  # Toca o áudio sem abrir nada
        os.remove(temp_path)  # Remove o áudio temporário
    except Exception as e:
        print(f"[ERRO ao falar] {e}")
