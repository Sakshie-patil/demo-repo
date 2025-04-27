🐧 Step-by-step Flutter Installation on Ubuntu
✅ Step 1: Update your system
Open Terminal and run:

bash
sudo apt update
sudo apt upgrade
✅ Step 2: Install required dependencies
bash

sudo apt install git curl unzip xz-utils zip libglu1-mesa
✅ Step 3: Download the Flutter SDK
bash
cd ~
curl -O https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.19.5-stable.tar.xz
(Check Flutter's website for the latest version if needed)

✅ Step 4: Extract the SDK
bash

tar xf flutter_linux_3.19.5-stable.tar.xz
✅ Step 5: Add Flutter to PATH
Open your .bashrc or .zshrc (based on your shell):

bash
nano ~/.bashrc
Add this line at the end:

bash
export PATH="$PATH:$HOME/flutter/bin"
Then, apply the changes:

bash
source ~/.bashrc
✅ Step 6: Check Flutter setup
bash
flutter doctor
This will check your environment and tell you what needs to be fixed (like Android Studio, emulator, etc.)


✅ Step 9: Create your first Flutter app
bash
flutter create my_app
cd my_app
flutter run
