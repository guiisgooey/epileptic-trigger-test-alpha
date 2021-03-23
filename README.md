# Gif and Video Epileptic Trigger Test (Alpha)

This program is currently a work in progress and all included methods and modules are not guaranteed to last.
The purpose of this program is to provide a way to detect if a gif/video may be harmful to users with epilepsy,
light sensitivity, or other sensitivities in order to provide accesibility for these users.

### Prerequisites

The following software is required to run this program:

```
Python Version 3.9 or later
```

```
Pillow Version 8.1.2
```

```
OpenCV-Python Version 4.5.1.48
```

### Installation and Running

#### 1. Clone the repository

#### 2. Create a Python Virtual Environment:

On Windows:

Open the desired location of your virtual environment in the command prompt and run the following line, where 'environment_name' is the desired named of your virtual environment:

```
python -m venv environment_name
```

On Mac/Linux:

Open the desired location of your virtual environment in the terminal and run the following line, where 'environment_name' is the desired named of your virtual environment:

##### Notice: If you do not desire to create a virtual environment to run this program, you may use your main python interpreter to install the requirements and run the program.

```
$ python3 -m venv environment_name
```

#### 3. Activate the Virtual Environment:

On Windows:

Run the following command in the directory of the repository in the command prompt:

```
environment_name\Scripts\activate.bat
```

On Mac/Linux:

Run the following command in the directory of your virtual environment in the terminal:

```
$ source environment_name/bin/activate
```

#### 4. Download the prerequisites listed in requirements.txt using the following line of code:

```
$ pip install -r requirements.txt
```

To verify that the requirements are installed you may run:

```
$ pip list
```

#### 5. Run main.py

Windows:

Run the following code in the repository's directory in the terminal:

```
py main.py
```

Mac/Linux:

Run the following code in the repository's directory in the terminal:

```
$ python3 main.py
```

##### Notice: You may also run the code in any IDE that supports Python aslong as scripts are enabled on your system. You do not need scripts enabled if a virtual environment is not being utilized.

### epilepsy_test.py

epilepsy_test.py provides the functions used to determine if a gif may be harmful to a viewer with epilepsy or light sensitivity. Helper methods and inner functions within epilepsy_test.py are only there to make the code appear cleanlier.

### epilepsy_test_video.py (work-in-progress)

epilepsy_test_video.py currently provides the base frame test used in epilepsy_test.py converted to be used for videos. Further tests will be added in the future such as the split test and a sound level test.

### main.py

The purpose of main.py is to provide sample driver code for the tests provided in epilepsy_test.py

### test.py

The purpose of test.py is to verify that functions within epilepsy_test.py are working as intended as to not throw an exception during run time.

## Authors

- **Andrew Wagner** - [GuiIsGooey](https://github.com/guiisgooey)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Sources

- [Pillow](https://pillow.readthedocs.io/en/stable/) for insight into how the PIL library works for processing and mutating images.
- [OpenCV](https://pypi.org/project/opencv-python/) for insight into how the OpenCV python library works for processing videos.
