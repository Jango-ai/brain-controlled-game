import mne
from mne_realtime import LSLClient, MockLSLStream
from flask_sse import sse
import time
import random


def process_epoch(epoch):
    # IMPLEMENT HERE ARTIFACT DETECTION LOGIC
    # Use send_blink_artifact_event() to send the event to the game
    return ""


def start():
    sfreq = 256
    host = "localhost"
    epoch_size_in_seconds = 1

    channels = [
        "Fp1",
        "Fp2",
        "F3",
        "F4",
        "C1",
        "C3",
        "C2",
        "C4",
        "CP1",
        "CP3",
        "CP2",
        "CP4",
        "Cz",
        "O1",
        "O2",
        "Pz",
    ]

    stream_info = mne.create_info(
        ch_names=channels, sfreq=sfreq, ch_types="eeg", montage="standard_1020"
    )

    # COMMENT OUT THIS LOOP WHEN `process_epoch` IS IMPLEMENTED
    while True:
        send_server_ok_signal()
        send_blink_artifact_event()
        time.sleep(0.3)

    # with LSLClient(info=stream_info, host=host) as client:
    #     client_info = client.get_measurement_info()
    #     epoch = client.get_data_as_epoch(n_samples=epoch_size_in_seconds * sfreq)
    #     while True:
    #         send_server_ok_signal()
    #         process_epoch(epoch)


def send_server_ok_signal():
    sse.publish("ok", type="status")


def send_blink_artifact_event():
    sse.publish("blink", type="artifact")
