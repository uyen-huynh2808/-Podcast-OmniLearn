import subprocess
from pydub import AudioSegment
import os

voices = {
    "A": "vi_VN-vais1000-medium.onnx",
    "B": "vi_VN-25hours_single-low.onnx"
}

script = [
    ("A", "Xin chào, tôi là giọng A."),
    ("B", "Chào bạn, tôi là giọng B."),
    ("A", "Chúng ta có thể luân phiên trò chuyện."),
    ("B", "Đúng vậy, và kết hợp thành một file duy nhất.")
]

combined = AudioSegment.silent(duration=500)
temp_files = []

for i, (speaker, text) in enumerate(script):
    output_file = f"line{i}_{speaker}.wav"
    temp_files.append(output_file)

    # Tạo file wav bằng Piper
    cmd = [
        "piper",
        "--model", voices[speaker],
        "--output_file", output_file
    ]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    process.communicate(input=text.encode("utf-8"))

    seg = AudioSegment.from_wav(output_file)
    combined += seg + AudioSegment.silent(duration=300)

# Xuất file hội thoại hoàn chỉnh
final_file = "dialogue_full.wav"
combined.export(final_file, format="wav")
print(f"Xuất xong hội thoại: {final_file}")

# Xoá file tạm
for f in temp_files:
    if os.path.exists(f):
        os.remove(f)
print("Đã xoá file subfile tạm")
