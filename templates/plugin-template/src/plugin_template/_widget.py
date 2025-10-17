from napari import Viewer
from napari.layers import Image, Labels
from napari.utils.notifications import show_info

from magicgui import magic_factory

import pathlib
import datetime

import numpy as np

from skimage import filters
from skimage import morphology

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas


@magic_factory(call_button='Create Mask')
def simple_masking_widget(viewer: Viewer, image: Image,
                          median_filter:int=0, closing:int=3, opening:int=3):
    image_data = image.data  # збережемо дані в тимчасову змінну

    # виведемо ім'я шару та розмірність зображення
    show_info(f'Image name: {image.name}')
    show_info(f'Image shape: {image_data.shape}, dtype: {image_data.dtype}')

    # попередня обробка зображення медіанним фільтром
    preprocessed_image = filters.median(image_data,
                                        footprint=morphology.disk(median_filter))
    # побудова маски за допомогою порогу Отсу
    otsu_mask = preprocessed_image > filters.threshold_otsu(preprocessed_image)
    # закриттям маски позбавляємось дрібних прогалин
    pre_filtered_mask = morphology.closing(otsu_mask,
                                           footprint=morphology.disk(closing))
    # відкриттям маски видаляємо дрібні артефакти поза клітиною
    filtered_mask = morphology.opening(pre_filtered_mask,
                                       footprint=morphology.disk(opening))

    # додаємо шар Labels з отриманою маскою    
    viewer.add_labels(filtered_mask, name=f'{image.name}_simple_mask', opacity=0.5)


@magic_factory(call_button="Press me",
               slider_float={"widget_type": "FloatSlider", 'min': -5, 'max': 5},
               dropdown={"choices": ['first', 'second', 'third']},)
def widget_demo(viewer: Viewer,
                maybe: bool,
                some_int: int,
                spin_float:float=3.14159,
                slider_float:float=2.71828,
                string:str="Text goes here",
                dropdown:str='first',
                date=datetime.datetime.now(),
                filename=pathlib.Path('/some/path.ext')):
    ''' Widget fields example
    
    '''
    show_info(f'Buttom pressed')


@magic_factory(call_button="Build plot",
               b={"choices": [2, 5, 10]},)
def plot_demo(viewer: Viewer,
              b:int=5):
    ''' Matplotlib plotting example
    
    '''
    # Langmuir adsorption equation
    x = np.linspace(0,1,100)
    y = b*x / (1+b*x)
    
    mpl_fig = plt.figure()
    ax = mpl_fig.add_subplot(111)
    ax.plot(x,y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Langmuir adsorption model')
    viewer.window.add_dock_widget(FigureCanvas(mpl_fig), name='Plot')