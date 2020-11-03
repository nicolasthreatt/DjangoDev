from django.shortcuts import render
from .forms import StatForm, MultipleStatsForms
from django.forms import formset_factory
from .models import Stat

def home(request):
    return( render(request, 'home.html') )

def stats(request):

    multiple_form = MultipleStatsForms()

    if request.method == 'POST':
        filled_form = StatForm(request.POST)

        if filled_form.is_valid():
            created_stat = filled_form.save()
            created_stat_pk = created_stat.id
            note = 'Getting %s for %s' %(filled_form.cleaned_data['stat'],
                                         filled_form.cleaned_data['player'], )

            filled_form = StatForm()
        else: 
            note = 'Stat was not requested. Try again.'
            created_stat_pk = None
        
        return( render(request, 'stats.html', {'created_stat_pk':created_stat_pk,
                                                   'statform':filled_form,
                                                   'note':note,
                                                   'multiple_form':multiple_form
                                                   }) )
    else:
        form = StatForm()
        return( render(request, 'stats.html', {'statform':form,
                                               'multiple_form':multiple_form
                                               }) )

def more_stats(request):
    number_of_stats = 2

    filled_multiple_stats_form = MultipleStatsForms(request.GET)
    if(filled_multiple_stats_form.is_valid()):
        number_of_stats = filled_multiple_stats_form.cleaned_data['number']
    
    StatFormSet = formset_factory(StatForm, extra=number_of_stats)
    formset     = StatFormSet()

    if(request.method == 'POST'):
        filled_formset = StatFormSet(request.POST)
        if(filled_formset.is_valid()):
            for form in filled_formset:
                print(form.cleaned_data['player'])
            note = 'Stats have been received'
        else:
            note = 'Stats were not requested. Please try again'

        return render(request, 'more_stats.html', { 'note':note,
                                                    'formset':formset
                                                  })
    else:
        return render(request, 'more_stats.html', {'formset':formset})

def edit_stat(request, pk):
    stat = Stat.objects.get(pk=pk)
    form = StatForm(instance=stat)

    if(request.method == 'POST'):
        filled_form = StatForm(request.POST, instance=stat)
        if(filled_form.is_valid()):
            filled_form.save()
            form = filled_form
            note = 'Stat has been updated.'
            return render(request, 'edit_stat.html', {'note':note, 
                                                      'statform':form,
                                                      'stat': stat
                                                      }) 

    return render(request, 'edit_stat.html', {'statform':form, 'stat': stat})  