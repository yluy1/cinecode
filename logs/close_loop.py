import subprocess as s,pathlib
out=pathlib.Path('out/salon-canli')
for name in ['salon-canli.mp4','salon-canli.webm','efekt-katmani.webm']:
 src=out/name; ext=src.suffix
 for n,count in [('head',239),('first',1)]:
  s.run(['ffmpeg','-v','error','-y','-i',str(src),'-frames:v',str(count),'-c','copy','logs/'+n+ext],check=True)
 pathlib.Path('logs/concat.txt').write_text("file 'head"+ext+"'\nfile 'first"+ext+"'\n")
 cmd=['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','logs/concat.txt','-c','copy']
 if ext=='.mp4':cmd+=['-movflags','+faststart']
 s.run(cmd+['logs/closed'+ext],check=True)
 pathlib.Path('logs/closed'+ext).replace(src)
