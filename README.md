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

