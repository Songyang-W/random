# random

### to setup the space
open your terminal

run 
```
mkdir -p ~/repos/random/
cd ~/repos/
git clone https://github.com/Songyang-W/random.git
```
after download the code, go to the directory by
`cd ~/repos/random/`
```
chmod 777 n2w.py
chmod 777 w2n.py
```

### use code
##### coordinate calculator
```cd ~/repos/random/```

neuroglancer to webknossos: 
`./n2w.py "x,y,z"` <br>
webknossos to neuroglancer: 
`./w2n.py "x,y,z"`

example: `./n2w.py "24162, 19126, 3245" `

[link to fine segmentated (15nm/pxl) testing model](https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5522665323364352)
[link to coarse segmentated (60nm/pxl) out of box model](https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6380158698127360)
