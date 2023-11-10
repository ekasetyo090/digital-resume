import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.markdown('''
# Eka Setyo Agung Mahanani.S,Pi
##### *Resume* 
''')

image = Image.open('profile-pic.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Graduate Bachelor's degree in Fisheries Resource Utilization and a notable GPA of 3.51, graduating with
honors. My academic background has provided me with a robust foundation in data analysis, machine
learning, and technical analysis, complemented by a versatile skill set that includes proficiency in SQL,
Python, Pandas, NumPy, and Jupyter Notebook.
        
During my academic journey, I developed my analytical thinking and data processing skills, 
preparing me for a career in data analysis. In my spare time, I also engaged in technical analysis writing, 
where I produced financial market forecasts. 

Additionally, I have actively pursued further education, completing courses in data science, machine learning, 
and programming, including Data Science from Kelas.work and Dicoding, as well as CS50X from Harvard University. 
I am dedicated to continuous learning. I am eager to embark on a career as a Data Analyst, 
with the goal of bringing my academic achievements and fresh perspective to add value 
to data-driven projects and contribute to a dynamic work environment.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#eka-setyo-agung-mahanani-s-pi">Home <span class="sr-only">(current)</span></a>
      </li>
            <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#courses">Courses</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#project">Project</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([3,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([2,3])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
#####################
st.markdown('''
## Skills
''')

st.markdown('''
### Hard Skills
''')
txt3('Programming', '`Python`, `C`')
txt3('Database Management', '`SQLite3`')
txt3('Data Processing/Wrangling', '`SQL`, `Pandas`, `Numpy`,`Jupyter Notebook`')
txt3('Data Visualization', '`Matplotlib`, `Seaborn`, `Plotly`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web Development', '`Flask`, `HTML`, `CSS`,`streamlit`')
txt3('Technical Analysis', '`Tradingview`')
txt3('Keyword Analysis', '`Google Trend`')

st.markdown('''
### Soft Skills
''')
st.markdown('''
- Learning Agility
- Time Management
- Responsibility
- Trans-Contextual Thinking
- Creative Thinking
- Critical Thinking
- Social Skills
- Communication
- Problem Solving
''')
#####################
st.markdown('''
## Experience
''')

txt('**Data Analyst**, [Zwaan Adriana YouTube Channel](https://www.youtube.com/@ZwaanAdriana)','September 2023 - Present')
st.markdown('''
- Analyzing Optimal Time For Live Streaming.
- Analyzing Search Keyword Traffic.
- Increasing Relevancy Content With Target Audience.
- Increasing Subscriber Gaining Rate.
- Suggesting Future Content.
- [User Statistics](https://socialblade.com/youtube/channel/UCXmlLhyjTdvUuFxtKmptT1w/monthly)
''')

txt('**Technical Analysis Writer**, [Tradingview Profile](https://id.tradingview.com/u/ESA_MAHANANI/)','September 2019 - Present')
st.markdown('''
- Write Financial Market Forecast Articles.
- Analyzing Current Market Condition.
- Write Articles Focused On Educational.
- Articles : [Latest Focasting Articles](https://id.tradingview.com/chart/XAUUSD/PXrYHXML/), 
            [Latest Educational Articles](https://id.tradingview.com/chart/IDX30/8zGSwJyM/)
''')

txt('**Wastewater Treatment Intern** (PT. Inti Luhur Fuja Abadi)','March 2019 - May 2019')
st.markdown('''
- Conducted waste water quality assessments based on production volume ratios.
- Measured discharge volumes.
- Controlled waste water quality parameters in accordance with SNI.
''')


####################
st.markdown('''
## Education
''')

txt('**Bachelors of Fisheries** (Fishery Resource Utilization)', 'August 2019 - March 2021')
txt('*Dr. Soetomo University*, Surabaya','')
st.markdown('''
- GPA: `3.51`
- Graduated With Honors.
- [Thesis](https://drive.google.com/file/d/1_HriEBz6xgsUHyh3UsUyDHbyEmVh1OhR/view), 
            [Transcript](https://drive.google.com/file/d/1fK-REXaxIT8MGfuHb_sx7vGZhOZMYSkQ/view), 
            [Certificate](https://drive.google.com/file/d/1B-lZKMDnPBAr48-tibnMDBWZzs8OSEbd/view)
''')

txt('**Diplomas of Fisheries** (Fishery Product Processing)','August 2016 - August 2019')
txt('*Sidoarjo Polytechnic of Marine and Fisheries*, Sidoarjo','')
st.markdown('''
- GPA: `3.32`
- Received An Grade `A` For Final Project.
- [Final Project](https://drive.google.com/file/d/17ZysIYN1OeJPKPKuGTj9HZ9WjMgkT6TF/view), 
            [Transcript](https://drive.google.com/file/d/18WWHZD9xqdxN9_-ztwJbtDS0QBi4JBX9/view), 
            [Certificate](https://drive.google.com/file/d/1Ofb4dXEfJzTqiSJqnojpjjDAp8n13z2D/view)
''')

#####################
#####################

st.markdown('''
## Courses
''')

txt('**IDCamp 2023** (Data Science)', 'September 2023 - Present')
txt('*Indosat Ooredoo Hutchison X Dicoding*','')
st.markdown('''
- Data Science And Statistics.
- SQL, Python, Pandas, NumPy, And Jupyter Notebook.
- Seaborn, Matplotlib, And Streamlit.
- Tensorflow, And Scikit-Learn.
- Machine Learning.
- Artificial Neural Network(ANN), And Convolutional Neural Network(CNN).
- Project : [Air Quality Dashboard](https://github.com/ekasetyo090/air_quality_dashboard), 
            [Image Classification Model Training](https://colab.research.google.com/drive/1FDW7hYQKcQvZbCNimcYqPZ6pCj_LWctl?usp=sharing)
- Certificate : [Data Science](https://drive.google.com/file/d/1ifDQanD8x5B-tWH5TY1IQUu8ujq6271p/view), 
            [Python](https://drive.google.com/file/d/1L3LXnb1KpvWOMmMVOgoO8PLfPqZ-r5Rp/view), 
            [SQL](https://drive.google.com/file/d/19_hMSMmRakxYEtuZqVR7zTX4GgPYDQ-0/view), 
            [Python Analysis](https://drive.google.com/file/d/1ezaOpgWEwt4kArX_VY-lZ57dM6FrPIOO/view), 
            [Machine Learning](https://drive.google.com/file/d/1yhLvNdpgRm_kc8OY174gM-OCJpCcjir4/view)
''')

txt('**Data Science**', 'June 2023 - September 2023')
txt('*Kelas.work*','')
st.markdown('''
- Data Science And Statistics.
- SQL, Python, Pandas, NumPy, Seaborn, Matplotlib, And Jupyter Notebook.
- Tensorflow, And Scikit-Learn.
- Machine Learning.
- Artificial Neural Network(ANN), And Convolutional Neural Network(CNN).
- GIT Version Control System.
- Project : [Hipotesis Testing](https://colab.research.google.com/drive/1dE80Ot69mOwMLgne6sszX1lqiAiq-ACa?usp=sharing), 
            [House Pricing Analysis](https://colab.research.google.com/drive/1JcWQy0mOBEGduphTRc5DjjW29cRxEvja?usp=sharing), 
            [Game Prediction](https://colab.research.google.com/drive/17C8MEJV4fj7cYLTyPob_DJVZDzxgQoZS?usp=sharing), 
            [Stock Market Prediction](https://colab.research.google.com/drive/1n6M7o4w_yu5bAU45j0OC0sQF-wLdEtsP?usp=sharing)
- [Certificate](https://drive.google.com/file/d/1sFq3wdeFB0MG7AzHg2rF5qnYFx5963lF/view), 
            [Transcript](https://drive.google.com/file/d/1rrSiN_9vlSdUhIwv5A--dM1No9nm2Wun/view)
''')

txt('**Introduction To Computer Science** (CS50X)', 'June 2023 - August 2023')
txt('*Havard University*','')
st.markdown('''
- C, Python, SQL, HTML, CSS, JavaScript, And Flask.
- Data Structures, Algorithms, And Resource Management.
- Cryptography, Security Software And Computer Science.
- Project : [Metatrader 4 Market Data Exporter](https://github.com/ekasetyo090/CSV-EXPORTER)
- [Certificate](https://drive.google.com/file/d/15GY7s0uUjAW5FNXd17t9nS9GhufHnHJo/view) 
''')

#####################
st.markdown('''
## Project
''')
txt4('Hololive(ID-3) Fans Dashboard', 'A data app for studiying talent performance base on their statistics', 'https://hololiveid3-fan-dashboard.streamlit.app/')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/eka-setyo-agung-mahanani/')
txt2('X (Former Twitter)', 'https://twitter.com/vex_39')
txt2('GitHub', 'https://github.com/ekasetyo090')
