# 🕵️‍♂️ Meta Hunter (Forensic Image Inspector)

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/asfaqovi/meta-hunter)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Category](https://img.shields.io/badge/Category-OSINT%20%26%20Forensics-red?style=for-the-badge)](https://github.com/topics/osint)

> **"Data never sleeps, and neither does the metadata."**

**Meta Hunter** is a lightweight Digital Forensics and OSINT tool designed to extract hidden data from images. It peels back the visual layer to reveal the device fingerprint, timestamps, and precise GPS coordinates hidden within the file's EXIF data.

---

## ⚡ Features

* 📍 **Geolocation Extraction:** Automatically converts raw GPS data into readable Decimal Degrees.
* 🗺️ **Auto-Mapping:** Generates a direct Google Maps link to the exact location of the photo.
* 📷 **Device Fingerprinting:** Identifies the specific Camera Make, Model, and Software used.
* 🕒 **Temporal Analysis:** precise timestamp extraction for timeline verification.
* 🛡️ **Error Handling:** Gracefully handles scrubbed images or invalid formats.

---

## 🛠️ Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/asfaqovi/meta-hunter.git](https://github.com/asfaqovi/meta-hunter.git)
    cd meta-hunter
    ```

2.  **Install Dependencies**
    This tool requires the `Pillow` library for image processing.
    ```bash
    pip install Pillow
    ```

---
## 🚀 Usage

You can run the tool on any specific image file.

**Basic Command:**
```bash
python inspector.py target_image.jpg

[*] Analyzing: target_image.jpg
------------------------------
Make: NIKON
Model: COOLPIX P6000
DateTime: 2008:11:01 21:15:07
Software: Nikon Transfer 1.1 W

[+] GPS Data Found:
    Latitude: 43.467156...
    Longitude: 11.885394...
    Google Maps: [https://www.google.com/maps?q=43.467,11.885](https://www.google.com/maps?q=43.467,11.885)
---

## 👥 Authors & Contributors

This project is a collaborative effort.

| Developer | Role | GitHub |
|-----------|------|--------|
| **Asfaq Ovi** | 🧠 Lead Logic & Scripting | [@asfaqovi](https://github.com/asfaqovi) |
| **[PARTNER NAME HERE]** | 🧪 Testing & Documentation | [@PARTNER_USERNAME](https://github.com/PARTNER_USERNAME) |

*(To join the team: Edit this file, add your name to the table above, and commit the changes!)*

---

## 🤝 How to Contribute (The Easy Way)

1.  Click the **Pencil Icon** ✏️ at the top right of this README file.
2.  Scroll down to the **Authors** table.
3.  Add your name, role, and GitHub profile link.
4.  Scroll to the bottom and click **Commit changes**.
5.  🎉 You are now an official contributor!

---

## ⚖️ Disclaimer

*This tool is intended for educational purposes, security research, and authorized digital forensics investigations only. The authors are not responsible for any misuse of this software.*

---

<div align="center">
	<sub>Built with 💀 and 🐍 by the Security Team</sub>
</div>
