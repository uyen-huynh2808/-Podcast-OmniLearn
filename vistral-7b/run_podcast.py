from model_loader import generate_response

prompt = """
Bạn là một giảng viên có nhiệm vụ giúp học viên tiếp thu nhanh hơn.
Hãy chuyển nội dung đoạn văn sau thành một kịch bản podcast ngắn,
theo dạng hội thoại tự nhiên giữa hai người (A và B).

Yêu cầu:
- Giữ nguyên kiến thức cốt lõi, không thêm thông tin sai lệch.
- Giọng điệu gần gũi, trò chuyện như bạn bè.
- Chia nhỏ ý thành đối thoại qua lại, giúp người nghe dễ nhớ.
- Có ví dụ minh họa nếu phù hợp.

Đoạn văn:
"Đọc sách mỗi ngày không chỉ giúp mở rộng vốn từ vựng mà còn rèn luyện trí nhớ.
Các nghiên cứu cho thấy thói quen đọc sách 20 phút mỗi ngày có thể cải thiện khả năng tập trung,
giảm căng thẳng và tăng khả năng thấu hiểu người khác."
"""

print("🎙️ Podcast Script:\n")
print(generate_response(prompt))
