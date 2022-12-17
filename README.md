# Talk2ChatGPT

This project allows you to talk to [ChatGPT](https://chat.openai.com/chat).

_Use your voice to asynchronously ask ChatGPT questions, freeing up your hands to work on other activities._

<div align='center'>
  <kbd>
    <a href='https://chat.openai.com/chat'>
      <img src='http://g.recordit.co/y5mFXR81F8.gif' title='Talk2ChatGPT' width='' alt='Talk2ChatGPT' height=640/>
    </a>
  </kbd>
</div>

## Introduction

Since its inception, [ChatGPT](https://openai.com/blog/chatgpt/) has taken the world by storm. Within a matter of days, many developers have begun building [open-source projects](https://github.com/search?q=chatgpt) on top of it, even with it being a "Free Research Preview" (likely to be removed in the future).

There are many impressive ways to interface with ChatGPT through hacky workarounds – this isn't one of them.

Instead, this implementation is much simpler and will always work regardless of changing internet security features put in place by OpenAI.

## Installation

This project relies on [speech_recognition](https://github.com/Uberi/speech_recognition) for converting your voice into text and [pyautogui](https://github.com/asweigart/pyautogui) for typing this text into the OpenAI chat.

- [speech_recognition](https://github.com/Uberi/speech_recognition) incorporates both on-device (local) and off-device (cloud) capabilities for converting speech to text.
- [pyautogui](https://github.com/asweigart/pyautogui) runs local software to control your computer peripherals (keyboard and mouse).

In this project, `speech_recognition` will need access to your microphone, instructions for setting this up is available at [speech_recognition#pyaudio-for-microphone-users](https://github.com/Uberi/speech_recognition#pyaudio-for-microphone-users).

In this project, `pyautogui` will have control of a keyboard for the purpose of hands-free engagement with the chat. Instructions on giving your system this privilege is available at [google.com](https://www.google.com) (for mac: `System Preferences` → `Security & Privacy` → `Accessibility` → `Terminal` → ✅).

**If you are not comfortable with any of these, do not proceed.**

Otherwise, simply install with:

```bash
pip install -r requirements.txt
```

You can also use and get access to a local copy of [Whisper](https://openai.com/blog/whisper/), allowing you to "Whisper to ChatGPT 😆", by following the instructions at [speech_recognition#whisper-for-whisper-users](https://github.com/Uberi/speech_recognition#whisper-for-whisper-users).

## Example

A brief example of using this program.

Essentially you want to run `python main.py` in a terminal and then navigate to [ChatGPT/chat](https://chat.openai.com/chat) and place your cursor inside the text box. Because of this requirement, you will get the best usage of this program by running it on a separate computer that will not compete with you over your keyboard.

To control the keyboard via voice, a short prompt will need to be spoken. By default this is set to `openai`. So saying the phrase `openai spit me some bars about large language models` will produce `spit me some bars about large language models` (as shown in the [introduction](#introduction)).

For a list of different settings, run:

```bash
$ python main.py -h

usage: main.py [-h] [--engine {google,sphinx,whisper}] [--prompt PROMPT] [--message MESSAGE] [--interval INTERVAL]

Talk2ChatGPT (https://chat.openai.com/chat)

optional arguments:
  -h, --help            show this help message and exit
  --engine              {google,sphinx,whisper}
                        speech recognition engine (default: google)
  --prompt PROMPT       prompt to control keyboard with voice
  --message MESSAGE     message shown when not being prompted
  --interval INTERVAL   number of seconds in between each keypress
```

The expected output, when running with default settings, is:

```bash
# $ python main.py --engine google --prompt openai --message Listening --interval 1e-2
$ python main.py

# Ask permission on startup
Start listening? [Y/n]: # y

Say something!
result2:
{   'alternative': [{'confidence': 0.98762912, 'transcript': 'what is GPT'}],
    'final': True}
Google thinks you said: what is GPT

Say something!
result2:
{   'alternative': [{'confidence': 0.99242381, 'transcript': 'what is deep learning'}],
    'final': True}
Google thinks you said: what is deep learning

etc.
```

The response from ChatGPT for the first question (as of December 15, 2022) is:

> GPT stands for "Generative Pre-training Transformer." It is a type of artificial intelligence model that has been developed by OpenAI and is used for natural language processing tasks such as language translation, summarization, and question answering.
>
> GPT is a type of transformer model, which means that it uses self-attention mechanisms to process input data and generate output. It is trained using a process called pre-training, which involves feeding the model large amounts of text data and allowing it to learn patterns and relationships within the data.
>
> GPT has been highly successful at a variety of natural language processing tasks and has been used to develop applications such as language translation systems, chatbots, and content generation tools. It has also been used for research in the field of artificial intelligence and has contributed to the development of more advanced models for natural language processing.

## Disclaimer

[MIT License](LICENSE), most importantly: The author is not liable for any damages incurred during the use of this Software whatsoever.

**Careful what you say to sit. You are giving a computer program complete control over your keyboard. I would highly advise against saying any computer related commands. You have been warned!**
