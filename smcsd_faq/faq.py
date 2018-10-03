
# coding: utf-8
import pandas as pd


if __name__ == "__main__":
    # load data
    data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTxXDbXulcbfeyzHUokMuT8jFMpwCKjq5VtZZCeUnt6k5LHgrHAaR_Cw2rpfutaA9HtrNTr802gPzET/pub?output=csv")

    #clean data
    data = data.sort_values('order', ascending=True).reset_index()

    #list items
    items = []
    for row in range(len(data)):
        text = data.loc[row,'text'].strip()
        question = data.loc[row,'question']
        number = data.loc[row, 'order']
        if data.loc[row,'link'] == 'None':
            link = ''
        else:
            link = """<br><a href="{}">Learn more.</a>""".format(data.loc[row,'link'])
        item = """
        <h2>{}. {}</h2>
        <p>{} {}</p>
        """.format(number, question, text, link)
        items.append(item)

    html = ''.join(items)
    filepath = './smcsd_faq/faq.html'
    with open(filepath, "w") as html_file:
        html_file.write(html)