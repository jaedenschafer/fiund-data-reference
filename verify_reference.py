"""Validate the public reference manifests; does not download media or grant rights."""
from pathlib import Path
import json
import re


def check(root):
    photos = json.loads((root / 'manifests/photos.json').read_text())
    video = json.loads((root / 'manifests/video.json').read_text())
    speech = json.loads((root / 'manifests/speech.json').read_text())
    assert photos['file_count'] == len(photos['items']) == 7
    assert all(x['width'] > 0 and x['height'] > 0 for x in photos['items'])
    assert video['bytes'] == 1750092
    assert float(video['probe']['format']['duration']) == 14.25
    streams = video['probe']['streams']
    assert len(streams) == 1, 'Reference montage has one silent video stream'
    assert (streams[0]['codec_name'], streams[0]['width'], streams[0]['height'],
            streams[0]['r_frame_rate']) == ('h264', 1280, 720, '24/1')
    audio = [x for x in speech['items'] if x['file'].endswith('.mp3')]
    assert len(audio) == 1 and audio[0]['bytes'] == 162360
    assert float(audio[0]['probe']['format']['duration']) == 13.525333
    assert audio[0]['probe']['streams'][0]['sample_rate'] == '48000'
    assert audio[0]['probe']['streams'][0]['channels'] == 1
    items = photos['items'] + [video] + speech['items']
    assert len(items) == len({x['file'] for x in items}) == 11
    for item in items:
        assert item['bytes'] > 0
        assert re.fullmatch(r'[a-f0-9]{64}', item['sha256'])
    assert all(x['permission_scope'] for x in [photos, video, speech])
    print('PASS: 3 metadata manifests; 11 distinct referenced files.')
    print('This checks metadata structure and recorded facts, not license or data quality.')


if __name__ == '__main__':
    check(Path(__file__).resolve().parent)
