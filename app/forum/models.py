from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse


class Thread(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('thread_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('thread_update', args=(self.pk,))
