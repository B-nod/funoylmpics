from multiprocessing import context
from .models import Category,ScoreBoard

def get_all_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return context


def get_all_score(request):
    scores = ScoreBoard.objects.all()
    context = {
        "scores": scores
    }
    return context