import os
import pickle
import streamlit as st
import streamlit_option_menu as option_menu
from PIL import Image

st.set_page_config(page_title='diseases prediction outbreaks', page_icon='doctor-fill', layout='wide')

diabetes=pickle.load(open(r'C:/Users/User/Documents/predictions/training_modules/diabetes.sav','rb'))
heart=pickle.load(open(r'C:/Users/User/Documents/predictions/training_modules/heart.sav','rb'))
parkinson=pickle.load(open(r'C:/Users/User/Documents/predictions/training_modules/parkinsons.sav','rb'))
malediabetes=pickle.load(open(r'C:/Users/User/Documents/predictions/training_modules/diabetesmale.sav','rb'))

with st.sidebar:
    choice=option_menu.option_menu('Diseases Diagnosis System',['Diabetes disease','Heart disease','Parkinsons disease'],menu_icon='hospital-fill',icons=['activity','heart-fill','person-fill'])

if choice=='Diabetes disease':
        st.title('Diabetes Diagnose system')
        #st.subheader('Fill in the following details to predict diabetes disease')
        img=Image.open(r'C:\Users\User\Documents\predictions\training_modules\88eb89d4-a1e5-45fd-9ec8-46847f6bb347-765x765.jpg')
        st.image(img,width=150)
        st.subheader('Fill in the following details to predict diabetes disease')
        malefemale=st.radio("Select Patient's Gender",('Male','Female'))
        #prediction=diabetes.predict([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]])

        if malefemale =='Female':
          col1,col2=st.columns(2)
          with col1:
            pregnancies=st.number_input('Enter number of pregnancies',min_value=0,max_value=10)

            skin_thickness=st.number_input('Enter the skin thickness',min_value=0.0,max_value=100.0)

            dpf=st.number_input('what is DiabetesPedigreeFunction of patient',min_value=0,max_value=2)

            blood_pressure=st.number_input('what is the blood pressure',min_value=0.0,max_value=200.0)
          with col2:
            glucose=st.number_input('Enter glucose level',min_value=0.0,max_value=200.0)

            insulin=st.number_input('what is the insulin level',min_value=0.0,max_value=500.0)

            age=st.number_input('Enter age',min_value=0,max_value=100)

            bmi=st.number_input('Enter BMI',min_value=0.0,max_value=100.0)

            prediction=diabetes.predict([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]])

          if st.button('Test Results'):
            if prediction==1:
                st.error('You have diabetes')
                st.warning('If you found to be diabetic please consult a doctor and verify the results')
                st.markdown('### Here are some measures to be followed')
                st.info('Be more physically active')
                st.info('Loose extra weight')
                st.info('Eat healthy plant foods and avoid sugar')

            else:
                st.success('You dont have diabetes')
        elif malefemale=='Male':
                            skin_thickness=st.number_input('Enter the skin thickness',min_value=0.0,max_value=100.0)

                            dpf=st.number_input('what is DiabetesPedigreeFunction of patient',min_value=0,max_value=2)

                            blood_pressure=st.number_input('what is the blood pressure',min_value=0.0,max_value=200.0)

                            glucose=st.number_input('Enter glucose level',min_value=0.0,max_value=200.0)

                            insulin=st.number_input('what is the insulin level',min_value=0.0,max_value=500.0)

                            age=st.number_input('Enter age',min_value=0,max_value=100)

                            bmi=st.number_input('Enter BMI',min_value=0.0,max_value=100.0)

                            maleprediction=malediabetes.predict([[glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]])

                            if st.button('Test Results'):
                              if maleprediction==1:
                                st.error('You have diabetes')
                                st.warning('If you found to be diabetic please consult a doctor and verify the results')
                                st.markdown('### Here are some measures to be followed')
                                st.info('Be more physically active')
                                st.info('Loose extra weight')
                                st.info('Eat healthy plant foods and avoid sugar')

                              else:
                                  st.success('You are not diabetic')
                                  


##########################################################################################################################

elif choice=='Heart disease':
     st.title('Heart Disease Diagnose System ')
     img2=Image.open(r'C:\Users\User\Documents\predictions\training_modules\heart-intro-photo-1.jpg')
     st.image(img2,width=150)
     st.subheader('Enter the details of the patient')

     col1,col2=st.columns(2)

     with col1:
                age=st.number_input('Enter the age of the patient',min_value=0,max_value=100)

                sex2=st.radio("Select Gender", ('male', 'female')) 
                if sex2=='male':
                     sex=1
                else:
                     sex=0

                cp=st.number_input('Enter the CP count')

                trestbps=st.number_input('Enter trestbps',min_value=0.0,max_value=200.0)

                chol=st.number_input('Enter the cholestrol pf patient',min_value=0.0,max_value=800.0)
    
                fbs=st.number_input('Enter the fbs',min_value=0,max_value=1)

                restecg=st.number_input('Enter restecg of patient',min_value=0,max_value=1)
     with col2:
                thalach=st.number_input('Enter the thalach value',min_value=0)         #exang	oldpeak	slope	ca	thal

                exang=st.number_input('Enter the exang')

                oldspeak=st.number_input('Enter the oldspeak value',min_value=0.0)

                slope=st.number_input('Enter the slope of patient')

                ca=st.number_input('Enter the ca of patient')

                thal=st.number_input('Enter the thal')

                #restecg=st.number_input('Enter restecg of patient',min_value=0,max_value=1)
                predictionheart=heart.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldspeak,slope,ca,thal]])

     if st.button('Test Results'):
        if predictionheart==1:
            st.error('You have a Heart disease')
            st.warning('If you found to be Heart patient please consult a doctor and verify the results')
            st.markdown('### Here are some measures to improve heart health')
            st.info('Eat a healthy diet, exercise regularly, quit smoking, and get enough sleep.')
            st.info('Take medications to lower cholesterol, improve heart function, and reduce blood pressure')
            st.info('Avoid eating oil and ghee')

        else:
            st.success('You Have a healthy heart')

#########################################################################################################################
elif choice=='Parkinsons disease':
      st.title('Parkisons Disease Diagnose System')
      img3=Image.open(r'C:\Users\User\Documents\predictions\training_modules\images.jfif')
      st.image(img3,width=180)
      st.subheader('Enter the details of the patient')

      col1, col2,col3,col4 = st.columns(4)

      with col1:
        mdvp_fo = st.number_input(' Enter MDVP:Fo(Hz)', min_value=0.0)
        mdvp_fhi = st.number_input('Enter MDVP:Fhi(Hz)', min_value=0.0)
        mdvp_flo = st.number_input('Enter MDVP:Flo(Hz)', min_value=0.0)
        mdvp_jitter_percent = st.number_input('Enter MDVP:Jitter(%)', min_value=0.0)
        mdvp_jitter_abs = st.number_input('Enter MDVP:Jitter(Abs)', min_value=0.0)
       
      with col2:
        jitter_ddp = st.number_input('Enter Jitter:DDP', min_value=0.0)
        mdvp_shimmer = st.number_input('Enter MDVP:Shimmer', min_value=0.0)
        mdvp_shimmer_db = st.number_input('Enter MDVP:Shimmer(dB)', min_value=0.0)
        shimmer_apq3 = st.number_input('Shimmer:APQ3', min_value=0.0)
        shimmer_apq5 = st.number_input('Shimmer:APQ5', min_value=0.0)
        rpde=st.number_input('Enetr the RPDE',min_value=0.0)
       
        
      with col3:
            mdvp_rap = st.number_input('Enter the MDVP:RAP', min_value=0.0)
            mdvp_ppq = st.number_input('MDVP:PPQ', min_value=0.0)
            mdvp_apq = st.number_input('MDVP:APQ', min_value=0.0)
            shimmer_dda = st.number_input('Enter Shimmer:DDA', min_value=0.0)
            nhr=st.number_input('Enter the NHR value',min_value=0.0)
            dfa=st.number_input('Enter the DFA',min_value=0.0)
           
      with col4:
            hnr=st.number_input('Enter the HNR value',min_value=0.0)
            spread1=st.number_input('Enter the spread1')
            spread2=st.number_input('Enter the spread2')
            ppe=st.number_input('Enter the PPE')
            d2=st.number_input('Enter the D2')
            

            predictionparkinson = parkinson.predict([[mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter_percent,hnr,spread1,spread2,rpde,ppe,nhr,dfa,d2, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda]])

      if st.button('Test Results'):
        if predictionparkinson == 1:
            st.error('You have Parkinsons disease')
            st.warning('If you found to be Parkinsons patient please consult a doctor and verify the results')
            st.markdown('### Here are some measures to be followed')
            st.info('Exercise regularly especially to improve your nervous system')
            st.info('Drink green tea and caffeinated beverages')
            st.info('Have a balanced diet')
        else:
            st.success('You do not have Parkinsons disease')









     



    
                
    
          



   

  







