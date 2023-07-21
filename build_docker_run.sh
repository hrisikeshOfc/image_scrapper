echo [$(date)]: "START"
echo [$(date)]: "building docker image"
docker build -t image_scrapper .

echo [$(date)]: "starting the container"
docker run -d -p 5000:5000 --name image_scrapper image_scrapper:latest

echo [$(date)]: "END"