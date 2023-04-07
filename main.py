import os
from docx import Document

folder_path = "C:/Users/metek/Desktop/Makaleler"
total_word_count = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".docx"):
        doc = Document(os.path.join(folder_path, filename))
        word_count = 0
        for para in doc.paragraphs:
            word_count += len(para.text.split())
        total_word_count += word_count

print("Toplam Kelime Sayısı: ", total_word_count)