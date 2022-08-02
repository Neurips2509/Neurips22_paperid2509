import networkx as nx


def graph2dimacs(dimacs_filename,g):
    with open(dimacs_filename, "w") as f:
        f.write("p EDGE {} {}\n".format(g.number_of_nodes(), g.number_of_edges()))
        for u, v in g.edges():
            f.write("e {} {}\n".format(u, v))
        f.close()

#https://searchcode.com/codesearch/view/72684839/
def read_graph_dimacs_format(inputfile,graph_type=nx.Graph):
    if not graph_type in [nx.Graph,nx.MultiGraph,nx.DiGraph,nx.MultiDiGraph]:
        raise ValueError("We are asked to read an invalid graph type from input.")
    G=graph_type()
    G.name=''
    n = -1
    m = -1
    m_cnt = 0
    for i,l in enumerate(inputfile.readlines()):
        if l[0]=='c':
            G.name+=l[2:]
            continue
        if l[0]=='p':
            if n>=0:
                raise ValueError("Syntax error: "+"line {} contains a second spec line.".format(i))
            _,fmt,nstr,mstr = l.split()
            if (fmt!='edge')and(fmt!='EDGE'):
                raise ValueError("Input error: "+"Dimacs \'edge\' format expected.".format(i))
            n = int(nstr)
            m = int(mstr)
            G.add_nodes_from(range(0,n))
            continue
        if l[0]=='e':
            m_cnt +=1
            _,v,w=l.split()
            G.add_edge(int(v),int(w))

    if m!=m_cnt:
        raise ValueError("Syntax error: "+"{} edges were expected.".format(m))
    return G

