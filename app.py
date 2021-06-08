import numpy as np
from flask import Flask , request , jsonify , render_template
import jsonify
import requests
import sklearn
import pickle
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
     return render_template('index.html')
 

standard_scaler =StandardScaler()
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=request.form['Gender']
        
        if(Gender=="Male"):
            Gender = 0
            
            
        else:
            Gender = 1
            
         
        Customer_Type = request.form['Customer Type']
        
        if(Customer_Type=='Loyal Customer'):
            
            Customer_Type  = 0
            
        else:
            Customer_Type = 1
            
            
        Type_of_Travel=request.form['Type of Travel']
        
        if(Type_of_Travel=='Personal Travel'):
            
            Type_of_Travel= 0
            
            
        else:
            
            Type_of_Travel = 1   
            
            
             
        class_i=request.form['Class']
        if(class_i == "Eco Plus"):
            
            class_i=0
            
        elif(class_i=='Business'):
            class_i = 1
        else:
            class_i = 2    
             
             
    
        
        inflight_service = float(request.form['Inflight wifi service'])
        depa_time = float(request.form['Departure/Arrival time convenient'])
        easy_book = float(request.form['Ease of Online booking'])
        loco_gate = float(request.form['Gate location'])
        foodie = float(request.form['Food and drink'])
        onoline = float(request.form['Online boarding'])
    
       
        comforti = float(request.form['Seat comfort'])
        inflighto = float(request.form['Inflight entertainment'])
        onboard_servici = float(request.form['On-board service'])
        Leg_room = float(request.form['Leg room service'])
        bag_handle = float(request.form['Baggage handling'])
        checkini = float(request.form['Checkin service'])
        infi = float(request.form['Inflight service'])
        cleani = float(request.form['Cleanliness'])
        
        Age = int(request.form['Age']) 
        flight_distance = float(request.form['Flight Distance'])
        departure_delay = float(request.form['Departure Delay in Minutes'])
        

        list1=[[Gender,Customer_Type,Age,Type_of_Travel,class_i,flight_distance,departure_delay,inflight_service,
                                    depa_time,easy_book,loco_gate,foodie,onoline,comforti,inflighto,onboard_servici,Leg_room,bag_handle,
                                    checkini,infi,cleani]]
        
        list2=standard_scaler.fit_transform(list1)
        prediction = model.predict(list2)
        
           
        if prediction == 1:
            return render_template('output.html', prediction_text='satisfied')
       
        else:
            return render_template('output.html', prediction_text='neutral or dissatisfied')
    
    
    else:
        return render_template('output.html')
    

if __name__ == "__main__":
    app.run(debug=True)