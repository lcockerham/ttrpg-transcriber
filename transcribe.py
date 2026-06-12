import sys
import os

# ctranslate2 calls LoadLibrary at runtime, which uses PATH — prepend nvidia DLL dirs
_site_pkgs = os.path.join(os.path.dirname(sys.executable), "Lib", "site-packages")
_cuda_dirs = [
    os.path.join(_site_pkgs, "nvidia", "cublas", "bin"),
    os.path.join(_site_pkgs, "nvidia", "cudnn", "bin"),
    os.path.join(_site_pkgs, "nvidia", "cuda_nvrtc", "bin"),
]
_extra = os.pathsep.join(d for d in _cuda_dirs if os.path.isdir(d))
if _extra:
    os.environ["PATH"] = _extra + os.pathsep + os.environ.get("PATH", "")

from faster_whisper import WhisperModel


def transcribe(audio_path, model_size="large-v3", output_path=None):
    print(f"Loading model: {model_size}")
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    print(f"Transcribing: {audio_path}")
    segments, info = model.transcribe(audio_path, beam_size=5)

    print(f"Detected language: {info.language} (prob {info.language_probability:.2f})")
    print(f"Duration: {info.duration:.1f}s")
    print()

    if output_path is None:
        base = os.path.splitext(audio_path)[0]
        output_path = base + ".txt"

    with open(output_path, "w", encoding="utf-8") as f:
        for segment in segments:
            timestamp = f"[{segment.start:7.2f}s --> {segment.end:7.2f}s]"
            line = f"{timestamp}  {segment.text.strip()}"
            print(line)
            f.write(line + "\n")

    print(f"\nTranscript saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file> [model_size]")
        sys.exit(1)

    audio = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else "large-v3"
    transcribe(audio, model)
