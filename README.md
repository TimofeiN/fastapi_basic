# FastAPI basic app


#### BUILD
`docker build -t fastapi_app .`  

#### ADD PACKAGE
`docker run -it -v $(pwd)/app:/home/appuser/app fastapi_app bash`\
`poetry add <package_name>`  

#### RUN APP
`docker run -p 8000:8000 fastapi_app`  