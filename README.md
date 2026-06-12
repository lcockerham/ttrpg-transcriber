# ttrpg-transcriber

GPU-accelerated transcription for TTRPG session recordings, using [faster-whisper](https://github.com/SYSTRAN/faster-whisper).

Accepts any audio format supported by ffmpeg (`.m4a`, `.mp3`, `.wav`, `.ogg`, etc.).
Output is a timestamped `.txt` file next to the input file.

## Requirements

- Python 3.10+
- NVIDIA GPU with CUDA (runs on CPU if you change `device="cuda"` to `device="cpu"`)
- `faster-whisper` — `pip install faster-whisper`

## Usage

```bash
python transcribe.py <audio_file> [model_size]
```

`model_size` defaults to `large-v3`. Other options: `tiny`, `base`, `small`, `medium`, `large-v2`.

**Example:**
```bash
python transcribe.py session-05.m4a
# output: session-05.txt
```

## Use as a git submodule

```bash
git submodule add https://github.com/lcockerham/ttrpg-transcriber tools/transcriber
git submodule update --init   # after cloning a repo that includes it
```
