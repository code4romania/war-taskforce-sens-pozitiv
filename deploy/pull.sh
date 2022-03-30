set -e

cd /home/ec2-user/war-taskforce-oncologie-pediatrica
git reset --hard HEAD
git pull

docker-compose build --build-arg ENVIRONMENT=development
docker-compose up -d
