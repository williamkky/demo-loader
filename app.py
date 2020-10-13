from flask import Flask, render_template
import time
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bar_admin.html')

@app.route('/get_data')
def get_data():
    time.sleep(5)
    return render_template('get_data.html')

@app.route('/new_loader')
def new_loader():
    time.sleep(5)
    return render_template('new_loader.html')

@app.route('/show_photo')
def show_photo():
    photos = json.loads(requests.get('https://storage.googleapis.com/k11musea_demo/photos.json').text)
    photo_list_for_display = [k for k,v in photos.items()]

    total = len(photo_list_for_display)

    # # Passing pagination of photos
    #
    # page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    #
    # if per_page_default != 'all':
    #     per_page, offset = set_per_page(display_per_page=per_page_default, page=page)
    # else:
    #     per_page, offset = set_per_page(display_per_page=total, page=page)
    #
    # # pagination_photos = get_dict_results(dict_input = photo_dict_session, offset=offset, per_page=per_page)
    # pagination_photos = get_list_results(list_input=photo_list_for_display, offset=offset, per_page=per_page)
    # if total == 0:
    #     per_page = 10000000
    # pagination = Pagination(page=page, per_page=per_page, total=total,
    #                         css_framework='bootstrap4')

    return render_template('list_image.html',
                           photo_dict = photos,
                           photos = photo_list_for_display,
                           total = total)

if __name__ == '__main__':
    app.run()
