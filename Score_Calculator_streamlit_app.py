import streamlit as st

# this is the main function in which we define our webpage  
def main():       
    
    #heading_txt = f'<h5>Enter below indicated values to check your overall IELTS band score<h5>'
    #st.markdown(heading_txt, unsafe_allow_html=True)
    
    Test_type_txt = f'<span style="font-family:Source Sans Pro - Semi Bold; color:#C70039; font-size: 18px;"><strong>Select IELTS Test Type</strong></span>'
    st.markdown(Test_type_txt, unsafe_allow_html=True)
    test_type=st.radio('Test Type' , ('Academic', 'General Training'), label_visibility="hidden")


    txt1 = f'<br><span style="font-family:Source Sans Pro - Semi Bold; color:#C70039; font-size: 18px;"><strong>Enter Number Of Correct Answers (out of 40) in Listening Test</strong></span>'
    txt2 = f'<br><span style="font-family:Source Sans Pro - Semi Bold; color:#C70039; font-size: 18px;"><strong>Enter Number Of Correct Answers (out of 40) in Reading Test</strong></span>'
    txt3 = f'<br><span style="font-family:Source Sans Pro - Semi Bold; color:#C70039; font-size: 18px;"><strong>Select Writing Score</strong></span>'
    txt4 = f'<br><span style="font-family:Source Sans Pro - Semi Bold; color:#C70039; font-size: 18px;"><strong>Select Speaking Score</strong></span>'

    # Listening band score calculation (Same for AC & GT):
    st.markdown(txt1, unsafe_allow_html=True)
    L_correct_answers = st.number_input('Enter Listening Score', min_value=0, max_value=40, step = 1, label_visibility="hidden")
    
    if L_correct_answers <1.0 : 
            Listening_input = st.slider('Listening', min_value =0.0 , max_value =9.0 , step =0.5 , value = 0.0, label_visibility="hidden", disabled = True)
    else:  
      if 39<=L_correct_answers<=40 :
        calc_listening_score = 9.0
      elif 37<=L_correct_answers<=38 :
        calc_listening_score =8.5
      elif 35<=L_correct_answers<=36 :
        calc_listening_score =8.0
      elif 32<=L_correct_answers<=34 :
        calc_listening_score =7.5
      elif 30<=L_correct_answers<=31 :
        calc_listening_score =7.0
      elif 26<=L_correct_answers<=29 :
        calc_listening_score =6.5
      elif 23<=L_correct_answers<=25 :
        calc_listening_score =6.0
      elif 18<=L_correct_answers<=22 :
        calc_listening_score =5.5
      elif 16<=L_correct_answers<=17 :
        calc_listening_score =5.0
      elif 13<=L_correct_answers<=15 :
        calc_listening_score =4.5
      elif 11<=L_correct_answers<=12 :
        calc_listening_score =4.0
      elif 8<=L_correct_answers<=10 :
        calc_listening_score =3.5
      elif 6<=L_correct_answers<=7 :
        calc_listening_score =3.0
      elif 4<=L_correct_answers<=5 :
        calc_listening_score =2.5
      elif L_correct_answers==3 :
        calc_listening_score =2.0
      elif 1<=L_correct_answers<=2 :
        calc_listening_score =1.0
      else :
        calc_listening_score =0.0

      Listening_input = st.slider('Listening', min_value =0.0 , max_value =9.0 , step =0.5 , value = calc_listening_score, label_visibility="hidden", disabled = True)


    
    st.markdown(txt2, unsafe_allow_html=True)
    R_correct_answers = st.number_input('Enter Reading Correct Answers', min_value=0, max_value=40, step = 1, label_visibility="hidden")
    
    if R_correct_answers <1.0 : 
      Reading_input = st.slider('Reading', min_value =0.0 , max_value =9.0 , step =0.5 , value = 0.0, label_visibility="hidden", disabled = True)
    else: 
      if test_type == "Academic":
        #Academic :
        if 39<=R_correct_answers<=40 :
          calc_AC_reading_score = 9.0
        elif 37<=R_correct_answers<=38 :
          calc_AC_reading_score =8.5
        elif 35<=R_correct_answers<=36 :
          calc_AC_reading_score =8.0
        elif 33<=R_correct_answers<=34 :
          calc_AC_reading_score =7.5
        elif 30<=R_correct_answers<=32 :
          calc_AC_reading_score =7.0
        elif 27<=R_correct_answers<=29 :
          calc_AC_reading_score =6.5
        elif 23<=R_correct_answers<=26 :
          calc_AC_reading_score =6.0
        elif 19<=R_correct_answers<=22 :
          calc_AC_reading_score =5.5
        elif 15<=R_correct_answers<=18 :
          calc_AC_reading_score =5.0
        elif 13<=R_correct_answers<=14 :
          calc_AC_reading_score =4.5
        elif 10<=R_correct_answers<=12 :
          calc_AC_reading_score =4.0
        elif 8<=R_correct_answers<=9 :
          calc_AC_reading_score =3.5
        elif 6<=R_correct_answers<=7 :
          calc_AC_reading_score =3.0
        elif 4<=R_correct_answers<=5 :
          calc_AC_reading_score =2.5
        elif R_correct_answers==3 :
          calc_AC_reading_score =2.0
        elif 1<=R_correct_answers<=2 :
          calc_AC_reading_score =1.0
        Reading_input = st.slider('Reading', min_value =0.0 , max_value =9.0 , step =0.5 , value = calc_AC_reading_score, label_visibility="hidden", disabled = True)
        
      else: #i.e. General Training 
        if R_correct_answers==40 :
          calc_GT_reading_score = 9.0
        elif R_correct_answers==39 :
          calc_GT_reading_score =8.5
        elif 37<=R_correct_answers<=38 :
          calc_GT_reading_score =8.0
        elif R_correct_answers==36 :
          calc_GT_reading_score =7.5
        elif 34<=R_correct_answers<=35 :
          calc_GT_reading_score =7.0
        elif 32<=R_correct_answers<=33 :
          calc_GT_reading_score =6.5
        elif 30<=R_correct_answers<=31 :
          calc_GT_reading_score =6.0
        elif 27<=R_correct_answers<=29 :
          calc_GT_reading_score =5.5
        elif 23<=R_correct_answers<=26 :
          calc_GT_reading_score =5.0
        elif 19<=R_correct_answers<=22 :
          calc_GT_reading_score =4.5
        elif 15<=R_correct_answers<=18 :
          calc_GT_reading_score =4.0
        elif 12<=R_correct_answers<=14 :
          calc_GT_reading_score =3.5
        elif 9<=R_correct_answers<=11 :
          calc_GT_reading_score =3.0
        elif 5<=R_correct_answers<=8 :
          calc_GT_reading_score =2.5
        elif 2<=R_correct_answers<=4 :
          calc_GT_reading_score =2.0
        elif R_correct_answers==1 :
          calc_GT_reading_score =1.0
        Reading_input = st.slider('Reading', min_value =0.0 , max_value =9.0 , step =0.5 , value = calc_GT_reading_score, label_visibility="hidden", disabled = True)


    

    st.markdown(txt3, unsafe_allow_html=True)
    Writing_input = st.slider('Writing', min_value =0.0 , max_value =9.0 , step =0.5 , label_visibility="hidden")
    
    st.markdown(txt4, unsafe_allow_html=True)
    Speaking_input = st.slider('Speaking', min_value =0.0 , max_value =9.0 , step =0.5 , label_visibility="hidden")
    
    st.markdown(f'<br>', unsafe_allow_html=True)

    m = st.markdown("""<p> <center> <style>
                          div.stButton > button:first-child {
                              background-color: #C70039;
                              color:#ffffff;
                              font-weight:bold;                            
                          }
                          div.stButton > button:hover {
                              background-color: #ffffff;
                              color:#C70039;
                              font-weight:bold;
                          }
                          div.stT
                  </style></center></p>""", unsafe_allow_html=True)


    if st.button("Calculate Overall Band Score"): 

      section_scores = {"L" : Listening_input, "R" : Reading_input, "W" : Writing_input, "S" : Speaking_input}

      for section, score in section_scores.items():
        if round((score%1),2) <= 0.25:
          section_scores[section] = (int(score/1))*1.0
          #print(section, " : ", section_scores[section])
        elif 0.25 < round((score%1),2) < 0.75:
          section_scores[section] = section_scores[section] = int(score/1)+0.5
          #print(section, " : ", section_scores[section])
        elif round((score%1),2) >= 0.75:
          section_scores[section] = int(score/1)+1.0
          #print(section, " : ", section_scores[section])

      #calculating final band score
      avg = round((section_scores['L']+ section_scores['R']+section_scores['W']+ section_scores['S'])/4, 2)
      #print("Average = ", avg)
      if round((avg%1),2) <= 0.25:
          Final_Band_Score = (int(avg/1))*1.0
      elif 0.25 < round((avg%1),2) < 0.75:
          Final_Band_Score = int(avg/1)+0.5
      elif round((avg%1),2) >= 0.75:
          Final_Band_Score = int(avg/1)+1.0

      Result = f'<br><center><h3 style="color:#C70039;">Final Band Score = {Final_Band_Score}</h3><center>'
      st.markdown(Result, unsafe_allow_html=True)
      

if __name__=='__main__': 
    main()
