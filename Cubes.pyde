##############
# Created by Eric Davidson
# Generate structures built from cubes (or slabs) with Perlin noise
##############


# Dimensions of the structure
grid_height = 20
grid_width = 20


# Customize the basic block
block_size = 50
block_height = 50
lines = 5
sw = 4

# Adjust the parameters affecting perlin noise
noise_scale = .01
noise_multiplier = 100
noise_dampener = 2

# Eventually multiplied by block size
image_border_buff = 5


# Important (and fragile) code used to center the structure based on block size
#################
w = grid_width * block_size + grid_height * block_size + image_border_buff * block_size
h = grid_height * block_size/2 + grid_width * block_size/2 + (int(noise(0, 0) * noise_multiplier) / noise_dampener * block_height) + image_border_buff * block_size

start_block_x = w/2 - grid_height/2 * block_size + grid_width/2 * block_size
start_block_y = h/2 - grid_height/2 * block_size/2 - grid_width/2 * block_size/2 + (int(noise(0, 0) * noise_multiplier) / noise_dampener * block_height/2)
#################


# Basic Block, centered on top face
def draw_block(x, y):
    beginShape()
    
    # Top Face
    vertex(x - block_size, y)
    vertex(x, y - block_size/2)
    vertex(x + block_size, y)
    vertex(x, y + block_size/2)
    endShape(CLOSE)
    
    # Left Face
    beginShape()
    vertex(x - block_size, y)
    vertex(x, y + block_size/2)
    vertex(x, y + block_height + block_size/2)
    vertex(x - block_size, y + block_height)
    endShape(CLOSE)
    
    #Add lines to left face (Helps with depth)
    line_sep = block_height/lines
    for l in range(lines):
        line(x - block_size, y + (l * line_sep), x, y + block_size/2 + (l * line_sep))
    
    # Right Face
    beginShape()
    vertex(x + block_size, y)
    vertex(x, y + block_size/2)
    vertex(x, y + block_height + block_size/2)
    vertex(x + block_size, y + block_height)
    endShape(CLOSE)
    
    
def setup():
    size(w, h)
    
    # Need to extract to variable
    background(190, 194, 249)
    
    # Take advantage of screen resolution
    pixelDensity(2)
    
    # Width of lines
    strokeWeight(sw)

    # Color of cubes
    fill(254, 171, 227)
    
    
    # Debugging for centering structure
    # line(w/2, 0, w/2, h)
    # line(0, h/2, w, h/2)
    
    # Draw each cube
    for x in range(grid_height):
        for y in range(grid_width):
            
            # Generate Perlin Noise and normalize
            cubes = int(noise(x * noise_scale, y * noise_scale) * noise_multiplier) / noise_dampener
            
            # Use normalized perlin noise to generate towers
            for i in range(cubes):
                draw_block((start_block_x + x*block_size) - y*block_size, (start_block_y + x*(block_size/2)) + y*(block_size/2) - i*(block_height))
    
    # Save to example folder
    save('Examples/Vapor/' + str(grid_height) + '-' + str(grid_width) + '.png')
    
    