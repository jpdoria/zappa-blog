import os
import markdown2

from dateutil.parser import parse
from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
jenv = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)


@app.route('/', methods=['GET'])
def category(category='posts'):
    """
    This is the list of posts that are shown in '/'
    """
    try:
        # Get the markdown files in 'posts' directory
        items = []

        for filename in os.listdir(category):
            if 'index.md' in filename:
                continue
            if filename[-3:] == '.py':
                continue

            item = markdown2.markdown_path('{0}/{1}'.format(category,
                                           filename), extras=['metadata'])
            item.metadata['slug'] = filename.split('/')[-1].replace('.md', '')

            items.append(item)

        # Display list of posts in '/'
        template = 'templates/category.html'
        render_data = {}
        render_data[u'title'] = 'Jack of All Trades, Master of None'
        render_data[u'category'] = category
        render_data[u'items'] = sorted(items, key=lambda item: parse(
                                       item.metadata.get('date_created', '')),
                                       reverse=True)

        rendered = jenv.get_template(template).render(render_data)

        return rendered
    except IOError as e:
        print(e)
        return render_template('404.html'), 404


@app.route('/<item_slug>', methods=['GET'])
def item(item_slug, category='posts'):
    """
    Display a single post
    """
    try:
        path = '{0}/{1}.md'.format(category, item_slug)
        html = markdown2.markdown_path(path, extras=['metadata'])
        metadata = html.metadata

        if 'template' in metadata.keys():
            template = metadata['template']
        else:
            template = 'templates/item.html'

        render_data = metadata.copy()
        render_data[u'body'] = html
        render_data[u'category'] = category
        render_data[u'item_slug'] = item_slug
        rendered = jenv.get_template(template).render(render_data)

        return rendered
    except IOError as e:
        return render_template('404.html'), 404

# For local development only
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
