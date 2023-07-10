from calendar import different_locale
from mimetypes import init
import os
import subprocess
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import plotly.express as px
import pandas as pd
import seaborn as sns
from PIL import Image
import numpy as np # np mean, np random 
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 

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
		# Start the AVD
		avd_command = ['xvfb-run', '-s', '-screen 0 1024x768x24', '/opt/android-sdk/emulator/emulator', '-avd', 'myavd', '-no-snapshot-save']
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

		st.write("Logs saved in", pdf_file)

    elif choice == "Android Debug Bridge":
        st.subheader("Perform adb commands for the application")
	menu = [""]
        

if __name__ == '__main__':
    main()
