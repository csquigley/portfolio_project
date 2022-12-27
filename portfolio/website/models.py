from django.db import models
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.ImageField(upload_to='media/post_images',default='post_images/giant_cat.png',blank=True)
    
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    image_url = models.ImageField(upload_to='project_images',default='post_images/giant_cat.png',blank=True)
    code_snippet = models.TextField(blank=True)
    code_snippet_is_html = models.BooleanField(default=False,verbose_name='Already HTML?')
    github_url = models.URLField(blank=True)
    def __str__(self):
        return f'{self.title}'
    def save(self,*args,**kwargs):
        if self.code_snippet_is_html == False:
            self.code_snippet = highlight(self.code_snippet, PythonLexer(), HtmlFormatter())
        self.code_snippet_is_html = True
        super().save(*args, **kwargs)


#project subsections will have different styling depending on the type
SECTION_TYPES = {
    ('opt1','image_section'),
    ('opt2','text_section'),
    ('opt3','code_section'),
    ('opt4','sub_section'),
    ('opt5','html_section'),
}
#each of these will be associated with a different section template
#allowing for more options to organize project posts
SECTION_TEMPLATES = {
    ('CF','CONTENT_FULL'),
    ('IR','IMAGE_RIGHT'),
    ('IL','IMAGE_LEFT'),
}

class ProjectSection(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    section_type = models.CharField(max_length=4,choices=SECTION_TYPES,default='opt1',null=False,blank=False)
    section_template = models.CharField(max_length=2,choices=SECTION_TEMPLATES,default='CF',null=False,blank=False)
    subtitle = models.CharField(max_length=200,blank=True)

    content = models.TextField(blank=True)
    #if content is html you can disply it raw and apply your own CSS
    content_is_html = models.BooleanField(default=False,verbose_name='Already HTML?')
    image_url = models.ImageField(upload_to='media/project_images',blank=True)
    image_description = models.CharField(max_length=300,blank=True)
    customCSS = models.FileField(upload_to='media/customCSS',blank=True)
    use_customCSS = models.BooleanField(default=False,verbose_name='use custom CSS?')
    #a code snippet will go through pygmentS
    code_snippet = models.TextField(blank=True)
    code_snippet_is_html = models.BooleanField(default=False,verbose_name='Already HTML?')

    def save(self,*args,**kwargs):
        if self.customCSS is not None:
            self.use_customCSS = True
        if self.code_snippet_is_html == False:
            self.code_snippet = highlight(self.code_snippet, PythonLexer(), HtmlFormatter())
        self.code_snippet_is_html = True
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.project.title}'
    
