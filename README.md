# Laser_beam

docker file to quickly setup [fb laser](https://github.com/facebookresearch/LASER)

## Usage

### To build the image

```bash
git clone https://github.com/putcn/laser_beam.git
cd laser_beam
docker build . -t <your image tag here>
```

### To test/run the image

```bash
docker run --rm -it <your image tag here>
root@8e07f9e1ff2f:/# cd LASER/source/
python sentence_encoder_test.py
[[ 0.00441647 -0.00051235  0.00179952 ...  0.00338433  0.00369184
  -0.00079282]]
```

The output is the embedding for sentence "i like bananas"