!ls ../input/embeddings

train_df = pd.read_csv("../input/02_train.csv")
test_df = pd.read_csv("../input/02_test.csv")
print("Train shape: ", train_df.shape)
print("Test shape: ", test_df.shape)

#show the first rows in the file
train_df.head() 

#TARGET DISTRIBUTION
#We want to take a look at the distribution of the target variable 
#in order to understan more about the imbalance and so on. 

cnt_srs = train_df['target'].value_counts()
trace = got.Bar(
    x=cnt_srs.index,
    y=cnt_srs.values,
    marker=dict(
        color=cnt_srs.values,
        colorscale = 'Picnic'
        reversescale = True
    ),
)

layout = go.Layout(
    title = 'Target Count',
    font = dict(size = 18)
)

data = [trace]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = 'TargetCount')
        
        #Target distribution

labels = (np.array(cnt_srs.index))
sizes = (np.array((cnt_srs / cnt_srs.sum())*100))

trace = go.Pie(labels=labels, values=sizes)
layout = go.Layout(
    title = 'Target distribution',
    fot=dict(size=18),
    width=600,
    heigh=600,
)
