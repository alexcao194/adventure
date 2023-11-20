from framework.core.singleton import Singleton
from framework.utils.vector2 import Vector2
from framework.core.assets import Assets


class MediaQuery(Singleton):
    '''
    MediaQuery is a singleton class that contains the size of the window and the aspect ratio.
    '''
    size = Vector2(1200, 800)
    aspect_ratio = size.x / size.y
    font_family = Assets.font
    font_size = 32
    