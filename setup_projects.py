import subprocess
import keyboard as kb
import pyautogui as pag
import time
from inputimeout import TimeoutOccurred, inputimeout


# paths
NLP_folder = r"E:\code_playground\python\Jarvis_NLP\phase_3"
Jarvis_folder = r"E:\code_playground\Jarvis\jarvis_v1"
OpenCV_folder = r"E:\code_playground\python\openCV"


# go_to_dektop_1
def goto_dektop_1():
    for _ in range(10):
        kb.press_and_release("ctrl+windows+left")
        time.sleep(0.1)


# setup_NLP
def setup_NLP():
    goto_dektop_1()
    print("Starting setup...")
    time.sleep(2)
    kb.press_and_release("ctrl+windows+right")
    time.sleep(1)

    subprocess.run(["code", NLP_folder], shell=True)
    time.sleep(2)

    kb.press_and_release("ctrl+windows+right")
    subprocess.run(
        [
            "cmd",
            "/c",
            "start chrome https://chatgpt.com/c/68a8a833-9dc4-8324-9e32-9f2c7f5fc8a9",
        ]
    )
    time.sleep(4)

    kb.press_and_release("ctrl+t")
    time.sleep(0.3)

    pag.write("https://chatgpt.com/?temporary-chat=true", interval=0.08)
    kb.press_and_release("enter")
    time.sleep(3)

    kb.press_and_release("ctrl+windows+left")


# setup_Jarvis
def setup_Jarvis():
    goto_dektop_1()
    print("Starting setup...")
    time.sleep(2)
    kb.press_and_release("ctrl+windows+right")
    time.sleep(1)

    subprocess.run(["code", Jarvis_folder], shell=True)
    time.sleep(2)

    kb.press_and_release("ctrl+windows+right")
    subprocess.run(
        [
            "cmd",
            "/c",
            "start chrome https://chatgpt.com/?temporary-chat=true",
        ]
    )
    time.sleep(4)

    kb.press_and_release("ctrl+t")
    time.sleep(0.3)

    pag.write("http://localhost:3000", interval=0.08)
    kb.press_and_release("enter")
    time.sleep(3)

    kb.press_and_release("ctrl+windows+left")

# setup_opencv
def setup_OpenCV():
    goto_dektop_1()
    print("Starting setup...")
    time.sleep(2)
    kb.press_and_release("ctrl+windows+right")
    time.sleep(1)

    subprocess.run(["code", OpenCV_folder], shell=True)
    time.sleep(2)

    kb.press_and_release("ctrl+windows+right")
    subprocess.run(
        [
            "cmd",
            "/c",
            "start chrome https://chatgpt.com/?temporary-chat=true",
        ]
    )
    time.sleep(4)

    kb.press_and_release("ctrl+t")
    time.sleep(0.3)

    pag.write("https://www.youtube.com/watch?v=yQu_3e7MAr0", interval=0.08)
    kb.press_and_release("enter")
    time.sleep(3)

    kb.press_and_release("ctrl+windows+left")


# start_setup -> based on input
def start_setup(input):
    if input.strip().lower() in ["1", "nlp", "nlp setup"]:
        setup_NLP()
    elif input.strip().lower() in ["2", "jarvis", "jarvis setup"]:
        setup_Jarvis()
    elif input.strip().lower() in ["3", "opencv", "opencv setup"]:
        setup_OpenCV()
    else:
        return

if __name__ == "__main__":
    try:
        # user_input
        user_input = inputimeout(
            prompt="Select one within 60 seconds or I setup openCV project!\n1. NLP Setup\n2. Jarvis Setup\n3. OpenCV Setup\n> ",
            timeout=60,
        )
        start_setup(user_input)
    except TimeoutOccurred:
        # if no input was given
        print("No input was given!\nSetting up Jarvis project!")
        setup_Jarvis()