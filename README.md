<img src="./fiund-profile-icon.png" alt="Fiund logo" width="80" height="80">

# Fiund

[Official Fiund website](https://fiund.com/) · [Fiund on Hugging Face](https://huggingface.co/Fiund)

Fiund helps AI teams scope and source training data across speech, podcast audio, real photography, video, first-person video, robot learning, enterprise documents and call records. Its specialist websites provide modality-specific specifications and evaluation resources. Availability, sample scope, participant permissions and commercial use are confirmed for each project. Buyer and supplier identities remain confidential.

## Specialist websites

- [Data Egocentric](https://dataegocentric.com/) — Egocentric and first-person video
- [Business Datasets](https://businessdatasets.com/) — Enterprise documents and business workflows
- [Video Training Data](https://videotrainingdata.com/) — Real video training data
- [Photo Datasets](https://photodatasets.com/) — Real photographic image data
- [Robotic Datasets](https://roboticdatasets.com/) — Robot learning and human motion data
- [Call Datasets](https://calldatasets.com/) — Call audio and transcript data
- [Podcast Datasets](https://podcastdatasets.com/) — Podcast archives and conversational audio
- [AIPodcast](https://www.aipodcast.io/) — Speech data for ASR and diarization

## Inspectable public references

- [Photo measurements and manifest](https://photodatasets.com/source-studies/studio-environment-photo-reference/)
- [Video properties and montage limitations](https://videotrainingdata.com/source-studies/studio-montage-reference/)
- [Speech excerpt and automatic-transcript limitations](https://www.aipodcast.io/source-studies/solo-speech-asr-reference/)
- [Podcast package lineage](https://podcastdatasets.com/source-studies/solo-podcast-source-package/)

Public examples are editorial references, not a blanket training license. The speech and podcast package studies reference the same underlying excerpt, not two unique recordings. No buyer or supplier identities or private contracts are included.

Contact: hello@fiund.com

## Measured reference inventory

These three JSON manifests describe already-public, first-party editorial examples. Raw media is not mirrored in this repository.

| Manifest | What was measured | Limitation |
| --- | --- | --- |
| [Photos](manifests/photos.json) | Seven JPEG files, each with dimensions, byte count and SHA-256 | Camera views of three named studio set groups; not seven independent environments |
| [Video](manifests/video.json) | 14.25 seconds; H.264, 1280×720, 24 fps; 1,750,092 bytes | Silent edited montage, not an uninterrupted trajectory |
| [Speech](manifests/speech.json) | 13.525333 seconds; mono MP3, 48 kHz; 162,360 bytes, plus text and cue references | Automatic transcript, not gold-standard ASR labels or forced alignment |

The speech and podcast studies use the **same excerpt**. Their durations must not be summed as separate audio inventory. Across the three manifests there are eleven distinct referenced files: seven photos, one video, one audio excerpt, one text transcript and one cue file. No buyer or supplier collection is released here.

## Validate the metadata

Run `python3 verify_reference.py` from this repository. Python's standard library is sufficient. It checks the local manifests for file counts, positive byte counts, hash syntax, expected measured video/audio properties and unique-file accounting. It does not download recordings or establish copyright ownership, participant consent, training permission, annotation accuracy or corpus availability.

For a new data project, check source scope, participant permissions, use restrictions, uniqueness, delivered file properties and annotation quality separately. A file checksum establishes byte identity; it does not establish license rights. Filename camera groups are not scene-level dataset splits. Edited montage frames do not demonstrate synchronized action logs or calibrated sensor data.

## Publication and permission scope

Prepared November 14, 2026 from the linked public Fiund reference studies. This repository is Fiund-authored documentation, not an independent review, benchmark or third-party endorsement. Public playback is not an unrestricted data license. No open license is granted here for source photographs, recordings, transcripts, voices or likenesses. Confirm a proposed commercial or research use directly with Fiund.
