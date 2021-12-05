## Background
- For many reasons realted to convenience around using stan with OPENCL
- Easy for beginer to directly get into coding aspect without worrying about infra

## Test
```
# Problems around container not starting
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

DOCKER_BUILDKIT=1 docker build -f dockerfile-gpu . -t stan-gpu:1.0.0
docker run --gpus all -it prophet-gpu:1.0.0
# Testing Force compile to use opencl
python /home/prophet/example.py 1 c
```
