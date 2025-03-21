from django.db import models

# Create your models here.
class Team(models.Model):
  id = models.AutoField(primary_key=True)
  avatar = models.ImageField('头像', upload_to='team', help_text='图片尺寸1：1')
  name = models.CharField('姓名', max_length=100)
  position = models.CharField('职务', max_length=100)
  rank = models.IntegerField('排序')

  class Meta:
    db_table = 'team'
    verbose_name = '团队管理'
    verbose_name_plural = '团队管理'

#__str__ 是用于告诉 Python：“如果我要把这个对象变成字符串，该显示什么？”
#就像你给对象贴了个标签，别人问“你是谁”，它会说：“我是张三 - 项目经理”。
  def __str__(self):
    return self.name