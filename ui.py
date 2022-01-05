from lib_all import *
from inferance import predict

streamlit.subheader("Nhận diện vật thể ")
image_file = streamlit.file_uploader("Tải ảnh cần dự đoán", type="jpg")

if image_file is not None:

    # To See details
    file_details = {"filename":image_file.name, "filetype":image_file.type,
                    "filesize":image_file.size}
    streamlit.write(file_details)

    # To View Uploaded Image
    img = Image.open(image_file)
    streamlit.image(img,width=700)

    with open(os.path.join("data/database", "ask.jpg"), "wb") as f:
        f.write((image_file).getbuffer())


    img_file_path = "data/database/ask.jpg"
    img = predict(img_file_path)
    cv2.imwrite("data/database/result.jpg", img)

    streamlit.success("Đã xử lý thành công")

    ask_img_path = "./data/database/result.jpg"
    if ask_img_path is not None:
        img = Image.open(ask_img_path)
        streamlit.image(img,width=700)