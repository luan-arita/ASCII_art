## ASCII-Art

A program that turns images into ASCII Art. 

It is created by extracting RGB tuples from all of the image's pixels (with the help of Pillow), converting those into single-value brightness numbers and, finally, associating those brightness numbers into its respective ASCII character (which are ordered from thinnest to boldest). 

It also features colored images. The RGB values are converted into binary numbers through bitwise operators, which allows us to identify which colors between the three (R, G, B) are most predominant in the pixel and, consequently, 8 possible colors to view.

Other features that could be implemented are GIF support, another method for a broader color identification and a possible GUI.

![WindowsTerminal_MvnmkYNLTf](https://github.com/luan-arita/ASCII_art/assets/35427506/15efeab0-b896-467e-8a9e-4266ac52f670)

## Usage
1. Download [main.py](https://github.com/luan-arita/ASCII_art/blob/main/main.py)
2. Add your image in the same folder as `main.py`.
3. Execute:
```sh
python -u main.py imageFilename [i] [-c] [-m {1, 2, 3}] [-hs HEIGHT]
```
positional arguments:

  filename              Name of the image file

optional arguments:

  `-h, --help`:            show this help message and exit
  
  `-i, --invert`:          Inverts all the brightness.
  
  `-c, --color`:           Adds colours to the image.
  
  `-m {1,2,3}, --map {1,2,3}`:        Choose brightness mappings. 1 for Average, 2 for Lightness and 3 for Luminosity.
  
  `-hs HEIGHT, --height HEIGHT`:      Choose image size by adjusting its height.

  ## Features
- Three different ways of mapping RGB values into brightness:
  * Average: `(R + G + B) / 3`
  * Lightness: `(max(R, G, B) + min(R, G, B)) / 2`
  * Luminosity: `0.21 R + 0.72 G, + 0.07 B`
 <p float="left">
  <img src="/1.png" width="250" />
  <img src="/2.png" width="250" /> 
  <img src="/3.png" width="250" />
</p>

- Invert image brightness

![sai2_3s7Xr3GIjt](https://github.com/luan-arita/ASCII_art/assets/35427506/6d5175df-3256-4746-bf7f-80852a1a14ea)

- Change image resolution

![WindowsTerminal_nVsjMgO2EO](https://github.com/luan-arita/ASCII_art/assets/35427506/efe542f4-993d-47ef-8bd6-b96e4e09d74c)


- 8 different colors

![WindowsTerminal_AeUBm8FAJE](https://github.com/luan-arita/ASCII_art/assets/35427506/132bbb4e-3227-4d21-8257-6bdf1996e7a3)


  ## Known Issues


  * Depending on the program you're using to view the ASCII Art the image's aspect ratio may look wrong. That's because of the height of the characters, whereas in Windows Command Prompt, for example, has characters roughly three times tall as they are wide. To fix this, we have to print each character in each row two to three times to stretch the image back out. This can be easily changed in the function `get_ASCII_matrix`. I personally Window's Terminal, but using Notepad or any other program may end up looking different.

## Contact

[Luan Arita](https://www.linkedin.com/in/luan-arita-319870262/) - luan.arita@unesp.br

## Acknowledgements
* [Robert Heaton](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/) for guiding on how to make this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/sathwikmatsa/ASCII-art/blob/master/LICENSE) file for details


