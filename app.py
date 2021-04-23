import streamlit as st
import pandas as pd
import  numpy as np
import pickle

from sklearn import datasets
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


st.write("""
# DDos Attack Classification App
This app predicts the **Type of the DDos Attack**!
""")

st.write('---')

le = LabelEncoder()

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header(' Input Parameters')



def user_input_features():

    PKT_SIZE = st.sidebar.slider('PKT_SIZE', 55.000000,65535.000000)
    NUMBER_OF_PKT = st.sidebar.slider('NUMBER_OF_PKT',47.000000,26.000000)
    NUMBER_OF_BYTE = st.sidebar.slider('NUMBER_OF_BYTE',8.000000,641596.000000)

    PKT_IN = st.sidebar.slider('PKT_IN',1985,2009, 1997)
    PKT_OUT = st.sidebar.slider('PKT_OUT', 31.290000,300.888400)
    PKT_R = st.sidebar.slider('PKT_R', 31.290000,300.888400)
    PKT_DELAY_NODE =st.sidebar.slider('PKT_DELAY_NODE', 0.000000,0.114464)
    PKT_RATE = st.sidebar.slider('PKT_RATE',0.977957,1118.279350)
    BYTE_RATE = st.sidebar.slider('BYTE_RATE', 3.00,300.888400)
    PKT_AVG_SIZE = st.sidebar.slider('PKT_AVG_SIZE', 55.000000,65535.200000)
    UTILIZATION = st.sidebar.slider('UTILIZATION',0.000025,0.236498)
    PKT_DELAY = st.sidebar.slider('PKT_DELAY',0.000000,0.153680)
    PKT_SEND_TIME = st.sidebar.slider('PKT_SEND_TIME',0.000000,75.882365)
    PKT_RESEVED_TIME = st.sidebar.slider('PKT_RESEVED_TIME',0.071942,75.953648)
    FIRST_PKT_SENT=st.sidebar.slider('FIRST_PKT_SENT',0.000000,25.000000)
    LAST_PKT_RESEVED=st.sidebar.slider('LAST_PKT_RESEVED',9.045728,75.999821)  
    PKT_TYPE = st.sidebar.selectbox('Outlet_Size',('tcp','ack','cbr','ping'))  
    
     
    data = {'PKT_SIZE': PKT_SIZE,
            'NUMBER_OF_PKT': NUMBER_OF_PKT,
            'NUMBER_OF_BYTE': NUMBER_OF_BYTE,
            'PKT_IN': PKT_IN,
            'PKT_OUT':PKT_OUT,
            'PKT_R': PKT_R,
            'PKT_DELAY_NODE': PKT_DELAY_NODE,
            'PKT_RATE':PKT_RATE,
            'BYTE_RATE':BYTE_RATE,
            'PKT_AVG_SIZE':PKT_AVG_SIZE,
            'UTILIZATION':UTILIZATION,
            'PKT_DELAY':PKT_DELAY,
            'PKT_SEND_TIME':PKT_SEND_TIME,
            'PKT_RESEVED_TIME':PKT_RESEVED_TIME,
            'FIRST_PKT_SENT':FIRST_PKT_SENT,
            'LAST_PKT_RESEVED':LAST_PKT_RESEVED,
            'PKT_TYPE':PKT_TYPE
             }   


    features = pd.DataFrame(data, index=[0])

    return data

df = user_input_features()




def encoder(variable_value,classes_list):

    encoder_list = [0] * len(classes_list)
    for index,classe  in enumerate(classes_list):
            if(variable_value==classe):
                encoder_list[index]=1        
    return encoder_list




PKT_TYPE_Classes=['tcp','ack','cbr','ping']


PKT_TYPE_Encoding=encoder(df['PKT_TYPE'],PKT_TYPE_Classes)

Low_Fat,Regular,Non_Edible = PKT_TYPE_Encoding[0],PKT_TYPE_Encoding[1],PKT_TYPE_Encoding[2]

cbr,ping,tcp=PKT_TYPE_Encoding[2],PKT_TYPE_Encoding[3],PKT_TYPE_Encoding[0]

features_df = pd.DataFrame(df, index=[0])

# st.write(Tier_3)



num_df=['PKT_SIZE', 'NUMBER_OF_PKT', 'NUMBER_OF_BYTE', 'PKT_IN', 'PKT_OUT',
       'PKT_R', 'PKT_DELAY_NODE', 'PKT_RATE', 'BYTE_RATE', 'PKT_AVG_SIZE',
       'UTILIZATION', 'PKT_DELAY', 'PKT_SEND_TIME', 'PKT_RESEVED_TIME',
       'FIRST_PKT_SENT', 'LAST_PKT_RESEVED']




scaler = StandardScaler()
scaledd_values=scaler.fit_transform(features_df[num_df])
scaledd_df=pd.DataFrame(scaledd_values,columns=num_df)

PKT_SIZE=scaledd_df['PKT_SIZE']
NUMBER_OF_PKT=scaledd_df['NUMBER_OF_PKT']
NUMBER_OF_BYTE=scaledd_df['NUMBER_OF_BYTE']
PKT_IN=scaledd_df['PKT_IN']
PKT_OUT=scaledd_df['PKT_OUT']
PKT_R=scaledd_df['PKT_R']
PKT_DELAY_NODE=scaledd_df['PKT_DELAY_NODE']
PKT_RATE=scaledd_df['PKT_RATE']
BYTE_RATE=scaledd_df['BYTE_RATE']
PKT_AVG_SIZE=scaledd_df['PKT_AVG_SIZE']
UTILIZATION=scaledd_df['UTILIZATION']
PKT_DELAY=scaledd_df['PKT_DELAY']
PKT_SEND_TIME=scaledd_df['PKT_SEND_TIME']
PKT_RESEVED_TIME=scaledd_df['PKT_RESEVED_TIME']
FIRST_PKT_SENT=scaledd_df['FIRST_PKT_SENT']
LAST_PKT_RESEVED=scaledd_df['LAST_PKT_RESEVED']



load_clf = pickle.load(open('Support_vector_model.pkl', 'rb'))



prediction=load_clf.predict([[PKT_SIZE,NUMBER_OF_PKT,NUMBER_OF_BYTE,PKT_IN,PKT_OUT,PKT_R,PKT_DELAY_NODE,PKT_RATE,BYTE_RATE,PKT_AVG_SIZE	,UTILIZATION,PKT_DELAY,PKT_SEND_TIME,PKT_RESEVED_TIME,FIRST_PKT_SENT,LAST_PKT_RESEVED,cbr,ping,tcp]])

            

st.header('Specified Input parameters')
st.write(df)
st.write('---')


prediction_proba = load_clf.predict_proba([[PKT_SIZE,NUMBER_OF_PKT,NUMBER_OF_BYTE,PKT_IN,PKT_OUT,PKT_R,PKT_DELAY_NODE,PKT_RATE,BYTE_RATE,PKT_AVG_SIZE,UTILIZATION,PKT_DELAY,PKT_SEND_TIME,PKT_RESEVED_TIME,FIRST_PKT_SENT,LAST_PKT_RESEVED,cbr,ping,tcp]])


st.subheader('Prediction')


DDos_classes =np.array(['Normal','UDP-Flood','Smurf','SIDDOS','HTTP-FLOOD'])
st.write(DDos_classes[prediction])



if prediction==0:
    st.write('Normal')
elif prediction==1:
    st.write('UDP-Flood')
elif prediction==2:
    st.write('Smurf')
elif prediction==3:
    st.write('SIDDOS')
else:
    st.write('HTTP-FLOOD')





st.subheader('Prediction Probability')
st.write(prediction_proba)

