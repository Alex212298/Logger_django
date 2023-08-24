import logging

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render



logger = logging.getLogger(__name__)


def index(request):
    logger.error(msg='ВЫЗОВ ЛОГА')
    return JsonResponse({"success": True})