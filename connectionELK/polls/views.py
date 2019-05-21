import logging

from django.http import HttpResponse
from django.template import loader

from .models import Question

logger = logging.getLogger("Vistas")


def index(request):
    logger.info("Pasamos por el index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    logger.info("info-You're looking at question %s." % question_id)
    logger.warning("warning-You're looking at question %s." % question_id)
    logger.error("error-You're looking at question %s." % question_id)
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    logger.info("You're looking at the results of question %s." % question_id)
    logger.warning("You're looking at the results of question %s." % question_id)
    logger.error("You're looking at the results of question %s." % question_id)
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    logger.info("info-You're voting at question %s." % question_id)
    logger.warning("You're voting at question %s." % question_id)
    logger.error("You're voting at question %s." % question_id)
    return HttpResponse("You're voting on question %s." % question_id)
