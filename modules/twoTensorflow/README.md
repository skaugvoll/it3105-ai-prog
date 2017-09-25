## Module two - AI Prog.
# TensorFlow interface
__Sigve Skaugvoll & Thomas Wold__,  October 26, 2017.

### Task at hand:
Use Tensorflow to classify data from a wide variety of sources, including the classic MNIST benchmark
of digit images

A primary goal of this assignment is to streamline this trial-and-error process so that many different networks
can be experimented with in a short period of time. To this end, you will build an interface to Tensorflow
that facilitates these experiments

#### Requirements:
- system must be object-oriented and as modular as the classes Gann and Gannmodule in Tutor(ial)3.py
- No god damn recompilation...


### How to run
#### Prerequesits
- Python 3.5 or greater.
- TensorFlow
- mathplotlib

***How to make twoTensorFlow run***
I'm using virtualenv and virtualenvwrapper for python on unix.
So I installed tensorflow in my virtualenvironemnt. Thus I need to have the environment activated for tensorflow to be "installed" and working.

If i'm trying to run tensorflow code in a editor such as PyCharm and not from the terminal / command line. I need to let my IDEA know that I'm
using a virtual environment. To let Pycharm know, do the following:
- Hit the pyCharm on the statusline and then preferences or (cmd + ,)
- Then on the left, in the dropdown menu, chose your project : in my case it's IT3105 - AI PROG
- Then choose project interpreter.
- In the dropdown at the top, scroll to see if your virtualenv is listed there, if so, choose it.
- If its not listed, try hitting : show all, and see if it's there
  - If its not listed there either, we have to find it. click on the box with three dots. [...]
    - Choose local, and then navigate to where your virtual environemnt is "located" i.e : /users/<username>/.virtualenvs/<virtual env name>

Now when we have selected our virtual env as our project interpreter, we have to wait for the IDE to update, index and do IDE stuff... Usually takes about a couple of minutes.


### TensorFlow
https://www.tensorflow.org/
> TensorFlow™ is an open source software library for numerical computation using data flow graphs.
Nodes in the graph represent mathematical operations,
while the graph edges represent the multidimensional data arrays (tensors) communicated between them.
The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API.
TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization
for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.


#### API
https://www.tensorflow.org/api_docs/python/

### Mathplotlib
#### Installing
- pip install mathplotlib
- $ cd ~
- $ cd .matplotlib/
- # vim matplotlibrc
> backend: TkAgg

What this means is :
There's a directory located at "~/" root called matplotlib. so cd --> ~/.matplotlib.
Create a file called matplotlibrc --> ~/.matplotlib/matplotlibrc there and add the following code: backend: TkAgg
