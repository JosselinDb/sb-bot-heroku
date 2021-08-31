import re
class Sign:
    """
        __ensures__
    Représente un message envoyé contenant des règles

        __attributes__
    color : int (read-only)
        Code couleur du message pour l'embed
    image_url : str (read-only)
        Url de l'image pour le thumbnail de l'embed
    articles : str (read-only)
        Différents articles du panneau


        __methods__
    
    generate_rules(articles_files) : list[str]
        Récupère la liste des articles à partir du lien du fichier
    """

    def __init__(self, id : str, title : str, color : int, image_url : str, /, articles_file = None, content = None) -> None:
        self._id = id
        self._title = title
        self._articles = None if articles_file is None else Sign.generate_rules(articles_file)

        self.description = self._make_description_from_articles() if content is None else content

        self._color = color
        self._image_url = image_url

    
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title    
    
    @property
    def articles(self):
        return self._articles
    
    @property
    def color(self):
        return self._color
    
    @property
    def image_url(self):
        return self._image_url


    @staticmethod
    def generate_rules(articles_file : str) -> list:
        """
            __ensures__
        Récupère la liste des articles contenu dans le fichier, et la renvoit

            __attributes__
        articles_file: le fichier qui contient les articles. format: article1\n\narticle2\n\n...
        """

        with open(articles_file, 'r', encoding="utf-8") as file:
            articles = filter(
                lambda line: line.strip(" \n") != '',
                file.readlines()
            )

            return list(articles)


    def _make_description_from_articles(self) -> str:
        return "".join(map(
            lambda article: re.sub(r'(.+)', r'► \1\n', article),
            self.articles)
        )