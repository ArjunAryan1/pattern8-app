# Pattern 8: So / That's Why - Android App

A language learning app for Hindi/English "So / That's why" pattern with 10 Home & Family Q&A pairs.

## Features
- **13 screens**: Title, Category Overview, 10 Q&A pairs, Summary
- **Dark modern UI** with cyan/orange/green accents
- **Bilingual content**: Hindi (Devanagari) + English
- **Smooth slide transitions** between questions
- **Offline capable** - no internet required after install

## Quick Start (GitHub Actions - Recommended)

### 1. Create GitHub Repository
```bash
# Initialize git repo
cd kivy_app
git init
git add .
git commit -m "Initial commit: Pattern 8 language learning app"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/pattern8-app.git
git push -u origin main
```

### 2. Automatic APK Build
- Push to `main` branch → **Debug APK** builds automatically
- Create a tag `v1.0.0` → **Release APK** builds and attaches to GitHub Release
- Download APK from **Actions → Artifacts** or **Releases**

### 3. Install on Device
1. Go to **Actions** tab in your GitHub repo
2. Click latest workflow run
3. Download `pattern8-debug-apk` artifact
4. Transfer `pattern8-debug.apk` to phone
5. Enable "Install from unknown sources" in Android settings
6. Install and enjoy!

---

## Local Build (Advanced - Requires Linux/WSL)

### Prerequisites
- Ubuntu 22.04+ or WSL2
- 8GB+ RAM, 10GB+ disk space

```bash
# Install dependencies
sudo apt update && sudo apt install -y \
  git zip unzip openjdk-17-jdk-headless \
  python3-pip autoconf libtool pkg-config \
  zlib1g-dev libncurses5-dev libncursesw5-dev \
  libtinfo5 cmake libffi-dev libssl-dev automake

# Install buildozer
pip install buildozer==1.5.0

# Build
cd kivy_app
buildozer android debug
```

---

## Project Structure
```
kivy_app/
├── main.py                 # Kivy app with all screens
├── buildozer.spec          # Build configuration
├── .github/workflows/
│   └── build-apk.yml       # GitHub Actions workflow
└── README.md               # This file
```

## App Screens
| Screen | Content |
|--------|---------|
| Title | Pattern 8 branding |
| Category | Pattern structure + key connectors |
| Q1-Q10 | Hindi/English Q&A with animated connector |
| Summary | Key takeaways + practice exercises |

## Customization
Edit `main.py`:
- **QA_PAIRS** list - add/modify questions
- **COLORS** dict - change theme
- **Screen classes** - modify layouts

Edit `buildozer.spec`:
- `title`, `package.name`, `package.domain`
- `version`, `icon.filename`, `presplash.filename`
- `android.permissions`, `android.api`, `android.minapi`

---

## License
MIT License - Feel free to use for learning/teaching!

## Support
- Check **Actions** tab for build logs
- Open issue for bugs/features
- APK size: ~15-20 MB (debug), ~8-12 MB (release)