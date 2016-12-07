# -*- coding: utf-8 -*-
from django.http import JsonResponse
from djangoApiDec.djangoApiDec import queryString_required
from KCM.KCM import KCM
import os

@queryString_required(['lang', 'keyword', 'num'])
def kcmApi(request):
	"""Generate list of term data source files
	Returns:
		if contains invalid queryString key, it will raise exception.
	"""
	keyword = request.GET['keyword']
	lang = request.GET['lang']
	num = int(request.GET['num'])
	kcmObject = KCM( num, 'model', 'KCM/')
	model = kcmObject.getFilePath(lang)
	kcmObject.setMissionType('json')
	pq = kcmObject.get_cor_term_freq_pq(model, keyword, 1)
	result = kcmObject.getOrCreate(keyword, kcmObject.return_top_n_cor_terms, pq)

	return JsonResponse(result, safe=False)