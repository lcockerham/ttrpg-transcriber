# ttrpg-transcriber

GPU-accelerated transcription for TTRPG session recordings, using [faster-whisper](https://github.com/SYSTRAN/faster-whisper).

Accepts any audio or video format supported by ffmpeg (`.m4a`, `.mp3`, `.wav`, `.ogg`, `.mov`, `.mkv`, etc.).
Output is a timestamped `.txt` file next to the input file.

## Requirements

- Python 3.10+
- NVIDIA GPU with CUDA if available; otherwise it falls back to CPU automatically (e.g. on a Mac)
- `pip install -r requirements.txt`

On CPU, `large-v3-turbo` is several times faster than `large-v3` with similar accuracy. A 67-minute session took about 20 minutes on an Apple Silicon MacBook Air.

Without installing anything, using [uv](https://docs.astral.sh/uv/):

```bash
uv run --with-requirements requirements.txt python transcribe.py session-05.m4a large-v3-turbo
```

## Usage

```bash
python transcribe.py <audio_file> [model_size]
```

`model_size` defaults to `large-v3`. Other options: `tiny`, `base`, `small`, `medium`, `large-v2`, `large-v3-turbo`.

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
