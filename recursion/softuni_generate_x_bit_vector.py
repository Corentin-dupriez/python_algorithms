n = int(input())
vector = [0] * n



def generate_x_bit_vector(vector: list, idx = 0):
  if idx == len(vector):
    print(vector)
    return
  for i in range(0,2):
    vector[idx] = i 
    generate_x_bit_vector(vector, idx + 1)
    
  

print(generate_x_bit_vector(vector))
