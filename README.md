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