# NRGmile
An accurate and customizable code for determine the difficulty and energy mile rating of a given route.

## Introduction
Traditionally, the hiking and running community has relied on anecdotal evidence for determining the difficult of a route.
Later on, a basic measure of the energy miles spent on a given route was developed by Paul Petzoldt based off the overall distance traveled and the elevation gain.
However, this measure did not take into account many important factors that affect performance, including: (1) variations in elevation of the projected hiking distances, (2) consideration for negative (downwards) slopes, (3) the various terrains one might encounter e.g dirt, snow, sleet, etc., (4) weight of backpack, and (5) individual differences in ability.

**The focus of this project is building a more accurate model for determining route difficulty rating.** By combining exercise science studies with numerical methods, we hope to achieve the first step in developing a robust difficulty measurement system.

## Potential Uses
Some potential uses for this system include:
- Planning long backpacking routes that require a relatively even distribution of energy miles each day
- Finding the fastest marathons that yield the fastest times (think Boston Marathon qualifying)
- Determining if a hike is suitable for your fitness level
- Determining proper training routes
- And many more...

## How to Use
1. Download or clone this repository. Make sure you have Python 3 installed on your system.
2. Add your route CSV file to the main directory.
  - It is important that the CSV file is in the proper format. 
    1. There must be two columns in the CSV.
    2. The first column heading should read "distance (mi)" and the second column heading should read "altitude (ft)". The column entries should be in the corresponding measurement unit.
    3. There can be no duplicate values in the distance (mi) column.
3. The main file you will be running is "nrgmile.py" within the main directory. Edit the file to read in your specific CSV file and change any parameters you see fit.
4. If you wish to fine-tune the inner workings of the algorithm, most of the numerical techniques are programmed in the "main.py" file within the main directory.

## More Information
Find more detailed information and mathematical foundation for this algorithm at https://tomoverman.github.io/NRGmile/

## Future Improvements
We are looking to collaborate with like-minded adventurers who have background in applied mathematics, exercise science, or software development. We are looking to conduct our own tailored exercise experiments on the effects of various factors on human performance; we need help from exercise scientists or biologists in making this happen in as unbiased of a manner as possible.

## Questions or Advice
Please email tomoverman2025@u.northwestern.edu for suggestions and/or questions. 
