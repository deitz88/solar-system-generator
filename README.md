# Solar System Generator

SSG is an amalgamation of coding and my love of space. Within this repo, there is the landing page, generative solar system page with options, and a separate nebula generator. have fun and try giving it a go!

This is a 2-for-1 generative project, build for a generative-art bounty. 

While this is a work in progress to make this a Web-App based version, the terminal command based version works as outlined below. 


## Usage

Clone the repo. 

You must install the `pycairo` dependency:


```bash
pip install pycairo
```

navigate to the `Terminal-Based` dir and run:   (for solar system generation)

```bash
python3 generate.py 
````

or for nebula generation:
```bash
python3 nebula_generator.py
```
Generations will be rendered in the `Examples` folder inside the `Terminal-Based` dir

## Examples:
#### Solar System:
<p align="left" margin='10px'>
<img src="https://user-images.githubusercontent.com/16360065/134600719-1305e52e-7e23-4fd1-bb63-b0f3b1cea078.png" width=40% height=40% />
<img src="https://user-images.githubusercontent.com/16360065/134600723-b4b78078-19ff-498c-a9b9-29d18c3efa36.png" width=40% height=40% />
  </p>
<p align="left" margin='10px'>
<img src="https://user-images.githubusercontent.com/16360065/134600730-d992f99e-7b9f-4cf3-b446-44884330021b.png" width=40% height=40% />
<img src="https://user-images.githubusercontent.com/16360065/134601315-c16e65d9-4829-4b9c-92c4-9678b38b0f30.png" width=40% height=40% />
  </p>



#### Nebulas:
<p align="left" margin='10px'>
<img src="https://user-images.githubusercontent.com/16360065/134600779-3f83e53e-b1a3-4893-aa79-a71ca30d3863.png" width=40% height=40% />
<img src="https://user-images.githubusercontent.com/16360065/134600786-db61b2c1-b36d-4a30-a18a-5498b3197159.png" width=40% height=40% />
  </p>
<p align="left" margin='10px'>
<img src="https://user-images.githubusercontent.com/16360065/134601552-f9525ef9-25b9-4af8-974c-e163fdaf30e4.png" width=40% height=40% />
<img src="https://user-images.githubusercontent.com/16360065/134601685-3c83864b-252f-45df-9f98-d8965c80690f.png" width=40% height=40% />
  </p>
  
## Code Snippets:
##### top-level color selection for nebula: 
```bash
float_gen = lambda a, b: random.uniform(a, b)

colors = []
for x in range(10):
    colors.append((0,0,0))
for i in range(15):
    colors.append((float_gen(.1, 1), float_gen(.1, float_gen(.5, .65)), float_gen(.1, 1)))
    colors.append((0, 0, 0))
```
<h6>the above code favors red and blue, creating deep purples, reds, and blues. </h6>


##### Favorite snippet from solar system generator:
```bash
def points_on_circum(r, width, height, border):
    points_positive = []
    for x in range(0, 100):
        xcoord = (math.cos(1.8*x) * r) + width/2
        ycoord = -1 * (math.sin(1.8*x) * r) + height - border
        if((xcoord > 0 and xcoord < width - border+50) and (ycoord > 0 and ycoord < height - border + 100)):
            points_positive.append((xcoord, ycoord))
    return points_positive
```
<h6>the above code finds all avail points on the circum of the generated arcs, and will randomly place a planet on its arc.</h6>

