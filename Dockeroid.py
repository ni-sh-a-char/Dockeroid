from calendar import different_locale
from mimetypes import init
import os
import subprocess
import streamlit as st
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
		command = ['xvfb-run','-s', '-screen 0 1024x768x24','/opt/android-sdk/emulator/emulator','-avd', 'myavd','-no-snapshot-save']
            	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	        stdout, stderr = process.communicate()
            	# Print the output
	        st.write(stdout)

    elif choice == "Android Debug Bridge":
        st.subheader("Perform adb commands for the application")
        

if __name__ == '__main__':
    main()
