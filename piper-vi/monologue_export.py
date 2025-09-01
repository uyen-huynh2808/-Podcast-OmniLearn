import subprocess
from pydub import AudioSegment

# Chọn giọng đọc
VOICE_MODEL = "vi_VN-vais1000-medium.onnx"

# Văn bản độc thoại
TEXT = "Xin chào, tôi là trợ lý Ây-Ai của bạn. Đây là một ví dụ về độc thoại được tạo bởi Pip-pơ."

# File output
OUTPUT_FILE = "monologue.wav"

def create_monologue(text, output_file=OUTPUT_FILE):
    # Gọi Piper để sinh file wav
    cmd = [
        "piper",
        "--model", VOICE_MODEL,
        "--output_file", output_file
    ]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    process.communicate(input=text.encode("utf-8"))

    # Kiểm tra lại file bằng pydub
    audio = AudioSegment.from_wav(output_file)
    print(f"Xuất xong độc thoại: {output_file}, thời lượng {len(audio)/1000:.2f} giây")

if __name__ == "__main__":
    create_monologue(TEXT)
