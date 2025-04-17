# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
       ___  
      /___\\ 
      (o o) 
     \( : )/
      ( : )
      ( : )
     """,
     # Stage 1: Bottom part starts melting
     """
       ___  
      /___\\ 
      (o o) 
     \( : )/
      ( : )
     """,
     # Stage 2: Only the head remains
     """
       ___  
      /___\\ 
      (o o) 
     \( : )/
     """,
     # Stage 3: Snowman completely melted
     """
       ___  
      /___\\ 
      (o o) 
     """,
     # Stage 4: Only the base remains
     """
       ___  
      /___\\ 
     """
 ]

def get_snowman_stage(stage):
    print(STAGES[stage])