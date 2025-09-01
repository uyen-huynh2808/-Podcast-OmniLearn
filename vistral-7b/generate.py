from transformers import AutoTokenizer, AutoModelForCausalLM

HF_TOKEN = "your token "   # ⚠️ thay bằng token cá nhân

model_id = "Viet-Mistral/Vistral-7B-Chat"

# Load tokenizer + model với token
tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    # load_in_4bit=True,
    trust_remote_code=True,
    use_auth_token=HF_TOKEN
)

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

messages = [{"role": "user", "content": prompt}]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=400,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1
)

print("🎙️ Podcast Script:\n")
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
