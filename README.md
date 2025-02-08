# Cat-Dog-Classification

## How to Run

1. conda create -n catdog python=3.11.11 -y
2. conda activate catdog
3. pip install -r requirements.txt
4. python app.py
5. open in browser: http://localhost:8080/

docker images
docker ps -a
docker run -d -p 5002:5002 imageclassificationproject:latest 
docker stop $(docker ps -q) --- this will stop all running containers






