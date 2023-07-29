from django.core.management import BaseCommand
from news.models import Article, Author, Category
import openai
from django.conf import settings
from django.core.files.base import ContentFile
from urllib.request import urlopen

class Command(BaseCommand):
    help = 'Generate article'

    openai.api_key = settings.OPEN_AI_KEY

    def add_arguments(self, parser):
        parser.add_argument('article_prompt', type=str, help='What should the article be about')
        parser.add_argument('image_prompt', type=str, help='Generate image')

    def handle(self, *args, **options):
        article_prompt = options['article_prompt']
        image_prompt = options['image_prompt']

        title_prompt = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = f'Generate a article title based of this {article_prompt}',
            max_token = 256,
        )

        title = title_prompt.choices[0].text_strip()

        body_prompt = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = f'Generate a article body based of this title {title}',
            max_token = 256,
        )

        body = body_prompt.choices[0].text_strip()

        response = openai.Image.create(
            prompt = image_prompt,
            n = 1,
            size = "1024x1024"
        )
        image_url = response['data'][0]['url']

        article = Article()
        article.title = title
        article.body = body
        article.author = Author.objects.first()
        article.status = 'draft'
        article.category = Category.objects.first()

        article.image = ContentFile(urlopen(image_url).read(), f'{title}.jpg')

        article.save()


        self.stdout.write(self.style.sucess('Successfully generated article "%s"' % article_prompt))