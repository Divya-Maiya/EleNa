# Simplified Elevation Navigation


### Download and Install Dependencies 
1. Navigate to the folder where your project folder needs to be hosted and run the following commands:

```
$ git clone https://github.com/Divya-Maiya/EleNa.git
$ cd EleNa
```

### Requirements 
To download the required requirements for this project, run the following
```
$ pip install -r requirements.txt
```

### How to run the Project
1. Start by running the backend by executing the following commmands: 

```
$ python server.py
```
Upon successful execution of the above command, a Python backend server should be running.

2. To get the UI for the project, run the following: 
```
$ cd src/frontend
$ npm install
$ npm start
```

3. You should be able to see a browser window open to `http://localhost:3000` and should display the screen mentioned in the Output/Screenshots section of this ReadME. 


## How to test the Project
For testing, **Mockito**, **unittest** and **pytest** frameworks are used.

To run all unit tests, run the following command 
```
$ cd test
$ python -m unittest
$ cd ..
```

## Code Coverage Statistics
To get the code coverage related statistics, please run the following in `EleNa/` 
```
$ coverage run -a -m --source=src/ --omit="*src/frontend*,*/test*" pytest -v -m unittests
$ coverage report -m  --omit="*src/frontend*,*/test*"
$ coverage html --omit="*src/frontend*,*/test*"
``` 

## Best Programming Practices followed 
1. **Client-Server Architecture**: Interaction between JavaScript frontend and Python backend follows a Client-Server Architecture pattern.
2. **Model-View-Controller Architecture**: The Python backend follows an Model-View-Controller Architecture Pattern.
3. **Design Pattern**: A **template design pattern** is used by the algorithms (A*, Dijkstra's and BFS) implemented.
4. **Modularity / Code Organization**: The code has a package structure that shows modularity.
5. **Encapsulation**: Encapsulation has been achieved as the code is organized into classes
6. **Reusability**: Since the code is modular, it allows for reusability. 
7. **Test Suite**: A detailed test-suite has been included with a code-coverage of ~85%
8. **Type Safety / Exception Handling**: Exception handling has been included using try/except/raise blocks. 
9. **Version Control**: From the beginning of the project, **Git** has been used as a version control system.
10. **Debuggability**: Logging statements have been added to ensure debuggability. 


## Results  

### Frontend Screenshots
#### Initial UI screen to take user input: 
![image](https://user-images.githubusercontent.com/91640174/144970011-59f6c8d2-98e4-463f-886f-13b7dc54234e.png)


#### UI display of Elevation Path Statistics
![image](https://user-images.githubusercontent.com/91640174/144970028-6a8edc32-fdf0-41e0-9203-1f6d6c9286d3.png)


#### The final output map with the trace of the path: 
![image](https://user-images.githubusercontent.com/91640174/144970048-152b0d3a-8ab0-4790-9a2d-d1f611fa7da6.png)


### Algorithm performance 
The following table summarizes the time taken by all the algorithms - 
| Algorithm     | A*    | Dijkstra's    |     BFS       |
| ------------- | ------------- | ------------- | ------------- |
| Shortest Path  | 1.00  | 1.20  | 1.3627  |


### Code Coverage 

![image](https://user-images.githubusercontent.com/91640174/144973057-a9dabe8a-b697-4c5a-8731-10d8e36f6c60.png)


### Usability Survey
https://forms.gle/wEAsN9YZ6NdXAHNX6

### System Architecture 
![System Architecture](./architecture.jpg)


