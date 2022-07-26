from flask import Flask,request,render_template
import pickle
import pandas as pd
import requests

app=Flask(__name__)

#opening pickle file
movie_data=pickle.load(open('movie_listdict.pkl','rb'))
movies=pd.DataFrame(movie_data)#dataframe

#Similarity data
similarity=pickle.load(open('similarity.pkl','rb'))
#similarity_data=S

def poster_fetch(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c902f39c977a35c4af22570f38d28fe9&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    title=data['title']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path,title

   


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/',methods=['POST', 'GET'])
def recommend():
    movie=request.form['recommend']
   
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    

    
    
    recomendation=[]
    recommeded_movies_posters=[]
    for i in distances[1:6]:

        movie_id=movies.iloc[i[0]].id
        

        recomendation.append(movies.iloc[i[0]].original_title)
        recommeded_movies_posters.append(poster_fetch(movie_id))
        
    return render_template('index.html',recomendation1=recomendation,poster=recommeded_movies_posters)

      
    


       
    

if __name__ == '__main__':

    app.run(debug=True)

     