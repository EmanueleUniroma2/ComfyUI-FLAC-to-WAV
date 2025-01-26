
from pydub import AudioSegment
import os
import torch

class AudioToWavConverter:
    """
    A custom node to convert input audio files to WAV format

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`AUDIO`):
        The type of each element in the output tuple.
    RETURN_NAMES (`wav_audio`):
        The name of each output in the output tuple.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio_input": ("AUDIO", {}),
            }
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("wav_audio",)
    FUNCTION = "convert_audio"
    CATEGORY = "audio"

    def convert_audio(self, audio_input):
        # Extract the file name without extension
        input_file = audio_input
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{file_name}.wav"

        # Load the input audio file
        audio = AudioSegment.from_file(input_file)

        # Export as WAV
        audio.export(output_file, format="wav")

        return (output_file,)

