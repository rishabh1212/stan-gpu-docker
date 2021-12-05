git clone https://github.com/facebook/prophet
cp setup.py requirements.txt prophet/python/
cp models.py prophet/python/prophet/
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
DOCKER_BUILDKIT=1 docker build -f dockerfile-gpu . -t prophet-gpu:1.0.
# docker run --gpus all -it prophet-gpu:1.0.0
