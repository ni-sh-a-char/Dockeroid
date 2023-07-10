import os
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import screeninfo
import streamlit as st

# APK file upload function
def upload_apk():
    st.subheader('APK File Upload')
    uploaded_file = st.file_uploader('Upload APK file')
    if uploaded_file is not None:
        with open('/app/app.apk', 'wb') as file:
            file.write(uploaded_file.getbuffer())
        st.write('File uploaded successfully')

# Install APK function
def install_apk():
    st.subheader('Install APK')
    adb_install_command = ['adb', 'install', '/app/app.apk']
    process = subprocess.Popen(adb_install_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    if error:
        st.error(f'Error installing APK:\n{error}')
    else:
        st.success('APK installed successfully')

# Uninstall APK function
def uninstall_apk():
    st.subheader('Uninstall APK')
    package_name = st.text_input('Enter package name')
    adb_uninstall_command = ['adb', 'uninstall', package_name]
    process = subprocess.Popen(adb_uninstall_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    if error:
        st.error(f'Error uninstalling APK:\n{error}')
    else:
        st.success('APK uninstalled successfully')

# Clear App Data function
def clear_app_data():
    st.subheader('Clear App Data')
    package_name = st.text_input('Enter package name')
    adb_clear_command = ['adb', 'shell', 'pm', 'clear', package_name]
    process = subprocess.Popen(adb_clear_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    if error:
        st.error(f'Error clearing app data:\n{error}')
    else:
        st.success('App data cleared successfully')

# List Installed Packages function
def list_installed_packages():
    st.subheader('List Installed Packages')
    adb_list_command = ['adb', 'shell', 'pm', 'list', 'packages']
    process = subprocess.Popen(adb_list_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    if error:
        st.error(f'Error listing installed packages:\n{error}')
    else:
        packages = output.split('\n')
        packages = [pkg.replace('package:', '') for pkg in packages if pkg]
        st.write('Installed packages:')
        for pkg in packages:
            st.write(pkg)

def main():

    #image = Image.open('logo.png')

    #st.image(image, use_column_width=True)

    st.title("Dockeroid")

    menu = ["Intro","Android Virtual Device","Android Debug Bridge"]
    choice = st.sidebar.selectbox("Select Activity", menu)
    if choice == "Intro":
        st.subheader("Dockeroid: Docker powered Android")

    elif choice == "Android Virtual Device":
        st.subheader("Launch the virtual android device")
        virtual = st.button("Start the Android Virtual Device")
        if virtual:
		        # Get the screen size
                screen = screeninfo.get_monitors()[0]
                screen_width = screen.width
                screen_height = screen.height
                screen_depth = 24

		        # Start the AVD
                avd_command = ['xvfb-run', '-s', f'-screen 0 {screen_width}x{screen_height}x{screen_depth}', '/opt/android-sdk/emulator/emulator', '-avd', 'myavd', '-no-snapshot-save']
                avd_process = subprocess.Popen(avd_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

		        # Wait for the AVD to start
                avd_process.wait()

		    # Run adb logcat command
                logcat_command = ['adb', 'logcat']
                logcat_process = subprocess.Popen(logcat_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                logcat_output, logcat_error = logcat_process.communicate()

		    # Save logs in a PDF file
                pdf_file = "logcat.pdf"
                pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)
                pdf_canvas.setFont("Courier", 10)
                pdf_canvas.drawString(50, 750, "ADB Logcat Output:")
                pdf_canvas.drawString(50, 700, logcat_output)
                pdf_canvas.save()
                st.success("Logs saved in logcat.pdf")
                # Provide download link for the PDF file
                with open(pdf_file, "rb") as f:
                    st.download_button("Download PDF", f.read(), file_name="logcat.pdf", mime="application/pdf")

    elif choice == "Android Debug Bridge":
        st.subheader("Perform adb commands for the application")
        menu_options = ['Install APK', 'Uninstall APK', 'Clear App Data', 'List Installed Packages']
        selected_option = st.sidebar.selectbox('Select an option', menu_options)
	
	# Main program
        if selected_option == 'Install APK':
            upload_apk()
            install_apk()
        elif selected_option == 'Uninstall APK':
            uninstall_apk()
        elif selected_option == 'Clear App Data':
            clear_app_data()
        elif selected_option == 'List Installed Packages':
            list_installed_packages()
        
if __name__ == '__main__':
    main()
