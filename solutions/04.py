import numpy as np

def evaluate(drawings: list, boards: list) -> int:
  """"
  approach:
    - keep numbers and hit-array separate
    - determine 'bingo' by using array.sum(axis=0) and array.sum(axis=1). Diagonal checks are not required
    - calculate score by multiplying (np.multiply) boards with hit-array and then use array.sum() on the result
  """
  
  """iterate over drawings"""
  hits = [np.ones((len(board), len(board)), dtype=int) for board in boards]
  for draw in drawings:
    """check each board"""
    for board_id, board in enumerate(boards):
      for row_id, column_id in np.ndindex(board.shape):
        if board[row_id][column_id] == draw:
          hits[board_id][row_id][column_id] = 0
          if check_winner(row_id, column_id, hits[board_id]):
            score = np.multiply(boards[board_id], hits[board_id]).sum() * draw
            print("Winning board:")
            print(boards[board_id])
            print("Hit list:")
            print(hits[board_id])
            print("Score:")
            print(score)
            return score


def check_winner(row_id: int, column_id:int, hit_board: np.array) -> bool:
  for s in hit_board.sum(axis=0):
    if s == 0:
      return True
  for s in hit_board.sum(axis=1):
    if s == 0:
      return True
  return False
            


def main():
  boards = []
  
  """read drawings"""
  try:
    drawings = input("Please enter drawings as comma separated list:")
    if drawings == "":
      print("no drawings entered")
      exit
    drawings = [int(draw) for draw in drawings.split(",")]
  except EOFError:
    pass
  
  """read boards"""
  newln_cnt = 0
  board = []
  while True:
      try:
        input_ = input("")
        if input_ == "":
          """create a new board after each empty line"""
          if board:
            boards.append(np.array(board))
          board = []
          newln_cnt += 1
        else:
          newln_cnt = 0
          """clear spaces"""
          board.append([int(element) for element in input_.split(" ") if element != ""])
        if newln_cnt == 2:
          break
      except EOFError:
          break
  
  evaluate(drawings, boards)


if __name__ == '__main__':
  main()