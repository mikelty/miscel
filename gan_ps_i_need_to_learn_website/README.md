### Use GAN to photoshop people
- 'i need to learn myself' is a website in china that teaches people
 stuff (adobe ae, etc.) for free. they have a hundred or so images
 of their vip students holding a sign that says 'i need to learn myself 
 website'. 
- i'm trying to use cyclegan (keras-gan or tensorflow) to photoshop random
dudes so they it looks like they're holding that sign.
- cyclgan can be very tricky to train, as is the case for all gans. so
don't hope to find da vinci here.
- i do not intend any malicious or commercial use for this thing, had it 
worked well. neither should you, or anyone really for that matter.
- crawl.py crawls pictures on that website and random dudes' head shots.
- gen.py is the gan that does the work.
- version is tf 2.3.0 and keras 2.3.0, windows 10, python 3.7.