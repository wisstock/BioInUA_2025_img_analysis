import numpy as np


def a_and_b(a, b):
    ''' Приклад функції, що додає два числа.
    '''
    return a + b


def background_correction(input_img:np.ndarray,
                          background_percentile:float=1):
    ''' Функція для корекції фону зображення за допомогою віднімання
    перцентиля інтенсивності.

    Parameters
    ----------
    input_img : np.ndarray
        Вхідне зображення у вигляді numpy масиву.
    background_percentile : float, optional
        Перцентиль інтенсивності, що використовується для оцінки фону.
        За замовчуванням 1.
    
    Returns
    -------
    np.ndarray
        Кореговане зображення з віднятим фоном з типом даних, що відповідає
        вхідному зображенню.
    '''
    back_int = np.percentile(input_img,
                             background_percentile)
    corr_img = input_img - back_int
    corr_img = corr_img.clip(min=0)
    return corr_img.astype(input_img.dtype)


if __name__ == "__main__":
    print("This module is a part of the package template.")