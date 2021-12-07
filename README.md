# Simplified Elevation Navigation

## Downloading the Project 
To download the project, run the following:

```
$ git clone https://github.com/Divya-Maiya/EleNa.git
$ cd EleNa
```

## Requirements 
To download the requried requirements for this project, run the following
```
$ pip install -r requirements.txt
```

## How to run the Project
To get the entire application to work, start by running the backend by executing the following commmands: 

```
$ python server.py
```
Upon successful execution of the above command, a Python backend server should be runnin on port 5000. 

To get the UI for the project, run the following: 
```
$ cd src/frontend
$ npm install
$ npm start
```

Upon successful execution of the above commands, a browser window should open navigated to `http://localhost:3000` and should display the screen mentioned in the Output/Screenshots section of this ReadME. 

## How to test the Project
To run all unit tests, run the following command 
```
$ cd test
$ python -m unittest
$ cd ..
```

## Code Coverage Statistics
To get the code coverage related statistics, please run the following in `EleNa/` 
```
$ coverage run --source=src -m unittest discover -s test && coverage report
``` 

## Results  

### Frontend Screenshots
#### Initial UI screen to take user input: 
![image](https://user-images.githubusercontent.com/91640174/144970011-59f6c8d2-98e4-463f-886f-13b7dc54234e.png)

#### UI display of Elevation Path Statistics
![image](https://user-images.githubusercontent.com/91640174/144970028-6a8edc32-fdf0-41e0-9203-1f6d6c9286d3.png)

#### The final output map with the trace of the path: 
![image](https://user-images.githubusercontent.com/91640174/144970048-152b0d3a-8ab0-4790-9a2d-d1f611fa7da6.png)

### Code Coverage 


