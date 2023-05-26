# DTMF

A DTMF decoder written in Rust Python.

## What is it?

This program aims to detect dial tone signal sounds from your microphone. Open your phone's keypad and start dialing some numbers. Do you hear different beeps for different keys? Congratulations, these beeps are DTMF.
Each digit has its unique dual-tone signal that can be easily decoded by telephone stations and other radio stuff. For more information, please refer to [Wikipedia](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling).

## What is the real language of this program?

By Rusted Python, I mean that the decoder is written in Rust with a slightly modified Rust crate "dtmf". I wrote a simple wrapper module in Python. The module receives a list of float32 samples that can be taken from a WAV file using Scipy or from the microphone.
The microphone decoding part is written in Python using the awesome Sounddevice library. It receives the float32 samples from the microphone and sends them straight to the Rust Python module.

## Building

You need to have Rust installed for this. The compiled Windows 64-bit Python 3.11 PYD may be available soon, maybe? To build, you need to:

* pip install maturin
* pip install poetry
* pip install sounddevice

I don't know if you actually need Poetry, but just in case...

Then run:

* poetry run maturin develop

This will compile the code to a Python extension. Congratulations! Now just run main.py and try to give it some DTMF beeps to listen.