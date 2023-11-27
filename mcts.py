import random
import math

class Node:
    def __init__(self, player_main, player_lawan, move=None):
        self.player_main = player_main
        self.player_lawan = player_lawan
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0

def ucb_score(parent_visits, node_wins, node_visits, exploration_weight=1.41):
    if node_visits == 0:
        return float('inf')
    return (node_wins / node_visits) + exploration_weight * math.sqrt(math.log(parent_visits) / node_visits)

def select_best_child(node):
    if not node.children:
        return None
    return max(node.children, key=lambda child: ucb_score(node.visits, child.wins, child.visits))

def expand(node):
    moves = generate_moves(node.player_main, node.player_lawan)
    for move in moves:
        new_player_main, new_player_lawan = masukan0(move, node.player_main, node.player_lawan)
        new_node = Node(new_player_main, new_player_lawan, move)
        node.children.append(new_node)
    return random.choice(node.children)

def simulate(node):
    player_main_sim = node.player_main
    player_lawan_sim = node.player_lawan

    while not cek0(player_main_sim) and not cek0(player_lawan_sim):
        move = random.choice(generate_moves(player_main_sim, player_lawan_sim))
        player_main_sim, player_lawan_sim = masukan0(move, player_main_sim, player_lawan_sim)

    return evaluate(player_main_sim, player_lawan_sim)

def backpropagate(node, result):
    while node is not None:
        node.visits += 1
        node.wins += result
        node = node.parent

def mcts(player_main, player_lawan, iterations=1000):
    root = Node(player_main, player_lawan)

    for _ in range(iterations):
        node = root
        while node.children:
            node = select_best_child(node)

        if node.visits > 0:
            node = expand(node)

        result = simulate(node)
        backpropagate(node, result)

    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.move

# ... (existing code)

# Update the AI move section in the main loop
if gilir == 1:
    if difficulty_level == "human":
        nilai = inputan(player_1, player_2)
    else:
        nilai = mcts(player_1, player_2, iterations=1000)
    player_1, player_2 = masukan0(nilai, player_1, player_2)
    gilir = 2
