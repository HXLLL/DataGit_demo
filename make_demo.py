import os

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

cmd = "/home/hxl/Repo/DataGit_online/bin/dg.sh"
repo_dir = "/home/hxl/demo/imagenet_corrupted"
os.chdir(repo_dir)

for method in d.keys():
    for s in range(1, 6):
        print(f"{cmd} checkout -v 2")
        os.system(f"{cmd} checkout -v 2")
        print(f"{cmd} branch --name {method}_{s}")
        os.system(f"{cmd} branch --name {method}_{s}")
        print(f"{cmd} checkout -b {method}_{s}")
        os.system(f"{cmd} checkout -b {method}_{s}")
        print(f"{cmd} transform -m '{method}_{s}' /home/hxl/demo/transformer/{method}_{s} entry.sh")
        os.system(f"{cmd} transform -m '{method}_{s}' /home/hxl/demo/transformer/{method}_{s} entry.sh")
        print(f"{cmd} commit -m '{method}_{s}'")
        os.system(f"{cmd} commit -m '{method}_{s}'")
        print(f"{cmd} push -b {method}_{s}")
        os.system(f"{cmd} push -b {method}_{s}")

