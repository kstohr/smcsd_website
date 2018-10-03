
# coding: utf-8
import pandas as pd


if __name__ == "__main__":
    # load data
    FAQ_GOOGLE_SHEET = os.environ.get('FAQ_GOOGLE_SHEET')
    data = pd.read_csv(FAQ_GOOGLE_SHEET)

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
    filepath = 'faq.html'
    with open(filepath, "w") as html_file:
        html_file.write(html)