import streamlit as st
import pandas as pd
import helper
from PIL import Image

# adding markdown for music button
st.sidebar.markdown('*Groove- Theme song*', unsafe_allow_html=False)

# adding music button in the sidebar
button= st.sidebar.button('Music', key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)

# if click on music button is clicked show audio controls for playback
if button:
     st.sidebar.audio(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\audio\IPL-theme-RMX.wav', format="audio/wav", start_time=0)


# Sidebar theme image
image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\1.png')
st.sidebar.image(image, caption='Indian Premire League')

# reading main DataFrame
data= pd.read_csv(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\matches.csv')
df = pd.DataFrame(data)

# Sidebar main title
st.sidebar.title('IPL DATA ANALYSIS')

# First main checkbox
user_menu= st.sidebar.checkbox('Overall Analysis')

# if the first checkbox is checked then show the sub check boxes
if user_menu:
    a= st.sidebar.checkbox('Total matches per season')
    b= st.sidebar.checkbox('Team Performance')
    c= st.sidebar.checkbox('Player of the match')
    d= st.sidebar.checkbox('Overall match result')
    e= st.sidebar.checkbox('Toss Statistics')
    f= st.sidebar.checkbox('Toss decision')

    # if respective sub check box is selected then show the related details
    if a :
        match_per_season=helper.match_per_season(df)
        st.title ('Total number of matches played in each season')
        st.plotly_chart(match_per_season)

    if b :
        winners=helper.winners(df)
        st.title('Team Performance')
        st.plotly_chart(winners)

    if c :
        pom=helper.pom(df)
        st.title('Player of the match statistics')
        st.table(pom)

    if d :
        overall_match_result=helper.overall_match_result(df)
        st.title('Over all results of the match')
        st.plotly_chart(overall_match_result)

    if e :
        toss_winner_count=helper.toss_winner_count(df)
        st.title('Number of times toss won')
        st.plotly_chart(toss_winner_count)

    if f :
        toss_decision=helper.toss_decision(df)
        st.title('Decision of field / bat after wining toss')
        st.plotly_chart(toss_decision)

# Second main checkbox
user_menu_1= st.sidebar.checkbox('Season wise analysis')

# if second main checkbox is selected then show below sub check boxes
if user_menu_1:
    a= st.sidebar.checkbox('IPL-2008')
    b= st.sidebar.checkbox('IPL-2009')
    c= st.sidebar.checkbox('IPL-2010')
    d= st.sidebar.checkbox('IPL-2011')
    e= st.sidebar.checkbox('IPL-2012')
    f= st.sidebar.checkbox('IPL-2013')
    g= st.sidebar.checkbox('IPL-2014')
    h= st.sidebar.checkbox('IPL-2015')
    i= st.sidebar.checkbox('IPL-2016')
    j= st.sidebar.checkbox('IPL-2017')
    k= st.sidebar.checkbox('IPL-2018')
    l= st.sidebar.checkbox('IPL-2019')

    # Show respective details with respective sub check box selection
    if a:
        matches_in_cities_2008 = helper.matches_in_cities_2008(df)
        m_2008 = helper.m_2008(df)
        st.title('Team Performance')
        st.plotly_chart(m_2008)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2008)

    if b:
        matches_in_cities_2009 = helper.matches_in_cities_2009(df)
        m_2009 = helper.m_2009(df)
        st.title('Team Performance')
        st.plotly_chart(m_2009)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2009)

    if c:
        matches_in_cities_2010 = helper.matches_in_cities_2010(df)
        m_2010 = helper.m_2010(df)
        st.title('Team Performance')
        st.plotly_chart(m_2010)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2010)

    if d:
        matches_in_cities_2011 = helper.matches_in_cities_2011(df)
        m_2011 = helper.m_2011(df)
        st.title('Team Performance')
        st.plotly_chart(m_2011)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2011)

    if e:
        matches_in_cities_2012 = helper.matches_in_cities_2012(df)
        m_2012 = helper.m_2012(df)
        st.title('Team Performance')
        st.plotly_chart(m_2012)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2012)

    if f:
        matches_in_cities_2013 = helper.matches_in_cities_2013(df)
        m_2013 = helper.m_2013(df)
        st.title('Team Performance')
        st.plotly_chart(m_2013)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2013)

    if g:
        matches_in_cities_2014 = helper.matches_in_cities_2014(df)
        m_2014 = helper.m_2014(df)
        st.title('Team Performance')
        st.plotly_chart(m_2014)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2014)

    if h:
        matches_in_cities_2015 = helper.matches_in_cities_2015(df)
        m_2015 = helper.m_2015(df)
        st.title('Team Performance')
        st.plotly_chart(m_2015)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2015)

    if i:
        matches_in_cities_2016 = helper.matches_in_cities_2016(df)
        m_2016 = helper.m_2016(df)
        st.title('Team Performance')
        st.plotly_chart(m_2016)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2016)

    if j:
        matches_in_cities_2017 = helper.matches_in_cities_2017(df)
        m_2017 = helper.m_2017(df)
        st.title('Team Performance')
        st.plotly_chart(m_2017)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2017)

    if k:
        matches_in_cities_2018 = helper.matches_in_cities_2018(df)
        m_2018 = helper.m_2018(df)
        st.title('Team Performance')
        st.plotly_chart(m_2018)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2018)

    if l:
        matches_in_cities_2019 = helper.matches_in_cities_2019(df)
        m_2019 = helper.m_2019(df)
        st.title('Team Performance')
        st.plotly_chart(m_2019)
        st.title('Number of matches in each city')
        st.table(matches_in_cities_2019)

# Adding a select box- allows users to select a vaue from the dropdown menu
user_menu_2 = st.sidebar.selectbox(
     'Team wise analysis',
     (helper.teams(df))

)
st.write('Selected:', user_menu_2)

# show respective details with respective selected value from the dropdown
if user_menu_2 == 'Sunrisers Hyderabad':
    srh = df[df['team1'] == 'Sunrisers Hyderabad']
    T_n_m = len(srh)
    toss_wins = len(srh[srh['toss_winner'] == 'Sunrisers Hyderabad'])
    decided_t_field = len(srh[srh['toss_decision'] == 'field'])
    winner = len(srh[srh['winner'] == 'Sunrisers Hyderabad'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\sunrisers.jpg')
    st.image(image, caption='Sunrisers Hyderabad')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)


if user_menu_2 == 'Mumbai Indians':
    mi = df[df['team1'] == 'Mumbai Indians']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Mumbai Indians'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Mumbai Indians'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\mi.jpg')
    st.image(image, caption='Mumbai Indians')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)


if user_menu_2 == 'Gujarat Lions':
    mi = df[df['team1'] == 'Gujarat Lions']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Gujarat Lions'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Gujarat Lions'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\gl.jpg')
    st.image(image, caption='Gujarat Lions')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Rising Pune Supergiant':
    mi = df[df['team1'] == 'Rising Pune Supergiant']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Rising Pune Supergiant'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Rising Pune Supergiant'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\rps.png')
    st.image(image, caption='Rising Pune Supergiant')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Royal Challengers Bangalore':
    mi = df[df['team1'] == 'Royal Challengers Bangalore']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Royal Challengers Bangalore'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Royal Challengers Bangalore'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\rcb.jpg')
    st.image(image, caption='Royal Challengers Bangalore')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Kolkata Knight Riders':
    mi = df[df['team1'] == 'Kolkata Knight Riders']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Kolkata Knight Riders'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Kolkata Knight Riders'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\kkr.jpg')
    st.image(image, caption='Kolkata Knight Riders')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Delhi Daredevils':
    mi = df[df['team1'] == 'Delhi Daredevils']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Delhi Daredevils'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Delhi Daredevils'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\DD.png')
    st.image(image, caption='Delhi Daredevils')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Kings XI Punjab':
    mi = df[df['team1'] == 'Kings XI Punjab']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Kings XI Punjab'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Kings XI Punjab'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\KXIP.jpg')
    st.image(image, caption='Kings XI Punjab')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Chennai Super Kings':
    mi = df[df['team1'] == 'Chennai Super Kings']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Chennai Super Kings'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Chennai Super Kings'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\csk.jpg')
    st.image(image, caption='Chennai Super Kings')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Rajasthan Royals':
    mi = df[df['team1'] == 'Rajasthan Royals']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Rajasthan Royals'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Rajasthan Royals'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\RR.jpg')
    st.image(image, caption='Rajasthan Royals')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Deccan Chargers':
    mi = df[df['team1'] == 'Deccan Chargers']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Deccan Chargers'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Deccan Chargers'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\Dec_ch.jpg')
    st.image(image, caption='Deccan Chargers')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Kochi Tuskers Kerala':
    mi = df[df['team1'] == 'Kochi Tuskers Kerala']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Kochi Tuskers Kerala'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Kochi Tuskers Kerala'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\ktk.jpg')
    st.image(image, caption='Kochi Tuskers Kerala')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Pune Warriors':
    mi = df[df['team1'] == 'Pune Warriors']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Pune Warriors'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Pune Warriors'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\p_war.jpg')
    st.image(image, caption='Pune Warriors')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Rising Pune Supergiants':
    mi = df[df['team1'] == 'Rising Pune Supergiants']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Rising Pune Supergiants'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Rising Pune Supergiants'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\rps.png')
    st.image(image, caption='Rising Pune Supergiants')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)

if user_menu_2 == 'Delhi Capitals':
    mi = df[df['team1'] == 'Delhi Capitals']
    T_n_m = len(mi)
    toss_wins = len(mi[mi['toss_winner'] == 'Delhi Capitals'])
    decided_t_field = len(mi[mi['toss_decision'] == 'field'])
    winner = len(mi[mi['winner'] == 'Delhi Capitals'])

    image = Image.open(r'C:\Users\Asus\Projects\IPL Ananlysis\dataset\images\del_cap.jpg')
    st.image(image, caption='Delhi Capitals')

    col1,col2 = st.columns(2)
    with col1:
        st.header('Number of matches')
        st.title(T_n_m)
    with col2:
        st.header('Number of toss wins')
        st.title(toss_wins)

    col1, col2 = st.columns(2)
    with col1:
        st.header('Field first')
        st.title(decided_t_field)
    with col2:
        st.header('Number of wins')
        st.title(winner)