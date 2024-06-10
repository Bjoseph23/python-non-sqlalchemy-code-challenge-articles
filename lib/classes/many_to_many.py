class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string between 5 and 50 characters.")
        self._title=title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self ]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        articles= Article(self, magazine, title)
        return articles

    def topic_areas(self):
        return list(set([article.magazine.catrgory for article in self.articles()])) if self.articles() else None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = name

        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = category

    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category

    @name.setter
    def name(self, name):
        self._name = name

    @category.setter
    def category(self, category):
        self._category = category

    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return [ articles.author for articles in self.articles()]

    def article_titles(self):
        titles=[article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        pass
    