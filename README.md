# Movies Recommendation System 

This is a web application that functions as a Content-Based Recommendation System. Users can search for a movie by its title, and the application will provide five similar movies based on the user's search.

For this application, I used The Movie Database (TMDb) API (https://developers.themoviedb.org/3/getting-started/introduction) to fetch movie posters and titles

##### Live link of this web app: https://mlmoviesrecommendation.herokuapp.com

##### Dataset Link : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

##### Languages and libraries used:
  1)Python 
  
  2)Pandas
  
  3)Numpy
  
  4)Scikit-Learn
  
  5)Flask
  
  6)JavaScript
  
  ##### Frontend designed by : HTML  ,CSS  ,BootSrap  ,JavaScipt
  ##### Teconologies Used : 
  
  Data Preprocessing
  
  Natural Language Processing
  
  Machine Lerning
  
  
  for finding the similarity by through Cosine Similarity
  
  #### App Demo
  
  ![2022-07-25](https://user-images.githubusercontent.com/64775171/180815062-ea07045d-5441-4d06-a168-bfdfebe114b3.png)

![2022-07-25 (2)](https://user-images.githubusercontent.com/64775171/180815172-698ee6d0-4132-4ef5-b8c8-193dd3ab364b.png)

![2022-07-25 (3)](https://user-images.githubusercontent.com/64775171/180815262-c4c24f82-5968-413b-b220-04d0347724a0.png)

### Similarity Score :
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

##### How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are theymay still be oriented closer together. The smaller the angle, higher the cosine similarity.

![70401457-a7530680-1a55-11ea-9158-97d4e8515ca4](https://user-images.githubusercontent.com/64775171/180818286-a8281f5f-edc0-44f1-a9f5-cbda9a77e378.png)


Cosine Similarity :[ Understanding the Math behind Cosine Similarity](https://www.youtube.com/watch?v=ieMjGVYw9ag)
