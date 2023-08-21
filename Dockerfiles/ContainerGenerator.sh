sudo docker login

cd BaseElastic
sudo docker build -t jcardonar/elasticjobs .
sudo docker push jcardonar/elasticjobs
cd ..

cd Controller
sudo docker build -t jcardonar/controller .
sudo docker push jcardonar/controller 
cd ..

