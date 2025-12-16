# Secret Notes Encryptor

A simple **Tkinter-based Python app** that lets you **write, encrypt, and decrypt secret notes** using a custom master key.  
All encrypted notes are stored locally in a text file — safe and simple!

---

##  Features

-  **Encrypt your notes** with a custom master key  
-  **Decrypt messages** instantly with the same key  
-  **Saves encrypted notes** to a local `Notes.txt` file  
-  **Easy-to-use GUI** built with Tkinter  
-  Optional image banner (replace `Secret.png` with your own)

---

##  How It Works

1. Enter your **note title**
2. Type your **secret message**
3. Choose a **master key** (used for both encryption and decryption)
4. Click **"Save & Encrypt"** to store the encrypted note in `Notes.txt`
5. To **decrypt**, paste the encrypted message into the text box, enter your master key, and click **"Decrypt"**

>  Make sure to remember your master key — without it, your message cannot be decrypted!

---

 File Structure
SecretNoteEncryptor/
│
├── SecretNote.py        # Main app file
├── .gitignore           
├── Secret.png        # Optional image for UI
└── README.md            # Project description


##  Built With

- [Python 3](https://www.python.org/)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html)  
- [Base64](https://docs.python.org/3/library/base64.html)

---

## 💡 Developer

**Sharode**  
> A simple GUI app to protect your private notes 🔒  
