FROM python:3.12-alpine

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

# IF you wan run api then follow the steps.
# 1. go and change the configurion under smart_manager.json >> settings >> api == true
# 2. go and edit smart_manager.json >> settings >> api-server-config >> host == "0.0.0.0"
# 3. uncomment the below code (to expose the port 8000) and then build the image
# ```
# EXPOSE 8000
# ```
# 4. then run the image as container by typing the following command in your terminal
# docker run -p 8000:8000 [image-name:tag]
# Note: change the [image-name:tag] with actual value.s
# 5. then go to your localhost:8000 for asseccing the api untill the container is running.

CMD ["python", "SmartManager/main.py"]