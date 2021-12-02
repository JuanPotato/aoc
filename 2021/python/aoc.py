from pathlib import Path

def parse_list(s, *types, line='\n', sep=' '):
    if not types:
        types = (str,)

    for line in s.strip().split('\n'):
        t = tuple(type(word) for type,word in zip(types, line.split(' ', len(types) - 1)))
        if len(t) == 1:
            t = t[0]
        yield t

def chunk(l, n):
    return (l[i*n:(i+1)*n] for i in range((len(l) + n - 1) // n))

def window(l, n):
    return (l[i:i+n] for i in range(len(l) - n + 1))

def get_input(script):
    path = Path(script).with_suffix('.input')
    with path.open() as f:
        return f.read()
