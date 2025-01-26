
from pydub import AudioSegment
import os
import torch

class AnyType(str):
    """A special class that is always equal in not equal comparisons"""
    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

class AudioToWavConverter:
    """
    A custom node to convert input audio files to WAV format

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    RETURN_NAMES (`tuple`):
        The name of each output in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. 
    CATEGORY (`str`):
        The category the node should appear in the UI.
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
    CATEGORY = "Audio Processing"

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

