# Use the base Ubuntu image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    openjdk-11-jdk \
    adb \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils \
    virt-manager \
    unzip \
    wget

# Set up KVM permissions
RUN adduser $USER kvm
RUN adduser $USER libvirt

# Set up Android SDK
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH=${PATH}:${ANDROID_SDK_ROOT}/tools:${ANDROID_SDK_ROOT}/platform-tools

# Create a named folder
RUN mkdir -p /app

# Download Android Command Line Tools
RUN mkdir -p ${ANDROID_SDK_ROOT} && cd ${ANDROID_SDK_ROOT} && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip -O android-tools.zip && \
    unzip android-tools.zip && \
    rm android-tools.zip

# Accept Android SDK licenses
RUN yes | ${ANDROID_SDK_ROOT}/tools/bin/sdkmanager --licenses

# Install required Android SDK components
RUN ${ANDROID_SDK_ROOT}/tools/bin/sdkmanager "platform-tools" "platforms;android-30" "build-tools;30.0.3" "extras;google;google_play_services" "system-images;android-30;google_apis;x86"

# Create an AVD
RUN echo "no" | ${ANDROID_SDK_ROOT}/tools/bin/avdmanager create avd --name myavd --package "system-images;android-30;google_apis;x86" --device "pixel" --sdcard 512M --force

# Set environment variables
ENV ANDROID_HOME=${ANDROID_SDK_ROOT}
ENV ANDROID_AVD_HOME=/root/.android/avd

# Set the default command
CMD ["/bin/bash"]
