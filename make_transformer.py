import os
import shutil
import collections

d = collections.OrderedDict()
d['Gaussian_Noise'] = None
d['Shot_Noise'] = None
d['Impulse_Noise'] = None
d['Defocus_Blur'] = None
d['Glass_Blur'] = None
d['Motion_Blur'] = None
d['Zoom_Blur'] = None
d['Snow'] = None
d['Frost'] = None
d['Fog'] = None
d['Brightness'] = None
d['Contrast'] = None
d['Elastic'] = None
d['Pixelate'] = None
d['JPEG'] = None

d['Speckle_Noise'] = None
d['Gaussian_Blur'] = None
d['Spatter'] = None
d['Saturate'] = None


for k in d.keys():
    for severity in range(1,6):
        d = "transformer/%s_%d" % (k, severity)
        if not os.path.exists(d):
            os.mkdir(d)
        shutil.copy('transformer/make_imagenet_c.py', d)
        entry_d = os.path.join(d, "entry.sh")
        with open(entry_d, "w") as f:
            f.write(
f"""
#!/bin/bash

BASEDIR=$(dirname "$0")
cd $BASEDIR
python make_imagenet_c.py $@ {k} {severity}
""")
        os.system(f"chmod a+x {entry_d}")
