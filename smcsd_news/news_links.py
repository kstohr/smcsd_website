
# coding: utf-8
import pandas as pd

# load data
data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRL_OqBRKS_FDjqoVvOfMnL5sRjuPRW0u9KAGt1HSAc8mLWSF6QrGxg67ERcVkOY9InrG9slMkSnGnC/pub?output=csv")

#clean data
data = data.sort_values('type', ascending=False).reset_index()

#list items
items = []

def build_html(df, link_type):
    items = []
    data = df[df['type'] == link_type].reset_index()
    for row in range(len(data)):
        title = data.loc[row,'title'].strip().upper()
        link = data.loc[row,'link'].strip()
        source = data.loc[row, 'source']
        author = data.loc[row, 'author']
        date = data.loc[row, 'date']
        item = """
<h3><a href="{}">{}</a></h3>
{}, {}, {}""".format(link, title, source, author, date)
        items.append(item)
    pre = """<h2> {}</h2>""".format(link_type)
    post = "<hr>"
    html = pre + ''.join(items) + post
    html = html.replace('nan,', '')
    return html

l_lists = []
for l_type in list(set(data['type'])):
    l_html = build_html(data, l_type)
    l_lists.append(l_html) 

html = ''.join(l_lists)
                                                            
with open("news_links.html", "w") as html_file:
                  html_file.write(html)