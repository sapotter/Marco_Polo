# HOWTO Create macOS Polo

## Create environment

```shell
mamba env create -f macOS/environment-$(uname -m).yml 2>&1 | tee env-$(uname -m)-output.txt
```

## Run `pyinstaller` to create executable

```shell
platform=$(uname -m); pyinstaller --clean -y macOS/Polo.spec 2>&1 | tee pyinstall-"${platform}"-output.txt; unset platform
```

## Create DMG installer

```shell
platform=$(uname -m); vol_label="Polo macOS-${platform}"; create-dmg --volname "${vol_label}" \
--volicon macOS/application.icns \
--background macOS/background.png \
--window-size 800 450 \
--icon-size 128 \
--icon "Polo.app" 350 200 \
--hide-extension "Polo.app" \
--app-drop-link 600 195 \
--no-internet-enable \
~/Desktop/"${vol_label}.dmg" dist/Polo.app; unset platform vol_label
```
