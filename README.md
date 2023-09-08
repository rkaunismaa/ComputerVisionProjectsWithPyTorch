# ComputerVisionProjectsWithPyTorch

Walk through of the book 'Computer Vision Projects with PyTorch" by Kulkarni, Shivananda, Sharma (Apress 2022)

The repo can be found [here](https://github.com/apress/computer-vision-projects-with-pytorch)

## Wednesday, August 30, 2023

3:35pm Let's use the docker container 'hfpt_July21' for this project, shall we ... This container was spun up from the image hfpt:20230721, which was created from the image hfpt:20230721 ... 'docker pull huggingface/transformers-pytorch-gpu' on July 21, 2023.

I am going to type in as much of the code as possible, because there is way more to learn, through the practical exercise of typing in the code for yourself rather than copy/paste it from a repo. 

Right. Gotta first do the ..

git config user.email 'your email'
git config user.name 'your username'

... before I can commit. Done. First commit done. 

4:03pm Skimmed through the first chapter. They try to hammer through a lot of details regarding convolutions in a CNN.  Gonna continue on with Chapter 2.

Need to pull down the data from this [Chest X-ray Images](https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images) Kaggle competition ...

The book code uses torchsummary to display information about the model, but that code base has been deprectated with torchinfo, so I am going to ...

pip install torchinfo

... and use that instead.

7:12pm The ImageClassification.ipynb all works. Nice! ... Resume at page 69, 'The Second Variation of the Model' tomorrow ... 

## Thursday, August 31, 2023

10:43am Continuing from page 69. Running the same notebook as above but with changes to JUST the transformations on the training data.

11:35am I was running the notebook that ran yesterday on docker hfpt_July21 and it kept crashing. A Reboot solved the crashing problem. 

## Friday, September 1, 2023

4:00pm That failing notebook (Chapter_02/cv_reg_batch_aug_2.ipynb) was because it was running out of computer ram. Increasing the swapfile from 2gb to 32gb and reducing the number of epochs from 15 to 12 allowed the notebook to run without errors. And this was running under the new docker container created off of the 'docker pull huggingface/transformers-pytorch-gpu' image I pulled down on Wednesday. 

So keep this in mind! Always pay attention to cpu memory and gpu memory when you run a notebook.

## Sunday, September 3, 2023

6:25pm Continuing with chapter 3 "Building an Object Detection Model"

6:37pm Looks like we need to download assets from the [OpenCv repo](https://github.com/opencv/opencv/tree/master/data/haarcascades) but the names are different from what is shown in the book. I am going to pull down what I think are the assets with the most similar names from the book and give them a go ... sigh ... the assets are already part of the repo for this book! ... 

7:13pm hmm I can't access my video camera using opencv in the first notebook of chapter 3 ... gonna pass and move on.

## Monday, September 4, 2023

2:39pm Continuing with chapter 3 ... Hmm the book uses Yolo V3 but a quick search reveals there is now a YOLO V7! Gotta wonder about the value of attempting to use V3 when we have V7!

2:47pm Hah! Nope! There is a [YOLO V8](https://pypi.org/project/ultralytics/) At this point I wonder if I should just mess with V8 ... 

2:54pm Ultralytics offers a [docker image](https://hub.docker.com/r/ultralytics/ultralytics) Yeah, what the hell, let's pull er down and see what we get!

4:30pm Damn ... its a 12.8gb docker image! Gonna give er a spin later ...

## Tuesday, September 5, 2023

1:09pm Yeah, grinding through chapter 3 ... 

2:31pm Actually, gonna take [facenet-pytorch](https://github.com/timesler/facenet-pytorch) for a spin ... and yeah, will just add it here, cuz why not?

3:30pm Damn ... pip install mmcv ... gets stuck at Building wheel for mmcv (setup.py) ... gonna let er run and see if it actually concludes ... In the mean time, gonna get started with 'An Introduction to Statistical Learning with Applications in Python' ...

4:05pm Damn ... pip install mmcv only finished now!! I am glad I waited! ...ok gonna continue messing with this facenet-pytorch stuff ... 

5:33pm some progress made but then getting stuck ... 

## Wednesday, September 6, 2023

9:54am Continuing to try to get FaceNetPyTorch/lfw_evaluate.ipynb to run ...  

12:51pm OK ...  gonna step away from dicking with the facenet-pytorch code in my own docker image hfpt_Sept1 and pull down the docker image the author of the code has created ... https://github.com/timesler/docker-jupyter-dl-gpu

Jupyter Lab
docker run --rm -p 8888:8888 -v <local path>:/home/jovyan/ timesler/jupyter-dl-gpu:latest jupyter lab

... which of course needs to change to ... 

docker run --rm -p 8888:8888 -v /home/rob/Data/Documents/Github/rkaunismaa/ComputerVisionProjectsWithPytorch:/home/jovyan/ timesler/jupyter-dl-gpu:latest jupyter lab

2:38pm OK ... so I ran that image with ...

docker run --name fn_pt --gpus all -it --user 0 -v /home/rob/Data/Documents/Github/rkaunismaa:/home/jovyan/ --env HF_DATASETS_CACHE=/home/rob/Data2/huggingface/datasets --env TRANSFORMERS_CACHE=/home/rob/Data2/huggingface/transformers -p 8888:8888 timesler/jupyter-dl-gpu:latest bash

... and then once I had the bash prompt, I ran ...

jupyter lab --notebook-dir=/home/jovyan --ip 0.0.0.0 --no-browser --allow-root

AND that one notebook that was not working in the hfpt_Sept1 container DID run! ... yeah, pytorch was at 1.3.1 ... so no wonders why it failed

## Thursday, September 7, 2023

1:49pm Been reading up on vector databases and have concluded what I want to try is [DeepImageSearch](https://pypi.org/project/DeepImageSearch/). This project builds on top of [Facebook AI Similarity Search](https://faiss.ai/). Gonna install this to the hfpt_Sept1 container and give er a go ... And yeah, this again deviates from the original intent of this repo, but meh ... 

Right ... DeepImageSearch is NOT a vector database, but "DeepImageSearch is a powerful Python library that combines state-of-the-art computer vision models for feature extraction with highly optimized algorithms for indexing and searching." ... I MAY look into trying a vector database such as [chroma](https://www.trychroma.com/) or [milvus](https://milvus.io/) after I get a better understanding on how to do image similarity search with DeepImageSearch. 

4:41 OK ... Ran all the MyMatch images through DeepImageSearch, asked it to find similar images, and it appeared to work! It is still not using the GPU even though I loaded faiss-gpu to the container ... meh for now.

4:49pm It looks like [Faiss Getting Started](https://github.com/facebookresearch/faiss/wiki/Getting-started) resource could be good for digging into faiss. I think the next thing to try is to JUST use faiss and not DeepImageSearch in a notebook. I really want to see if I can get the gpu engaged!

## Friday, September 8, 2023

8:56am DeepImageSearch is just one python file of 278 lines of code. A Load_Data class and a Search_Setup class. Simple stuff! It looks like a good resource to study to understand how to work with faiss.. 

9:33am Again, stuff on [DeepFace](https://pypi.org/project/deepface/) keeps coming up. Yeah. Gonna give this a go today.

9:37am Right. DeepFace uses TensorFlow. So if I want to play with this, then I need to switch to a docker image with tensorflow. ugh ... wow, I have no tensorflow containers to begin with. Well then, let's run 'docker pull tensorflow/tensorflow:latest-gpu-jupyter' shall we ... 

9:44am Hmm DeepFace was created by Facebook in 2014 but today uses tensorflow ... ?
