
# coding: utf-8
import os
import pandas as pd
import datetime as dt

if __name__ == "__main__":
    TIMELINE_GOOGLE_SHEET = os.environ.get('TIMELINE_GOOGLE_SHEET')
    data = pd.read_csv(TIMELINE_GOOGLE_SHEET)
    
    # load data
    data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRWJb_ArGuAv1bFfuI1LErzd5J8SYUoWFH4VrgKFvPJy01Yj8PhP-wg5rNTUXyKcOYw24LFhscgAMCh/pub?output=csv")
    
    if data.empty == False: 
        print('Data loaded...')

    #clean data
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values('date', ascending=False).reset_index()

    #html header
    header = """
    <!DOCTYPE html>
    <html>

    <head>
        <link rel="stylesheet" href="styles.css">
        <base target="_parent">
        </head>

    <body>
        <ul class="timeline">
    """

    #html footer
    footer = """
        </ul>
        </body>
        </html>
        """

    #list items
    items = []
    for row in data.index:
        text = data.loc[row,'text'].strip()
        label = data.loc[row,'label']
        if '*Exact date' in text:
            date = data.loc[row,'date'].strftime('%Y')
        else:
            date = data.loc[row,'date'].strftime('%B %Y')
        if data.loc[row,'link'] == 'None':
            link = ''
        else:
            link = """<br><a href="{}">Read Source</a>""".format(data.loc[row,'link'])
        item = """<li>
                <p class="timeline-date">{}</p>
                <div class="timeline-content">
                <h3>{}</h3>
                <p>{} {}</p>
                </div>
                </li>""".format(date,
                                label,
                                text,
                                link)
        items.append(item)

    ul = ''.join(items)
    html = header + ul + footer
    filepath = 'index.html'
    with open(filepath, "w") as html_file:
        html_file.write(html)
        print('New html file written..')
    
    print("File update complete: {}".format(filepath))