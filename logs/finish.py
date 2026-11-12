import subprocess as s, time,glob,json
from PIL import Image,ImageDraw
import numpy as np
while len(glob.glob('frames-final/*.png'))<240 or len(glob.glob('effects/*.png'))<240: time.sleep(5)
out='out/salon-canli/'
for folder,name,codec,crf in [('frames-final','salon-canli.mp4','libx264','18'),('frames-final','salon-canli.webm','libvpx-vp9','24'),('effects','efekt-katmani.webm','libvpx-vp9','24')]:
 cmd=['ffmpeg','-v','error','-y','-framerate','30','-i',folder+'/%06d.png','-c:v',codec,'-crf',crf,'-pix_fmt','yuv420p','-threads','2']
 cmd+=['-movflags','+faststart','-preset','fast','-x264-params','keyint=1'] if codec=='libx264' else ['-b:v','0','-deadline','good','-cpu-used','4','-g','1']
 s.run(cmd+[out+name],check=True)
fs=sorted(glob.glob('frames-final/*.png')); ds=[];prev=None
for f in fs:
 a=np.asarray(Image.open(f).convert('RGB'),dtype=np.int16)
 if prev is not None:ds.append(float(np.abs(a-prev).mean()))
 else:first=a
 prev=a
metrics={'first_last_source_rgb_mae_255':float(np.abs(first-a).mean()),'adjacent_source_rgb_mae_255':float(np.mean(ds)),'frames':240,'fps':30,'duration':8,'strength':2}
open(out+'metrics.json','w').write(json.dumps(metrics,indent=2))
sheet=Image.new('RGB',(1280,360))
for k,i in enumerate([0,34,68,102,136,170,204,239]):sheet.paste(Image.open(fs[i]).resize((320,180)),((k%4)*320,(k//4)*180))
sheet.save(out+'kontakt.jpg')
print(metrics,flush=True)
