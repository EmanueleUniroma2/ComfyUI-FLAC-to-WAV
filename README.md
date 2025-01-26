# ComfyUI-FLAC-to-WAV
A custom node to convert flac files to wav inside comfy UI

ComfyUI Custom Node: FLAC to WAV Converter
Welcome to the ComfyUI Custom Node: FLAC to WAV Converter repository! This project provides a custom node for ComfyUI that allows you to easily convert .flac audio files to .wav format, making it simpler to work with a variety of audio tools and applications.

Features
- Efficient Conversion: Quickly convert .flac files to .wav format with minimal quality loss.
- Easy Integration: Seamlessly integrate this custom node into your ComfyUI workflow.
- Lightweight and Fast: Built with performance in mind to handle even large audio files efficiently.
- Open Source: Licensed under the MIT License for open collaboration and contribution.

Requirements
Python 3.6+
pydub library
ffmpeg or libav library

Installation
Clone the Repository:

sh
git clone https://github.com/yourusername/comfyui-flac-to-wav.git
cd comfyui-flac-to-wav

Install Dependencies:

sh
pip install pydub
Ensure ffmpeg or libav is Installed:

Ubuntu/Debian:

sh
sudo apt-get install ffmpeg
macOS (using Homebrew):

sh
brew install ffmpeg
Windows:

Download the FFmpeg executable and add it to your system's PATH.

Usage
Here's a quick example of how to use the custom node in your ComfyUI workflow:

python
from pydub import AudioSegment
```
class FlacToWavNode:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def convert(self):
        audio = AudioSegment.from_file(self.input_path, format="flac")
        audio.export(self.output_path, format="wav")`

# Example Usage

```converter = FlacToWavNode("example.flac", "output.wav")
converter.convert()
print("Conversion complete: example.flac -> output.wav")`

Contributing
Contributions are welcome! Please fork this repository and submit a pull request to add features, fix bugs, or improve documentation. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Feel free to reach out for any questions or suggestions:

GitHub: yourusername

Email: youremail@example.com
