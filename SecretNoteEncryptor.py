efrom tkinter import *
from tkinter import messagebox
import base64

def encode(key, clear):
    encrypt = []
    for x in range(len(clear)):
        key_c = key[x % len(key)]
        enc_c = chr((ord(clear[x]) + ord(key_c)) % 256)
        encrypt.append(enc_c)
    return base64.urlsafe_b64encode("".join(encrypt).encode()).decode()

def decode(key, encrypt):
    decrypt = []
    encrypt = base64.urlsafe_b64decode(encrypt).decode()
    for x in range(len(encrypt)):
        key_c = key[x % len(key)]
        dec_c = chr((256 + ord(encrypt[x]) - ord(key_c)) % 256)
        decrypt.append(dec_c)
    return "".join(decrypt)

def save_and_encrypt():
    Title = TitleEntry.get()
    Message = SecretTextEntry.get("1.0", END).strip()
    MasterKey = MasterKeyEntry.get()

    if len(Title) == 0 or len(Message) == 0 or len(MasterKey) == 0:
        messagebox.showwarning(title="Error", message="Please fill all the fields")
    else:
        encrypted_message = encode(MasterKey, Message)

        try:
            with open("Notes.txt", "a", encoding="utf-8") as data:
                data.write(f"\n{Title}\n{encrypted_message}\n")
        except FileNotFoundError:
            with open("Notes.txt", "w", encoding="utf-8") as data:
                data.write(f"\n{Title}\n{encrypted_message}\n")
        finally:
            TitleEntry.delete(0, END)
            SecretTextEntry.delete("1.0", END)
            MasterKeyEntry.delete(0, END)
            messagebox.showinfo(title="Success", message="Your note has been saved & encrypted!")

def decrypt():
    encryptedmessage = SecretTextEntry.get("1.0", END).strip()
    MasterKey = MasterKeyEntry.get()

    if len(encryptedmessage) == 0 or len(MasterKey) == 0:
        messagebox.showwarning(title="Error", message="Please fill all the fields")
    else:
        try:
            decrypted_message = decode(MasterKey, encryptedmessage)
            SecretTextEntry.delete("1.0", END)
            SecretTextEntry.insert("1.0", decrypted_message)
        except Exception:
            messagebox.showwarning(title="Error", message="Please enter your encrypted message correctly")

window = Tk()
window.title("Secret Notes")
window.geometry("400x600")
window.config(bg="black")

try:
    Image = PhotoImage(file="Secret.png")
    SmallImage = Image.subsample(2, 2)
    ImgLabel = Label(window, image=SmallImage, bg="black", pady=60)
    ImgLabel.pack(pady=25)
except Exception:
    ImgLabel = Label(window, text="[Image Missing]", bg="black", fg="red", font=("Segoe UI", 12, "bold"))
    ImgLabel.pack(pady=25)

Title = Label(text="Enter Your Title", font=("Segoe UI", 11, "bold"), bg="black", fg="lightgrey")
Title.place(relx=0.5, y=205, anchor="center")

TitleEntry = Entry(width=40, bg="dimgray", fg="white", font=("Segoe UI", 10, "bold"))
TitleEntry.place(relx=0.5, y=235, anchor="center")

SecretText = Label(text="Enter Your Secret Text", font=("Segoe UI", 11, "bold"), bg="black", fg="lightgrey")
SecretText.place(relx=0.5, y=275, anchor="center")

SecretTextEntry = Text(width=30, height=7, bg="dimgray", fg="black", font=("Segoe UI", 12, "bold"))
SecretTextEntry.place(relx=0.5, y=375, anchor="center")

MasterKeyLabel = Label(text="Enter Your Master Key", fg="white", bg="black", font=("Segoe UI", 11, "bold"))
MasterKeyLabel.place(relx=0.5, y=475, anchor="center")

MasterKeyEntry = Entry(width=40, bg="dimgray", fg="darkkhaki", font=("Segoe UI", 10, "bold"))
MasterKeyEntry.place(relx=0.5, y=510, anchor="center")

SaveButton = Button(text="Save & Encrypt", fg="maroon", bg="dimgray", command=save_and_encrypt)
SaveButton.place(relx=0.4, y=570, anchor="center")

DecryptButton = Button(text="Decrypt", bg="dimgray", command=decrypt)
DecryptButton.place(relx=0.6, y=570, anchor="center")

window.mainloop()
