from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.dee= Editor(first_name = 'dee', last_name ='sawe', email ='dee@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.dee,Editor))

    def test_save_method(self):
        self.dee.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.dee= Editor(first_name = 'dee', last_name ='sawe', email ='sawe@gmail.com')
        self.dee.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.dee)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news=Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        today='2020-11-11'
        date=dt.datetime.strptime(today, '%Y-%m-%d').date()
        newsByDate=Article.days_news(date)
        self.assertTrue(len(newsByDate)==0)

