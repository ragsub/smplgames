from django.shortcuts import render
import random
from games.seek.forms import CountForm

# Create your views here.
def seek(request):

    ROWS = 4
    COLS = 4

    row_range = range(ROWS)
    col_range = range(COLS)

    context={}
    context['row_range'] = row_range
    context['col_range'] = col_range

    context['col'] = random.choice(row_range)
    context['row'] = random.choice(col_range)

    if request.method == 'POST':
        form = CountForm(request.POST)
        if form.is_valid():
            seek_cookie = request.session.get('seek_cookie',None)
            cookie_count = seek_cookie['count']
            cookie_best = seek_cookie['best']

            cookie_count = cookie_count + 1
            seek_cookie['count'] = cookie_count
            form.cleaned_data['count'] = cookie_count

            if cookie_count > cookie_best:
                seek_cookie['best'] = cookie_count

            request.session['seek_cookie'] = seek_cookie
            context['form'] = form
            context['best'] = seek_cookie['best']
            return render(request=request,template_name='seek/__core_seek.html',context=context)
    else:
        context['form'] = CountForm()
        seek_cookie = request.session.get('seek_cookie',None)
        if seek_cookie:
            seek_cookie['count'] = 0
        else:
            seek_cookie = {'count':0,'best':0}
        
        request.session['seek_cookie'] = seek_cookie
        context['best'] = seek_cookie['best']


        return render(request=request,template_name='seek/seek.html',context=context)