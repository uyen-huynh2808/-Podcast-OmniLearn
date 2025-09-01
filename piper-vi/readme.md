1. Tải model về path /piper-vi/ theo link:

https://huggingface.co/rhasspy/piper-voices/blob/main/vi/vi_VN/25hours_single/low/vi_VN-25hours_single-low.onnx

https://huggingface.co/rhasspy/piper-voices/blob/main/vi/vi_VN/25hours_single/low/vi_VN-25hours_single-low.onnx.json

https://huggingface.co/rhasspy/piper-voices/blob/main/vi/vi_VN/vais1000/medium/vi_VN-vais1000-medium.onnx

https://huggingface.co/rhasspy/piper-voices/blob/main/vi/vi_VN/vais1000/medium/vi_VN-vais1000-medium.onnx.json

https://huggingface.co/rhasspy/piper-voices/blob/main/vi/vi_VN/vivos/x_low/vi_VN-vivos-x_low.onnx

https://huggingface.co/rhasspy/piper-voices/blob/main/vi/vi_VN/vivos/x_low/vi_VN-vivos-x_low.onnx.json

2. Tạo môi trường ảo

      python3 -m venv piper-env

3. Chuyển sang môi trường ảo

      source piper-env/bin/activate
   
4. Cài đặt thư viện

      pip install piper-tts
   
      pip install pydub
 
5. Locate tới file path

      cd ~/piper-vi/

6. Độc thoại

      python monologue_export.py

7. Đối thoại

      python dialogue_export.py
