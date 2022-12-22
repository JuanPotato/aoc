#!/usr/bin/python3

from aoc import *

def solve(input_str):
    return (get_password(input_str), get_password2(input_str))

def teleport(r, c, face):
        # 1: top of face 1
        if r == -1 and 50 <= c < 100 and face == 3: # up
            # to left of face 6
            nr, nc, nface = 100 + c, 0, 0 # right

        # 1: left of face 6
        elif 150 <= r < 200 and c == -1 and face == 2: # left
            # to top of face 1
            nr, nc, nface = 0, r - 100, 1 # down

        # 2: top of face 2
        elif r == -1 and 100 <= c < 150 and face == 3: # up
            # to bottom of face 6
            nr, nc, nface = 199, c - 100, 3 # up

        # 2: bottom of face 6
        elif r == 200 and 0 <= c < 50:
            # to top of face 2
            nr, nc, nface = 0, c + 100, 1 # down

        # 3: left of face 1
        elif 0 <= r < 50 and c == 49 and face == 2: # left
            # to left of face 4
            nr, nc, nface = 149 - r, 0, 0 # right

        # 3: left of face 4
        elif 100 <= r < 150 and c == -1 and face == 2: # left
            # to left of face 1
            nr, nc, nface = 149 - r, 50, 0 # right

        # 4: right of face 2
        elif 0 <= r < 50 and c == 150 and face == 0: # right
            # to right of face 6
            nr, nc, nface = 149 - r, 99, 2 # left

        # 4: right of face 5
        elif 100 <= r < 150 and c == 100 and face == 0: # right
            # to right of face 2
            nr, nc, nface = 149 - r, 149, 2 # left

        # 5: bottom of face 2
        elif r == 50 and 100 <= c < 150 and face == 1: # down
            # to right of face 3
            nr, nc, nface = c - 50, 99, 2 # left

        # 5: right of face 3
        elif 50 <= r < 100 and c == 100 and face == 0: # right
            # to bottom of face two
            nr, nc, nface = 49, r + 50, 3 # up

        # 6: left of face 3
        elif 50 <= r < 100 and c == 49 and face == 2: # left
            # to top of face 4
            nr, nc, nface = 100, r - 50, 1 # down

        # 6: top of face 4
        elif r == 99 and 0 <= c < 50 and face == 3: # up
            # to left of face 3
            nr, nc, nface = 50 + c, 50, 0 # right

        # 7: bottom of face 5
        elif r == 150 and 50 <= c < 100 and face == 1: # down
            # to right of face 6
            nr, nc, nface = 100 + c, 49, 2 # left

        # 7: right of face 6
        elif 150 <= r < 200 and c == 50 and face == 0: # right
            # to bottom of face 5
            nr, nc, nface = 149, r - 100, 3 # up

        else:
            raise ValueError('Undefined Behaviour')
        
        return nr, nc, nface

def get_password(input_str):
    board, path = input_str.split('\n\n')
    board = lmap(list, board.split('\n'))
    path = re.findall(r'\d+|L|R', path)

    r,c = 0,0
    face = 0

    for ci,tile in enumerate(board[r]):
        if tile == '.':
            c = ci
            break

    for p in path:
        if p == 'L':
            face = (face - 1) % 4
            board[r][c] = '>v<^'[face]

        elif p == 'R':
            face = (face + 1) % 4
            board[r][c] = '>v<^'[face]

        else:
            d = int(p)
            while d > 0:
                match face:
                    case 0: dr,dc =  0, 1 # right
                    case 1: dr,dc =  1, 0 # down
                    case 2: dr,dc =  0,-1 # left
                    case 3: dr,dc = -1, 0 # up

                nr = r + dr
                nc = c + dc
                d -= 1

                if not (0 <= nr < len(board) and 0 <= nc < len(board[nr])) or board[nr][nc] == ' ':
                    loopr = r
                    loopc = c
                    while 0 <= loopr < len(board) and 0 <= loopc < len(board[loopr]) and board[loopr][loopc] != ' ':
                        loopr -= dr
                        loopc -= dc

                    nr = loopr + dr
                    nc = loopc + dc

                if board[nr][nc] != '#':
                    r = nr
                    c = nc
                    board[r][c] = '>v<^'[face]

    return (1000 * (r + 1) + 4 * (c + 1) + face)

def get_password2(input_str):
    board, path = input_str.split('\n\n')
    board = lmap(list, board.split('\n'))
    path = re.findall(r'\d+|L|R', path)

    r,c = 0,0
    face = 0

    for ci,tile in enumerate(board[r]):
        if tile == '.':
            c = ci
            break

    for p in path:
        if p == 'L':
            face = (face - 1) % 4
            board[r][c] = '>v<^'[face]

        elif p == 'R':
            face = (face + 1) % 4
            board[r][c] = '>v<^'[face]

        else:
            d = int(p)
            while d > 0:
                match face:
                    case 0: dr,dc =  0, 1 # right
                    case 1: dr,dc =  1, 0 # down
                    case 2: dr,dc =  0,-1 # left
                    case 3: dr,dc = -1, 0 # up

                nr = r + dr
                nc = c + dc
                nface = face
                d -= 1

                # What you are about to see is hard coded solution. Viewer discretion is advised.
                if not (0 <= nr < len(board) and 0 <= nc < len(board[nr])) or board[nr][nc] == ' ':
                    nr,nc,nface = teleport(nr, nc, face)

                if board[nr][nc] == ' ':
                    raise ValueError('Undefined Behaviour')

                if board[nr][nc] != '#':
                    r = nr
                    c = nc
                    face = nface
                    board[r][c] = '>v<^'[face]

    return (1000 * (r + 1) + 4 * (c + 1) + face)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (123046, 195032)

if __name__ == '__main__':
    main()


