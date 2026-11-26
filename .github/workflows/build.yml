name: JARVIS APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Depoyu indir
        uses: actions/checkout@v4

      - name: Python kur
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Sistem paketlerini kur
        run: |
          sudo apt update
          sudo apt install -y git zip unzip openjdk-17-jdk

      - name: Buildozer kur
        run: |
          pip install --upgrade pip
          pip install buildozer cython==0.29.36

      - name: APK oluştur
        run: buildozer android debug

      - name: APK dosyasını yükle
        uses: actions/upload-artifact@v4
        with:
          name: JARVIS-APK
          path: bin/*.apk
