# ensemble-lvq
Ensemble lvq is based on the idea of transfer learning cum ensemble technique with lvq models.

# why?
The idea explores the possibility of harnessing transfer learning cum ensemble learning in lvq models. In this regard the hard voting scheme  and soft voting is applied to achieve the classification results. 

# How to use
To use ensemble-lvq, you must access learned prototypes from different models of lvq as transfered prototypes. So for a data set to be classified, apply the methods in ```hybrid.py``` script to obtain the predicated labels and the prediction probabilities as well as the votes which supports the outcomes. To exemplify, refer to ```test_iris_.py```  and ```test_wdbc_.py```. To try a simulation of performance accuracy refer to ```test_iris1.py``` and ```test_wdbc.py```. Please note that optimal performance in this regard is based on how well either your transfered prototypes or pre-trained models are trained.


# simulated results
Below is a simulation of the technique with the iris data set using the ```test_iris1.py```
![en1](https://user-images.githubusercontent.com/82911284/166089235-914ebcfb-2076-4ae3-8b15-cafd092efd7c.png)


# Questions?
For questions contact abekaotoo@gmail.com


