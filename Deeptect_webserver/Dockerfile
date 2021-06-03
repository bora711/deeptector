FROM python:3                         
WORKDIR /usr/src/app                   

## Install packages 
COPY requirements.txt ./              
RUN pip install -r requirements.txt


## Copy all src files 
COPY . .                              

## Run the application on the port 8080 
EXPOSE 8000                            

#CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"] 
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Deeptect_webserver.wsgi:application"]