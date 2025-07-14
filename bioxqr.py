import qrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

def generate_qr():
    url = url_entry.get()
    if url.strip() == "":
        result_label.config(text="Please enter a valid URL.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("generated_qr.png")

    qr_image = Image.open("generated_qr.png")
    qr_image = qr_image.resize((200, 200))
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    result_label.config(text="QR Code generated successfully!")

Label(root, text="Enter URL:", font=("Arial", 14)).pack(pady=10)
url_entry = Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 10))
result_label.pack()

root.mainloop()