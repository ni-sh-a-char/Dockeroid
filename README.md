
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8304168.svg)](https://doi.org/10.5281/zenodo.8304168)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) ![BASH](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
# Why to turn off the security to install the apps from unknown sources when the browser can have it...
# Dockeroid
Website for Android application emulation and testing. The website could be used to test the android application by using the apk for installation and proper display of the application upon the android emulator using docker.
# About the Dockerfile
This Dockerfile sets up a Docker image based on the Ubuntu operating system and provides the following capabilities:

* Installs necessary packages: Python 3, OpenJDK 11, ADB (Android Debug Bridge), QEMU-KVM, libvirt-daemon-system, libvirt-clients, bridge-utils, virt-manager, unzip, and wget.

* Sets up KVM permissions by adding the current user to the kvm and libvirt groups, allowing access to KVM features.

* Sets up the Android SDK by defining the environment variables ANDROID_SDK_ROOT and updating the PATH to include the SDK tools and platform-tools directories.

* Creates a named folder named /app within the Docker image. This folder can be used to store and access files or data within the container.

* Downloads the Android Command Line Tools, extracts them, and removes the downloaded archive.

* Accepts the Android SDK licenses automatically.

* Installs required Android SDK components, including platform tools, Android platform version 30, build tools version 30.0.3, Google Play services, and the Google APIs system image for Android version 30.

* Creates an Android Virtual Device (AVD) named "myavd" using the specified system image and device configuration.

* Sets environment variables for the Android SDK and AVD.

* Sets the default command to /bin/bash, which opens a Bash shell when running a container from the image.

With this Dockerfile, you can build a Docker image that includes Ubuntu, the Android SDK, ADB, and other necessary tools and packages for Android development and testing.
