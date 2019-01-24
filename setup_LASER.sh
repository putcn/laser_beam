# install conda
wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b -p /root/miniconda
export PATH="/root/miniconda/bin:$PATH"
source /root/miniconda/bin/activate

export LASER=/LASER

# install faiss
conda install -y faiss-cpu -c pytorch

# install pytorch 1.0
conda install -y pytorch-cpu torchvision-cpu -c pytorch

# for Greek and Chinese segmenter
yes | pip install transliterate jieba

cd $LASER
bash ./install_models.sh
bash ./install_external_tools.sh



