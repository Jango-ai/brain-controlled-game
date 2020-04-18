import mne
from mne_realtime import LSLClient, MockLSLStream
from flask_sse import sse
import time
import random
import numpy as np

def process_epoch(epoch):
    # IMPLEMENT HERE ARTIFACT DETECTION LOGIC
    raw = epoch.get_data()
    range1 = np.amax(raw[0][0]) - np.amin(raw[0][0])
    range2 = np.amax(raw[0][1]) - np.amin(raw[0][1])
    range3 = np.amax(raw[0][2]) - np.amin(raw[0][2])
    range4 = np.amax(raw[0][3]) - np.amin(raw[0][3])
    signal_range = (range1+range2+range3+range4)/4
    signal_out4=np.amax(raw[0][4])-np.amin(raw[0][4])
    signal_out6=np.amax(raw[0][6])-np.amin(raw[0][6])
    signal_out8=np.amax(raw[0][8])-np.amin(raw[0][8])
    signal_out10=np.amax(raw[0][10])-np.amin(raw[0][10])
    signal_out_range = (signal_out4 + signal_out6 + signal_out8 + signal_out10)/4
    if (signal_range >= 170 and signal_range <= 420 and signal_out_range < signal_range/2):
        send_blink_artifact_event()
    # Use send_blink_artifact_event() to send the event to the game
    return ""


def start():
    sfreq = 256
    host = "localhost"
    epoch_size_in_seconds = 0.6

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

    #This loop is for testing the game without EEG input
    #COMMENT OUT THIS LOOP WHEN `process_epoch` IS IMPLEMENTED
    #while True:
    #    send_server_ok_signal()
    #    send_blink_artifact_event()
    #    time.sleep(0.3)

    with LSLClient(info=stream_info, host=host) as client:
        client_info = client.get_measurement_info()
        while True:
            epoch = client.get_data_as_epoch(n_samples=epoch_size_in_seconds * sfreq)
            send_server_ok_signal()
            process_epoch(epoch)
            time.sleep(0.3)


def send_server_ok_signal():
    sse.publish("ok", type="status")


def send_blink_artifact_event():
    sse.publish("blink", type="artifact")
