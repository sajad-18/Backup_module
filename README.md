# 📦 Backup Module – Windows User Folder Backup Tool

## 📌 About the Project

**Backup Module** is a standalone, Windows-focused Python tool designed to simplify the process of **backing up critical user directories** before reinstalling or upgrading the operating system.  
It offers an **interactive, automated, and user-friendly** approach to selecting, calculating, and copying important files with a progress display, ensuring no data is lost during system migration.

---

## ✨ Features

### 🔹 Core Functionality
- Prompts the user for **folder names** to back up from the Windows `Users` directory  
- Automatically locates the correct folder paths based on the given names  
- Calculates **total file count** and **overall size** before starting the backup  
- Asks the user to select the **destination folder** for backup  
- Checks the target drive’s **free and used space**, ensuring sufficient capacity before proceeding  
- **Error handling** for insufficient space and invalid folder names  

### 🔹 Backup Process
- Recreates the **original folder structure** in the destination  
- Copies files with a **real-time progress bar** showing:
  - Percentage completed  
  - Number of files copied vs. total files  
  - Elapsed time since start  
- Generates a **text file listing all installed software** in the backup folder for post-reinstallation reference  

---

## 🛠 How It Works

1. **User Input** – Enter the folder names you wish to back up.  
2. **Path Detection** – The module locates the exact directories under `C:\Users`.  
3. **Size & File Count Calculation** – Shows the user the backup size and file count.  
4. **Destination Selection** – The user chooses a target drive or folder.  
5. **Space Check** – Ensures there’s enough free space before proceeding.  
6. **Folder Structure Creation** – Prepares destination directories.  
7. **File Copying** – Displays real-time progress, file counts, and elapsed time.  
8. **Software List Export** – Saves a `.txt` file of installed applications in the backup folder.  

---

## 🚀 Usage

1. Clone or download the repository.  
2. Run the script with Python 3:
   ```sh
   python backup_module.py
   ```
3. Follow the on-screen instructions.
💡 No additional installation or dependencies are required.

---

## 🖥 Technologies Used
- Python – Core scripting language
- os, shutil, psutil – For file handling and system information
- tqdm / custom progress display – For real-time copy progress feedback

---

##👨‍💻 Contact Me
- 📧 Email: [sajjad.ir8415@gmail.com](mailto:sajjad.ir8415@gmail.com)
- 💼 LinkedIn: [Sajjad Esmaeilzadeh](https://www.linkedin.com/in/sajad-esmaeilzadeh/)
- 🌐 Personal Website: [Sevelop.ir](www.sevelop.ir)

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it.
