# Problem Approach 

1. Take a high resolution picture of the finished puzzle and all of the puzzle pieces
2. Digitize each piece using some sort of edge detection algorithm 
3. Template match each piece to the finished picture and get a set of canidate positions for the piece 
4. With this set of canidate positions in hand, start a search using the piece geometry to further pinpoint where a piece belongs. 
5. Output final result 





# Resources

### Digitizing pieces 
https://towardsdatascience.com/solving-jigsaw-puzzles-with-python-and-opencv-d775ba730660

### Template Matching 
https://medium.com/cornell-tech/jigsolved-computer-vision-to-solve-jigsaw-puzzles-70b8ad8099e5

### Existing Repos  
Solve by Shape only, requires high res scans of each piece 
https://github.com/kellinwood/PuzzleSolver

### Papers
**A Fully Automated greedy square jigsaw puzzle solver**
Only concerned with shape
https://www.cs.bgu.ac.il/~ben-shahar/Publications/2012-Pomeranz_Shemesh_and_Ben_Shahar-A_Fully_Automated_Greedy_Square_Jigsaw_Puzzle_Solver.pdf

**Jigsaw Puzzle Solver using shape and color**
Uses shape + color info at boundary for fitting, stil does not use completed picture 
https://pdfs.semanticscholar.org/75b2/e0dd5e141b1f74100ffb379660f988e22b75.pdf?_ga=2.179986852.1001705749.1562359496-589338213.1562359496

**Computer Vision System for Solving Jigsaw Puzzles**
Solving square pieces using color info at boundaries only
https://pdfs.semanticscholar.org/4391/27dc17d8be5493f6f8dc4f27fcecde02b3f9.pdf
