import subprocess as s,numpy as np,json
out='out/salon-canli/';res={}
for name in ['salon-canli.mp4','salon-canli.webm','efekt-katmani.webm']:
 p=s.Popen(['ffmpeg','-v','error','-i',out+name,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=s.PIPE)
 prev=None;ds=[];n=0
 while True:
  raw=p.stdout.read(1920*1080*3)
  if not raw:break
  a=np.frombuffer(raw,dtype=np.uint8).astype(np.int16)
  if prev is None:first=a
  else:ds.append(float(np.abs(a-prev).mean()))
  prev=a;n+=1
 p.wait();res[name]={'frames':n,'first_last_rgb_mae_255':float(np.abs(first-a).mean()),'adjacent_rgb_mae_255':float(np.mean(ds))}
open(out+'decoded-metrics.json','w').write(json.dumps(res,indent=2));print(res)
