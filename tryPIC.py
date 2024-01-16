from PIL import Image
import os
import streamlit as st
                                 
def compress(input_folder, output_folder, max_size_kb=250):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path_jpg = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                # Resize the image to 35%
                width, height = img.size
                new_width = int(width * 0.30)
                new_height = int(height * 0.30)
                resized_img = img.resize((new_width, new_height))

                # Compress the resized image at least once
                resized_img.save(output_path_jpg, quality=resized_img.info.get('quality', 65) - 5)


        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue


def main():
    st.title("圖片壓縮和轉換成 GIF")

    # 讓使用者輸入圖片資料夾路徑
    input_folder = st.text_input("輸入圖片的資料夾路徑:")

    # 讓使用者選擇輸出資料夾
    output_folder = input_folder+"\\FinishCompress"

    # 按鈕，當使用者按下後執行壓縮和轉換的操作
    if st.button("開始壓縮和轉換"):
        if input_folder and output_folder:
            compress(input_folder, output_folder)
            st.success("壓縮和轉換完成！")

if __name__ == "__main__":
    main()

# streamlit run tryPIC.py