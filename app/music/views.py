# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from app.music.models import *
from django.conf import settings


# presently using generic views for everything. add custom views here as needed

def getFinalList(user):
    songs = Song.objects.all()
    votes = SongVote.objects.filter(voter=user)
    votesHash = {}
    finalList = []
    for v in votes:
       votesHash[v.song.id] = v.amount
    for s in songs:
       newS = {}
       newS["song"] = s
       newS["id"] = s.id
       newS["votes"] = s.votes()

       if s.id in votesHash:
          newS["vote"] = votesHash[s.id]
       else:
          newS["vote"] = 0

       newS["states"] = calcVisibility(newS["vote"])
       finalList.append(newS)

    finalList = sorted(finalList, key=lambda a: a["id"], reverse=True)
    return finalList


def music_submit_song(request):
  if request.user.is_authenticated():
    if request.method == "POST":
        # LOL CHECK
        title = request.POST['title']
        artist = request.POST['artist']
        title = title.strip()
        artist = artist.strip()
        
        notes = request.POST['notes'] if 'notes' in request.POST else ""

        songdetails =  (artist + " - " + title)
        existingSongs = Song.objects.filter(title__iexact=title, artist__iexact=artist)
        if existingSongs.count() > 0:
           existingSongs[0].vote(request.user, 1)
           songdetails += " already exists! A vote"
           return render_to_response('music/music.html', {'submitted': True, 'songdetails': songdetails, 'songs': getFinalList(request.user)}, context_instance=RequestContext(request))

        if title == "" or artist == "":
           return render_to_response('music/music.html', {'songs': getFinalList(request.user), 'submitted': False},context_instance=RequestContext(request))


        if 'hassong' in request.POST:
           hassong = "on" == request.POST['hassong']
        else:
           hassong = False


        # submit complete, show a little <thanks> note, and display form again
        s = Song(artist=artist, title=title, notes=notes, submitter_hassong=hassong, submitter=request.user)
        s.save()

        s.vote(request.user, 1)

        return render_to_response('music/music.html', {'submitted': True, 'songdetails': songdetails, 'songs': getFinalList(request.user)}, context_instance=RequestContext(request))

    else:
        # yay submit a song template
        return render_to_response('music/music.html', {'songs': getFinalList(request.user), 'submitted': False},context_instance=RequestContext(request))
  else:
    messages.error(request, "You need to login first")
    return redirect('/login?redirect=/music')

# returns a list for disabled state for up, none, and down
def calcVisibility(voteAmt):
   res = []
   res.append(True if voteAmt > 0 else False)
   res.append(True if voteAmt == 0 else False)
   res.append(True if voteAmt < 0 else False)
   return res 


def music_vote(request):
  if request.user.is_authenticated():
    if request.method == "POST":
        song_id = request.POST['song_id']
        vote = request.POST['vote']
        voteAmt = 0
        if vote == "up":
            voteAmt = 1
        elif vote == "none":
            voteAmt = 0
        else:
            voteAmt = -1

        # find the song
        s = Song.objects.get(id=song_id)
        u = request.user
        s.vote(u, voteAmt)

        res = str(s.votes())
        for s in calcVisibility(voteAmt):
           res += ";" + str(s)


        return HttpResponse(res)
  else:
    messages.error(request, "You need to login first")
    return redirect('/login?redirect=/music')

