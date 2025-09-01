from transformers import AutoTokenizer, AutoModelForCausalLM

HF_TOKEN = "your_token"
MODEL_ID = "Viet-Mistral/Vistral-7B-Chat"

print("⏳ Đang load model, vui lòng chờ...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_auth_token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    trust_remote_code=True,
    use_auth_token=HF_TOKEN
)

print("✅ Model đã load xong!")

def generate_response(prompt: str) -> str:
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

    return tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
