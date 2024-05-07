# NOTE TO PROFESSSOR: 
I created an entirely new repository to submit code, as I was getting some git conflict issues and was running low on time.
This was the previous repository: https://github.com/insp7/right-whale-recognition. It has all the commits and version history (incase if you were wondering why does this repo has few commits)
Kindly consider this code. This is similar to that repo, with just me adding citations for the code and this one does not have a few of the newly explored preprocessing approaches for which I did not train the model anyways.

# Right Whale Recognition -- Kaggle Challenge (2015-17)
To identify endangered right whales in aerial photographs 

From Wikipedia:
Right whales comprise three species of substantial baleen whales within the genus Eubalaena:
the North Atlantic right whale (E. glacialis), the North Pacific right whale (E. japonica), and the Southern right whale (E. australis).

### Annotation Credits

<code>annotations/whale_faces_Vinh.json</code> - [Annotations by Vinh Nguyen](https://www.kaggle.com/competitions/noaa-right-whale-recognition/discussion/17421) <br />
<code>annotations/train_with_points.csv</code> - [Annotations from Anil Thomas](https://www.kaggle.com/competitions/noaa-right-whale-recognition/discussion/17555). Anil Thomas' project [repo](https://github.com/anlthms/whale-2015)


NOTE: I had tried to use these to further preprocess the data, however, that approach is incomplete and have not trained the model on that preprocessed data. It can be performed as future work.

### Code & Structure Explanation

Initially I trained a naive CNN model for this problem. It is present in the file <code>naive-cnn.ipynb</code>.

Later on, I explored the Vision Transformer(ViT) approach and trained a ViT model.
The code for data preparation can be found in <code>prepare_data_for_vision_transformer.ipynb</code>
The code for training the Vision Trasnformer model can be found in <code>train_vit.ipynb</code>
The code for testing(performing inference) the vision transformer model can be found in <code>test_vit.ipynb</code>

NOTE: I have not uploaded the <code>dataset</code> directory. It contains the image data and appropriate csv files. [All data sourced from the kaggle challenge]

The files <code>extract_bonnet_blowhead.ipynb</code>, <code>extract_bounding_box.ipynb</code> have code to perform the preprocessing which was a popular approach in the top 10 solutions. However, while the preproecssing is performed, I have not trained my model on the preprocessed data. Hence, KINDLY IGNORE these files and you may not consider these for this submission.

<code>img_scale_ratio_info.csv</code> contains the scaling ratio by which the image was initially resized.
<code>notes.txt</code> are just some notes I prepared for myself to assist working on this project.