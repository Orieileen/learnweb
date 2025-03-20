from django.db import models

# Create your models here.
class Slide(models.Model):
  id = models.AutoField(primary_key=True)
  image = models.ImageField('幻灯片', upload_to='slide', help_text='最佳尺寸1920*1280')
  title = models.CharField('标题', max_length=200, help_text='一级标题')
  content = models.CharField('内容', max_length=200, help_text='二级标题')

  class Meta:
    db_table = 'slide'
    verbose_name = '幻灯片管理'
    verbose_name_plural = '幻灯片管理'