#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import pyautogui
import argparse


ENGINES = {
    "google": "recognize_google",
    "sphinx": "recognize_sphinx",
    "whisper": "recognize_whisper",
}


def recognize(recognizer, audio, engine, **kwargs) -> str:
    text = ""
    stt = getattr(recognizer, ENGINES[engine])
    engine = engine.capitalize()
    try:
        text = stt(audio, **kwargs)
        print(f"{engine} thinks you said: " + text)
    except sr.UnknownValueError:
        print(f"{engine} could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from {engine}")
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Talk2ChatGPT (https://chat.openai.com/chat)"
    )
    parser.add_argument(
        "--engine",
        type=str,
        default="google",
        choices=["google", "sphinx", "whisper"],
        help="speech recognition engine (default: google)",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="openai",
        help="prompt to control keyboard with voice",
    )
    parser.add_argument(
        "--message",
        type=str,
        default="Listening",
        help="message shown when not being prompted",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1e-2,
        help="number of seconds in between each keypress",
    )
    args = parser.parse_args()

    while "y" != input("Start listening? [Y/n]: ").lower():
        continue

    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nSay something!")
            pyautogui.typewrite(message=args.message, interval=args.interval)
            audio = r.listen(source)

        # recognize speech
        text = recognize(r, audio, args.engine)
        pyautogui.press(keys="backspace", presses=len(args.message))
        if text.startswith(args.prompt):
            text = text[len(args.prompt) :]
            text = text.strip()
            pyautogui.typewrite(message=text + "\n", interval=args.interval)
