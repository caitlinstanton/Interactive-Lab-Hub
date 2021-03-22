#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call
import socket
import deepspeech_demo
import json

import time
from random import randint
import board
import busio
from i2c_button import I2C_Button

# initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_pi import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

global not_active
not_active = True

app = Flask(__name__)
socketio = SocketIO(app)
button = I2C_Button(i2c)


@app.route('/')
def index():
    """Video streaming home page."""
    global ARGS
    deepspeech_demo.setup(ARGS)
    while not i2c.try_lock():
        pass
    devices = i2c.scan()
    i2c.unlock()
    print('I2C devices found:', [hex(n) for n in devices])
    default_addr = 0x6f
    if default_addr not in devices:
        print('warning: no device at the default button address', default_addr)
    button.led_bright = 0
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        button.led_bright = 0
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    model = deepspeech_demo.setup(ARGS)
    vad_audio = deepspeech_demo.VADAudio(
        aggressiveness=ARGS.vad_aggressiveness,
        device=ARGS.device,
        input_rate=ARGS.rate,
        file=ARGS.file)
    print("Listening (ctrl-C to exit)...")
    global not_active
    while not_active:
        frames = vad_audio.vad_collector()
        not_active = deepspeech_demo.interpret(ARGS, model, frames)
    print("done")

    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/wizard', methods=["POST"])
def handle_speak():
    jsdata = request.form['javascript_data']
    print("Saying " + jsdata)
    call(f"espeak '{jsdata}'", shell=True)
    button.led_bright = 255
    return "Wizarding done!"


if __name__ == '__main__':
    DEFAULT_SAMPLE_RATE = 16000
    import argparse
    parser = argparse.ArgumentParser(
        description="Stream from microphone to DeepSpeech using VAD")

    parser.add_argument(
        '-v',
        '--vad_aggressiveness',
        type=int,
        default=2,
        help=
        "Set aggressiveness of VAD: an integer between 0 and 3, 0 being the least aggressive about filtering out non-speech, 3 the most aggressive. Default: 3"
    )
    parser.add_argument('--nospinner',
                        action='store_true',
                        help="Disable spinner")
    parser.add_argument(
        '-w',
        '--savewav',
        help="Save .wav files of utterences to given directory")
    parser.add_argument('-f',
                        '--file',
                        help="Read from .wav file instead of microphone")

    parser.add_argument(
        '-m',
        '--model',
        required=True,
        help=
        "Path to the model (protocol buffer binary file, or entire directory containing all standard-named files for model)"
    )
    parser.add_argument('-s',
                        '--scorer',
                        help="Path to the external scorer file.")
    parser.add_argument(
        '-d',
        '--device',
        type=int,
        default=None,
        help=
        "Device input index (Int) as listed by pyaudio.PyAudio.get_device_info_by_index(). If not provided, falls back to PyAudio.get_default_device()."
    )
    parser.add_argument(
        '-r',
        '--rate',
        type=int,
        default=DEFAULT_SAMPLE_RATE,
        help=
        f"Input device sample rate. Default: {DEFAULT_SAMPLE_RATE}. Your device may require 44100."
    )
    global ARGS
    ARGS = parser.parse_args()
    if ARGS.savewav: os.makedirs(ARGS.savewav, exist_ok=True)
    app.run(host='0.0.0.0', threaded=True)