# -Vecna-Ransomware-Simulation-Educational-Purpose

This project simulates basic ransomware behavior using Python and the `cryptography` library. It encrypts all files in the current directory (except internal scripts) and generates a decryption key.

> ⚠️ For educational use only. Do **not** run on real or important data.

---

## 📦 Requirements

- Python 3.x  
- Install cryptography:  
  ```bash
  pip install cryptography
  ```

---

## ▶️ How to Use

### 🔐 Encrypt Files

```bash
python3 vecna.py
```

- Encrypts all files in the folder.
- Saves encryption key as `thekey.key`.

### 🔓 Decrypt Files

```bash
python3 decrypt.py
```

- Uses `thekey.key` to decrypt files.

---

## 📁 Notes

- Safe to use only in a test or virtual environment.
- Files excluded: `vecna.py`, `decrypt.py`, `thekey.key`.

---

## 🎯 Purpose

To help students safely understand ransomware behavior, encryption, and file recovery in a lab setup.

