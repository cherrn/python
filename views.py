from flask import Response, request, redirect, Blueprint

# services
from feedback_service import send_feedback
from login_service import login_user
from news_services import create, show_ukr_news, show_eng_news, show_new_details, delete_new


views_bp = Blueprint('views_functions', __name__)


@views_bp.route('/')
def index():
    return Response(status=200)


@views_bp.route('/category/feedback', methods=['POST', 'GET'])
def feedBackForm(): 
    if request.method == 'POST':
        send_feedback()       
        return redirect('/')
           
    return Response(status=200)


@views_bp.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        logined_user = login_user()
        return logined_user

    return Response(status=200)


@views_bp.route('/create-news', methods=['GET', 'POST'])
def create_news():
    if request.method == 'POST':
        create()        

    return Response(status=200)


@views_bp.route('/uk_news', methods=['POST', 'GET'])
def news_in_ukrainian():
    ukrain_news = show_ukr_news()

    return ukrain_news

    

@views_bp.route('/en_news', methods=['POST', 'GET'])
def news_in_english():
    english_news = show_eng_news()

    return english_news


@views_bp.route('/news/<int:id>', methods=['POST', 'GET'])
def news_details(id):
    details = show_new_details(new_id=id)

    return details


@views_bp.route('/news/<int:id>/delete', methods=['DELETE'])
def news_delete(id):
    deleted_new = delete_new(new_id=id)

    return deleted_new
