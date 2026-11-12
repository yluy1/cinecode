from PIL import Image
import numpy as np,glob,json
fs=sorted(glob.glob('frames/*.png')); prev=None; ds=[]
for f in fs:
 a=np.array(Image.open(f).convert('RGB')).astype(np.int16)
 if prev is not None: ds.append(float(np.abs(a-prev).mean()))
 else: first=a
 prev=a
print(json.dumps({'frames':len(fs),'first_last':float(np.abs(first-a).mean()),'mean_change':float(np.mean(ds))}))
