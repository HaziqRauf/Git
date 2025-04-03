import streamlit as st
import subprocess
import sys
import os
from PIL import Image

filelist = []

def main():
    st.title("Pavement Distress Dashboard YOLOv5")

def save_dir(exp_dir):
    save_dir.saved_dir = exp_dir
    return exp_dir

def return_dir(SAVEDIR):
    pastedir = str(SAVEDIR)
    fulldir = "/home/jimbo/Documents/fyp/InterfaceFYP/streamlit/yolov5/%s" % pastedir
    print(fulldir)
    subprocess.run([f"xdg-open", fulldir])

    for root, dirs, files in os.walk(fulldir):
        for file in files:
            filename=os.path.join(root, file)
            filelist.append(filename)
            print(filelist)
            # st.write(filelist)
    return fulldir

#Uploading an image
f = st.file_uploader("Choose a file")
if f is not None:
    filename = f.name

#Uploading multiple image
#uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
#for uploaded_file in uploaded_files:
    # filename = uploaded_file.name

    weightpath = "/home/jimbo/Documents/fyp/InterfaceFYP/streamlit/yolov5/runs/train/exp4/weights/best.pt"
    imgsize = "416"
    confint = "0.1"
    tarpath = "/home/jimbo/Pictures/%s" % filename 

    st.image(tarpath)
    subprocess.run([f"{sys.executable}", "detect.py", "--weights", weightpath, "--img", imgsize, "--conf", confint, "--source", tarpath])

    detectpath = "/home/jimbo/Documents/fyp/InterfaceFYP/streamlit/yolov5/runs/detect"
    # temp_dir = return_dir()
    print(filelist)
    # st.image(filelist)
    # print(filelist)
    for imagefile in filelist:
        st.write(imagefile)
        st.image(imagefile)

    print(filelist)
    # temp_dir = return_dir(filename)
    # print(temp_dir)

    # print(return_dir(temp_dir))

    # subprocess.Popen(r'/home/jimbo/Documents/fyp/InterfaceFYP/streamlit/yolov5/runs/detect', shell=True)
    # st.image(str(return_dir(str(save_dir.saved_dir)+temp_dir)))

else:
    path_in = None

if __name__ == 'main':
    try:
        main()
    except SystemExit:
        pass
