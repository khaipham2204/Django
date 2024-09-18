# Fixing the N+1 Queries Problem
> https://docs.djangoproject.com/en/5.1/ref/models/querysets/

## Content
The select_related and prefetch_related methods are used to reduce the number of queries made to the database.
- The select_related method is used to follow a relationship of type ForeignKey or OneToOneField.
- The prefetch_related method is used when we have a multiple relationship with another model, i.e. a relationship of type ManyToMany or a reverse ForeignKey
