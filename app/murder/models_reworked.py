def emailRoundPlayer(sender, **kwargs):
   if kwargs['created']:
      instance = kwargs['instance']
      # only send email on new RoundPlayer instances, not on every kill
      message = render_to_string('murder/email/newround.txt', {'rp':instance})
      send_mail('Welcome to Murder@CSE. Semester 2 2013', message, 'csesoc.murder@cse.unsw.edu.au', [instance.player.email], fail_silently=False)

post_save.connect(emailRoundPlayer, sender=RoundPlayer)
