import numpy as np
import itertools
import scipy.sparse as sp
import csp_utils
import random
import networkx as nx


def generate_instance(n, k, r, p):
    a = np.log(k) / np.log(n)
    v = k * n
    s = int(p * (n ** (2 * a)))
    iterations = int(r * n * np.log(n) - 1)

    parts = np.reshape(np.int64(range(v)), (n, k))
    nand_clauses = []

    for i in parts:
        nand_clauses += itertools.combinations(i, 2)

    edges = set()
    for _ in range(iterations):
        i, j = np.random.choice(n, 2, replace=False)
        all = set(itertools.product(parts[i, :], parts[j, :]))
        all -= edges
        edges |= set(random.sample(tuple(all), k=min(s, len(all))))

    nand_clauses += list(edges)
    clauses = {'NAND': nand_clauses}

    instance = csp_utils.CSP_Instance(language=csp_utils.is_language,
                                      n_variables=v,
                                      clauses=clauses)
    return instance


def get_random_instance(hardness = 0.5):
    n = np.random.randint(10, 26)
    k = np.random.randint(5, 21) # k \geq 1/(1-p)
# for very large graphs #neurips rbt
#    n = np.random.randint(30, 50)
#    k = np.random.randint(25, 40) # k \geq 1/(1-p)
    p = np.random.uniform(0.3, 0.8) # original code should is 1.0
    a = np.log(k) / np.log(n)
    r = - a / np.log(1 - p) # the hardest parameters, see https://arxiv.org/pdf/cs/0302001.pdf
    r = hardness*r
    i = generate_instance(n, k, r, p)
    G = nx.Graph()
    G.add_edges_from(i.clauses['NAND'])
    return G,n
