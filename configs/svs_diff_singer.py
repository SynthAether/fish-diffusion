from fish_diffusion.datasets.audio_folder import AudioFolderDataset

_base_ = [
    "./svc_hubert_soft.py",
]

phonemes = [
    "AP",
    "SP",
    "E",
    "En",
    "a",
    "ai",
    "an",
    "ang",
    "ao",
    "b",
    "c",
    "ch",
    "d",
    "e",
    "ei",
    "en",
    "eng",
    "er",
    "f",
    "g",
    "h",
    "i",
    "i0",
    "ia",
    "ian",
    "iang",
    "iao",
    "ie",
    "in",
    "ing",
    "iong",
    "ir",
    "iu",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "ong",
    "ou",
    "p",
    "q",
    "r",
    "s",
    "sh",
    "t",
    "u",
    "ua",
    "uai",
    "uan",
    "uang",
    "ui",
    "un",
    "uo",
    "v",
    "van",
    "ve",
    "vn",
    "w",
    "x",
    "y",
    "z",
    "zh",
]

preprocessing = dict(
    text_features_extractor=dict(
        _delete_=True,
        type="OpenCpopTranscriptionToPhonemesDuration",
        phonemes=phonemes,
        transcription_path="dataset/transcriptions.txt",
    ),
)

model = dict(
    type="DiffSinger",
    text_encoder=dict(
        _delete_=True,
        type="FastSpeech2Encoder",
        input_size=len(phonemes) + 1,
        hidden_size=256,
    ),
)

dataset = dict(
    _delete_=True,
    train=dict(
        type="AudioFolderDataset",
        path="dataset/diff-singer/train",
        speaker_id=0,
    ),
    valid=dict(
        type="AudioFolderDataset",
        path="dataset/diff-singer/valid",
        speaker_id=0,
    ),
)

trainer = dict(
    precision=32,
)