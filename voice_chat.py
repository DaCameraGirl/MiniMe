import whisper
import sounddevice as sd
import numpy as np
import tempfile
import wave
import os
from datetime import datetime

def record_audio(duration=10, sample_rate=16000):
    """Record audio from microphone"""
    print("🎤 Recording... Speak now!")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("✅ Recording complete!")
    return audio_data, sample_rate

def save_audio_to_file(audio_data, sample_rate):
    """Save audio data to a temporary WAV file"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
        with wave.open(temp_file.name, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_data.tobytes())
        return temp_file.name

def transcribe_audio(audio_file_path):
    """Transcribe audio using Whisper"""
    print("🔄 Transcribing...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)
    return result["text"]

def main():
    """Main voice chat function"""
    print("🔥 Angela's Voice Chat with Claude! 🔥")
    print("Press Enter to start recording (10 seconds max)")
    print("Type 'quit' to exit")
    
    while True:
        user_input = input("\n📝 Press Enter to record or type message: ").strip()
        
        if user_input.lower() == 'quit':
            print("👋 Goodbye Angela!")
            break
            
        if user_input == "":
            # Record audio
            try:
                audio_data, sample_rate = record_audio()
                audio_file = save_audio_to_file(audio_data, sample_rate)
                text = transcribe_audio(audio_file)
                
                # Clean up temp file
                os.unlink(audio_file)
                
                print(f"🎯 You said: '{text}'")
                print("📋 Copy this text and paste it in your chat with Claude!")
                
                # Save to clipboard if possible
                try:
                    import pyperclip
                    pyperclip.copy(text)
                    print("✅ Text copied to clipboard!")
                except ImportError:
                    print("💡 Install pyperclip with: pip install pyperclip")
                    
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print(f"📝 You typed: '{user_input}'")

if __name__ == "__main__":
    main()