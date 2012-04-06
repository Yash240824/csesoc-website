from django.shortcuts import get_object_or_404, render_to_response

def slug(request, path):
    p = get_object_or_404(Static, slug=path.replace('/','_'))
    #until the database gets fixed
    import re
    template = re.sub(r'.*templates/', '', p.template)
    return render_to_response(template, { 'allSponsors' : sponsorsList(request), 'object' : p }, context_instance=RequestContext(request) )
    
def index(request):
   return render_to_response('404.html')
