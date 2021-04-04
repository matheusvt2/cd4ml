# CD4ML project

Project for studying a way to decouple machine learning model from its app.

## Getting Started

Please go to my article on Medium, that's where I describe step by step the purpose of this project https://matheusvt.medium.com/deploying-a-decoupled-ml-model-an-application-on-aws-31dfd44beaa3

Project architecture:
![Project architecture](imgs/arquitetura-real.png "Project architecture")
### Project structure

```
├── app # Application folder, to use on application pipeline
│   ├── app.py
│   ├── appspec.yml # CodeDeploy file
│   ├── buildspec.yml # CodeBuild file 
│   ├── dockerfile
│   ├── requirements.txt 
│   ├── scripts
│   │   ├── kill_container.sh
│   │   ├── load_image.sh
│   │   └── start_container.sh
│   ├── static
│   │   └── images
│   │       ├── iris_setosa.png
│   │       ├── iris_versicolor.png
│   │       └── iris_virginica.png
│   └── templates
│       ├── home.html
│       ├── layout.html
│       └── predict.html
├── data
│   └── iris.csv
├── experimentation.ipynb
├── imgs
│   └── serving.png
├── LICENSE.md
├── modeling.py
├── output
│   └── randomforest_model.pkl
└── readme.md
```

### Prerequisites

What things you need to install the software and how to install them


- AWS account — May be some costs, be aware!
- 8 GB RAM / 100 GB Disk laptop.
- Application and Model.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Matheus Villela Torres* - *Initial work* - [matheusvt2](https://github.com/matheusvt2)

See also the list of [contributors](https://github.com/matheusvt2/cd4ml/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **app**

https://medium.com/@nutanbhogendrasharma/deploy-machine-learning-model-with-flask-on-heroku-cd079b692b1d


* **cd4ml concept**

https://martinfowler.com/articles/cd4ml.html

* **set AWS git credentials**

https://docs.aws.amazon.com/pt_br/codecommit/latest/userguide/setting-up-https-unixes.html

* **codepipeline hands-on**

https://www.youtube.com/watch?v=kaZOF4EEPqk

* **mlflow image** 

https://github.com/matheusvt2/mlflowserver

First run the mysql server
```
docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_TCP_PORT=3306 -p 3306:3306  mysql:latest mysql --default-authentication-plugin=mysql_native_password
```
Now, just start a container setting the BACKEND_URI, MLFLOW_PORT and ARTIFACT_ROOT as follow:
```
docker run -it --rm --name mlflow -p 5000:5000 -e BACKEND_URI=mysql+pymysql://root:root@192.168.15.17:3306/mlflow -e MLFLOW_PORT=5000 -e ARTIFACT_ROOT=/mlflow/mlflow-artifacts  matheusvt/mlflowserver:1.12.1
Artifact Root is /mlflow/mlflow-artifacts
```

