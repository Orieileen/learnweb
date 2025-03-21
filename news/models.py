from django.db import models
#富文本编辑器（不需要上传图片用这个）
from ckeditor.fields import RichTextField
#富文本编辑器上传（需要上传图片就用这个）
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField('分类名称', max_length=20)

  class Meta:
    db_table = 'categrory'
    verbose_name = '分类管理'
    verbose_name_plural = '分类管理'

  def __str__(self):
    return self.name
  
class News(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField('标题', max_length=200)
  content = RichTextUploadingField()
  #                                                   blank:提交表单允许为空   null：运行数据库存null（就是可以不填）
  cover = models.ImageField('封面', upload_to='news', blank=True, null=True, help_text='封面图片')
  #设置auto_now_add=True后, editable=True不会生效
  created_at = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
  updated_at = models.DateTimeField('更新时间', auto_now=True, editable=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='分类')

  class Meta:
    db_table = 'news'
    verbose_name = '新闻管理'
    verbose_name_plural = '新闻管理'
  
  def __str__(self):
    return self.title
