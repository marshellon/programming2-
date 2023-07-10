# Week 2.6

# Use
Code examination 
The code is written in a Jupiter notebook .
My comments and refractors are located below the code.
It is not necessary to run the code to read it. 
This code is not mine and so cannot be licensed in the same way that the creator's work can.



# Article reviews

### Software Engineering for Machine Learning: Characterizing and Detecting

SE3ML is an abbreviation for software engineer for machine learning. Following this article, they discuss many ways in which a machine learning model can be mismatched with the real world.
Before we go into the specifics of how a model can be miscalculated, we first define what a machine learning mismatch is. 

Machine learning mismatch refers to discrepancies or divergences that might occur between the distribution of training data and the distribution of deployment or test data in a machine learning system. 
Mismatches in multiple dimensions, such as data, model, and system conditions, can have an impact on the performance and dependability of machine learning models.

the examples they give in the article are:

- computing-resource mismatch : low system performance due to a lack of computational resources in the production environment necessary to execute the model.

- Data-distribution mismatch : Model accuracy is low since the training data does not correspond to the production data.

- Test-data mismatch: incapacity of software developers to properly test a component due to a lack of test data or a lack of understanding of the component or knowledge of how to test it.

- monitoring mismatch: lack of production-level monitoring systems to collect ML-relevant parameters such as model correctness.

- API mismatch: the requirement to produce a large amount of glue code (Code that connects or combines various software components or systems) because the ML component expects different inputs and outputs than the system into which it is incorporated.

We won't have to deal with any of these challenges in my project because we won't be creating a machine learning model, but I can understand scenarios when they could arise.
one could be. One scenario is what we are doing right now with programming, and the other is creating a machine learning model to forecast anomalies in the system based on sensor data. 
One issue I experienced with this was that the model was trained for multiple types of data. That is, the model was trained on a data set with 52 features, but when it was deployed, the inmcomming data only included 50 features. 
As a result, the model was unable to forecast the anomalies using this data. This is a example for Data-distribution mismatch. 
The same reasoning applies to the test-data mismatch: 
testing the model without proper data is difficult. Most of the time, the data you receive must be divided into three components. This is frequently not practicable or practical with train data, test data, and validation data.
cause you need a lot of data to train the model en to test the data. Also, massive data requires a good and fast system, which may not be the case.



### Tackling Collaboration Challenges in the Development of ML-Enabled Systems

Communication hurdles, as well as variations in expertise and expectations, cause collaboration issues in software development.
Coordination between data scientists and software engineers is required for the creation of ML-enabled systems. 
While research on ML-enabled systems has mostly focused on specific elements, there is a need for larger system-wide viewpoints in ML-enabled system software engineering approaches.



