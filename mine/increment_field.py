class Cliente(models.Model):
    """This is the client data model, it holds all client information. This
       docstring has to be improved."""
    def number():
        no = Cliente.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    clientcode = models.IntegerField(_('Code'), max_length=6, unique=True,
                                     default=number)
