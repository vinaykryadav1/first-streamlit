# IMPORT
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.title('Welcome my world')
st.write('Hello world')
st.success('Success')
st.info('information')
st.warning('Warning')
st.error('error')
st.exception(ZeroDivisionError('not possible'))
st.help(ZeroDivisionError)
st.code('x = 10\n''for i in range(x):\n''\tprint(i)')

st.checkbox('Male')
if st.checkbox('Adult'):
    st.write('Hello Gen-z')

#st.radio('Select : ', ('Male','Female','Other'))
radio_box = st.radio('Select : ', ('Male','Female','Other'))
if(radio_box == 'Male'):
    st.write('You are Male')
elif(radio_box == 'Female'):
    st.write('You are Female')
elif(radio_box == 'Other'):
    st.write('You are Other Gender')

st.subheader('SelectBox')
select_box = st.selectbox("A to Z : ",['A','B','C','D','E'])
st.write("You have selected : ", select_box)

st.subheader('MultiSelectBox')
multiselect_box = st.multiselect("A to Z : ",['A','B','C','D','E'])
st.write("You have selected : ", multiselect_box)

st.button('Click Me')
st.slider("Slider : ",1,50, step=2)
st.text_input('Name : ')
password = st.text_input("Password : ", type='password')

st.text_area('Write about yourself')

st.number_input('enter your age',18,80)
st.date_input('enter DOB' )
st.time_input('time')

# file upload
st.header('File Upload')
# file upload CSV and execl
document = st.file_uploader('CSV and Excel: ', type=['csv','xlsx'])
if document is not None:
    if document.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':  # Excel file type
        df = pd.read_excel(document)
    elif document.type == 'text/csv':  # CSV file type
        df = pd.read_csv(document)
    else:
        st.error("Unsupported file type")
    st.table(df.head())

# file upload image
img_file = st.file_uploader('upload image : ', type=['png','jpeg','jpg'])
if img_file is not None:
    st.image(img_file)

# file upload video
video_file = st.file_uploader('upload video :', type=['mkv','mp4'])
if video_file is not None:
    st.video(video_file)

# file upload audio
audio_file = st.file_uploader('upload video :', type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())

st.header('Plots')
chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['A','B','C'])

st.subheader('Line Chart') # Line chart
st.line_chart(chart_data)
st.subheader('Area Chart')  # Area chart
st.area_chart(chart_data)
st.subheader('Bar Chart')   # Bar chart
st.bar_chart(chart_data)

st.subheader('Matplotlib and seaborn')
# loading dataframe
df = pd.read_csv('products.csv')
st.dataframe(df)
# Bar plot with matplotlib
fig = plt.figure(figsize = (15,7))
df['productLine'].value_counts().plot(kind='bar')
st.pyplot(fig)
# Bar plot with seaborn
fig = plt.figure(figsize = (15,7))
sns.distplot(df['productScale'])
st.pyplot(fig)
# Multiple Graph in one column
col1, col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['productScale'],kde = False)
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure()
    sns.set_theme(context='poster', style='darkgrid')
    sns.distplot(df['productScale'],hist = False)
    st.pyplot(fig2)

# Scatter Plot
fig,ax = plt.subplots(figsize = (15,7))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

# count-plot
fig = plt.figure(figsize = (15,7))
sns.countplot(data=df, x = 'productLine')
st.pyplot(fig)

# Box-Plot
fig = plt.figure(figsize = (15,7))
sns.boxplot(data=df, x = 'productLine', y ='productVendor')
st.pyplot(fig)

# Violin-Plot
fig = plt.figure(figsize = (15,7))
sns.violinplot(data=df, x = 'productLine', y ='productVendor')
st.pyplot(fig)

# Altari scatter plot
chart_data =pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a',y = 'b',size = 'c', tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

# Interactive charts with line and area chart
lang_list = df.columns.tolist()
lang_choices = st.multiselect('choose head', lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)
st.area_chart(new_df)

# data Visualisation with plotly (Pie Chart)
st.dataframe(df.head())
fig = px.pie(df, values = 'buyPrice', names = 'productLine',opacity =.8)
st.plotly_chart(fig)

# histogram
x = np.random.randn(200)
y = np.random.randn(200)
z = np.random.randn(200)
hist_data = [x,y,z]
group_label = ['group-1','group-2','group-3']
fig = ff.create_distplot(hist_data,group_label)
st.plotly_chart(fig)




