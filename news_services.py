import locale
from flask import jsonify, request, redirect, Response, abort
from sqlalchemy import func
from pytz import timezone

from models import db, Article
from config import Config
from create_service import save_file


def create():
    json_data = request.get_json()

    password = json_data.get('password')
    title = json_data.get('title')
    text = json_data.get('text')
    description = json_data.get('description')
    language = json_data.get('language')
    image_file = json_data.get('image_file')
    image_url = json_data.get('image_url')

    if password == Config.PASSWORD_TO_ADD_NEWS:
        file_path = save_file(image_file)
        if file_path:
            article = Article(title=title, text=text, description=description,
                              image_file=file_path, image_url=image_url, language=language)
            try:
                db.session.add(article)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return jsonify({'error': str(e)})
    return 'ERROR'


def show_ukr_news():
    session = db.session  # Получение сессии из объекта db
    articles = session.query(Article).filter(func.lower(Article.language) == 'uk').order_by(Article.date.desc()).all()

    # Определите часовой пояс Украины (Europe/Kiev)
    ukraine_timezone = timezone('Europe/Kiev')
    article_list = []

    for article in articles:
        # Преобразуйте дату в часовой пояс Украины
        local_time = article.date.astimezone(ukraine_timezone)

        # Установите локаль на украинский
        locale.setlocale(locale.LC_TIME, 'uk_UA.utf8')

        # Форматирование даты с учетом выбранной локали
        formatted_date = local_time.strftime('%Y  %d-%B   %H:%M')

        article_dict = {
            'id': article.id,
            'title': article.title,
            'description': article.description,
            'image_url': article.image_url,
            'image_file': article.image_file,
            'date': formatted_date
        }

        article_list.append(article_dict)

    return jsonify(article_list)


def show_eng_news():

    session = db.session  # Получение сессии из объекта db
    articles = session.query(Article).filter(func.lower(Article.language) == 'en').order_by(Article.date.desc()).all()

    # Определите часовой пояс Украины (Europe/Kiev)
    ukraine_timezone = timezone('Europe/Kiev')
    article_list = []

    # Установите локаль на английский
    locale.setlocale(locale.LC_TIME, 'en_US.utf8')

    for article in articles:
        # Преобразуйте дату в часовой пояс Украины и отформатируйте ее
        local_time = article.date.astimezone(ukraine_timezone)
        formatted_date = local_time.strftime('%Y  %d-%B   %H:%M')

        article_dict = {
            'id': article.id,
            'title': article.title,
            'description': article.description,
            'image_url': article.image_url,
            'image_file': article.image_file,
            'date': formatted_date
        }

        article_list.append(article_dict)

    return jsonify(article_list)


def show_new_details(new_id):
    session = db.session  # Получение сессии из объекта db

    article = session.get(Article, new_id)  # Использование Session.get() для получения статьи по ID

    if article is None:
        print(id)
        return jsonify({'error': 'Article not found'})

    article_dict = {
        'title': article.title,
        'text': article.text,
        'image_url': article.image_url,
        'image_file': article.image_file,
        'date': article.date.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(article_dict)


def delete_new(new_id):
    session = db.session
    article = session.get(Article, new_id)

    if article is None:
        return abort(404)  # Возвращаем ошибку 404, если статья не найдена
    try:
        session.delete(article)
        session.commit()
        return Response(status=204)
    except:
        return "ERROR DELETING"
