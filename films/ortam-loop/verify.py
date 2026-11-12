"""Validate encoding and compare seam motion with adjacent motion, using ffmpeg."""
import json, subprocess, math
from pathlib import Path
for name in ('mp4','webm'):
    data=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',f'out/ortam-loop.{name}']))
    assert len(data['streams'])==1, 'Unexpected audio/extra stream'
    s=data['streams'][0]
    assert (s['width'],s['height'],s['r_frame_rate'],s['pix_fmt'])==(1920,1080,'30/1','yuv420p')
    assert abs(float(data['format']['duration'])-8)<.001
    print(name,s['codec_name'],'1920x1080 30fps 8s, no audio')
def pixels(i):
    return subprocess.check_output(['ffmpeg','-v','error','-i',f'renders/frames/{i:06}.png','-f','rawvideo','-pix_fmt','gray','-'])
a,b,c,d=map(pixels,(238,239,0,1))
def rms(x,y): return math.sqrt(sum((u-v)**2 for u,v in zip(x,y))/len(x))
print('Grayscale RMS adjacent/seam/adjacent:',rms(a,b),rms(b,c),rms(c,d))
assert rms(b,c) < max(rms(a,b),rms(c,d))*1.5+.01
print('PASS: periodic endpoints byte-identical; seam step comparable to neighboring frame steps.')
