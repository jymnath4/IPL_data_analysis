import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def match_per_season (df):
    Season = df['Season'].value_counts()
    Season = pd.DataFrame(Season)
    Season = Season.reset_index()
    Season = Season.sort_values('index')
    Season = Season.rename(columns={'Season': 'Count of matches'})
    Season = Season.rename(columns={'index': 'season'})
    return px.bar(Season, x='season',y='Count of matches')

def winners (df):
    winners = b = df['winner'].value_counts()
    winners = pd.DataFrame(winners)
    winners = winners.reset_index()
    winners = winners.rename(columns={'index': 'team', 'winner': 'number of wins'})
    return px.bar(winners, x='team',y='number of wins',color_discrete_sequence=px.colors.qualitative.Alphabet)

def pom (df):
    Pl_of_match = df['player_of_match'].value_counts()
    Pl_of_match = pd.DataFrame(Pl_of_match)
    Pl_of_match = Pl_of_match.reset_index()
    Pl_of_match = Pl_of_match.rename(
        columns={'index': 'Player', 'player_of_match': 'No. of times awarded player of match'})
    return Pl_of_match

def overall_match_result (df):
    fig = px.pie(df, values=['743', '9', '4'], names=['Normal', 'Tie', 'No result'], title='Over all match decision')
    return fig

def toss_decision (df):
    fig = px.pie(df, values=['463','293'], names=['Choose to field after winning toss','Choose to bat after winning toss'],
             title='Toss decision',)
    return fig

def toss_winner_count (df):
    toss_stats = df['toss_winner'].value_counts()
    toss_stats = pd.DataFrame(toss_stats)
    toss_stats = toss_stats.reset_index()
    toss_stats = toss_stats.rename(columns={'index': 'Team', 'toss_winner': 'No. of times toss winner'})
    fig = px.bar(toss_stats, x='Team', y='No. of times toss winner', color_discrete_sequence=px.colors.qualitative.Vivid)
    return fig
def matches_in_cities_2008 (df):
    season_2008 = df[df['Season'] == 'IPL-2008']
    Matches_city = season_2008['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2009 (df):
    season_2009 = df[df['Season'] == 'IPL-2009']
    Matches_city = season_2009['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2010 (df):
    season_2010 = df[df['Season'] == 'IPL-2010']
    Matches_city = season_2010['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2011 (df):
    season_2011 = df[df['Season'] == 'IPL-2011']
    Matches_city = season_2011['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2012 (df):
    season_2012 = df[df['Season'] == 'IPL-2012']
    Matches_city = season_2012['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2013 (df):
    season_2013 = df[df['Season'] == 'IPL-2013']
    Matches_city = season_2013['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2014 (df):
    season_2014 = df[df['Season'] == 'IPL-2014']
    Matches_city = season_2014['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2015 (df):
    season_2015 = df[df['Season'] == 'IPL-2015']
    Matches_city = season_2015['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2016 (df):
    season_2016 = df[df['Season'] == 'IPL-2016']
    Matches_city = season_2016['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2017 (df):
    season_2017 = df[df['Season'] == 'IPL-2017']
    Matches_city = season_2017['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2018 (df):
    season_2018 = df[df['Season'] == 'IPL-2018']
    Matches_city = season_2018['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2018 (df):
    season_2018 = df[df['Season'] == 'IPL-2018']
    Matches_city = season_2018['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def matches_in_cities_2019 (df):
    season_2019 = df[df['Season'] == 'IPL-2019']
    Matches_city = season_2019['city'].value_counts()
    Matches_city = pd.DataFrame(Matches_city)
    Matches_city = Matches_city.reset_index()
    Matches_city = Matches_city.rename(columns={'index': 'City', 'city': 'No. of matches played'})
    return Matches_city

def m_2008 (df):
    season_2008 = df[df['Season'] == 'IPL-2008']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig=px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2009 (df):
    season_2008 = df[df['Season'] == 'IPL-2009']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2010 (df):
    season_2008 = df[df['Season'] == 'IPL-2010']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2011 (df):
    season_2008 = df[df['Season'] == 'IPL-2011']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2012 (df):
    season_2008 = df[df['Season'] == 'IPL-2012']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2013 (df):
    season_2008 = df[df['Season'] == 'IPL-2013']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2014 (df):
    season_2008 = df[df['Season'] == 'IPL-2014']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2015 (df):
    season_2008 = df[df['Season'] == 'IPL-2015']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2016 (df):
    season_2008 = df[df['Season'] == 'IPL-2016']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2017 (df):
    season_2008 = df[df['Season'] == 'IPL-2017']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2018 (df):
    season_2008 = df[df['Season'] == 'IPL-2018']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def m_2019 (df):
    season_2008 = df[df['Season'] == 'IPL-2019']
    Matches_winner = season_2008['winner'].value_counts()
    Matches_winner = pd.DataFrame(Matches_winner)
    Matches_winner = Matches_winner.reset_index()
    Matches_winner = Matches_winner.rename(columns={'index': 'Team', 'winner': 'Number of wins'})
    fig= px.bar(Matches_winner, x='Team', y='Number of wins', color_discrete_sequence=px.colors.qualitative.Light24)
    return fig

def teams (df):
    team_list = df['team1'].unique().tolist()
    team_list.insert(0, 'None')
    return team_list

def srh_details (df):
    srh = df[df['team1'] == 'Sunrisers Hyderabad']
    T_n_m= len(srh)
    toss_wins= len(srh[srh['toss_winner'] == 'Sunrisers Hyderabad'])
    decided_t_field= len(srh[srh['toss_decision'] == 'field'])
    winner= len(srh[srh['winner'] == 'Sunrisers Hyderabad'])
    print("Total number of matches played= {}".format(T_n_m))