# Laser_beam

docker file to quickly setup [fb laser](https://github.com/facebookresearch/LASER)

## Usage

You have 2 choices to use this image:

1. locally build your own
1. directly use the prebuilt one

### To build the image

```bash
git clone https://github.com/putcn/laser_beam.git
cd laser_beam
docker build . -t <your image tag here>
```

The output is the embedding for sentence "i like bananas"

### Run the prebuilt image

```bash
docker pull putcn/laser_beam
```

## To test/run the image

```bash
docker run --rm -it <your image tag here or putcn/laser_beam>
root@8e07f9e1ff2f:/# cd LASER/source/
root@8e07f9e1ff2f:/LASER/source# python sentence_encoder_test.py
Building prefix dict from the default dictionary ...
Dumping model to file cache /tmp/jieba.cache
Loading model cost 1.109 seconds.
Prefix dict has been built succesfully.
[[ 1.5119603e-03 -7.4540594e-06 -9.5952407e-04 ...  1.8422114e-02
   2.2908637e-02  1.3493976e-02]
 [ 8.6149918e-03  4.4238050e-03  4.7992445e-03 ...  2.9314332e-02
   3.9299182e-03  1.4128728e-02]]
similarity 0.685504
```

**Please note that LASER is installed in the directory of ```/LASER```**